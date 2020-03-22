from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Path webdriver
chrome_path = 'chromedriver.exe'
chrome_option = Options()
chrome_option.add_argument('--headless')
chrome = webdriver.Chrome(executable_path=chrome_path,
                          chrome_options=chrome_option)


def waitTag(xpath):
    # Menunggu sampai path tag ada
    WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))


def getPage(url, username, password):
    # Kunjungi URL agar dapat masuk kehalam login
    chrome.get(url)
    # Klik tombol lanjut login
    waitTag(
        '/html/body/div[1]/div[3]/div/div/div/section/div/div/div/div[3]/form/button')
    chrome.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div/div/div/section/div/div/div/div[3]/form/button').click()

    # Melakukan login
    waitTag(
        '/html/body/div[1]/div[2]/div/section/div/div[2]/div[1]/div/div[2]/form/div[3]/button')
    chrome.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    chrome.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    chrome.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/section/div/div[2]/div[1]/div/div[2]/form/div[3]/button').click()

    # Ambil page source
    return chrome.page_source
