import requests
URL  = 'https://www.amazon.in/Laptops/b?ie=UTF8&node=1375424031&ref_=sd_allcat_sbc_mobcomp_laptops'
page  = requests.get(URL)
f = open("am_file.txt", 'w')
f.write(page.text)
f.close()