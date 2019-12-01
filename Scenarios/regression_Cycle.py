from Locators.signIn_Page_Locators import signIn_Page_elements as element_signin
from Config.getting_credentials import getting_credentials as credentials
from Config.device_setup import device_Setup

from Locators.signIn_Page_Locators import signIn_Page_Actions as action_signIn
from Locators.createChat_Page_Locators import createChat_Page_elements as element_chat
from Locators.createChat_Page_Locators import createChat_Page_actions as action_createChat
from Locators.startChat_Page_Locators import startChat_Page_elements as startChat_element
from Locators.startChat_Page_Locators import startChat_Page_actions as action_startChat
from Config.read_Config import read_Config


class Basic_Cycle_Ran(device_Setup):
    def test_1_sign_in(self):
        user_name = credentials().get_values()[0]
        password = credentials().get_values()[1]
        action_signIn(self.driver).set_email_field_values(user_name)
        action_signIn(self.driver).set_email_field_values(user_name)
        action_signIn(self.driver).wait_presence_of_element_by_id(element_signin().email_text_field())
        action_signIn(self.driver).set_password_field_values(password)
        action_signIn(self.driver).wait_presence_of_element_by_xpath(element_signin().sign_in_button())
        action_signIn(self.driver).click_signIn_Button()
        action_signIn(self.driver).wait_presence_of_element_by_id(element_signin().on_boarding_tab())
        action_signIn(self.driver).check_intro_message_appears()
        action_signIn(self.driver).wait_presence_of_element_by_id(element_chat().multiple_options())

    def test_2_create_chat(self):
        action_signIn(self.driver).wait_presence_of_element_by_id(element_chat().multiple_options())
        action_createChat(self.driver).click_select_multiple_option()
        action_createChat(self.driver).click_chat_button()
        action_createChat(self.driver).click_groupChat_button()
        action_createChat(self.driver).click_members()
        action_createChat(self.driver).click_NextButton()
        action_signIn(self.driver).wait_presence_of_element_by_id(element_chat().group_name())
        action_createChat(self.driver).set_GroupName(read_Config().group_Name())
        action_createChat(self.driver).click_CreateChat_button()
        action_createChat(self.driver).go_back()
        action_signIn(self.driver).wait_presence_of_element_by_id(element_chat().multiple_options())
        action_createChat(self.driver).check_group_created()

    def test_3_start_chat(self):
        action_signIn(self.driver).wait_presence_of_element_by_id(element_chat().multiple_options())
        action_createChat(self.driver).click_createdChat_button()
        action_signIn(self.driver).wait_presence_of_element_by_id(startChat_element().message_Text_field())
        action_startChat(self.driver).set_message_on_messageText(read_Config().message())
        action_startChat(self.driver).click_send_message_button()
        action_startChat(self.driver).click_emoji_button()
        action_signIn(self.driver).wait_presence_of_element_by_id(startChat_element().emoji_button())
        action_startChat(self.driver).click_onSelected_sticker()
        action_startChat(self.driver).click_onSelected_sticker()
        action_startChat(self.driver).select_picture()

    def test_4_create_topic(self):
        action_signIn(self.driver).wait_presence_of_element_by_id(element_chat().multiple_options())
        action_createChat(self.driver).click_createdChat_button()
        action_signIn(self.driver).wait_presence_of_element_by_id(startChat_element().message_Text_field())
        action_startChat(self.driver).click_topic_list()
        action_startChat(self.driver).click_new_topic()
        action_startChat(self.driver).set_topic_name(read_Config().topic_Name())
        action_startChat(self.driver).click_create_button()
        action_signIn(self.driver).wait_presence_of_element_by_id(startChat_element().message_Text_field())

    def test_5_add_new_Member(self):
        action_signIn(self.driver).wait_presence_of_element_by_id(element_chat().multiple_options())
        action_createChat(self.driver).click_createdChat_button()
        action_signIn(self.driver).wait_presence_of_element_by_id(startChat_element().engineer_text_button())
        action_startChat(self.driver).click_Engineer_Button()
        action_startChat(self.driver).click_member_button()
        action_signIn(self.driver).wait_presence_of_element_by_id(startChat_element().add_new_member_button())
        action_startChat(self.driver).click_add_mew_member()
        action_startChat(self.driver).wait_Till_element_Clickable(startChat_element().contact_actions())
        action_startChat(self.driver).click_add_contact()














