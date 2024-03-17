import allure

from pages.elements_page import TestElementBox


@allure.suite("PurrWeb")
class TestElements:
    @allure.feature("All test")
    class TestTextBox:
        def test_text_box(self, driver):
            with allure.step("Open"):
                all_page = TestElementBox(driver, 'https://staging.d2twwklgqmrfet.amplifyapp.com/login')
                all_page.open()
            with allure.step("Authorization"):
                all_page.Authorization()
            with allure.step("Upload_the_Files"):
                all_page.Upload_the_Files()
            with allure.step("Choose_the_Signers"):
                all_page.Choose_the_Signers()