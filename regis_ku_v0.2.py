#!/usr/bin/python
#-*-coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
with requests.Session() as session:
	while True :
		# username = input("username : ")
		# password = input("password : ")
		username = "b5610503850"
		password = "ce-leb2raTe"
		payload_login = {
			"form_username" : username,
			"form_password": password,
			"zone":"0"
		}
		code = "01175111" 
		# code = input("Code : ")
		Lc_Section = "0"	
		# Lc_Section = input("Lc_Section: ")
		Lc_Credit = "0"
		# Lc_Credit = input("Lc_Credit : ")
		Lb_Section = "11"
		# Lb_Section = input("Lb_Section : ")
		Lb_Credit = "1"
		# Lb_Credit = input("Lb_Credit : ")
		Cred_Lec = "0"
		# Cred_Lec = Lc_Credit
		Cred_Lab = "1"
		# Cred_Lab = Lb_Credit
		print ("waiting...")

		headers = {
			"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding" : "gzip, deflate, br",
			"Accept-Language" : "en-US,en;q=0.8,th;q=0.6",
			"Cache-Control" : "max-age=0",
			"Connection" : "keep-alive",
			"Content-Length" : "58",
			"Content-Type" : "application/x-www-form-urlencoded",
			"Host" : "std.regis.ku.ac.th",
			"Origin" : "https://std.regis.ku.ac.th",
			"Referer" : "https://std.regis.ku.ac.th/_Login.php",
			"Upgrade-Insecure-Requests" : "1",
			"User-Agent" : "Mozilla/4.5 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) "
		}
		payload_add = {
			"Rg_Type":"C",
			"Lc_Section":Lc_Section,
			"Lc_Credit":Lc_Credit,
			"Q_Type1":"",
			"Lb_Section":Lb_Section,
			"Q_Type2":"2",
			"Q_Type2": "",
			"Lb_Credit":Lb_Credit,
			"Status_Add":"Y",
			"Std_Type":"1",
			"Cs_Code":code,
			"B_Cred_Lec":Cred_Lec,
			"B_Cred_Lab":Cred_Lab,
			"Code_Flag":"9",
			"Sm":"2",
			"Yr":"59",
	 		"Total_Credit":"11",
			"Chk_Course":"N",
			"drop":"Y",
			"addsubject":"Y"
		}
		success = False
		login = session.post("https://std.regis.ku.ac.th/_Login.php", data=payload_login ,headers=headers)
		checkLogin = "_Member_Information.php" in login.text
		if ( checkLogin ) :
			delay = int(input("Logged in : PASS \nDelay time : "))	
			cred= session.get("https://std.regis.ku.ac.th/_Student_RptKu.php?mode=PRTKU2") 

			time_add = 1
			if code not in cred.text :

				while code not in cred :
					time.sleep(delay)
					print ("time : %d"%time_add)
					add = session.post("https://std.regis.ku.ac.th/inst_regis.php", data=payload_add ,headers=headers)
					cred= session.get("https://std.regis.ku.ac.th/_Student_RptKu.php?mode=PRTKU2") 
					session.get("https://std.regis.ku.ac.th/_Student_Registration.php") # check login
					time_add+=1
					success = True 
				print ("success => code : %s ... %d times "%(code,time_add))

			else :
				print ("success => code : %s ... %d times "%(code,time_add))
		else :
			print("Logged in : FALSE \n Please try again ...")
		if success :
			break