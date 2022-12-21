import sublist3r,subprocess,requests,sys,re,argparse
from art import *

# banner

tprint("Cygnus")
print()

# Instantiate the parser

parser = argparse.ArgumentParser(description='Optional app description')

parser.add_argument('-d',help='domain/url name to enumerate')
parser.add_argument('-f',help='file path to enumate the domains in it')
parser.add_argument('-m',help='more domains to find on the target ')


args = parser.parse_args()


if not args.d and not args.f:
    print("use -h flag for how to use")
    exit()

# using crt.sh for find subdomains

print("using crt.sh to find subdomains ...")

r = requests.get("https://crt.sh/?q=" + args.d).text

myregex = r'(?:[a-zA-Z0-9*](?:[a-zA-Z0-9*\-]{,61}[a-zA-Z0-9*])?\.)+[a-zA-Z*]{2,6}'

domains = re.findall(myregex, r)

remove = ['sectigo.com', 's.png', 'github.com', 'GitHub-Mark-32px.png','crt.sh', 'crt.sh', 'fonts.googleapis.com', 'span.headin', 'span.title', 'span.text', 'span.whiteo', 'table.option', 'td.outer', 'th.outer', 'th.headin', 'th.option', 'td.option', 'td.text', 'td.headin', 'table.lint', 'crt.sh', 'feed-icon-28x28.png', 'crt.sh', 'WILGUS.JEREMY.BRANDO', 'DOCHERTY.TIMOTHY.JAMES']

crtsh = list(set(domains) - set(remove))


# wildcards enumeration

wildcards = []


for dom in crtsh:

    if dom.endswith(args.d):
        print(dom)

    if dom.startswith("*"):
        wildcards.append(dom)



# get more targets
# install using pip


# print("using sublist3r to find domains ...")
# sublist3rd = sublist3r.main(args.d, 40, None, ports=None, silent=True, verbose= False, enable_bruteforce= False, engines=None)

# star enumerate form crt.sh and not star
# ready for diresearch
# wildcards of not

#    if dom.endswith(args.d):
#        print(dom)

# amass.decode('utf8', 'strict') + 
# print("using amass for subdomain enumerations ...")
# cmd = "amass enum -d " + args.d
# proc = subprocess.Popen([cmd], stdout=subprocess. PIPE, shell=True)
# (amass, err) = proc.communicate()
