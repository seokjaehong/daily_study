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
        # 크롤링 결과를 저장하기 위한 리스트 초기화
        title_result = []
        info_result = []
        result = []
        if url == 'https://www.skku.edu/skku/campus/skk_comm/notice06.do':
            # 공지사항 표 읽기
            ul = soup.select_one('ul.board-list-wrap')
            # title 리스트 불러오기
            titles = ul.select('li > dl > dt > a')
            # title 리스트를 순회하며 각 title을 title_result에 저장
            for title in titles:
                title_result.append(title.get_text().strip())
            # 세부정보 리스트 불러오기
            infos = ul.select('li > dl > dd > ul')
            # 세부정보 리스트를 순회하며 번호, 작성자,작성일, 조회수를 info_result에 저장
            for li in infos:
                info_set = li.text.strip().split('\n')
                number, author, created_date, view_cnt = info_set[0].replace('No.', ''), info_set[4], info_set[5], \
                                                         info_set[
                                                             6].replace('조회수', '')
                info_result.append((number, author, created_date, view_cnt))
            # 해당 페이지의 크롤링 결과를 저장
            for x, y in zip(title_result, info_result):
                result.append([x, y[0], y[1], y[2], y[3]])
        return result


    def print_description(start_dt, end_dt, file_name):
        """
        크롤링 결과를 출력하는 함수
        """
        t_delta = (end_dt - start_dt).total_seconds()
        print(f'`{file_name}` 파일에 크롤링 결과가 저장되었습니다.')
        print(f'소요 시간{round(t_delta, 2)}초')
        print(
            f'시작 시간: {start_dt.year}년 {start_dt.month}월 {start_dt.day}일 {start_dt.hour}시 {start_dt.minute}분 {start_dt.second}초')
        print(f'완료 시간: {end_dt.year}년 {end_dt.month}월 {end_dt.day}일 {end_dt.hour}시 {end_dt.minute}분 {end_dt.second}초')
        print("안녕히 가십시오")


    def export_csv(file_name, result, columns):
        """
        크롤링 결과를 csv파일로 저장하는 함수
        """
        with open(file_name, 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(result)


    def run(url, page_num):
        """
        크롤링 함수 실행 함수
        page는
        """

        result = []
        columns = []
        for p in range(page_num):
            # 사용자의 요청한 웹사이트 주소 검증
            if url == 'https://www.skku.edu/skku/campus/skk_comm/notice06.do':
                # 크롤링할 항목 초기화
                columns = ['제목', '번호', '작성자', '작성날짜', '조회수']
                # 성균관대학교 공지사항의 경우, offset이라는 파라미터에 따라 Pagination이 구성되어있고, page*10를 offset으로 설정
                offset = str(p * 10)
                response = requests.get(url + '?mode=list&&articleLimit=10&article.offset=' + offset)
            # 잘못입력한 경우 종료
            else:
                break
            # 크롤링에 대한 http에러코드가 200이 면 세부내용을 크롤링 , 아닌 경우 종료
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')

                t_result = get_crawler_data(soup, url)

                result += t_result
        return result, columns


    while not is_finished:
        #
        page_num = 10
        url = input('웹사이트 주소:')
        start_dt = datetime.now()
        start_str = start_dt.strftime('%Y%m%d%H%M')
        format_prefix = '.csv'
        # 저장할 파일이름을 현재시간+.csv 으로 생성
        file_name = start_str + format_prefix

        result, columns = run(url, page_num)
        if len(result) == 0:
            print('잘못된 웹사이트를 입력하셨습니다. 프로그램을 종료합니다')
            is_finished = True
        else:
            export_csv(file_name, result, columns)

            end_dt = datetime.now()

            print_description(start_dt, end_dt, file_name)
            str_finished = input('계속하시겠습니까?')

            if str_finished == '네':
                is_finished = False
            else:
                is_finished = True
