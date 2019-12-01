
class createChat_Page_elements:
    def multiple_options(self):
        multiple_options = 'createButton'
        return multiple_options

    def chat_button(self):
        chatButton = "chatSheet"
        return chatButton

    def groupChat_button(self):
        groupChat = "xpath=//*[@text='Group Chat']"
        return groupChat

    def contact_name(self):
        first_contactName = "xpath=//*[@id='contact_checkbox' and (./preceding-sibling::* | ./following-sibling::*)" \
                            "[./*[./*[@text='N']]]]"
        second_contactName = "xpath=//*[@id='contact_checkbox' and (./preceding-sibling::* | ./following-sibling::*)" \
                             "[./*[./*[@text='S']]]]"
        return first_contactName, second_contactName

    def group_name(self):
        groupName = 'workspace_name_edittext'
        return groupName

    def next_button(self):
        group_NextButton = 'group_chat_next_button'
        return group_NextButton

    def create_chat(self):
        createChat = 'add_group_detail_next_textview'
        return createChat

    def created_chat_group(self):
        created_chatGroup = "//*[@text='Engineer']"
        return created_chatGroup

    def navigate_back(self):
        navigate_back = "//*[@contentDescription='Navigate up']"
        return navigate_back



class createChat_Page_Locators(createChat_Page_elements):

    def __init__(self, driver):
        self.driver = driver
        self.chat_elements = createChat_Page_elements()

    def select_multipleOptions(self):
        multiple_Options = self.driver.find_element_by_id(self.chat_elements.multiple_options())
        return multiple_Options

    def select_chat_button(self):
        click_chat_button = self.driver.find_element_by_id(self.chat_elements.chat_button())
        return click_chat_button

    def select_groupChat_button(self):
        click_groupChat_button = self.driver.find_element_by_xpath(self.chat_elements.groupChat_button())
        return click_groupChat_button

    def select_CreateChat_button(self):
        select_createChat_button = self.driver.find_element_by_id(self.chat_elements.create_chat())
        return select_createChat_button

    def select_created_chat_group(self):
        selected_created_chat_group = self.driver.find_element_by_xpath(self.chat_elements.created_chat_group())
        return selected_created_chat_group

    def select_navigate_back(self):
        select_navigate_back = self.driver.find_element_by_xpath(self.chat_elements.navigate_back())
        return select_navigate_back

    def groupName_field(self):
        groupName_field = self.driver.find_element_by_id(self.chat_elements.group_name())
        return groupName_field

    def select_NextButton(self):
        select_NextButton = self.driver.find_element_by_id(self.chat_elements.next_button())
        return select_NextButton


class createChat_Page_actions(createChat_Page_Locators):
    def click_on_member(self):
        click_1st_member_checkbox = self.driver.find_element_by_xpath(self.chat_elements.contact_name()[0])
        click_2nd_member_checkbox = self.driver.find_element_by_xpath(self.chat_elements.contact_name()[1])
        return click_1st_member_checkbox, click_2nd_member_checkbox

    def click_select_multiple_option(self):
        self.select_multipleOptions().click()

    def click_chat_button(self):
        self.select_chat_button().click()

    def click_groupChat_button(self):
        self.select_groupChat_button().click()

    def click_members(self):
        self.click_on_member()[0].click()
        self.click_on_member()[1].click()

    def click_NextButton(self):
        self.select_NextButton().click()

    def set_GroupName(self, value):
        self.groupName_field().send_keys(value)

    def click_CreateChat_button(self):
        self.select_CreateChat_button().click()

    def check_group_created(self):
        if self.select_created_chat_group().is_displayed():
            print('Group Created')
        else:
            raise ('Group Not Created')

    def click_createdChat_button(self):
        self.select_created_chat_group().click()

    def go_back(self):
        self.select_navigate_back().click()











