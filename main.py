import requests,json,os,sys,random,datetime,time,re
from time import sleep as turu
from firzah import metode
from firzah import fungsi as cek
from firzah_logo import fungsi
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
def cokzar():
    try:
        os.system('clear')
        fungsi.banlog()
        cok = {'cookie': input(f'{tanda} ENTER COOKIE:{g} ')}
        link = ses.get('https://www.facebook.com/adsmanager/manage/campaigns' , cookies = cok).text
        gx = re.search("act=(.*?)&nav_source",str(link)).group(1)
        get = ses.get('https://www.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(gx), cookies = cok).text
        tok = re.search('accessToken="(.*?)"',str(get)).group(1)
        open(".tokzar.txt", "w").write(tok)
        open(".cokzar.txt", "w").write(cok['cookie'])
        print(''+tanda+' TOKEN: '+g+'{}'.format(tok))
        zahra_animasi2(f'{tanda} Login berhasil! Jalankan ulang scriptnya')
        exit()
    except(Exception) as e:
        print(f'{tanda} Cookies Mokad') ; time.sleep(3)
        print(e)
        log_zar()
def log_zar():
    try:
        token = open('.tokzar.txt','r').read()
        cok = open('.cokzar.txt','r').read()
        tokene.append(token)
        try:
            gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokene[0], cookies={'cookie':cok})
            nteng = json.loads(gerap.text)['id']
            zara(nteng)
        except KeyError:
            cokzar()
        except requests.exceptions.ConnectionError:
            exit()
    except IOError:
        cokzar()
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

def zara(id):
    try:
        cok = open('.cokzar.txt','r').read()
    except IOError:
        cokzar()
    os.system('clear')
    fungsi.banzar()
    pilihan = f"{tanda} {w}1. crack\n{tanda} {w}2. crack mail\n{tanda} 3. cek hasil crack\n{tanda} 0. keluar hapus cookie"
    cetak_panel(pilihan, 60)
    zahra = input(f'{tanda} input:{g} ')
    if zahra == '1':
        metode.nge_krek2()
    elif zahra == '3':
        cek.res()
    elif zahra == '2':
        metode.mail()
    elif zahra == '0':
        zahra_animasi2(f'{tanda} sedang menghapus cookie')
        turu(3)
        tokenku='.tokzar.txt'
        cokiku='.cokzar.txt'
        if os.path.exists(tokenku):
            os.remove(tokenku)
        if os.path.exists(cokiku):
            os.remove(cokiku)
        log_zar()
    else:
        log_zar()
def aku():
    os.makedirs('/storage/emulated/0/FIRZAH', exist_ok=True)
    os.makedirs('/storage/emulated/0/FIRZAH/CP', exist_ok=True)
    os.makedirs('/storage/emulated/0/FIRZAH/OK', exist_ok=True)
    os.makedirs('/storage/emulated/0/FIRZAH/DUMP', exist_ok=True)
    log_zar()
aku()
