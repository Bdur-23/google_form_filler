from selenium import webdriver
import time,random

total = 132

#3 different percentages of questions for 3 pages

flt = [[1]*round((5/total)*100) + [2]*round((96/total)*100),
       [1]*round((4/total)*100) + [2]*round((8/total)*100) + [3]*round((9/total)*100) + [4]*round((39/total)*100) + [5]*round((42/total)*100),
       [1]*round((39/total)*100) + [2]*round((49/total)*100) + [3]*round((11/total)*100) + [4]*round((2/total)*100),
       [1]*round((3/total)*100) + [2]*round((28/total)*100) + [3]*round((33/total)*100) + [4]*round((37/total)*100),
       [2]*total,
       [5]*total,
       [1]*round((3/total)*100) + [2]*round((12/total)*100) + [3]*round((44/total)*100) + [4]*round((43/total)*100),
       [1]*round((37/total)*100) + [2]*round((45/total)*100) + [3]*round((19/total)*100),
       [1],
       [1]*round((14/total)*100) + [2]*round((71/total)*100) + [3]*round((16/total)*100)]

for i in flt:
  random.shuffle(i)


slt = [[1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100)]

for i in slt:
  random.shuffle(i)


tlt = [[1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100),
       [1]*round((20/total)*100) + [2]*round((20/total)*100) + [3]*round((20/total)*100) + [4]*round((20/total)*100) + [5]*round((20/total)*100)]

#it enters the answers randomly so in statistics it seems random
for i in tlt:
  random.shuffle(i)

#opening chrome by selenium
web = webdriver.Chrome()
for _ in range(2):

  web.get("https://docs.google.com/forms/d/e/1FAIpQLSczgJ7b24UlVRNtpRPfuizKw2kHekcRC-iphyyQFNY5-kI2rA/viewform")
  web.maximize_window()

#for first page
  for i in range(10):
    if i == 8:
      continue
    u = flt[i].pop(random.randrange(len(flt[i])))
    if i == 9 and (u in [2,3]):
      web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span').click()
    if i == 9 and (u in [1,3]):
      web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span').click()
      
    web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{i+1}]/div/div/div[2]/div/div/span/div/div[{u}]/label/div/div[2]/div/span').click()

  web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span').click() 

#for second page
  for i in range(14):
    u = slt[i].pop(random.randrange(len(slt[i])))
    web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{i+2}]/div/div/div[2]/div/span/div/label[{u}]/div[2]/div/div/div[3]/div').click()

  web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span').click()

#for third page
  for i in range(8):
    u = tlt[i].pop(random.randrange(len(tlt[i])))
    web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{i+2}]/div/div/div[2]/div/span/div/label[{u}]/div[2]/div/div/div[3]/div').click()

  web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span').click()








