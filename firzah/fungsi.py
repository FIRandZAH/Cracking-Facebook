import requests,json,os,sys,random,datetime,time,re
from time import sleep as turu
tokene = []
ses = requests.Session()
gr = '\033[1;32;41m'
k = '\033[33m'
w = '\033[1;37m'
g = '\033[1;32m'
r = '\033[1;31m'
b = '\033[1;34m'
p = '\033[1;35m'
c = '\033[1;36m'
y = '\033[1;33m'
reset = '\033[0m'
warna_warni = random.choice([g, r, b, p, y])
tanda = f'{p}[{w}+{p}]{w}'
def res():
	pilihan = f"""{tanda} 1. Hasil CP
{tanda} 2. Hasil OK
{tanda} 0. kembali"""
	cetak_panel(pilihan, 60)
	kz = input(f'{tanda} input:{g} ')
	if kz in ['1','01']:
		try:vin = os.listdir('/storage/emulated/0/FIRZAH/CP')
		except FileNotFoundError:
			print(f'{tanda} File Tidak Di Temukan ')
			time.sleep(3)
			exit()
		if len(vin)==0:
			print(f'{tanda} Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('/storage/emulated/0/FIRZAH/CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{tanda} '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+w)
				else:
					lol.update({str(cih):str(isi)})
					print(f'{tanda} '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+w)
			geeh = input(f'{tanda} input:{g} ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{tanda} Pilih Yang Bener sayang ')
				exit()
			try:lin = open('/storage/emulated/0/FIRZAH/CP/'+geh,'r').read().splitlines()
			except:
				print(f'{tanda} File Tidak Di Temukan ')
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{tanda} CP\033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			input(f'{tanda} Back Enter ')
			log_zar()
	elif kz in ['2','02']:
		try:vin = os.listdir('/storage/emulated/0/FIRZAH/OK')
		except FileNotFoundError:
			print(f'{tanda} File Tidak Di Temukan ')
			time.sleep(2)
			exit()
		if len(vin)==0:
			print(f'{tanda} Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('/storage/emulated/0/FIRZAH/OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{tanda} '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+w)
				else:
					lol.update({str(cih):str(isi)})
					print(f'{tanda} '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+w)
			geeh = input(f'{tanda} input:{g} ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{tanda} Pilih Yang Bener sayang ')
				exit()
			try:lin = open('/storage/emulated/0/FIRZAH/OK/'+geh,'r').read().splitlines()
			except:
				print(f'{tanda} File Tidak Di Temukan ')
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{tanda} OK\033[32m {cpkuni[0]}|{cpkuni[1]}|\033[32m{cpkuni[2]}\033[0m')
				nocp +=1
			input(f'{tanda} Back Enter ')
			log_zar()
	elif kz in ['0','00']:
		log_zar()
	else:
		printf(f'{tanda} Pilih Yang Bener sayang ')
		exit()

def zahra_animasi2(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.10)
def zahra_animasi3(berjalan):
    for gas in str(berjalan) + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.0010)
def cetak_panel(teks, lebar):
    garis_atas = (f'{g}~{w}') * lebar
    teks_tengah = teks.center(lebar)
    garis_bawah = (f'{g}~{w}') * lebar

    panel = f"{garis_atas}\n{teks_tengah}\n{garis_bawah}"
    print(panel)
