from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time

s = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeGUsVprVjSQeb_Og3NMdkoydms8TsXYazNSIIJSZG6Wc2G0g/viewform")

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# Enter Email Address
email_address = "emanfatima0060@gmail.com"
email = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
email.click()
email.send_keys(email_address)
time.sleep(1)

# Select Gender
gender = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label')
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label - Male
gender.click()
time.sleep(1)

# Age
age = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]/label')
age.click()
time.sleep(1)

# Education Level
education = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]/label')
# browser,find_element_by_css_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label')
education.click()
time.sleep(1)

# Name of Organization
organization = "Continental Call Center Pvt. Ltd"
email = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
email.click()
email.send_keys(organization)
time.sleep(1)

# Department
dept = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[6]/label')
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label - HR
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[4]/label - ME
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[5]/label - PM
dept.click()
time.sleep(1)

# Time
timey = "2 Years"
email = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
email.click()
email.send_keys(timey)
time.sleep(1)

# Position Level
pl = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[4]/label')
pl.click()
time.sleep(1)

# Next Button
next_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
next_btn.click()
time.sleep(2)

# Mentor Recommended
mr = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label')
mr.click()
time.sleep(1)

# My mentor recommended me
mr1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span')
mr1.click()
time.sleep(1)

# Supported me
sm = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label')
sm.click()
time.sleep(1)

# My mentor has alerted me
mam = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label')
mam.click()
time.sleep(1)

# My mentor has helped me
mhm = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label')
mhm.click()
time.sleep(1)

# My mentor has kept me informed
mki = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label')
mki.click()
time.sleep(1)

# My mentor has discussed concerns
mdc = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label')
mdc.click()
time.sleep(1)

# My mentor has encouraged me
mem = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label')
mem.click()
time.sleep(1)

# My mentor has conveyed empathy
mce = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label')
mce.click()
time.sleep(1)

# My mentor has conveyed feelings
mcf = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[1]/label')
mcf.click()
time.sleep(1)

# My mentor has shared personal experiences
mspe = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[1]/label')
mspe.click()
time.sleep(1)

# My mentor has discussed my concerns
mdmc = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[1]/label')
mdmc.click()
time.sleep(1)

# Model my behavior
mmb = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[1]/label')
mmb.click()
time.sleep(1)

# admire my mentor's ability
amma = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div/span/div/div[1]/label')
amma.click()
time.sleep(1)

# respect my mentor's knowledge
rmk = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[1]/label')
rmk.click()
time.sleep(1)

# respect my mentor's ability to teach and instruct others
rmati = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[1]/label')
rmati.click()
time.sleep(1)

# Next Button p2
next_btnp2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
next_btnp2.click()
time.sleep(2)

# Extent to which
etw = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label')
etw.click()
time.sleep(1)

# extent to which your superiors
etwys = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label')
etwys.click()
time.sleep(1)

# importance that your superiors
itys = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label')
itys.click()
time.sleep(1)

# importance that your superiors placed on including changes
ityspin = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label')
ityspin.click()
time.sleep(1)

# importance that your superiors placed on not finalizing
itysponf = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]/label')
itysponf.click()
time.sleep(1)

# importance that your superiors placed on not finalizing the amount
itysponfa = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label')
itysponfa.click()
time.sleep(1)

# Overall, the influence that you had in setting your performance standards
overall = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label')
overall.click()
time.sleep(1)

# Overall, the influence that you had in determining the amount
overall1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label')
overall1.click()
time.sleep(1)

# Next Button p3
next_btnp3 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
next_btnp3.click()
time.sleep(2)

# Others in this company at my job level
job_level = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label')
job_level.click()
time.sleep(1)

# other employers are asking employees at my job level
job_level1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label')
job_level1.click()
time.sleep(1)

# company told me I would do when I accepted this position
job_level2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label')
job_level2.click()
time.sleep(1)

# others below me in the company are asked to do
job_level3 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label')
job_level3.click()
time.sleep(1)

# my superior is asked to do
job_level4 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label')
job_level4.click()
time.sleep(1)

# Next Button p4
next_btnp4 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
next_btnp4.click()
time.sleep(2)

# systematically read the professional journals
professional = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
professional.click()
time.sleep(1)

# Other professions are actually more vital to society than mine
professional1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label')
professional1.click()
time.sleep(1)

# own decisions in regard to what is to be done in my work
professional2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label')
professional2.click()
time.sleep(1)

# Local Meetings
professional3 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label')
professional3.click()
time.sleep(1)

# essential for society
professional4 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]/label')
professional4.click()
time.sleep(1)

# fellow professionals
professional5 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label')
professional5.click()
time.sleep(1)

# People in this profession
professional6 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label')
professional6.click()
time.sleep(1)

#
professional7 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label')
professional7.click()
time.sleep(1)

#
professional8 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label')
professional8.click()
time.sleep(1)

# dedication of people
professional9 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[3]/label')
professional9.click()
time.sleep(1)

#
professional10 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[1]/label')
professional10.click()
time.sleep(1)

#
professional11 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[1]/label')
professional11.click()
time.sleep(1)

#
professional12 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[3]/label')
professional12.click()
time.sleep(1)

#
professional13 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div/span/div/div[1]/label')
professional13.click()
time.sleep(1)

#
professional14 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[1]/label')
professional14.click()
time.sleep(1)

professional15 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[3]/label')
professional15.click()
time.sleep(1)

#
professional16 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div/span/div/div[2]/label')
professional16.click()
time.sleep(1)

#
professional17 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/div/span/div/div[2]/label')
professional17.click()
time.sleep(1)

#
professional18 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/div/span/div/div[2]/label')
professional18.click()
time.sleep(1)

#
professional19 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/div/span/div/div[3]/label')
professional19.click()
time.sleep(1)

#
professional20 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/div/span/div/div[2]/label')
professional20.click()
time.sleep(1)

#
professional21 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/div/span/div/div[3]/label')
professional21.click()
time.sleep(1)

#
professional22 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/div/span/div/div[1]/label')
professional22.click()
time.sleep(1)

#
professional23 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/div/span/div/div[3]/label')
professional23.click()
time.sleep(1)

#
professional24 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/div/span/div/div[1]/label')
professional24.click()
time.sleep(1)

#
professional25 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/div/span/div/div[2]/label')
professional25.click()
time.sleep(1)

# Submit Button
submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div[2]/span/span')
submit_btn.click()
time.sleep(2)

driver.quit()