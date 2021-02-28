# @Author ：黄贝尔
# @Time ：2021/2/7__13:37
# #coding:utf-8
import unittest
from CN_001_homepage import homepage
import time
from selenium import webdriver
from config import chromeDriver_Path,hk_kefu_url,hk_url,hk_cart
from utils.seleniumtools import new_find_element

class HOMEPAGE(unittest.TestCase):
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



    def test_001_TUMIUAT_662_1(self):
        homepage1 = homepage(self.driver)
        homepage1.click_logo()
        assert self.driver.current_url == hk_url

    def test_002_TUMIUAT_662_2(self):
        homepage1 = homepage(self.driver)
        homepage1.click_vip_club()
        assert self.driver.current_url == f'{hk_url}tumi-exclusives-club/'
        assert new_find_element(self.driver,homepage.vip_Privilege).text == 'TUMI Exclusives Club Benefits'

    def test_003_TUMIUAT_662_3(self):
        homepage1 = homepage(self.driver)
        homepage1.click_lang_selector()
        assert self.driver.current_url == f'{hk_url}zh/'

    def test_004_TUMIUAT_662_4(self):
        homepage1 = homepage(self.driver)
        homepage1.click_offline_store()
        assert self.driver.current_url == f'{hk_url}store-locator/'
        assert new_find_element(self.driver,homepage.store_type).text == 'Store Type'

    def test_005_TUMIUAT_662_5(self):
        homepage1 = homepage(self.driver)
        homepage1.click_customer_service()
        assert self.driver.current_url == hk_kefu_url

    def test_006_TUMIUAT_662_6(self):
        homepage1 = homepage(self.driver)
        homepage1.click_cart()
        assert self.driver.current_url == hk_cart

    def test_007_TUMIUAT_662_7(self):
        homepage1 = homepage(self.driver)
        homepage1.click_login()
        time.sleep(0.5)
        assert new_find_element(self.driver,homepage.login_text).text == 'Log in to your TUMI.HK account'

    def test_008_TUMIUAT_664(self):
        homepage1 = homepage(self.driver)
        homepage1.search_for_Effective_Products()
        time.sleep(1)
        assert new_find_element(self.driver,homepage.keyword).text == 'suggested keywords "alp"'

    def test_009_TUMIUAT_665(self):
        homepage1 = homepage(self.driver)
        homepage1.Search_for_Invalid_Products()
        assert new_find_element(self.driver,homepage.no_search).text == 'SORRY, NO SEARCH RESULTS'

    def test_010_TUMIUAT_666(self):
        homepage1 = homepage(self.driver)
        homepage1.search_for_Effective_Products()
        homepage1.click_suggested_keyword()
        assert new_find_element(self.driver,homepage.have_search).text == 'SEARCH RESULTS'
        assert self.driver.find_element_by_xpath('ml[1]/body[1]/div[1]/main[1]/div[3]/div[1]/div[1]/div[2]').text == '"ALPHA"'

    def test_010_TUMIUAT_1521_1(self):
        homepage1 = homepage(self.driver)
        homepage1.click_f_luggage()
        assert new_find_element(self.driver,homepage.luggage_title).text =='All Luggage, from Checked Bags to Backpacks'

    def test_011_TUMIUAT_1521_2(self):
        homepage1 = homepage(self.driver)
        homepage1.click_f_backpacks()
        assert new_find_element(self.driver,homepage.backpacks_title).text =='Leather Backpacks & Sling Bags'

    def test_012_TUMIUAT_1521_3(self):
        homepage1 = homepage(self.driver)
        homepage1.click_f_totes()
        assert new_find_element(self.driver,homepage.totes_title).text =='Tote Bags for Men & Women'

    def test_013_TUMIUAT_1521_4(self):
        homepage1 = homepage(self.driver)
        homepage1.click_f_crossbodies()
        assert new_find_element(self.driver,homepage.crossbodies_title).text =='Cross Body Bags, Carry On Luggage & Totes'

    def test_014_TUMIUAT_1521_5(self):
        homepage1 = homepage(self.driver)
        homepage1.click_f_accessories()
        assert new_find_element(self.driver,homepage.accessories_title).text =='All Accessories, Electronics, Wallets & Money Clips'

    def test_015_TUMIUAT_1521_6(self):
        homepage1 = homepage(self.driver)
        homepage1.click_f_recycled()
        assert new_find_element(self.driver,homepage.recycled_title).text =="Men's & Women's styles made from recycled materials"

    def test_016_TUMIUAT_417_1(self):
        homepage1 = homepage(self.driver)
        homepage1.roll_to_bottom_AD_space()
        homepage1.click_bottom_AD_space_title()
        homepage1.new_page()
        assert self.driver.current_url == 'https://stage.tumi-hk.com/Alpha3/ '

    def test_017_TUMIUAT_417_2(self):
        homepage1 = homepage(self.driver)
        homepage1.roll_to_bottom_AD_space()
        homepage1.click_bottom_AD_space_img()
        homepage1.new_page()
        assert self.driver.current_url == 'https://stage.tumi-hk.com/Alpha3/'

    def test_018_TUMIUAT_417_3(self):
        homepage1 = homepage(self.driver)
        homepage1.roll_to_bottom_AD_space()
        homepage1.click_bottom_AD_space_explore()
        homepage1.new_page()
        assert self.driver.current_url == 'https://stage.tumi-hk.com/Alpha3/'

    def test_019_TUMIUAT_417_4(self):
        homepage1 = homepage(self.driver)
        homepage1.roll_to_bottom_AD_space()
        homepage1.click_bottom_AD_space_title2()
        homepage1.new_page()
        assert new_find_element(self.driver,homepage.tumi_different).text =='TUMI的独特之处'

    def test_020_TUMIUAT_417_5(self):
        homepage1 = homepage(self.driver)
        homepage1.roll_to_bottom_AD_space()
        homepage1.click_bottom_AD_space_img2()
        homepage1.new_page()
        assert new_find_element(self.driver,homepage.tumi_different).text =='TUMI的独特之处'

    def test_021_TUMIUAT_417_6(self):
        homepage1 = homepage(self.driver)
        homepage1.roll_to_bottom_AD_space()
        homepage1.click_bottom_AD_space_explore2()
        homepage1.new_page()
        assert new_find_element(self.driver,homepage.tumi_different).text =='TUMI的独特之处'

    def test_021_TUMIUAT_1515(self):
        homepage1 = homepage(self.driver)
        homepage1.login_phone_error()
        time.sleep(2)
        assert new_find_element(self.driver, homepage.username_error).text == '你的用户名或密码不正确。'

    def test_022_TUMIUAT_1514(self):
        homepage1 = homepage(self.driver)
        homepage1.login_no_phone()
        time.sleep(2)
        assert new_find_element(self.driver, homepage.j_username_error).text == '手机/邮箱 为必填选项'

    def test_023_TUMIUAT_423(self):
        homepage1 = homepage(self.driver)
        homepage1.login_no_password()
        time.sleep(2)
        assert new_find_element(self.driver, homepage.j_password_error).text == '密码 为必填选项'

    def test_024_TUMIUAT_424(self):
        homepage1 = homepage(self.driver)
        homepage1.login_password_error()
        time.sleep(2)
        assert new_find_element(self.driver, homepage.username_error).text == '你的用户名或密码不正确。'

    def test_025_TUMIUAT_409_1(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_logo()
        assert self.driver.current_url == cn_url
        homepage1.sign_out()

    def test_026_TUMIUAT_409_2(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_vip_club()
        assert self.driver.current_url == f'{cn_url}tumi-club/'
        assert new_find_element(self.driver,homepage.vip_Privilege).text == '会员专属礼遇'
        homepage1.sign_out()

    def test_026_TUMIUAT_409_3(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.move_to_wechat()
        homepage1.sign_out()
        # assert new_find_element(self.driver,assert_element.wechat_text).text == '扫一扫进入TUMI途明 微信精品店'

    def test_027_TUMIUAT_409_4(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_offline_store()
        assert self.driver.current_url == f'{cn_url}store-locator/'
        assert new_find_element(self.driver,homepage.store_type).text == '门店类型'
        homepage1.sign_out()

    def test_028_TUMIUAT_409_6(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_cart()
        time.sleep(1)
        assert self.driver.current_url == cn_cart
        homepage1.sign_out()

    def test_029_TUMIUAT_409_7(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_my_username()
        assert self.driver.current_url == cn_account
        homepage1.sign_out()

    def test_030_TUMIUAT_409_5(self):
        homepage1 = homepage(self.driver)
        homepage1.login()
        homepage1.click_customer_service()
        assert self.driver.current_url == cn_kefu_url

    def test_031_TUMIUAT_426(self):
        homepage1 = homepage(self.driver)
        homepage1.sign_out()
        assert new_find_element(self.driver, homepage.login_register_btn).text == '登录/注册'





