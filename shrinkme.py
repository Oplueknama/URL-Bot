from requests import Session
from bs4 import BeautifulSoup
from time import sleep

def run_shrinkme_bot(link, proxy=None, headless=None):
    s=Session()
    s.proxies={'http':proxy,'https':proxy}
    base_domain = 'shrinke.us'
    replace_with = 'en.shrinke.me'
    org_refer_url ='https://thekisscartoon.com'
    refer_url = 'https://themezon.net'

    s.cookies.set('ab','2', domain='.'+replace_with.split('/')[0])
    ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    
    hl=link
    while hl:
        r0 = s.get(hl, headers={'User-Agent': ua, 'Referer': org_refer_url}, allow_redirects=False)
        hl = r0.headers.get('Location')
    
    r1=s.get(link.replace(base_domain, replace_with), headers={'User-Agent': ua, 'Referer': refer_url})
    html=r1.text
    #print(html)
    soap=BeautifulSoup(html, 'html.parser')
    form_inputs = soap.select('form#go-link input')
    input_dict = {}
    for elem in form_inputs:
        input_dict[elem.get('name')] = elem.get('value')
    try:
        sleep(int(soap.select_one('#timer').text.strip()))
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except:
        import traceback
        print(traceback.format_exc(), '\n\n', html)
    
    r2=s.post(f'https://{replace_with}/links/go', data=input_dict, headers={'User-Agent': ua, 'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/x-www-form-urlencoded'})
    print('ShrinkMe:', r2.text)


if __name__ == "__main__":
    from all_links import random_shrinkme
    run_shrinkme_bot(random_shrinkme, headless=False)