from time import sleep
from cloudscraper import CloudScraper as Session
from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.errors import ElementNotFoundError

def isDuplicate():
    ip = Session().get('https://ip.oxylabs.io').text
    return ip in Session().get('https://ip-limiter-server.onrender.com/used').text

def addToDB():
    ip = Session().get('https://ip.oxylabs.io').text.replace('\n', '')
    return 'true' in Session().get('https://ip-limiter-server.onrender.com/add?ip=' + ip).text

def run_telegram_bot(link, proxy=None, headless=None):
    d = isDuplicate()
    if d:
        print('Error in TelegramLinks: Duplicate View')
        return
    options = ChromiumOptions()
    options.auto_port()
    options.set_argument('--start-maximized', True)

    page = ChromiumPage(options)
    # ============ Test ============
    # page.get('https://tiny.cc/mjqsxz')
    # input('Press Enter when VPN Connected...')
    # ============ End ============
    page.get('https://freegamer.blogspot.com/robots.txt')
    page.run_js(f'window.location.href = "{link}"')
    sleep(2)
    page.wait.doc_loaded()
    if '403 Forbidden' in page.title:
        page.quit()
        raise Exception('IP not allowed. 403 Forbidden Error!')
    btn6 = page.ele('#btn6')
    if not btn6:
        page.quit()
        raise Exception('`Continue` button is not found.')
    while btn6:
        page.run_js('''[...document.querySelectorAll('[style*="none"]')].forEach(function(e){e.removeAttribute('style')})''')
        try:
            btn6 = page.ele('#btn6')
            if btn6: btn6.click()
        except ElementNotFoundError:
            pass
        sleep(5)
    
    getLink = page.ele('css:.get-link')
    if not getLink:
        page.quit()
        raise Exception('Get Link button not found!')
    page.run_js(bypassFocusTimerJS)
    disabled = True
    while disabled: disabled = page.run_js("document.querySelector('.get-link').classList.contains('disabled')", as_expr=True)
    getLink.click()
    sleep(3)
    page.quit()
    if not d: addToDB()
    print('Telegram Links:', 'All Done')
    
        

bypassFocusTimerJS = '''for (event_name of ["visibilitychange", "webkitvisibilitychange", "blur"]) {window.addEventListener(event_name, function(event) {event.stopImmediatePropagation()}, true)} Object.defineProperty(document, 'visibilityState', {value: 'visible', writable: true});Object.defineProperty(document, 'hidden', {value: false, writable: true});document.dispatchEvent(new Event("visibilitychange"));'''


if __name__=='__main__':
    #from proxyscrape import get_session
    from all_links import random_telegramlinks
    print(random_telegramlinks)
    run_telegram_bot(random_telegramlinks)


