from selenium import webdriver
import time
import yagmail
import os



def get_drvier():
  
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver =webdriver.Chrome(options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver

def clean_text(text):
  output= text.split(" ")
  return output

def send_mail(numberl):
  sender=os.environ['SENDER']
  receiver=os.environ['RECEIVER']
  password = os.environ['PASSWORD']
  yag = yagmail.SMTP(user=sender, password=password)
  yag.send(to=receiver, contents=f'Il valore è di {numberl}' , subject=f'Il valore è di {numberl}' )

def main():
  driver = get_drvier()
  time.sleep(2)
  element = driver.find_element(by="xpath",value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
  segno = clean_text(element.text)[0][0]
  numero=clean_text(element.text)[0][0:5]
  if(segno=="-"):
    if(float(numero)>=0.10):
        send_mail(numero)

  else:
    print("niente da inviare")

main()