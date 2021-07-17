import requests

from bs4 import BeautifulSoup

GS_url="https://www.google.com/search?q="
list=[]

Count=raw_input("Enter country name::")

print("[+]Choose Option[+]")
print("[1]Docker(1)")
print("[2]Docker(2)")
print("[3]Docker(3)")
Dork=input("Enter your choice number::")

if Dork == 1 :
  
    D_url1="Inurl:/php?id=?"
    W1_url=GS_url+D_url1+Count
    work1 = requests.get(W1_url)
    data=work1.text
    soup=BeautifulSoup(data)
    for text in soup.all_find('a'):
        list.append(text.get('href'))
    filter=raw_input("Enter, what you want to filter word::|>")
    for txt in list:
        if filter in txt:
            print("Found::|>",txt)
        else:
            print("Not Found")
            break()
             

else:
     print("Coming Soon")
 
