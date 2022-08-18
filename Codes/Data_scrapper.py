
from optparse import Values
from bs4 import BeautifulSoup
import requests
import re

import pandas as pd
import csv


s = 0

Cur = []


Lis = ['/wiki/Assamese_language'
,
'/wiki/Amar_Asom'
,
'/wiki/Aji_(Assamese_Daily)'
,
'/wiki/Asomiya_Khabar'
,
'/wiki/Asomiya_Pratidin'
,
'/wiki/Dainik_Agradoot'
,
'/wiki/Dainik_Asam'
,
'/wiki/Dainik_Gana_Adhikar'
,
'/wiki/Dainik_Janambhumi'
,
'/wiki/Janasadharan'
,
'/wiki/Niyomiya_Barta'
,
'/wiki/Bengali_language'
,
'/wiki/Aajkaal'
,
'/wiki/Anandabazar_Patrika'
,
'/wiki/Bartaman'
,
'/wiki/Daily_Desher_Katha'
,
'/wiki/Dainik_Prantajyoti'
,
'/wiki/Dainik_Sambad'
,
'/wiki/Dainik_Statesman'
,
'/wiki/Dainik_Jugasankha'
,
'/wiki/Deshabrati'
,
'/wiki/Ebela'
,
'/wiki/Ei_Samay_Sangbadpatra'
,
'/wiki/Ekdin'
,
'/wiki/Ganadabi'
,
'/wiki/Ganashakti'
,
'/wiki/Jago_Bangla'
,
'/wiki/Kalantar'
,
'/wiki/Puber_Kalom'
,
'/wiki/Manush_Patrika'
,
'/wiki/Sakalbela'
,
'/wiki/Sangbad_Lahari'
,
'/wiki/Sangbad_Pratidin'
,
'/wiki/Syandan_Patrika'
,
'/wiki/Tripura_Bani'
,
'/wiki/Uttarbanga_Sambad'
,
'/wiki/Indian_English'
,
'/wiki/The_Asian_Age'
,
'/wiki/The_Assam_Tribune'
,
'/wiki/Bangalore_Mirror'
,
'/wiki/Business_Standard'
,
'/wiki/Central_Chronicle'
,
'/wiki/Daily_Excelsior'
,
'/wiki/Deccan_Chronicle'
,
'/wiki/Deccan_Herald'
,
'/wiki/The_Economic_Times'
,
'/wiki/Financial_Chronicle'
,
'/wiki/The_Financial_Express_(India)'
,
'/wiki/The_Free_Press_Journal'
,
'/wiki/Greater_Kashmir'
,
'/wiki/The_Hans_India'
,
'/wiki/The_Hindu'
,
'/wiki/Business_Line'
,
'/wiki/Frontline_(magazine)'
,
'/wiki/Hindustan_Times'
,
'/wiki/Kashmir_Reader'
,
'/wiki/Imphal_Free_Press'
,
'/wiki/The_Indian_Express'
,
'/wiki/Metro_India'
,
'/wiki/Mid-Day'
,
'/wiki/The_Milli_Gazette'
,
'/wiki/Mint_(newspaper)'
,
'/wiki/Mumbai_Mirror'
,
'/wiki/Mail_Today'
,
'/wiki/Orissa_Post'
,
'/wiki/Swarajya_(magazine)'
,
'/wiki/Telangana_Today'
,
'/wiki/The_North_East_Times'
,
'/wiki/The_New_Indian_Express'
,
'/wiki/The_Pioneer_(India)'
,
'/wiki/Star_of_Mysore'
,
'/wiki/The_Sentinel_(Guwahati)'
,
'/wiki/The_Siasat_Daily'
,
'/wiki/The_Sunday_Guardian'
,
'/wiki/The_Statesman_(India)'
,
'/wiki/The_Telegraph_(India)'
,
'/wiki/The_Times_of_India'
,
'/wiki/The_Tribune_(Chandigarh)'
,
'/wiki/Free_Press_Kashmir'
,
'/wiki/Kashmir_Times'
,
'/wiki/ThePrint'
,
'/wiki/Organiser_(magazine)'
,
'/wiki/Nagaland_Post'
,
'/wiki/Eastern_Mirror'
,
'/wiki/Nagaland_Page'
,
'/wiki/The_Morung_Express'
,
'/wiki/Young_India'
,
'/wiki/Media_in_Gujarati_language'
,
'/wiki/Bombay_Samachar'
,
'/wiki/Divya_Bhaskar'
,
'/wiki/Gujarat_Samachar'
,
'/wiki/Gujarat_Mitra'
,
'/wiki/Gujarat_Today'
,
'/wiki/Janmabhoomi_(Gujarati_newspaper)'
,
'/wiki/Jai_Hind_(newspaper)'
,
'/wiki/Jagat_Darpan'
,
'/wiki/Kutchmitra'
,
'/wiki/Mid-Day'
,
'/wiki/NavGujarat_Samay'
,
'/wiki/Nobat'
,
'/wiki/Phulchhab'
,
'/wiki/Sambhaav'
,
'/wiki/Sandesh_(Indian_newspaper)'
,
'/wiki/Hindi'
,
'/wiki/Aj_(newspaper)'
,
'/wiki/Amar_Ujala'
,
'/wiki/Business_Standard'
,
'/wiki/Dainik_Bhaskar'
,
'/wiki/Dainik_Jagran'
,
'/wiki/Dainik_Navajyoti'
,
'/wiki/Dainik_Tribune'
,
'/wiki/Deshbandhu_(newspaper)'
,
'/wiki/Divya_Himachal'
,
'/wiki/The_Economic_Times'
,
'/wiki/Hari_Bhoomi'
,
'/wiki/Herald_Young_Leader'
,
'/wiki/Hindustan_(newspaper)'
,
'/wiki/Jansatta'
,
'/wiki/Nava_Bharat'
,
'/wiki/Navbharat_Times'
,
'/wiki/Prabhat_Khabar'
,
'/wiki/Punjab_Kesari'
,
'/wiki/Rajasthan_Patrika'
,
'/wiki/Sanjeevni_Today'
,
'/wiki/Sudarshan_News'
,
'/wiki/Tehelka'
,
'/wiki/Kannada'
,
'/wiki/Hosa_Digantha'
,
'/wiki/Hai_Bangalore'
,
'/wiki/Janathavani'
,
'/wiki/Kannada_Prabha'
,
'/wiki/Karavali_Ale'
,
'/wiki/Karavali_Munjavu'
,
'/wiki/Lankesh_Patrike'
,
'/wiki/Mangaluru_Samachara'
,
'/wiki/Mysooru_Mithra'
,
'/wiki/Prajavani'
,
'/wiki/Samyukta_Karnataka'
,
'/wiki/Sanjevani'
,
'/wiki/Suddi_Sangaati'
,
'/wiki/Udayavani'
,
'/wiki/Usha_Kirana'
,
'/wiki/Varthabharathi'
,
'/wiki/Vijaya_Karnataka'
,
'/wiki/Vijayavani'
,
'/wiki/Vishwavani_News'
,
'/wiki/Konkani_language'
,
'/wiki/Sunaparant'
,
'/wiki/Malayalam'
,
'/wiki/Aksharanadam'
,
'/wiki/Asianet_News'
,
'/wiki/Chandrika_(newspaper)'
,
'/wiki/Deepika_(newspaper)'
,
'/wiki/Deshabhimani'
,
'/wiki/General_(newspaper)'
,
'/wiki/Janayugom'
,
'/wiki/Janmabhumi'
,
'/wiki/Kerala_Kaumudi'
,
'/wiki/Madhyamam'
,
'/wiki/Malayala_Manorama'
,
'/wiki/Mangalam_Publications'
,
'/wiki/Mathrubhumi'
,
'/wiki/Siraj_Daily'
,
'/wiki/Thejas'
,
'/wiki/Marathi_language'
,
'/wiki/Deshdoot'
,
'/wiki/Ekmat'
,
'/wiki/Kesari_(newspaper)'
,
'/wiki/Lokmat'
,
'/wiki/Loksatta'
,
'/wiki/Maharashtra_Times'
,
'/wiki/Nava_Kaal'
,
'/wiki/Navshakti'
,
'/wiki/Prahaar_(newspaper)'
,
'/wiki/Pudhari'
,
'/wiki/Sakal'
,
'/wiki/Saamana'
,
'/wiki/Sanchar'
,
'/wiki/Tarun_Bharat'
,
'/wiki/Odia_language'
,
'/wiki/The_Samaya'
,
'/wiki/The_Samaja'
,
'/wiki/Sambad'
,
'/wiki/Dharitri_(newspaper)'
,
'/wiki/Pragativadi'
,
'/wiki/Prameya'
,
'/wiki/Sakala_(Odia)'
,
'/wiki/Punjabi_language'
,
'/wiki/Ajit_(newspaper)'
,
'/wiki/Punjabi_Tribune'
,
'/wiki/Jag_Bani'
,
'/wiki/Rozana_Spokesman'
,
'/wiki/Sanskrit'
,
'/wiki/Sudharma'
,
'/wiki/Tamil_language'
,
'/wiki/Dina_Thanthi'
,
'/wiki/Dinakaran'
,
'/wiki/Dinamalar'
,
'/wiki/Dinamani'
,
'/wiki/Dinasudar'
,
'/wiki/Hindu_Tamil_Thisai'
,
'/wiki/Kannagi_(newspaper)'
,
'/wiki/Maalai_Malar'
,
'/wiki/Malai_Murasu'
,
'/wiki/Madras_Musings'
,
'/wiki/Makkal_Kural'
,
'/wiki/Nakkheeran'
,
'/wiki/Nellai_Maalai_Murasu'
,
'/wiki/Swadesamitran'
,
'/wiki/Theekkathir'
,
'/wiki/Thuglak'
,
'/wiki/Theekkathir'
,
'/wiki/Tamil_Nesan'
,
'/wiki/Tamil_Murasu'
,
'/wiki/Telugu_language'
,
'/wiki/Andhra_Bhoomi'
,
'/wiki/Andhra_Jyothi'
,
'/wiki/Andhra_Prabha'
,
'/wiki/Eenadu'
,
'/wiki/Janam_Sakshi'
,
'/wiki/Mana_Telangana'
,
'/wiki/Namasthe_Telangana'
,
'/wiki/Nava_Telangana'
,
'/wiki/Prajasakti'
,
'/wiki/Sakshi_(media_group)'
,
'/wiki/Suryaa_(newspaper)'
,
'/wiki/Vaartha'
,
'/wiki/Visalaandhra'
,
'/wiki/Zamin_Ryot'
,
'/wiki/Urdu'
,
'/wiki/Avadhnama'
,
'/wiki/Etemaad_Daily'
,
'/wiki/Hind_Samachar'
,
'/wiki/Taasir'
,
'/wiki/The_Munsif_Daily'
,
'/wiki/The_Siasat_Daily']


