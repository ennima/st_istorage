import os
import pandas as pd
from ftplib import FTP
from ftplib import all_errors
from subprocess import call
from time import time as time_i
import time
from datetime import datetime
import socket
import json, urllib

istorage = "192.168.196.99"
istorage_user = "archivo"
istorage_pass = "archivo01"

stratus = "192.168.196.139"
stratus_user = "mxfmovie"
stratus_pass = ""


json_data=open("conf.json").read()

conf_data = json.loads(json_data)
istorage_conf = conf_data['lic_server']+":"+conf_data['lic_file_port']+conf_data['lic_path']
print(istorage_conf)

try:
	with urllib.request.urlopen(istorage_conf) as url:
		data_istorage = json.loads(url.read().decode())
		istorage = data_istorage['istorage_host']
		istorage_user = data_istorage['istorage_user']
		istorage_pass = data_istorage['istorage_pass']
except Exception as e:
	print("#Error: Problema con el servidor de licencias -> ",e)

	

print(istorage+" : "+istorage_user)


# 1  get media name and path in stratus

media_name = "HEROE CHILANGO-FT_DF00546I"
media_path = "Noticias"
media_created = "8/17/2017 11:15:47 PM"

# 2  get media to local computer

print("Descargando.")
tiempo_inicial = time.time()
ftp = FTP(stratus)
print(ftp.login(stratus_user,stratus_pass))
ftp.cwd(media_path)
ftp.retrlines('LIST')
print("Descargando: "+media_name)


try:
	# print('RETR \''+archivo_down+'\'')
	ftp.retrbinary('RETR '+media_name, open(media_name, 'wb').write)
	download_success = True
except all_errors as e:
	print(e)

ftp.quit()
print( media_name + " listo para ingestar.") 

# 3  get metadata to media
# 4  send media to istorage
# 5  save metadata local
# 6  save metadata istorage