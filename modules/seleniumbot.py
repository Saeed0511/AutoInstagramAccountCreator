""" Creator : saeed0511

    main function borcore
 """

from time import sleep
from random import randint
from random import sample

import modules.config as config
# importing generated info
import modules.generateaccountinformation as accnt
from modules.storeusername import store
# library import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # and Krates
import requests
import re

class AccountCreator():
    def __init__(self, use_custom_proxy, use_local_ip_address):
        self.sockets = []
        self.use_custom_proxy = use_custom_proxy
        self.use_local_ip_address = use_local_ip_address
        self.url = 'https://www.instagram.com/'
        self.loginurl = 'https://www.instagram.com/accounts/login/'
        self.__collect_sockets()

    def __collect_sockets(self):
        r = requests.get("https://www.sslproxies.org/")
        matches = re.findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)
        revised_list = [m1.replace("<td>", "") for m1 in matches]
        for socket_str in revised_list:
            self.sockets.append(socket_str[:-5].replace("</td>", ":"))
        print (self.sockets)

    def createaccount(self, proxy=None):
        print("1")
        chrome_options = webdriver.ChromeOptions()
        if proxy != None:
            print ('use proxy %s' % proxy)
            chrome_options.add_argument('--proxy-server=%s' % proxy)
        driver = webdriver.Chrome(r"c:\Users\Ziaa\Downloads\Compressed\chromedriver_win32\chromedriver.exe")
        print("3")
        driver.get(self.url)
        print("4")
        sleep(3)
        
        name = accnt.username()
        # username

        # fill the email value
        email_field = driver.find_element_by_name('emailOrPhone')
        email_field.send_keys(accnt.genEmail())

        # fill the fullname value
        fullname_field = driver.find_element_by_name('fullName')
        fullname_field.send_keys(accnt.genName())

        # fill username value
        username_field = driver.find_element_by_name('username')
        username_field.send_keys(name)

        # fill password value
        password_field = driver.find_element_by_name('password')
        passW = accnt.generatePassword()
        password_field.send_keys(passW)

        submit = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')
        submit.click()
        
        sleep(3)
            

        print('Registering....')
        store(name)

        print("logging in...")
        sleep(3)
        try:
            errorUnder18 = driver.find_element_by_css_selector('.z79H6')
            if errorUnder18 is not None:
                print('dakhele if ')
                errorUnder18.click()
                sleep(2)
                asd = driver.find_element_by_css_selector('._0mzm-.sqdOP.L3NKy._4pI4F.cB_4K')
                asd.click()
        except Exception as e:
            print(e)
        print('ujnumkimiilomolmolmolmomomolmo')
        sleep(3)

        try:
            sthError = driver.find_element_by_id('ssfErrorAlert')
            if sthError is not None:
                submit.click()
        except Exception as e:
            print(e)
        print('no some thing wrong error!')
        sleep(5)
        
        # driver.get(self.loginurl)

        # usernamefield = driver.find_element_by_name('username')
        # usernamefield.send_keys(name)

        # passwordfield = driver.find_element_by_name('password')
        # passwordfield.send_keys(passW)
        try:
            turnOn = driver.find_element_by_css_selector('.aOOlW.bIiDR')
            turnOn.click()
            print('turn on buttin clicked!')
        except Exception as e:
            print(e)
        

        # aOOlW.HoLwm =====> Not Now Btn

        # submit = driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div/div/div[3]/button[2]')
        # submit.click()

        sleep(3)
        try:
            followBtns = driver.find_elements_by_css_selector('._0mzm-.sqdOP.L3NKy')
            print('getting follow btns!')
        #  arrrandom = sample(range(1,len(followBtns)), 5)
        #  print(arrrandom)
            followBtns[1].click()
            followBtns[6].click()   
            followBtns[9].click()
            followBtns[12].click()
            followBtns[17].click()
        except Exception as e:
            print(e)
        

      #  for i in arrrandom:
       #     print("random number is %s"%i)
            # sleep(1)
        #    arrrandom[i].click()

        sleep(3)

        try:
            getStartedBtn = driver.find_element_by_css_selector('.vF5nu._0mzm-.sqdOP.L3NKy')
            getStartedBtn.click()
            print('Get Started Btn')
        except Exception as e:
            print(e)
        
        
        # arrrandom = sample(range(1,6), 4)
        # print(arrrandom)
        # for i in arrrandom:
        #     print("random number is %s"%i)
        #     linkt = '//*[@id="react-root"]/section/main/section/div/div[2]/div/div/div[%s]/div[3]/button'%str(i)
        #     print(linkt)
            
        #     submit = driver.find_element_by_xpath(linkt)
        #     print('asdfsadf')
        #     print(submit)
        #     test = [btn.click() for btn in submit]
        #     print(test)
        #     sleep(1)
		
        # sleep(2)
        # submit = driver.find_element_by_xpath(
        #         '//*[@id="react-root"]/section/main/section/div/div[2]/button')
        # submit.click()
        
        sleep(3)
		
        driver.close()

    def creation_config(self):
        try:
            if self.use_local_ip_address == False:
                if self.use_custom_proxy == False:
                    for i in range(0, config.Config['amount_of_account']):
                        if len(self.sockets) > 0:
                            current_socket = self.sockets.pop(0)
                            try:
                                self.createaccount(current_socket)
                            except Exception as e: 
                                print('Error!, Trying another Proxy {}'.format(current_socket))
                                self.createaccount(current_socket)  

                else:
                    with open(config.Config['proxy_file_path'], 'r') as file:
                        content = file.read().splitlines()
                        for proxy in content:
                            amount_per_proxy = config.Config['amount_per_proxy']

                            if amount_per_proxy != 0:
                                print("Creating {} amount of users for this proxy".format(amount_per_proxy))
                                for i in range(0, amount_per_proxy):
                                    try:
                                        self.createaccount(proxy)

                                    except Exception as e:
                                        print("An error has occured" + e)

                            else:
                                random_number = randint(1, 20)
                                print("Creating {} amount of users for this proxy".format(random_number))
                                for i in range(0, random_number):
                                    try:
                                        self.createaccount(proxy)
                                    except Exception as e:
                                        print(e)
            else: 
                for i in range(0, config.Config['amount_of_account']):
                            try:
                                self.createaccount()
                            except Exception as e: 
                                print('Error!, Check its possible your ip might be banned')
                                self.createaccount()  


        except Exception as e:
            print(e)


def runbot():
    account = AccountCreator(config.Config['use_custom_proxy'], config.Config['use_local_ip_address'])
    account.creation_config()


