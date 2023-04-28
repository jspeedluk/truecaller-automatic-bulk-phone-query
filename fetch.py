from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import codecs
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import time

email_id="your outlook email id for sign-in"
password="microsoft account password"

def get_options():
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('debuggerAddress', 'localhost:90023')
    options.set_capability('detach', True)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    return options

driver=Chrome(
    options=get_options(),
)
driver.maximize_window()
# driver.fullscreen_window()
truecaller_url="https://www.truecaller.com/search/in/7297027240"

def write_to_file(filename, content):
    file=codecs.open(filename, 'w', encoding='utf-8')
    file.write(content)
    file.close()

def save_my_data(xxx, phone, name):
    file=codecs.open('data.csv', 'a+', encoding='utf-8')
    line = xxx + "," + phone + "," + name + "\n"
    file.write(line)
    file.close()

def dump_driver(filename, driver):
    fp=open(filename, 'wb')
    pickle.dump(driver, fp)
    fp.close()

def launchBrowser():
    driver.find_element(By.LINK_TEXT,"Sign in").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"MICROSOFT").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@type='email']").send_keys(email_id)
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(1)

driver.get("https://www.truecaller.com/#sign-in")
time.sleep(2)
val = int(input())
if val == 1:
    launchBrowser()

val = int(input())
l=["https://www.truecaller.com/search/in/7297027240", "https://www.truecaller.com/search/in/9680209864"]

c=100
end=199

if val > 0:
    while c < end:
        # driver.get(l[c])
        xxx = "{0:0=3d}".format(c)
        phone_str="852"+xxx+"1881"
        truecaller_url = "https://www.truecaller.com/search/in/"+phone_str
        driver.get( truecaller_url )
        time.sleep(3)
        name_el = driver.find_element(By.XPATH,"//div[ @data-v-d2a2579f and contains(@class, 'montserrat')]")
        name = name_el.text
        save_my_data(xxx, phone_str, name)
        c += 1
        time.sleep(3)
else:
    print("\nArray out of bound")

# driver.quit()