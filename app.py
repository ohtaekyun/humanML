# melon 크롤링

import requests
from bs4 import BeautifulSoup

def crawling(soup):
  # soup객체에서 정보 찾고 반환
  result = []
  tbody = soup.find('tbody')
  
  

  for div in tbody.find_all('div', class_='ellipsis rank01'):
    
    result.append(div.get_text().replace('\n',''))
  




  return result

def main():
  custom_header={
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
  }
  url = 'https://www.melon.com/chart/'
  req = requests.get(url, headers = custom_header)
  soup = BeautifulSoup(req.text, 'html.parser')
  result = crawling(soup)
  print(result[0:5])
  
  
  
  # print(req.status_code)
  # print(req.text)
  

if __name__ == "__main__":
  main()
