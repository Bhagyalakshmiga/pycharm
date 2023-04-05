from selenium.webdriver.common.by import By

class registration:
    myaccountlink="My Account"
    registrationlink="Register"
    enterfirstname="input-firstname"
    enterlastname="input-lastname"
    enterusername="input-email"
    enterpassword="input-password"
    checkbox="//input[@type='checkbox']"
    submitbutton="//button[@type='submit']"
    def __init__(self,driver):
          self.driver=driver
    def __len__(self):
           return len(self.enterusername)

    def clickonmyaccountlink(self):
          self.driver.find_element(By.LINK_TEXT,self.myaccountlink).click()

    def clickonregistrationlink(self):
          self.driver.find_element(By.LINK_TEXT,self.registrationlink).click()

    def clickonenterfirstname(self,fname):
           self.driver.find_element(By.ID,self.enterfirstname).send_keys(fname)

    def clickonenterlastname(self,lname):
           self.driver.find_element(By.ID,self.enterlastname).send_keys(lname)

    def clickonenterusername(self,uname):
           self.driver.find_element(By.ID, self.enterusername).send_keys(uname)

    def clickonenterpassword(self,password):
          self.driver.find_element(By.ID, self.enterpassword).send_keys(password)

    def clickoncheckbox(self):
          self.driver.find_element(By.XPATH,self.checkbox).click()
    def clickonsubmitbutton(self):
          self.driver.find_element(By.XPATH,self.submitbutton).click()
