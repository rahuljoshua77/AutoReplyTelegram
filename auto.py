import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os, string
import random
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
import re
import logging
 
cwd = os.getcwd()

opts = Options()
opts.headless = False
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.FIREFOX
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")

opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
#opts.add_experimental_option('excludeSwitches', ['enable-logging'])
path_browser = f"{cwd}\geckodriver.exe"

random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)
opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.{random_angka}.{random_angka_dua} Safari/537.36")
browser = webdriver.Firefox(options=opts, desired_capabilities=dc, executable_path=path_browser)

"""UNDER DEVELOPMENT, PLEASE FEEL FREE TO DEVELOP AGAIN"""

def open_browser():
    print(f"[*] Automation Reply Telegram!\n[*] Author: RJD")
    print(f"[*] Open Telegram")
    browser.get('https://web.telegram.org/k/')
    sleep(2)
    print(f"[*] Please Scan QR to Login!")
    check = input(str(f"[*] Have Scan? y/t:"))
     
    """use message txt for long text"""
    # message_file = "message.txt"
    # try:
    #     myfile = open(f"{cwd}/{message_file}","r",encoding='utf-8')
    #     get_message = myfile.read()
    # except Exception as e:
    #     print(f"[{time.strftime('%d-%m-%y %X')}] EROR: {e}")
    # #print(get_message)
    
    check = check.lower()
    if check == "y":
        print(f"[{time.strftime('%d-%m-%y %X')}] Please wait 5s...!\n[{time.strftime('%d-%m-%y %X')}] Auto Reply Started!")
        
        while True:

            try:
                """YOU CAN CHANGE KEY WITH YOUR COSTUM KEY"""

                key = "/ke1"

                """YOU CAN CHANGE MESSAGE HAI #1 WITH YOUR COSTUM MESSAGE"""

                message = "HAI #1"
                browser.find_element_by_xpath(f"//span[contains(text(), '{key}')]")

                """THE LOGIC IS IF THE KEY APPEAR, THE FIRST CHAT WILL BE CLICKED, PLEASE FIX THIS LOGIC"""

                browser.find_element_by_xpath('//*[@id="folders-container"]/div/ul/li[1]/div[1]').click()
                 
                try:
            
                    from_user = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, "(//span[contains(@class,'peer-title')])[1]"))).text
                     
                    print(f"[{time.strftime('%d-%m-%y %X')}]  [ {key} ] Detected from {from_user}!")
                    try:
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] Trying to auto reply!")
                        try:
                            input_message = browser.find_element_by_xpath("//div[data-placeholder='Message']")
                            input_message.click()
                        except:
                            input_message = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div/div[4]/div/div[1]/div[6]/div[1]/div[1]")

                        input_message.send_keys(message)
                        sleep(0.5)
                        input_message.send_keys(Keys.ENTER)
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] Success Auto Reply!")
                    except Exception as e:
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] [EROR INPUT] {e}")
                        pass
                except Exception as e:
                    print(f"[{time.strftime('%d-%m-%y %X')}] [EROR USER] {e}")
                    pass
            
            except:
                pass

            """TRY SECTION IN BELOW IS NOT NECCESERRY, IF YOU NOT USE IT, JUST COMMENT IT"""

            try:
                
                key = '/ke2'
                message = "HAI #2"
                browser.find_element_by_xpath(f"//span[contains(text(),'{key}')]")
                browser.find_element_by_xpath('//*[@id="folders-container"]/div/ul/li[1]/div[1]').click()
                
                try:
            
                    from_user = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, "(//span[contains(@class,'peer-title')])[1]"))).text
                    
                    print(f"[{time.strftime('%d-%m-%y %X')}] [ {key} ] detected from {from_user}!")
                    try:
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] Trying to auto reply!")
                        try:
                            input_message = browser.find_element_by_xpath("//div[data-placeholder='Message']")
                            input_message.click()
                        except:
                            input_message = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div/div[4]/div/div[1]/div[6]/div[1]/div[1]")
                        input_message.send_keys("HAI #2")
                        sleep(0.5)
                        input_message.send_keys(Keys.ENTER)
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] Success Auto Reply!")
                    except Exception as e:
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] [EROR INPUT] {e}")
                        pass
                except Exception as e:
                    print(f"[{time.strftime('%d-%m-%y %X')}] [EROR USER] {e}")
                    pass
            except:
                pass
            try:
                key = "/ke3"
                browser.find_element_by_xpath(f"//span[contains(text(),'{key}')]")
                browser.find_element_by_xpath('//*[@id="folders-container"]/div/ul/li[1]/div[1]').click()
                 
                try:
            
                    from_user = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, "(//span[contains(@class,'peer-title')])[1]"))).text
                    
                    print(f"[{time.strftime('%d-%m-%y %X')}] [ {key} ] detected from {from_user}!")
                    try:
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] Trying to auto reply!")
                        try:
                            input_message = browser.find_element_by_xpath("//div[data-placeholder='Message']")
                            input_message.click()
                        except:
                            input_message = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div/div[4]/div/div[1]/div[6]/div[1]/div[1]")
                        input_message.send_keys("HAI #3")
                        sleep(0.5)
                        input_message.send_keys(Keys.ENTER)
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] Success Auto Reply!")
                    except Exception as e:
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] [EROR INPUT] {e}")
                        pass
                except Exception as e:
                    print(f"[{time.strftime('%d-%m-%y %X')}] [EROR USER] {e}")
                    pass
            except:
                pass

            try:
                key = "/ke4"
                browser.find_element_by_xpath(f"//span[contains(text(),'{key}')]")
                browser.find_element_by_xpath('//*[@id="folders-container"]/div/ul/li[1]/div[1]').click()
                 
                try:
            
                    from_user = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, "(//span[contains(@class,'peer-title')])[1]"))).text
                    
                    print(f"[{time.strftime('%d-%m-%y %X')}] [ {key} ] detected from {from_user}!")
                    try:
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] Trying to auto reply!")
                        try:
                            input_message = browser.find_element_by_xpath("//div[data-placeholder='Message']")
                            input_message.click()
                        except:
                            input_message = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div/div[4]/div/div[1]/div[6]/div[1]/div[1]")
                        input_message.send_keys("HAI #4")
                        sleep(0.5)
                        input_message.send_keys(Keys.ENTER)
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] Success Auto Reply!")
                    except Exception as e:
                        print(f"[{time.strftime('%d-%m-%y %X')}] [  {from_user} ] [EROR INPUT] {e}")
                        pass
                except Exception as e:
                    print(f"[{time.strftime('%d-%m-%y %X')}] [EROR USER] {e}")
                    pass
            except:
                pass
            

    else:
        print(f"[{time.strftime('%d-%m-%y %X')}]  You don't login! Exit!")
        browser.quit()

open_browser()
