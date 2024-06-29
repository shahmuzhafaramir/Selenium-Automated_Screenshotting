#by Shah :)


from selenium import webdriver
import pandas as pd
import pyautogui

"""
Make sure GeckoDriver (mozilla firefox) or ChromeDriver is added to environment PATH
Code will loop till the end of the columns
Websites with login authentication cannot be screenshotted
"""

'Change link your file link'
file_link = r"C:\Users\trapn\Desktop\TLFP\TLFP SAVE PAGE CODE\Main\LINKS.xlsx"


'Make sure sheet name is correct'
df = pd.read_excel(file_link,sheet_name='Main',header=0)
link = df.iloc[:,0]
link_len = len(link)

'Filler website'
lazada = "https://www.lazada.com.my"

driver = webdriver.Firefox()
driver.maximize_window()

driver.get(lazada)
driver.implicitly_wait(2)
print("starting screenshot")


for i in range (0, link_len):
    web = link[i]
    print (web)
    
    'driver.get waits for website to fully load so be patient'
    driver.get(web)
    driver.implicitly_wait(2)
    
    'CLicks screen to remove popus on some websites'
    pyautogui.moveTo(200,200, duration=1)
    pyautogui.leftClick()
    
    
    'change link to your designated screenshot folder'
    driver.save_screenshot("{}{}{}".format(r"C:\Users\trapn\Desktop\TLFP\TLFP SAVE PAGE CODE\Main\screenshot\ ",i, ".png"))


driver.quit()
print("done screenshot")