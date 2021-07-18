import requests

from bs4 import BeautifulSoup
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"
	}
GS_url="https://www.google.com/search?q="

Count=input("Enter country name or gov site::|>")

print("[+]Choose Option[+]")
print("    [1]Docker(1)")
print("      [2]Docker(2)")
print("        [3]Docker(3)")
Dork=input("Enter your choice number::")
fff=("id=")
if Dork == "1" :
    list=[]
    D_url1="Inurl:/php?id=?"
    W1_url=GS_url+D_url1+Count
    work1 = requests.get(W1_url, headers=headers)
    data=work1.text
    soup=BeautifulSoup(data, "html.parser")
    for text in soup.find_all('a', href=True):
        list.append(text.get('href'))
    filter=input("Enter, what you want to filter word::|>")
    for txt in list:
        if filter in txt:
            print("[++]Found[++]")
            print(txt)
            print("")

else:
     print("Coming Soon")
 
