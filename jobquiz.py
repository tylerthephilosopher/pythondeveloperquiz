import csv

import requests

#Accessing CSV file and writing to list

file = open('C:\\Users\\tyler\\Documents\\Python Quiz Input - Sheet1.csv')
type(file)
csvreader = csv.reader(file)
rows = []

for row in csvreader:
    rows.append(row)

rows[0].append("Validity")

#company 1

company1 = []
for row in rows[1]:
    company1.append(row)

#company 2

company2 = []
for row in rows[2]:
    company2.append(row)

#company 3

company3 = []
for row in rows[3]:
    company3.append(row)

#company 4

company4 = []
for row in rows[4]:
    company4.append(row)

#company 5 

company5 = []
for row in rows[5]:
    company5.append(row)

#company 6 

company6 = []
for row in rows[6]:
    company6.append(row)

#company 7 

company7 = []
for row in rows[7]:
    company7.append(row)

#company 8 

company8 = []
for row in rows[8]:
    company8.append(row)

#company 9 

company9 = []
for row in rows[9]:
    company9.append(row)

#company 10

company10 = []
for row in rows[10]:
    company10.append(row)

#company 11 

company11 = []
for row in rows[11]:
    company11.append(row)

#website urls

url = "https://tools.usps.com/zip-code-lookup.htm?byaddress"
post_url = "https://tools.usps.com/tools/app/ziplookup/zipByAddress"

#begining of reqests session

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

#company 1 verification

payload1 = {'companyName': company1[0], 'address1': company1[1],'city' : company1[2], 'state': company1[3], 'zip-byaddress' : company1[4] }
r1 = s.post(post_url, data=payload1)
if r1.text.__contains__("ADDRESS NOT FOUND"):
    rows[1].append("Invalid")
else:
    rows[1].append("Valid")

#company 2 verification

payload2 = {'companyName': company2[0], 'address1': company2[1],'city' : company2[2], 'state': company2[3], 'zip-byaddress' : company2[4] }
r2 = s.post(post_url, data=payload2)
if r2.text.__contains__("ADDRESS NOT FOUND"):
    rows[2].append("Invalid")
else:
    rows[2].append("Valid")

#company 3 verification

payload3 = {'companyName': company3[0], 'address1': company3[1],'city' : company3[2], 'state': company3[3], 'zip-byaddress' : company3[4] }
r3 = s.post(post_url, data=payload3)
if r3.text.__contains__("ADDRESS NOT FOUND"):
    rows[3].append("Invalid")
else:
    rows[3].append("Valid")

#company 4 verification

payload4 = {'companyName': company4[0], 'address1': company4[1],'city' : company4[2], 'state': company4[3], 'zip-byaddress' : company4[4] }
r4 = s.post(post_url, data=payload4)
if r4.text.__contains__("ADDRESS NOT FOUND"):
    rows[4].append("Invalid")
else:
    rows[4].append("Valid")

#company 5 verification

payload5 = {'companyName': company5[0], 'address1': company5[1],'city' : company5[2], 'state': company5[3], 'zip-byaddress' : company5[4] }
r5 = s.post(post_url, data=payload5)
if r5.text.__contains__("ADDRESS NOT FOUND"):
    rows[5].append("Invalid")
else:
    rows[5].append("Valid")

#company 6 verification

payload6 = {'companyName': company6[0], 'address1': company6[1],'city' : company6[2], 'state': company6[3], 'zip-byaddress' : company6[4] }
r6 = s.post(post_url, data=payload6)
if r6.text.__contains__("ADDRESS NOT FOUND"):
    rows[6].append("Invalid")
else:
    rows[6].append("Valid")

#company 7 verification

payload7 = {'companyName': company7[0], 'address1': company7[1],'city' : company7[2], 'state': company7[3], 'zip-byaddress' : company7[4] }
r7 = s.post(post_url, data=payload4)
if r7.text.__contains__("ADDRESS NOT FOUND"):
    rows[7].append("Invalid")
else:
    rows[7].append("Valid")

#company 8 verification

payload8 = {'companyName': company8[0], 'address1': company8[1],'city' : company8[2], 'state': company8[3], 'zip-byaddress' : company8[4] }
r8 = s.post(post_url, data=payload4)
if r8.text.__contains__("ADDRESS NOT FOUND"):
    rows[8].append("Invalid")
else:
    rows[8].append("Valid")

#company 9 verification

payload9 = {'companyName': company9[0], 'address1': company9[1],'city' : company9[2], 'state': company9[3], 'zip-byaddress' : company9[4] }
r9 = s.post(post_url, data=payload4)
if r9.text.__contains__("ADDRESS NOT FOUND"):
    rows[9].append("Invalid")
else:
    rows[9].append("Valid")

#company 10 verification

payload10 = {'companyName': company10[0], 'address1': company10[1],'city' : company10[2], 'state': company10[3], 'zip-byaddress' : company10[4] }
r10 = s.post(post_url, data=payload10)
if r10.text.__contains__("ADDRESS NOT FOUND"):
    rows[10].append("Invalid")
else:
    rows[10].append("Valid")

#company 11 verification

payload11 = {'companyName': company11[0], 'address1': company11[1],'city' : company11[2], 'state': company11[3], 'zip-byaddress' : company11[4] }
r11 = s.post(post_url, data=payload11)
if r11.text.__contains__("ADDRESS NOT FOUND"):
    rows[11].append("Invalid")
else:
    rows[11].append("valid")


csv_file = open('C:\\Users\\tyler\\Documents\\Python Quiz Input - Sheet1.csv', 'w', newline="")
csvwriter = csv.writer(csv_file, delimiter=",")
for row in rows:
    csvwriter.writerow(row)
file.close()