import urllib.request as url
def randomWord():
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = url.Request("https://www.palabrasaleatorias.com/mots-aleatoires.php?fs=1&fs2=0&Submit=Nouveau+mot", headers=hdr)
    page = url.urlopen(req)
    page = page.read().decode("utf-8")

    start_index = 14164
    end_index = page.find('Chercher la signification en:')-17
    title = page[start_index:end_index]

    return title