from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import sys
import os
from datetime import datetime, timedelta, date
import pandas as pd
import multiprocessing
import threading
from __ import main

restart = False
if restart:
    main()

maps = {
    'gedebage_timur': 75,
    'gedebage_barat': 76,
    'gedebage_selatan': 77,
    'gedebage_utara': 78,
    'samsat': 2,
    'samsat_barat': 80,
    'samsat_selatan': 81,
    'samsat_utara': 82,
    'buahbatu': 3,
    'buahbatu_timur': 83,
    'buahbatu_selatan': 84,
    'buahbatu_barat': 85,
    'buahbatu_utara': 86,
    'batununggal': 4,
    'batununggal_barat': 88,
    'toha': 5,
    'toha_barat': 89,
    'toha_selatan': 90,
    'toha_utara': 91,
    'toha_timur': 92,
    'cibaduyut': 7,
    'kopo': 8,
    'pasirkoja_selatan': 94,
    'pasirkoja_barat': 95,
    'pasirkoja_utara': 96,
    'cibeureum': 11
}

options = Options()
options.add_argument('--headless')
service = ChromeService(executable_path=ChromeDriverManager().install())

i = 0

while True:
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1280, 960)
    now = datetime.now()
    delay = 3600
    if now.hour in range(6, 18) :
        delay = 900

    url = 'https://atcs-dishub.bandung.go.id/'
    driver.get(url)
    timeout = 10

    try:
        unk = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'live')))
    except TimeoutException:
        print('Kelamaan!')

    driver.execute_script('showStreamingModal(4);')
    time.sleep(1)
    element = driver.find_element(By.XPATH, '//video[@preload="auto"]')
    element.click()
    time.sleep(5)

    for k, v in maps.items():
        driver.execute_script(f'showStreamingModal({v});')
        element = driver.find_element(
            By.XPATH, '//video[@preload="auto"]')
        x, y, x1, y1 = 88, 175, 1190, 791
        time.sleep(20)
        for i in range(3):
            current = datetime.now()
            month, day, dofw, hour, minute, second = current.month, current.day, current.weekday(
            ), current.hour, current.minute, current.second
            weekend = 1 if dofw > 4 else 0
            filename = f'{k}-{month}-{day} {hour}-{minute}-{second}.png'
            ss_filename = f'img/{k}/{filename}'
            ss_file = driver.get_screenshot_as_png()

            image = Image.open(BytesIO(ss_file))
            image_crop = image.crop((
                x, y,
                x1, y1
            ))

            image_crop.save(ss_filename)
            print(f'{ss_filename} saved.')
            df = pd.read_csv('data.csv')
            data = pd.DataFrame(
                [[current, ss_filename, dofw, weekend]],
                columns=df.columns.tolist()
            )
            df = pd.concat([df, data], axis=0)
            df.to_csv('data.csv', index=False)
            time.sleep(5)
    driver.quit()
    i = i + 1
    if i >= 500:
        break
    time.sleep(delay)
