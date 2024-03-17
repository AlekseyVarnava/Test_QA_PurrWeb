import time
import os
import allure
import random

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import ElementLocators
from pages.base_page import BasePage


class TestElementBox(BasePage):
    locators = ElementLocators()

        # Authorization
    def Authorization(self, ):
        with allure.step("Авторизация пройдена"):
            list_log_pass = self.elements_are_visible(self.locators.LOG_AND_PASS)
            list_log_pass[0].send_keys('fluffskill@mail.ru')
            list_log_pass[1].send_keys('Varnava62zzz')
            self.element_is_visible(self.locators.NEXT1).click()

        # Upload the Files
    def Upload_the_Files(self, ):
        with allure.step("Загружен документ"):
            file_name, path = generated_file()
            self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
            #time.sleep(20)
            self.element_is_visible(self.locators.NEXT2).click()
            os.remove(path)

        # Choose the Signers
    def Choose_the_Signers(self, ):
        with allure.step("Введены данные подписантов"):
            person_info = next(generated_person())
            self.element_is_visible(self.locators.SIGN_SEND).click()
            self.element_is_visible(self.locators.ADD_SIGNERS).click()
            self.element_is_visible(self.locators.ADD_VIEWERS).click()
            email_me = person_info.email_me
            first_name = person_info.first_name
            name_email = self.elements_are_visible(self.locators.SIGNERS_NAME_EMAIL)
            name_email[0].send_keys(first_name)
            name_email[1].send_keys(email_me)
            self.element_is_visible(self.locators.VIEWERS_EMAIL).send_keys(email_me)
            self.element_is_visible(self.locators.NEXT3).click()
        #self.element_is_visible(self.locators.GOT_IT)
        with allure.step("Добавлена новая подпись"):
            all_fields = self.elements_are_visible(self.locators.ALL_FIELDS)
            all_fields[0].click()
            self.element_is_visible(self.locators.CANVAS).click()
            all_fields[0].click()
            signature = self.element_is_visible(self.locators.SIGNATURE)
            self.action_double_click(signature)
            self.element_is_visible(self.locators.ME).click()
            self.element_is_visible(self.locators.SPISOK_ME_OLD).click()
            self.element_is_visible(self.locators.DELETE_ME_PLD).click()
            self.element_is_visible(self.locators.DELETE_ACCEPT).click()
            self.element_is_visible(self.locators.CREATE_NOW).click()
            self.element_is_visible(self.locators.OPEN_FONT).click()
            list_font = self.elements_are_visible(self.locators.LIST_FONT)
            number_font = random.randint(0, 6)
            list_font[number_font].click()
            self.element_is_visible(self.locators.I_AGREE).click()
            self.element_is_visible(self.locators.NEXT4).click()
        time.sleep(6)
        with allure.step("Добавлены филды"):
            all_fields[1].click()
            self.action_move_by_offset(60, 10)
            self.action_left_click(None)
            all_fields[1].click()
            # time.sleep(1)
            all_fields[2].click()
            self.action_move_by_offset(-20, 20)
            self.action_left_click(None)
            all_fields[2].click()
            # time.sleep(1)
            all_fields[3].click()
            self.action_move_by_offset(-70, 20)
            self.action_left_click(None)
            all_fields[3].click()
            # time.sleep(1)
            all_fields[4].click()
            self.action_move_by_offset(-80, 20)
            self.action_left_click(None)
            all_fields[4].click()
        with allure.step("Документ сохранён"):
            self.element_is_visible(self.locators.SAVE).click()
        with allure.step("Документ отправлен на подпись"):
            self.element_is_visible(self.locators.SIGN_A_DOCUMENT).click()

        time.sleep(4)
