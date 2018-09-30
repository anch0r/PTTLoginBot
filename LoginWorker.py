# -*- coding: utf-8 -*-
import telnetlib
import time
from Status import Status

def telnetConnect(username_, password_, statusQueue_):
	host = 'ptt.cc'
	port = 23
	username = username_
	password = password_
	statusQueue = statusQueue_
	try:
		telnet = telnetlib.Telnet(host, 23)
		time.sleep(0.5)
		content = telnet.read_very_eager().decode('big5', 'ignore')

		if u'請輸入代號' in content:
			print ('輸入帳號中...')
			telnet.write((username + '\r\n').encode('ascii') )
			time.sleep(0.5)

			content = telnet.read_very_eager().decode('big5', 'ignore')
			print(content)

			if u'請輸入您的密碼' in content:
				print('輸入密碼中...')
				telnet.write((password + '\r\n').encode('ascii') )
				time.sleep(1)

				content = telnet.read_very_eager().decode('big5', 'ignore')
				print(content)

				if u'密碼不對或無此帳號' in content:
					print('帳密錯誤')
					telnet.write(('\r\n').encode('ascii') )
					time.sleep(0.5)
					telnet.close()
					statusQueue.put(Status.STAT_LOGIN_FAILED)			

				time.sleep(1)

				if u'請按任意鍵繼續' in content:
					print ('登入成功!')
					telnet.write(('\r\n').encode('ascii') )
					time.sleep(0.5)
					telnet.close()
					statusQueue.put(Status.STAT_LOGIN_SUCCESS)

		if u'系統過載' in content:
			telnet.write(('\r\n').encode('ascii') )
			time.sleep(0.5)
			telnet.close()
			statusQueue.put(Status.STAT_SERVER_OVERLOAD)

		telnet.close()

	except OSError:
		telnet.close()
		statusQueue.put(Status.STAT_OS_ERROR)