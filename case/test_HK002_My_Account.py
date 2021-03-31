# @Author ：黄贝尔
# @Time ：2021/2/9__13:39
# #coding:utf-8
import unittest
from HK_002_My_Account import my_account
import time
from selenium import webdriver
from config import chromeDriver_Path,hk_url
from utils.seleniumtools import new_find_element
from HK_001_homepage import homepage


class MyAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(chromeDriver_Path)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        self.driver.get(hk_url)
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(2)

    def tearDown(self):
        homepage1 = homepage(self.driver)
        my_account1 = my_account(self.driver)
        time.sleep(2)
        my_account1.move_to_logo()
        my_account1.click_account_logo()
        if new_find_element(self.driver,homepage.my_username).text != 'Login / Register':
            homepage1.sign_out()

    def test_032_TUMIUAT_821(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_info()
        assert new_find_element(self.driver,my_account.my_account_title).text == 'MY ACCOUNT'

    def test_033_TUMIUAT_822(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        assert new_find_element(self.driver,my_account.update_my_info).text == 'UPDATE PERSONAL INFORMATION'
        assert new_find_element(self.driver,my_account.update_my_password).text == 'UPDATE PASSWORD'
        assert new_find_element(self.driver,my_account.my_address).text == 'MY ADDRESS BOOK'

    def test_034_TUMIUAT_1530_1(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        time.sleep(6)
        b=new_find_element(self.driver,my_account.nearby_stores).text
        my_account1.click_nearby_stores()
        a = new_find_element(self.driver,my_account.store_name).text
        assert b.upper() == a

    def test_035_TUMIUAT_1530_2(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        time.sleep(6)
        my_account1.click_nearby_stores()
        my_account1.click_store_search()
        assert new_find_element(self.driver,my_account.store_type).text == 'Store Type'

    def test_036_TUMIUAT_823(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.input_diy()
        time.sleep(1)
        my_account1.click_diy_btn()
        time.sleep(1)
        assert new_find_element(self.driver, my_account.diy_title).text == 'Click on each slots to enter an alphabet, number or select any of the symbols displayed below for monogramming.'
        self.driver.refresh()

    def test_037_TUMIUAT_824(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_info()
        my_account1.clear_account_username()
        my_account1.input_account_username()
        my_account1.click_account_call()
        my_account1.click_call_miss()
        my_account1.clear_account_email()
        my_account1.input_account_email()
        my_account1.click_account_save_btn()
        assert new_find_element(self.driver, my_account.update_my_password).text == 'Update Password'

    def test_038_TUMIUAT_825(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_info()
        my_account1.clear_account_username()
        my_account1.click_account_call()
        my_account1.click_call_miss()
        my_account1.clear_account_email()
        my_account1.input_account_email()
        my_account1.click_account_save_btn()
        assert new_find_element(self.driver,my_account.userName_errors).text== 'Please enter a username.'

    def test_039_TUMIUAT_1578(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_info()
        my_account1.clear_account_username()
        my_account1.input_account_username()
        my_account1.click_account_call()
        my_account1.click_call_null()
        my_account1.clear_account_email()
        my_account1.input_account_email()
        my_account1.click_account_save_btn()
        assert new_find_element(self.driver,my_account.titleCode_errors).text== '请选择您的称呼'

    def test_040_TUMIUAT_1579(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_info()
        my_account1.clear_account_username()
        my_account1.input_account_username()
        my_account1.click_account_call()
        my_account1.click_call_miss()
        my_account1.clear_account_email()
        my_account1.input_account_email()
        my_account1.click_account_save_btn()
        assert new_find_element(self.driver, my_account.update_my_info).text == '更新个人信息'

    def test_041_TUMIUAT_1582(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_info()
        my_account1.clear_account_username()
        my_account1.input_account_username()
        my_account1.click_account_call()
        my_account1.click_call_miss()
        my_account1.clear_account_email()
        my_account1.click_account_save_btn()
        assert new_find_element(self.driver, my_account.update_my_info).text == '更新个人信息'

    def test_042_TUMIUAT_1583(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_info()
        my_account1.clear_account_username()
        my_account1.input_account_username()
        my_account1.click_account_call()
        my_account1.click_call_miss()
        my_account1.clear_account_email()
        my_account1.input_account_email()
        my_account1.click_no_save()
        assert new_find_element(self.driver, my_account.update_my_info).text == '更新个人信息'

    def test_043_TUMIUAT_571(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_address_book_btn()
        my_account1.click_creat_new_address()
        my_account1.input_address_consignee()
        my_account1.input_address_phone()
        my_account1.click_address_region()
        my_account1.click_address_beijing()
        my_account1.click_address_qu()
        my_account1.input_address_Detailed()
        my_account1.click_address_save()
        assert new_find_element(self.driver, my_account.creat_new_address).text == '添加收货地址'

    def test_044_TUMIUAT_572(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_address_book_btn()
        my_account1.click_address_edit()
        my_account1.input_address_consignee()
        my_account1.input_address_Detailed()
        my_account1.click_address_save()
        assert new_find_element(self.driver, my_account.creat_new_address).text == '添加收货地址'

    def test_045_TUMIUAT_573(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_address_book_btn()
        my_account1.click_address_del()
        assert new_find_element(self.driver, my_account.address_name).text != '测试测试测试测试'

    def test_046_TUMIUAT_1584(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_address_book_btn()
        my_account1.click_creat_new_address()
        my_account1.clear_address_consignee()
        my_account1.input_address_phone()
        my_account1.click_address_region()
        my_account1.click_address_beijing()
        my_account1.click_address_qu()
        my_account1.input_address_Detailed()
        my_account1.click_address_save()
        assert new_find_element(self.driver, my_account.nameErrors).text == '收货人为必填信息'

    def test_047_TUMIUAT_1585(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_address_book_btn()
        my_account1.click_creat_new_address()
        my_account1.input_address_consignee()
        my_account1.input_address_phone2()
        my_account1.click_address_region()
        my_account1.click_address_beijing()
        my_account1.click_address_qu()
        my_account1.input_address_Detailed()
        my_account1.click_address_save()
        assert new_find_element(self.driver, my_account.phoneErrors).text == '请输入正确的手机号码'

    def test_048_TUMIUAT_1586(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_address_book_btn()
        my_account1.click_creat_new_address()
        my_account1.input_address_consignee()
        my_account1.input_address_phone()
        my_account1.click_address_region()
        my_account1.click_address_beijing()
        my_account1.click_address_qu()
        my_account1.input_address_Detailed()
        my_account1.click_default_address()
        my_account1.click_address_save()
        assert new_find_element(self.driver, my_account.creat_new_address).text == '添加收货地址'
        my_account1.click_address_del()

    def test_049_TUMIUAT_1613(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_address_book_btn()
        my_account1.click_creat_new_address()
        my_account1.input_address_consignee()
        my_account1.input_address_phone()
        my_account1.input_addressEditTelphone()
        my_account1.click_address_region()
        my_account1.click_address_beijing()
        my_account1.click_address_qu()
        my_account1.input_address_Detailed()
        my_account1.click_address_save()
        assert new_find_element(self.driver, my_account.areaPhone_errors).text == '请输入完整的固定电话号码'

    def test_050_TUMIUAT_1588(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_address_book_btn()
        my_account1.click_creat_new_address()
        my_account1.input_address_consignee()
        my_account1.input_address_phone()
        my_account1.input_addressEditAreaCode()
        my_account1.click_address_region()
        my_account1.click_address_beijing()
        my_account1.click_address_qu()
        my_account1.input_address_Detailed()
        my_account1.click_address_save()
        assert new_find_element(self.driver, my_account.areaPhone_errors).text == '请输入完整的固定电话号码'


    def test_051_TUMIUAT_574(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_password()
        my_account1.input_now_password()
        my_account1.input_new_password()
        my_account1.input_confirm_new_password()
        my_account1.click_save_new_password()
        assert new_find_element(self.driver, my_account.modifly_password_successful).text == '您的密码已被更改'

    def test_052_TUMIUAT_574_2(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account2()
        my_account1.click_update_my_password()
        my_account1.input_now_password2()
        my_account1.input_new_password2()
        my_account1.input_confirm_new_password2()
        my_account1.click_save_new_password()
        assert new_find_element(self.driver, my_account.modifly_password_successful).text == '您的密码已被更改'

    def test_053_TUMIUAT_575(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_password()
        my_account1.input_new_password()
        my_account1.input_confirm_new_password()
        my_account1.click_save_new_password()
        assert new_find_element(self.driver, my_account.nowPassword_errors).text == '请输入您的当前密码'


    def test_054_TUMIUAT_576(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_password()
        my_account1.input_now_password2()
        my_account1.input_new_password2()
        my_account1.input_confirm_new_password2()
        my_account1.click_save_new_password()
        assert new_find_element(self.driver, my_account.nowPassword_errors).text == '请输入正确的密码'

    def test_055_TUMIUAT_577(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_password()
        my_account1.input_now_password()
        my_account1.input_confirm_new_password()
        my_account1.click_save_new_password()
        assert new_find_element(self.driver, my_account.newPassword_errors).text == '请输入您的新密码'

    def test_056_TUMIUAT_578(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_password()
        my_account1.input_now_password()
        my_account1.input_new_password()
        my_account1.click_save_new_password()
        assert new_find_element(self.driver, my_account.checkNewPassword_errors).text == '请输入您的确认密码'

    def test_057_TUMIUAT_579(self):
        my_account1 = my_account(self.driver)
        my_account1.go_to_my_account()
        my_account1.click_update_my_password()
        my_account1.input_now_password()
        my_account1.input_new_password()
        my_account1.input_confirm_new_password2()
        my_account1.click_save_new_password()
        assert new_find_element(self.driver, my_account.checkNewPassword_errors).text == '密码和确认密码不匹配'


















