from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


class startChat_Page_elements:
    def message_Text_field(self):
        message_Text_field = 'messageEditText'
        return message_Text_field

    def send_message_button(self):
        send_message_button = "xpath=//*[@class='android.widget.ImageButton' and ./parent::*[@id='menu']]"
        return send_message_button

    def emoji_button(self):
        emoji_button = 'sticker_icon'
        return emoji_button

    def sticker_Selection(self):
        sticker_selection = "xpath=(//*[@id='view_sticker_pager_item_recycler_view']/*/*/*[@id='view_sticker_item_image'])[1]"
        return sticker_selection

    def post_sticker(self):
        post_sticker = "xpath=(//*[@class='android.widget.RelativeLayout']/*[@class='android.widget.ImageView'])[1]"
        return post_sticker

    def gallery_icon(self):
        gallery_icon = "image_icon"
        return gallery_icon

    def capture_picture(self):
        capture_picture = "shutter_button"
        return capture_picture

    def picture_selected_gallery(self):
        picture_selected_gallery = "xpath=(//*[@id='recyclerview']/*/*[@id='check_view'])[1]"
        return picture_selected_gallery

    def picture_select_button(self):
        picture_select_button = 'button_apply'
        return picture_select_button

    def upload_picture(self):
        upload_picture = "xpath=//*[@text='Send 1']"
        return upload_picture

    def picture_upload_status(self):
        picture_upload_status = "//*[@id='status_text' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[./*[@id='image']]] and ./parent::*[@id='second_row']]]"
        return picture_upload_status

    def action_topic_list(self):
        action_topic_list = 'action_topic_list'
        return action_topic_list

    def start_new_topic(self):
        start_new_topic = 'side_menu_start_topic_button'
        return start_new_topic

    def add_new_topic(self):
        add_new_topic_field = "view_new_compose_view_topic_name"
        return add_new_topic_field

    def create_button(self):
        create_button = 'button'
        return create_button

    def engineer_text_button(self):
        engineer_text_button = 'toolbar_title_textview'
        return engineer_text_button

    def check_members_button(self):
        check_members_button = 'group_detail_member_view'
        return check_members_button

    def add_new_member_button(self):
        add_new_member_button = 'button_add_member'
        return add_new_member_button

    def contact_actions(self):
        contact_types = 'contact_action_image_view'
        return contact_types

    def add_Contact(self):
        add_Contact = "xpath=//*[@text='Add']"
        return add_Contact

    def go_back(self):
        go_Back = "//*[@contentDescription='Navigate up']"
        return go_Back

    def dialog_box(self):
        dialog_box = "xpath=//*[@text='Allow Eko to access photos, media, and files on your device?']"
        return dialog_box

    def allow_permission(self):
        allow_permission = "permission_allow_button"
        return allow_permission


