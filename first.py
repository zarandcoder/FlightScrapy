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
def dep_date_choose(month, day, year):
    dep_date_but = browser.find_element_by_xpath("//input[@id='flight-departing-hp-flight']")
    dep_date_but.clear()
    dep_date_but.send_keys(month + '/' + day + '/' + year)


def return_date_chooser(month, day, year):
    return_date_button = browser.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")

    for i in range(11):
        return_date_button.send_keys(Keys.BACKSPACE)
    return_date_button.send_keys(month + '/' + day + '/' + year)


#Getting the results
def search():
    search = browser.find_element_by_xpath("//button[@class='btn-primary btn-action gcw-submit']")
    search.click()
    time.sleep(20)
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
    dep_times = browser.find_elements_by_xpath("//span[@data-test-id='departure-time']")
    dep_times_list = [value.text for value in dep_times]

    #arrival times
    arr_times = browser.find_elements_by_xpath("//span[@data-test-id='arrival-time']")
    arr_times_list = [value.text for value in arr_times]

    #airline name
    airlines = browser.find_elements_by_xpath("//span[@data-test-id='airline-name']")
    airlines_list = [value.text for value in airlines]

    #prices
    prices = browser.find_elements_by_xpath("//span[@data-test-id='listing-price-dollars']")
    price_list = [value.text for value in prices]

    #durations
    durations = browser.find_elements_by_xpath("//span[@data-test-id='duration']")
    duration_list = [value.text for value in durations]

    #stops
    stops = browser.find_elements_by_xpath("//span[@class='number-stops']")
    stops_list = [value.text for value in stops]

    #layovers
    layovers = browser.find_elements_by_xpath("//span[@data-test-id='layover-airport-stops']")
    layovers_list = [value.text for value in layovers]


    now = datetime.datetime.now()
    current_date = (str(now.year) + '-' + str(now.month) + '-' + str(now.day))
    current_time = (str(now.hour) + ':' + str(now.minute))
    current_price = 'price' + '(' + current_date + '---' + current_time + ')'

    for i in range(len(dep_times_list)):
        try:
            df.loc[i, 'depature_time'] = dep_times_list[i]
        except Exception as e:
            pass

        try:
            df.loc[i, 'arrival_time'] = arr_times_list[i]
        except Exception as e:
            pass

        try:
            df.loc[i, 'airline'] = airlines_list[i]
        except Exception as e:
            pass

        try:
            df.loc[i, 'duration'] = duration_list[i]
        except Exception as e:
            pass

        try:
            df.loc[i, 'stops'] = stops_list[i]
        except Exception as e:
            pass

        try:
            df.loc[i, 'layovers'] = layovers_list[i]
        except Exception as e:
            pass

        try:
            df.loc[i, str(current_price)] = price_list[i]
        except Exception as e:
            pass

    print("Dataframe was created and filled")

    #TODO: Implementing notification with telegram
