import os, sys

print ("\033[1;32mSilahkan Masukkan Nama Admin& Password Admin")

print ("\033[1;32atau silahkan Hubungi Mr.004 No Wa 081228244243 ")

username = 'Mr.004'      

password = 'Dia Newbie'



		if pwd == password:

			print "\033[1;32mAlhmdllh sudah masuk juga..", 

			sys.exit()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

## santet-online 08-03-2018 (12:12)
# -*- coding: utf-8 -*-
# BlackHole Security
##
import time
from core.misc import *
from core.onlen import *

clearscreen()
logo()
print """
Select from the menu Mr.004 
  01) Jangan Nyantet Goblok Dosa
  02) Kalau Mau Kaya Ya Kerja Asw
  03) Doakan Dia Yang Terbaik
  04) Minta Ama Yang Maha Kuasa
  05) Jangan Kebaykan Carding Asw 
  
  00) Exit the Santet Goblok
"""
santet = raw_input("santet > ")

if santet == "01" or santet == "1":
	netcat_rat()
elif santet == "02" or santet == "2":
	facebookgroup_hijack()
elif santet == "03" or santet == "3":
	sms_bomber_jdid()
elif santet == "04" or santet == "4":
	sms_spoof_elk()
elif santet == "05" or santet == "5":
	denialofservice_attack()
else:
	print "\nERROR: Wrong Input..."
	time.sleep(2)
	restart_program()