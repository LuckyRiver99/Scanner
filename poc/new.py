# -*- coding: utf-8 -*-
import re
import requests
import urllib3
import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading
from requests.packages.urllib3.exceptions import InsecureRequestWarning

logging.captureWarnings(True)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

lock = threading.Lock()

f = open("result.csv", "a", encoding='utf-8_sig')
f.write("源地址"+","+"跳转地址"+","+"状态码"+","+"标题"+'\n')
f = f.close()

def check(url,timeout=1):
	name = url
	print(name)
	header = {
		'Host': 'www.baidu.com',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
	}
	try:
		r = requests.get(url, headers=header, verify=False, allow_redirects=True, timeout=timeout)
		code = res.status_code
	except Exception as error:
		code = "无法访问"

	with lock:
		code1 = str(code)
		if code1 != "无法访问":
			try:
				urllib3.disable_warnings()
				r = requests.get(url, headers=header, verify=False, allow_redirects=True, timeout=timeout)
				r.encoding = r.apparent_encoding
				title = re.findall("(?<=\<title\>)(?:.|\n)+?(?=\<)", r.text, re.IGNORECASE)[0].strip()
			except:
				title = "[ ]"
			print(url + "," + r.url + "," + code1 + "," + title)
			with open("result.csv", "a", encoding='utf-8_sig') as f2:
				f2.writelines(url + "," + r.url + "," + code1 + "," + title + '\n')

		else:
			title = " "
			print(url + "," + " " + "," + code1 + "," + title)
			with open("result.csv", "a", encoding='utf-8_sig') as f2:
				f2.writelines(url + "," + " " + "," + code1 + "," + title + '\n')

