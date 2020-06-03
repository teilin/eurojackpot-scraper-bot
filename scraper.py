from selenium import webdriver
from datetime import datetime
from pytz import timezone
import pytz

driver = webdriver.Chrome()
driver.get('https://www.norsk-tipping.no/lotteri/eurojackpot/resultater')

months = { 'januar': 1, 'februar': 2, 'mars': 3, 'april': 4, 'mai': 5, 'juni': 6, 'juli': 7, 'august': 8, 'september': 9, 'oktober': 10, 'november': 11, 'desember': 12 }

def get_date():
    now = datetime.now()
    date_str = driver.find_element_by_xpath('//*[@id="LotteryGameBoard"]/div/div[1]/div/div').text
    day = int((date_str.split(' ')[1])[:-1])
    month = int(months[date_str.split(' ')[2]])
    #dt = datetime.strptime(str(now.year)+'-'+str(month)+'-'+str(day), '%Y-%m-%d')
    dt = datetime(now.year, month, day, 19, 0, 0)
    oslo = timezone('Europe/Oslo')
    return oslo.localize(dt)

def get_numbers():
    lottery_numbers = []
    for index_number in range(5):
        index_number = index_number + 1
        number = driver.find_element_by_xpath('//*[@id="LotteryGameBoard"]/div/div[2]/div/div[2]/li['+str(index_number)+']/div').text
        lottery_numbers.append(number)
    return lottery_numbers

def get_extra_numbers():
    lottery_numbers = []
    for index_number in range(2):
        index_number += 1
        number = driver.find_element_by_xpath('//*[@id="LotteryGameBoard"]/div/div[2]/div/div[4]/li['+str(index_number)+']/div').text
        lottery_numbers.append(number)
    return lottery_numbers

lottery_date = get_date()
lottery_numbers = get_numbers()
lottery_extra_numbers = get_extra_numbers()