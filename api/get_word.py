import urllib.request as url
def randomWord():
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = url.Request("https://www.palabrasaleatorias.com/mots-aleatoires.php?fs=10&fs2=0&Submit=Nouveau+mot", headers=hdr)
    page = url.urlopen(req)
    page = page.read().decode("utf-8")

    mots = []
    page = page.split('\n')
    mots.append(page[133])
    mots.append(page[148])
    mots.append(page[163])
    mots.append(page[178])
    mots.append(page[193])
    mots.append(page[208])
    mots.append(page[223])
    mots.append(page[238])
    mots.append(page[253])
    mots.append(page[268])
    
    return mots