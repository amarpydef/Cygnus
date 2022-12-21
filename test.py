import requests,re

def crtsh():
    r = requests.get("https://crt.sh/?q=icloud.com" ).text
    myregex = r'(?:[a-zA-Z0-9*](?:[a-zA-Z0-9*\-]{,61}[a-zA-Z0-9*])?\.)+[a-zA-Z*]{2,6}'
    domains = re.findall(myregex, r)
    remove = ['sectigo.com', 's.png', 'github.com', 'GitHub-Mark-32px.png','crt.sh', 'crt.sh', 'fonts.googleapis.com', 'span.headin', 'span.title', 'span.text', 'span.whiteo', 'table.option', 'td.outer', 'th.outer', 'th.headin', 'th.option', 'td.option', 'td.text', 'td.headin', 'table.lint', 'crt.sh', 'feed-icon-28x28.png', 'crt.sh', 'WILGUS.JEREMY.BRANDO', 'DOCHERTY.TIMOTHY.JAMES']
    final_list = list(set(domains) - set(remove))
    print(final_list)


crtsh()