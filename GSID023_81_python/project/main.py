from datetime import datetime
import csv
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    is_finished = False
    str_finished = '아니오'


    def get_crawler_data(soup, url):
        """
        url 을 입력받아 해당 페이지에서 호출할 데이터를 호출하는 함수
        """
        title_result = []
        info_result = []
        chart_result = []
        spec_result = []
        result = []
        if url == 'https://www.skku.edu/skku/campus/skk_comm/notice06.do':
            ul = soup.select_one('ul.board-list-wrap')
            titles = ul.select('li > dl > dt > a')
            for title in titles:
                title_result.append(title.get_text().strip())
            infos = ul.select('li > dl > dd > ul')
            for li in infos:
                info_set = li.text.strip().split('\n')
                number, author, created_date, view_cnt = info_set[0].replace('No.', ''), info_set[4], info_set[5], \
                                                         info_set[
                                                             6].replace('조회수', '')
                info_result.append((number, author, created_date, view_cnt))

            for x, y in zip(title_result, info_result):
                result.append([x, y[0], y[1], y[2], y[3]])
        elif url == 'https://www.jobkorea.co.kr/starter/spec/':

            ul = soup.select_one('ul.spListArea')
            titles = ul.select('li > div.coWrap > dl > dt > a.tit')
            for title in titles:
                title_result.append(title.get_text().strip())
            infos = ul.select('li > div.coWrap >dl > dd')
            info_temp = []
            for info in infos:
                info_temp.append(info.select_one('span').text)
                if len(info_temp) > 2:
                    info_result.append(info_temp)
                    info_temp = []
            # print(info_result)
            chart = ul.select('li > div.listBarGraph > div.inner > ul >li>span>span')
            chart_temp = []
            for c in chart:
                chart_temp.append(float(c.text))
                if len(chart_temp) > 3:
                    chart_result.append(chart_temp)
                    chart_temp = []
            # print(chart_result)
            specs = ul.select('li > div.spWrap > a > span')
            for spec in specs:
                spec_result.append(spec.text.strip())

            for a, b, c, d in zip(title_result, info_result, chart_result, spec_result):
                result.append([a, b[0], b[1].replace('"', ''), b[2].replace('"', ''), c[0], c[1], c[2], c[3], d])
        elif url == 'https://www.nytimes.com/section/universal/ko':

            ol = soup.select_one('div.css-13mho3u > ol')
            titles = ol.select('li > div > div.css-1l4spti > a > h2 ')
            for title in titles:
                title_result.append(title.get_text().strip())
            contexts = ol.select('li > div > div.css-1l4spti > a> p')
            context_result = []
            for context in contexts:
                context_result.append(context.get_text().strip())
            for a, b in zip(title_result, context_result):
                result.append([a, b])
        return result, columns


    def print_description(start_dt, end_dt, file_name):
        t_delta = (end_dt - start_dt).total_seconds()
        print(f'{file_name}파일에 크롤링 결과가 저장되었습니다.')
        print(f'소요 시간{round(t_delta, 2)}초')
        print(
            f'시작 시간{start_dt.year}년 {start_dt.month}월 {start_dt.day}일 {start_dt.hour}시 {start_dt.minute}분 {start_dt.second}초')
        print(f'완료 시간{end_dt.year}년 {end_dt.month}월 {end_dt.day}일 {end_dt.hour}시 {end_dt.minute}분 {end_dt.second}초')
        print("안녕히가십시오")


    def export_csv(file_name, result, columns):
        with open(file_name, 'w', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(result)


    def run(url, max_page):
        result = []
        columns = []
        stop_cnt = 1
        for p in range(1, max_page):
            if url == 'https://www.skku.edu/skku/campus/skk_comm/notice06.do':
                columns = ['제목', '번호', '작성자', '작성날짜', '조회수']
                offset = str(p * 10) if p == 1 else str((p - 1) * 10)
                response = requests.get(url + '?mode=list&&articleLimit=10&article.offset=' + offset)
            elif url == 'https://www.jobkorea.co.kr/starter/spec/':
                columns = ['회사명', '산업', '매출액', '사원수', '학업성취도', '외국어', '전문능력', '대외활동', '스펙지수']
                response = requests.get(url + '?IsFavorOn=0&IsAlumniOn=0&Page=' + str(p))
            elif url == "https://www.nytimes.com/section/universal/ko":
                columns = ['제목', '내용']
                stop_cnt += 1
                response = requests.get(url)
            # elif url == "https://tgd.kr/c/depressive":
            #     response = requests.get(url + '/page/' + str(p))

            else:
                break

            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')

                t_result = get_crawler_data(soup, url)

                result += t_result
            else:
                return response.status_code
            if stop_cnt > 1:
                break
        return result, columns


    while not is_finished:
        max_page = 10
        url = input('웹사이트 주소:')
        start_dt = datetime.now()
        start_str = start_dt.strftime('%Y%m%d%H%m')
        format_prefix = '.csv'
        file_name = start_str + format_prefix

        result, columns = run(url, max_page)

        export_csv(file_name, result, columns)

        end_dt = datetime.now()

        print_description(start_dt, end_dt, file_name)
        str_finished = input('계속하시겠습니까?')

        if str_finished == '네':
            is_finished = False
        else:
            is_finished = True
