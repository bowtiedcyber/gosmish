#!/usr/bin/python3
import sys
import sqlite3
con = sqlite3.connect('gosmish.db')
cur = con.cursor()
try:
    campaign = sys.argv[1]
except:
    print("enter campaign number as argument")
    exit()
success_set = set()
f = open('/var/log/apache2/access.log')
search_str = "GET /%s" %campaign
for line in f:
    if search_str in line:
        try:
            num = line.split("GET ")[1].split(" HTTP")[0].split("=")[1]
            success_set.add(num)
        except:
            pass
naughty_list = set()
for i in success_set:
    try:
        for row in cur.execute('SELECT * FROM victims WHERE contact_id=%s' %i):
            naughty_list.add(row)
    except:
        pass
print("")
print("The following failed the SMISHING test:")
print("")

for i in naughty_list:
    print("%s %s, %s"%(i[1],i[2],i[4]))


print("")
