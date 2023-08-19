import datetime
import os
import pandas as pd


def main():
    df = pd.DataFrame(columns=['timestamp', 'path_img', 'dofw', 'weekend'])
    df.to_csv('data.csv', index=False)

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

    os.mkdir('img')
    for key in maps.keys():
        os.mkdir(f'img/{key}')

    current = datetime.datetime.now()
    print(current.weekday())
    print(type(current.weekday()))
