import urllib.request as url

def randomWord(lang):
    """Take the words by scrapping on PALABRASALEARORIAS website

    Args:
        lang (str): the lang of the words

    Returns:
        str: the words random generated
    """
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    
    if lang == 'fr':
        req = url.Request("https://www.palabrasaleatorias.com/mots-aleatoires.php?fs=10&fs2=0&Submit=Nouveau+mot", headers=hdr)
        lines = [133,148,163,178,193,208,223,238,253,268]
        
    elif lang == 'en':
        req = url.Request("https://www.palabrasaleatorias.com/random-words.php?fs=10&fs2=0&Submit=New+word", headers=hdr)
        lines = [134,149,164,179,194,209,224,239,254,269]
        
    page = url.urlopen(req)
    page = page.read().decode("utf-8")
    mots = []
    page = page.split('\n')
    
    for line in lines:
        mots.append(page[line])
    
    return mots
