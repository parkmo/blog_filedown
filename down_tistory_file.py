import requests
from bs4 import BeautifulSoup

def download_fileblocks(url):
    # URL 요청 및 HTML 파싱
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Fileblock 요소 추출
    fileblocks = soup.find_all('figure', class_='fileblock')

    # 각 Fileblock 처리
    for fileblock in fileblocks:
        # 다운로드 링크 추출
        download_link = fileblock.find('a')['href']

        # 파일 이름 및 크기 추출
        filename_element = fileblock.find('span', class_='name')
        filename = filename_element.text.strip()
        size_element = fileblock.find('div', class_='size')
        size = size_element.text.strip()

        # 다운로드 및 저장
        print(f"다운로드: {filename} ({size})")
        response = requests.get(download_link, stream=True)
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

if __name__ == '__main__':
    # URL 입력 및 다운로드 시작
    url = input("Fileblock URL을 입력하세요: ")
    download_fileblocks(url)
