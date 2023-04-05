from selenium.webdriver.common.by import By


class loginpage:
    myaccountlink = "My Account"
    loginlink = "Login"
    enterusername = "input-email"
    enterpassword = "input-password"
    submitbutton = "//button[@type='submit']"

    def __int__(self, driver):
        self.driver = driver

    def clickonmyaccountlink(self):
        self.driver.find_element(By.LINK_TEXT, self.myaccountlink).click()

    def clickonloginlink(self):
        self.driver.find_element(By.LINK_TEXT, self.loginlink).click()

    def clickonenteremail(self, username):
        self.driver.find_element(By.ID, self.enterusername).send_keys(username)

    def clickonenterpassword(self, password):
        self.driver.find_element(By.ID, self.enterpassword).send_keys(password)

    def clickonsubmit(self):
        self.driver.find_element(By.XPATH, self.submitbutton).click()
