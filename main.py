from selenium import webdriver
import time

def get_drvier():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver =webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  output= text.split(": ")
  return output


def main():
  driver = get_drvier()
  time.sleep(2)
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)[1]

print(main())