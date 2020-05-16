#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
from time import sleep

TIMEOUT = 15

def message_input(driver):
  message_box = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="message"]' ) ))
  message_box.send_keys("Hi Papaya!\n\nThis message was delivered by a script I wrote using Selenium, which you can find on my github at https://github.com/MooseandSquvirrel/hi_papaya - I used a virtual environment if you'd like to test it with pipenv, make sure to have chromedriver on your PATH.\nMy name is Andy Gardner and I'm currently interning at 42 Silicon Valley, a non-profit coding school. I applied to your New Grad Software Engineer role for the Selenium script developer. I believe my experience writing Selenium scripts makes a good candidate for this role. So I thought I'd show it with a quick script I just wrote in a couple minutes. I like automating tasks and this roles seems like a great fit. \n\nHope to hear from you soon!\n\nBest,\nAndy :)")

def email_input(email, driver):
  email_box = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="contact-form"]/div[1]/div[2]/div/input' ) ))
  email_box.send_keys(email)

def name_input(full_name, driver):
	email_box = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="contact-form"]/div[1]/div[1]/div/input' ) ))
	email_box.send_keys(full_name)

def click_send(driver):
	button = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="contact-form"]/button' ) ))
	button.click()
	sleep(20)

def input_info(full_name, email, driver):
  name_input(full_name, driver)
  email_input(email, driver)
  message_input(driver)
  click_send(driver)

def commandline():
  full_name_check = ''
  email_check = ''
  while full_name_check != 'y':
    full_name = input("Enter your full name: ")
    full_name_check = input(f"You entered {full_name}, is this correct? (y or n): ")
  while email_check != 'y':
    email = input("Enter your email: ")
    email_check = input(f"You entered {email}, is this correct? (y or n): ")
  return full_name, email
  
def main():
    full_name, email = commandline()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://papayapay.com/contact")
    input_info(full_name, email, driver)

if __name__== "__main__":
  main()