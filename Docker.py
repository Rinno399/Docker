import request

from bs4 import BeautifulSoup

GS_url="https://www.google.com/search?q="
list=[]

Count=input("Enter country name::")

print="[+]Choose Option[+]"
print="[1]Docker(1)"
print="[2]Docker(2)"
print="[3]Docker(3)"
Dork=str(input("Enter your choice number::")

if Dork == 1:
    (
    D_url1="Inurl:/php?id=?"
    W1_url=GS_url+D_url+Count
    work1 = requests.get(W1_url)
    data=work1.text
    soup=BeautifulSoup(data)
    for text in soup.all_find('a')
        re = text.get('href')
        print("Found::|>",re)
    filter=raw_input("Enter, what you want to filter word::|>")
    list.append(re)
    for text in list:
        if filter in text:
            print("Found:|>",text)
   ) 
else:
     (
     print("Coming Soon")
     ) 
