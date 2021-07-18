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
  
    for txt in list:
        if fff in txt:
            print("[++]Found[++]")
            print(txt)
            print("")

elif Dork == "2" :
    list2=[]
    D_url2="inurl page.php? id= site:"
    W2_url=GS_url+D_url2+Count
    work2 = requests.get(W2_url, headers=headers)
    data2=work2.text
    soup2=BeautifulSoup(data2, "html.parser")
    for text in soup2.find_all('a', href=True):
        list2.append(text.get('href'))
  
    for txt in list2:
        if fff in txt:
            print("[++]Found[++]")
            print(txt)
            print("")
elif Dork == "3" :
    list3=[]
    D_url3="inurl index.php?id="
    W3_url=GS_url+D_url3+Count
    work3 = requests.get(W3_url, headers=headers)
    data3=work3.text
    soup3=BeautifulSoup(data3, "html.parser")
    for text in soup3.find_all('a', href=True):
        list3.append(text.get('href'))
  
    for txt in list3:
        if fff in txt:
            print("[++]Found[++]")
            print(txt)
            print("")
else:
    print("Something wrong")
 
