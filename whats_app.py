#this is whats app msg generatyed fopr my loove hope its funny for you
import selenium 
driver=Webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
name=input("ENTER USER NAME")
mag=input("your massage")
count=int(input("how many time you wants to say"))
input("enter input after scanning Qr code")
user=driver.find_element_by_xpath('//span@[title="{}"]'.format(name))
user.click()
msg_box=driver.find_element_by_class_name("input-container")
for i in range(count):
    msg_box.send_key('msg')
    button=driver.find_element_by_class_name("compose-btn-send")
    button.click()