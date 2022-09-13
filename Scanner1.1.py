# -*- coding: utf-8 -*-

import os
import time
from pyfiglet import Figlet
from optparse import OptionParser
from poc import new
from concurrent.futures import ThreadPoolExecutor

if __name__ == '__main__':
	# os.system('@echo off')
	os.system('chcp 936 >nul')
	f=Figlet(font='slant')
	print('\033[31m====================================================\033[0m')
	print('\033[34m{}\033[0m'.format(f.renderText('Scanner')))
	print('   \033[33mAuthor:LuckyRiver  ver:1.1  time:2022-09-08\033[0m')
	print('\033[31m====================================================\033[0m'+'\n')
	usage="\n"+"python3 %prog -u url"+"\n"+"python3 %prog -u url -t num"+"\n"+"python3 %prog -f url.txt"+"\n"+"python3 %prog -f url.txt -t"
	parser=OptionParser(usage=usage)
	parser.add_option('-u','--url',dest='url',help="target url")
	parser.add_option('-f','--file',dest='file',help="url file")
	parser.add_option('-t','--thread',type="int",dest='threads',help="thread number")
	(options,args)=parser.parse_args()
	start = time.time()

	if options.file:
		f=open(options.file,'r', encoding='utf-8')
		urls=f.readlines()
		thread_num = options.threads
		with ThreadPoolExecutor(max_workers=thread_num) as executor:
			for url in urls:
				url=url.strip('\n')
				# print(url)
				new.check(url)
		print('\033[34m[#]扫描已完成\033[0m')
	end = time.time()
	print("总耗时:", end - start, "秒")

	if options.url:
		new.check(options.url)
		print('\033[34m[#]扫描已完成\033[0m')
