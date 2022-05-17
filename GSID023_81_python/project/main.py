from datetime import datetime

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    is_finished = False
    str_finished = '아니오'


    def get_crawler_data(soup, url):
        title_result = []
        info_result = []
        chart_result = []
        spec_result = []
        result = []
        columns = []
        if url == 'https://www.skku.edu/skku/campus/skk_comm/notice06.do':
            columns = ['제목', '번호', '작성자', '작성날짜', '조회수']
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
            columns = ['회사명', '산업', '매출액', '사원수', '학업성취도', '외국어', '전문능력', '대외활동', '스펙지수']
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

        return result, columns


    def print_description(start_dt, end_dt, file_name):
        t_delta = (end_dt - start_dt).total_seconds()
        print(f'{file_name}파일에 크롤링 결과가 저장되었습니다.')
        print(f'소요 시간{round(t_delta, 2)}초')
        print(
            f'시작 시간{start_dt.year}년 {start_dt.month}월 {start_dt.day}일 {start_dt.hour}시 {start_dt.minute}분 {start_dt.second}초')
        print(f'완료 시간{end_dt.year}년 {end_dt.month}월 {end_dt.day}일 {end_dt.hour}시 {end_dt.minute}분 {end_dt.second}초')
        print("안녕히가세요")


    while not is_finished:
        url = input('웹사이트 주소:')
        # if url =='https://www.skku.edu/skku/campus/skk_comm/notice06.do':

        response = requests.get(url)
        title_result, info_result = [], []

        start_dt = datetime.now()
        start_str = start_dt.strftime('%Y%m%d%H%m')
        format_prefix = '.csv'

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            result, columns = get_crawler_data(soup, url)

            import csv

            file_name = start_str + format_prefix
            with open(file_name, 'w', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(columns)
                writer.writerows(result)

            end_dt = datetime.now()

            print_description(start_dt, end_dt, file_name)

            str_finished = input('계속하시겠습니까?')

            if str_finished == '네':
                is_finished = False
            else:
                is_finished = True
        else:
            print(response.status_code)
