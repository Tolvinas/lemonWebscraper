import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


def init_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.lemongym.lt/')
    return driver


def get_club_percentage_elements():
    driver.find_element(By.ID, 'cookies-custom').click()

    percentage_data_block = driver.find_element(By.CLASS_NAME, 'ipWidget-ClubMembersDisplayWidget')
    return percentage_data_block.find_elements(By.CLASS_NAME, 'col-xs-4')


def get_club_percentages():
    club_percentages = {}
    club_percentage_elements = get_club_percentage_elements()
    for clubPercentageElement in club_percentage_elements:
        name = clubPercentageElement.find_element(By.TAG_NAME, 'h3').text
        percentage = clubPercentageElement.find_element(By.TAG_NAME, 'h2').text
        club_percentages[name] = percentage
    return club_percentages


def write_club_data_to_json():
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    with open('clubPercentages.csv', 'a', newline='', encoding='utf-8') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=',')
        for club in clubPercentages:
            percentage = clubPercentages[club]
            csv_writer.writerow([club, percentage, date])


driver = init_web_driver()
clubPercentages = get_club_percentages()
driver.quit()
write_club_data_to_json()


