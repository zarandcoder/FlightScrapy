from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time
import datetime

import smtplib
from email.mime.multipart import MIMEMultipart

browser = webdriver.Chrome(executable_path='/home/vadim/chromedriver')
