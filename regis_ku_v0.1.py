#!/usr/bin/python
#-*-coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
with requests.Session() as session:
	# username = input("username : ")
	# password = input("password : ")
	username = "b5610503850"
	password = "ce-leb2raTe"
	payload_login = {
		"form_username" : username,
		"form_password": password,
		"zone":"0"
	}
	code = "01999141" 
	# code = input("Code : ")
	Lc_Section = "1"	
	# Lc_Section = input("Lc_Section: ")
	Lc_Credit = "3"
	# Lc_Credit = input("Lc_Credit : ")
	Lb_Section = "0"
	# Lb_Section = input("Lb_Section : ")
	Lb_Credit = "0"
	# Lb_Credit = input("Lb_Credit : ")
	Cred_Lec = Lc_Credit
	Cred_Lab = Lb_Credit
	print ("waiting...")

	headers = {
		"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding" : "gzip, deflate, br",
		"Accept-Language" : "en-US,en;q=0.8,th;q=0.6",
		"Cache-Control" : "max-age=0",
		"Connection" : "keep-alive",
		"Content-Length" : "58",
		"Content-Type" : "application/x-www-form-urlencoded",
		"Cookie":"AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=793872103%7CMCIDTS%7C17045%7CMCMID%7C05514100316205076959059793530602370672%7CMCAID%7CNONE%7CMCAAMLH-1473243783%7C3%7CMCAAMB-1473243783%7Chmk_Lq6TPIBMW925SPhw3Q; PHPSESSID=h544c61nmbjq9r7ufi6k1r70u4; __utmt=1; __utma=128244814.2018729027.1472815521.1484331817.1484377623.10; __utmb=128244814.45.10.1484377623; __utmc=128244814; __utmz=128244814.1472815521.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
		"Host" : "std.regis.ku.ac.th",
		"Origin" : "https://std.regis.ku.ac.th",
		"Referer" : "https://std.regis.ku.ac.th/_Login.php",
		"Upgrade-Insecure-Requests" : "1",
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
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
	
	login = session.post("https://std.regis.ku.ac.th/_Login.php", data=payload_login ,headers=headers)
	# r = session.get("https://std.regis.ku.ac.th/_Member_Information.php") # check login
	session.post("https://std.regis.ku.ac.th/inst_regis.php", data=payload_add ,headers=headers)
	session.get("https://std.regis.ku.ac.th/_Student_Registration.php") # check login

