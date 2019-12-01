from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

class signIn_Page_elements:

    def email_text_field(self):
        email = 'login_username_edittext'
        return email

    def password_field(self):
        password = 'login_password_edittext'
        return password

    def sign_in_button(self):
        signIn = "//*[@text='SIGN IN']"
        return signIn

    def intro_popup_message(self):
        intro_popup_message = "//*[@class='android.widget.LinearLayout' and (./preceding-sibling::* | ./following-sibling::*)" \
                              "[@id='view_onboarding_view_pager'] and " \
                              "./*[@class='android.widget.ImageView'] and ./parent::*[@class='android.widget.RelativeLayout']]"
        return intro_popup_message

    def proceed_arrow(self):
        proceed_arrow = "view_onboarding_forward"
        return proceed_arrow

    def get_started(self):
        get_started = "view_onboarding_tab_layout"
        return get_started

    def on_boarding_tab(self):
        on_boarding_tab = "view_onboarding_tab_layout"
        return on_boarding_tab


class signIn_Page_Locators(signIn_Page_elements):
    def __init__(self, driver):
        self.driver=driver
        self.signIn_elements = signIn_Page_elements()

    def email_text_field(self):
        email_text_field = self.driver.find_element_by_id(self.signIn_elements.email_text_field())
        return email_text_field

    def password_text_field(self):
        password_text_field = self.driver.find_element_by_id(self.signIn_elements.password_field())
        return password_text_field

    def signin_button(self):
        sign_in_button = self.driver.find_element_by_xpath(self.signIn_elements.sign_in_button())
        return sign_in_button

    def select_pop_up_message(self):
        select_pop_up_message = self.driver.find_element_by_xpath(self.signIn_elements.intro_popup_message())
        return select_pop_up_message

    def select_get_started(self):
        select_get_started = self.driver.find_element_by_id('view_onboarding_tab_layout')
        return select_get_started

    def select_proceed_arrow(self):
        select_proceed_arrow = self.driver.find_element_by_id(self.signIn_elements.proceed_arrow())
        return select_proceed_arrow

    def select_on_boarding_tab(self):
        select_on_boarding_tab = self.driver.find_element_by_id(self.signIn_elements.on_boarding_tab())
        return select_on_boarding_tab

class signIn_Page_Actions(signIn_Page_Locators):

    def wait_presence_of_element_by_xpath(self, element):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, element)))

    def wait_presence_of_element_by_id(self, element):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.ID, element)))

    def set_email_field_values(self, value):
        self.email_text_field().send_keys(value)

    def set_password_field_values(self, value):
        self.password_text_field().send_keys(value)

    def click_signIn_Button(self):
        self.signin_button().click()

    def check_intro_message_appears(self):
        if self.select_pop_up_message().is_displayed():
            while(self.select_pop_up_message().is_displayed()):
                self.select_proceed_arrow().click()
            self.select_get_started().click()





