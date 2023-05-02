import cloudscraper
import requests
from bs4 import BeautifulSoup
import pandas as pd

def create_scraper(): # Create a cloudscraper object
    return cloudscraper.create_scraper(delay=10, browser={'custom': 'ScraperBot/1.0'})

def fetch_calendar_page(scraper):
    r = scraper.get('https://www.forexfactory.com/calendar')
    soup = BeautifulSoup(r.text, 'html.parser')
    security_value = soup.find('input', {'name': 'flex[Calendar_mainCal][modelData]'})['value']
    return security_value

def send_post_request(scraper, security_value, current_month, first, current_year, end):
    data = f'securitytoken=guest&do=saveoptions&setdefault=no&ignoreinput=no&flex%5BCalendar_mainCalCopy1%5D%5BidSuffix%5D=&flex%5BCalendar_mainCalCopy1%5D%5B_flexForm_%5D=flexForm&flex%5BCalendar_mainCalCopy1%5D%5BmodelData%5D={security_value}&flex%5BCalendar_mainCalCopy1%5D%5Bbegindate%5D={current_month}+{first}%2C+{current_year}&flex%5BCalendar_mainCalCopy1%5D%5Benddate%5D={current_month}+{end}%2C+{current_year}&flex%5BCalendar_mainCalCopy1%5D%5Bcalendardefault%5D=today&flex%5BCalendar_mainCalCopy1%5D%5Bimpacts%5D%5Bhigh%5D=high&flex%5BCalendar_mainCalCopy1%5D%5B_cbarray_%5D=1&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Bgrowth%5D=growth&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Binflation%5D=inflation&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Bemployment%5D=employment&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Bcentralbank%5D=centralbank&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Bbonds%5D=bonds&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Bhousing%5D=housing&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Bsentiment%5D=sentiment&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Bpmi%5D=pmi&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Bspeeches%5D=speeches&flex%5BCalendar_mainCalCopy1%5D%5Beventtypes%5D%5Bmisc%5D=misc&flex%5BCalendar_mainCalCopy1%5D%5B_cbarray_%5D=1&flex%5BCalendar_mainCalCopy1%5D%5Bcurrencies%5D%5Beur%5D=eur&flex%5BCalendar_mainCalCopy1%5D%5Bcurrencies%5D%5Bgbp%5D=gbp&flex%5BCalendar_mainCalCopy1%5D%5Bcurrencies%5D%5Busd%5D=usd&flex%5BCalendar_mainCalCopy1%5D%5B_cbarray_%5D=1&false'
    headers = {
        'authority': 'www.forexfactory.com',
        'method': 'POST',
        'path': '/flex.php?',
        'scheme': 'https',
        'accept': '/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.forexfactory.com',
        'referer': 'https://www.forexfactory.com/calendar',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-requested-with': 'XMLHttpRequest'
    }
    r = scraper.post('https://www.forexfactory.com/flex.php?', data=data, headers=headers)
    return r.text
    #print(r.text)

def parse_calendar_data(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    calendar_table = soup.find('table', class_="calendar__table")
    column_headers = ['Date', 'Time', 'void', 'Currency', 'Impact', 'Event', 'Detail_void', 'Actual', 'Forecast', 'Previous', 'Graph_void']
    df = pd.DataFrame(columns = column_headers)
    for row in calendar_table.select('tr[class*="calendar__row calendar_row"]'):
        row_data = [td.get_text(strip=True) for td in row.find_all('td')]
        df.loc[len(df)] = row_data
    return df