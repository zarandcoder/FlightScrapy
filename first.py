#For accessing website and test automating
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Structuring data and utils for date handle
import pandas as pd
import time
import datetime


#Send the offerings to the mail but maybe I'll go telegram it
import smtplib
from email.mime.multipart import MIMEMultipart


browser = webdriver.Chrome(executable_path='chromedrive/chromedriver')
#Choose flight tab
choose_flight_only = "//button[@id='tab-flight-tab-hp']"
#Settings ticket type paths
return_ticket = "//label[@id='flight-type-roundtrip-label-hp-flight']"
one_way_ticket = "//label[@id='flight-type-one-way-label-hp-flight']"
multi_ticket = "//label[@id='flight-type-multi-dest-label-hp-flight']"


#Choose a ticket type
def ticket_type_chooser(ticket):
    try:
        ticket_type = browser.find_element_by_xpath(ticket)
        ticket_type.click()
    except Exception as e:
        print(e)
        pass


#Choose Depature country
def departure_country_chooser(dep_country):
    fly_from = browser.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")
    time.sleep(1)
    fly_from.clear()
    time.sleep(1.5)
    fly_from.send_keys(' '+dep_country)
    time.sleep(1.5)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(1.5)
    first_item.click()


#Choose Arrival country
def arrival_country_chooser(arrival_country):
    fly_to = browser.find_element_by_xpath("//input[@id='flight-destination-hp-flight']")
    time.sleep(1)
    fly_to.clear()
    time.sleep(1.5)
    fly_to.send_keys('  ' + arrival_country)
    time.sleep(1.5)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(1.5)
    first_item.click()


#Choosing depature and return dates
def dep_date_choose(month,day,year):
    dep_date_but = browser.find_element_by_xpath("//input[@id='package-departing-hp-package']")
    dep_date_but.clear()
    dep_date_but.send_keys(month + '/' + day + '/' + year)


def return_date_chooser(month, day, year):
    return_date_button = browser.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")

    for i in range(11):
        return_date_button.send_keys(Keys.BACKSPACE)
    return_date_button.send_keys(month + '/' + day + '/' + year)


#Getting the results
def search():
    search = browser.find_element_by_xpath("//button[@id='search-button-hp-package'")
    search.click()
    time.sleep(15)
    print("Ready!")


#Compile the data
df = pd.DataFrame()
def compile_data():
    global df
    global dep_times_list
    global arr_times_list
    global airlines_list
    global price_list
    global duration_list
    global stops_list
    global layovers_list

    #depature times
