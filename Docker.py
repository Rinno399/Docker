import requests

from bs4 import BeautifulSoup
headers = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 9; JKM-LX2 Build/HUAWEIJKM-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36"
	}
GS_url="https://www.google.com/search?q="
list=[]
filter = "id"
Count=raw_input("Enter country name::")

print("       [+]Choose Option[+]")
print("    [1]Docker(1)")
print("  [2]Docker(2)")
print("[3]Docker(3)")
Dork=input("Enter your choice number::|>")

if Dork == 1 :
  
    D_url1="Inurl:/php?id=?"
    W1_url=GS_url+D_url1+Count
    work1 = requests.get(W1_url)
    data=work1.text
    soup=BeautifulSoup(data, "html.parser")
    for text in soup.find_all('a'):
        list.append(text.get('href'))
        for text in list:
            if filter in text:
                print("!!!Found!!!",Count)
                print(text)
                print("")

else:
     print("Coming Soon")
 