for i in range(len(Lis)):
    Lis[i]='https://en.wikipedia.org'+Lis[i]

print(len(Lis))

while(s < len(Lis)):
    print(s)
    url = Lis[s]

    sf = ""

    for i in range(len(url)-1, 0, -1):
        if(url[i] == '/'):
            break
        sf = sf+url[i]

    sf = sf[::-1]

    pg = requests.get(url)

    soup = BeautifulSoup(pg.text, 'html.parser')

    # #  Looking for the table with the classes 'wikitable' and 'sortable'
    table = soup.find('table', class_='infobox hproduct')

    tablex = soup.find('table', class_='infobox vcard')

   

    ng = {}
    i = 0
    if(tablex != None):

        for mi in tablex.find_all('tbody'):

            # Find all data for each column
            rows = mi.find_all('tr')

            for row in rows:
                i = i+1
                if(i == 1):
                    covers = soup.select('table.infobox a.image img[src]')
                    for cover in covers:
                        if(cover['src']==""):
                            continue                    
                        ng["image"]="https:"+cover['src']
                    ng["Link"]= Lis[s]
                    ng["Name"] = sf
                    continue

                atb = row.find('th', class_="infobox-label")

                vals = row.find('td', class_="infobox-data")

                if(atb == None or vals == None):
                    continue

                ng[atb.text] = vals.text

        s=s+1
        Cur.append(ng)

        continue


    if(table == None):
        print(url)
        s = s+1
        continue
   
    for mi in table.find_all('tbody'):

        # Find all data for each column
        rows = mi.find_all('tr')

        for row in rows:
            i = i+1
            if(i == 1):
                covers = soup.select('table.infobox a.image img[src]')
                for cover in covers:
                    if(cover['src']==""):
                        continue                    
                    ng["image"]="https:"+cover['src']
                ng["Link"]= Lis[s]
                ng["Name"] = sf
                continue

            atb = row.find('th', class_="infobox-label")

            vals = row.find('td', class_="infobox-data")

            if(atb == None or vals == None):
                continue

            ng[atb.text] = vals.text



    Cur.append(ng)
    s = s+1


df = pd.DataFrame(data=Cur)

# convert into excel
df.to_excel("Magazines.xlsx", index=False)
print("Dictionary converted into excel...")