class startChat_Page_Locators(startChat_Page_elements):
    def __init__(self, driver):
        self.driver = driver
        self.startChat_elements = startChat_Page_elements()

    def select_message_text_field(self):
        select_message_text_field = self.driver.find_element_by_id(self.startChat_elements.message_Text_field())
        return select_message_text_field

    def select_send_message_button(self):
        select_Send_message_button = self.driver.find_element_by_xpath(self.startChat_elements.send_message_button())
        return select_Send_message_button

    def select_emoji_button(self):
        select_emoji_button = self.driver.find_element_by_id(self.startChat_elements.emoji_button())
        return select_emoji_button

    def select_sticker(self):
        select_sticker = self.driver.find_element_by_xpath(self.startChat_elements.sticker_Selection())
        return select_sticker

    def select_post_sticker(self):
        select_post_sticker = self.driver.find_element_by_xpath(self.startChat_elements.post_sticker())
        return select_post_sticker

    def select_gallery_icon(self):
        select_gallery_icon = self.driver.find_element_by_id(self.startChat_elements.gallery_icon())
        return select_gallery_icon

    def select_capture_picture(self):
        select_capture_picture = self.driver.find_element_by_id(self.startChat_elements.capture_picture())
        return select_capture_picture

    def select_picture_gallery(self):
        select_picture_gallery = self.driver.find_element_by_xpath(self.startChat_elements.picture_selected_gallery())
        return select_picture_gallery

    def select_selected_picture(self):
        select_selected_picture = self.driver.find_element_by_id(self.startChat_elements.picture_select_button())
        return select_selected_picture

    def select_upload_picture(self):
        select_upload_picture = self.driver.find_element_by_xpath(self.startChat_elements.upload_picture())
        return select_upload_picture

    def select_picture_upload_status(self):
        select_picture_upload_status = self.driver.find_element_by_xpath(self.startChat_elements.picture_upload_status())
        return select_picture_upload_status

    def select_action_topic_list(self):
        select_action_topic_list = self.driver.find_element_by_id(self.startChat_elements.action_topic_list())
        return select_action_topic_list

    def select_start_new_topic(self):
        select_start_new_topic = self.driver.find_element_by_id(self.startChat_elements.start_new_topic())
        return select_start_new_topic

    def select_add_new_topic(self):
        select_add_new_topic = self.driver.find_element_by_id(self.startChat_elements.add_new_topic())
        return select_add_new_topic

    def select_create_button(self):
        select_create_button = self.driver.find_element_by_id(self.startChat_elements.create_button())
        return select_create_button

    def select_engineer_text_button(self):
        select_engineer_text_button = self.driver.find_element_by_id(self.startChat_elements.engineer_text_button())
        return select_engineer_text_button

    def select_member_button(self):
        select_member_button = self.driver.find_element_by_id(self.startChat_elements.check_members_button())
        return select_member_button

    def select_add_new_member(self):
        select_add_new_member = self.driver.find_element_by_id(self.startChat_elements.add_new_member_button())
        return select_add_new_member

    def select_contact_types(self):
        select_contact_types = self.driver.find_element_by_id(self.startChat_elements.contact_actions())
        return select_contact_types

    def select_add_contact(self):
        select_add_contact = self.driver.find_element_by_xpath(self.startChat_elements.add_Contact())
        return select_add_contact

    def select_go_back(self):
        select_go_back = self.driver.find_element_by_xpath(self.startChat_elements.go_back())
        return select_go_back

    def select_dialog_box(self):
        select_dialog_box = self.driver.find_element_by_xpath(self.startChat_elements.dialog_box())
        return select_dialog_box

    def select_allow_button(self):
        select_allow_button = self.driver.find_element_by_id(self.startChat_elements.allow_permission())
        return select_allow_button


class startChat_Page_actions(startChat_Page_Locators):
    def set_message_on_messageText(self, message):
        self.select_message_text_field().send_keys(message)

    def click_send_message_button(self):
        self.select_send_message_button().click()

    def click_emoji_button(self):
        self.select_emoji_button().click()

    def click_onSelected_sticker(self):
        self.select_sticker().click()

    def click_post_sticker(self):
        self.select_post_sticker().click()

    def check_dialogue_box_displaying(self):
        try:
            if self.select_dialog_box().is_displayed():
                self.select_allow_button().click()
        except NoSuchElementException:
            print(None)

    def select_picture(self):
        self.select_gallery_icon().click()
        self.check_dialogue_box_displaying()
        self.select_picture_gallery().click()
        self.select_selected_picture().click()
        self.select_upload_picture().click()

    def wait_for_textTo_beInElement_byXPATH(self, element):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, element),'Sent'))

    def click_topic_list(self):
        self.select_action_topic_list().click()

    def click_new_topic(self):
        self.select_start_new_topic().click()

    def set_topic_name(self, topic_name):
        self.select_add_new_topic().send_keys(topic_name)

    def click_create_button(self):
        self.select_create_button().click()

    def click_Engineer_Button(self):
        self.select_engineer_text_button().click()

    def click_member_button(self):
        self.select_member_button().click()

    def click_add_mew_member(self):
        self.select_add_new_member().click()

    def wait_Till_element_Clickable(self, element):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.ID, element)))

    def click_add_contact(self):
        self.select_contact_types().click()
        self.select_add_contact().click()
        self.select_go_back().click()























