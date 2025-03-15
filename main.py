from cloudscraper import CloudScraper as Session
from all_links import *
# from telegramlinks import run_telegram_bot
# from arolinks import run_arolink_bot
from teraboxlinks import run_terabox_bot
from nanolinks import run_nano_bot
# from adrinolinks import run_adrino_bot
# from kingurl import run_kingurl_bot
# from udlinks import run_udlinks_bot
# from malink import run_malink_bot
# from zagl import run_zagl_bot
from random import randint
import urllib3, threading
from time import sleep
Thread=threading.Thread

d={'e':''}

def excepthook(l):
    d['e']+=str(l.exc_value) + '\n\n'

def isDuplicate():
    ip = Session().get('https://ip.oxylabs.io').text
    return ip in Session().get('https://ip-limiter-server.onrender.com/used').text

def addToDB():
    ip = Session().get('https://ip.oxylabs.io').text.replace('\n', '')
    return 'true' in Session().get('https://ip-limiter-server.onrender.com/add?ip=' + ip).text

threading.excepthook=excepthook

def main(proxy=None, **kw):
    t=[]
    # t.append(Thread(target=lambda: run_terabox_bot(random_teraboxlinks, proxy, **kw)))
    # t.append(Thread(target=lambda: run_nano_bot(random_nanolinks, proxy, **kw)))
    # t.append(Thread(target=lambda: run_arolink_bot(proxy, **kw)))
    # t.append(Thread(target=lambda: run_adrino_bot(random_adrino, proxy, **kw)))
    # t.append(Thread(target=lambda: run_udlinks_bot(random_udlinks, proxy, **kw)))
    # t.append(Thread(target=lambda: run_malink_bot(random_malink, proxy, **kw)))
    # t.append(Thread(target=lambda: run_zagl_bot(random_zagl, proxy, **kw)))
    # if not isDuplicate():
        # t.append(Thread(target=lambda: run_kingurl_bot(random_kingurl, None, **kw)))
        # t.append(Thread(target=lambda: run_telegram_bot(random_telegramlinks, None, **kw)))
        # addToDB()
    # else: print('Skipping some thread for duplicate view.')

    for v in t: v.start()
    for v in t: v.join()
    
    if d['e']!='': raise Exception(d['e'])
    from DrissionPage import ChromiumPage
    page = ChromiumPage()
    page.get('https://flixwonders.com')
    page.actions.move(300, 300)
    for i in range(100):
        sleep(0.1)
        x = randint(50, 200)
        y = randint(50, 200)
        page.actions.move(-x, -y)
        page.actions.move(x, y)
        page.actions.scroll(randint(10, 30))
    # page.actions.click()
    # Slow earning speed
    sleep(10)



if __name__ == '__main__':
    main()
