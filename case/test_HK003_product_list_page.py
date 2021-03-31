# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-02-15
import unittest
import time
from selenium import webdriver
from config import chromeDriver_Path,hk_url
from utils.seleniumtools import new_find_element
from HK_003_product_list_page import product_list
from config import hk_url
from HK_001_homepage import homepage

class Product_list(unittest.TestCase):
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

    def test_058_TUMIUAT_706_1(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_f_homepage()
        assert self.driver.current_url == hk_url

    def test_059_TUMIUAT_706_2(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_backpack()
        product_list1.click_f_homepage()
        assert self.driver.current_url == hk_url

    def test_060_TUMIUAT_706_3(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_bag()
        product_list1.click_f_homepage()
        assert self.driver.current_url == hk_url

    def test_061_TUMIUAT_706_4(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_accessories()
        product_list1.click_f_homepage()
        assert self.driver.current_url == hk_url

    def test_062_TUMIUAT_706_5(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_recommended()
        product_list1.click_f_homepage()
        assert self.driver.current_url == hk_url

    def test_063_TUMIUAT_707_1(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_all_product()
        assert new_find_element(self.driver,homepage.luggage_title).text  == 'All Luggage, from Checked Bags to Backpacks'

    def test_064_TUMIUAT_707_2(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_backpack()
        product_list1.click_all_product()
        assert new_find_element(self.driver,homepage.backpacks_title).text  == 'Leather Backpacks & Sling Bags'

    def test_065_TUMIUAT_707_3(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_bag()
        product_list1.click_all_product()
        assert new_find_element(self.driver,homepage.bag_title).text  == 'All Bags, Briefcases, Totes, Duffel Bags & Luggage'

    def test_066_TUMIUAT_707_4(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_accessories()
        product_list1.click_all_product()
        assert new_find_element(self.driver,homepage.accessories_title).text  == 'All Accessories, Electronics, Wallets & Money Clips'

    def test_067_TUMIUAT_708(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        assert new_find_element(self.driver,product_list.s_luggage_title).text == 'Carry On Luggage - Travel Rolling Luggage'

    def test_068_TUMIUAT_711(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_f_homepage()
        assert self.driver.current_url == hk_url

    def test_069_TUMIUAT_712_1(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_f_compare()
        assert new_find_element(self.driver,product_list.compare_text).text == 'Add 1 or 2 items'
        product_list1.click_f_compare()

    def test_070_TUMIUAT_712_2(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_f_compare()
        product_list1.click_s_compare()
        assert new_find_element(self.driver,product_list.immediately_to_compare).text == 'Compare now'
        product_list1.click_immediately_to_compare()
        product_list1.click_del_product()
        product_list1.click_s_compare()

    def test_071_TUMIUAT_712_3(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_f_compare()
        product_list1.click_s_compare()
        product_list1.click_t_compare()
        product_list1.click_fo_compare()
        assert new_find_element(self.driver,product_list.compare_error).text == 'YOU CAN COMPARE UP TO 3 PRODUCTS AT A TIME'
        product_list1.click_immediately_to_compare()
        product_list1.click_del_product()
        product_list1.click_del_product()
        product_list1.click_t_compare()

    def test_072_TUMIUAT_713(self):
        product_list1=product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        assert new_find_element(self.driver,product_list.hide_the_screening).text == 'Hide Filter'
        assert new_find_element(self.driver, product_list.screening_series).text == 'Collection'
        assert new_find_element(self.driver, product_list.screening_color).text == 'Color Family'
        assert new_find_element(self.driver, product_list.screening_prices).text == 'Price'


    def test_073_TUMIUAT_715(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        time.sleep(2)
        product_list1.click_screening_series_btn()
        product_list1.click_merge_serise()
        a=new_find_element(self.driver,product_list.merga_num).text
        b=a.replace('(','').replace(')','').strip()
        time.sleep(5)
        assert b == new_find_element(self.driver,product_list.mergaNum).text

    def test_074_TUMIUAT_716(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_hide_the_screening()
        assert new_find_element(self.driver,product_list.display_screen).text == 'Show Filter'

    def test_075_TUMIUAT_717(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_sortOptions1SelectBoxItText()
        product_list1.click_price_asc()
        time.sleep(5)
        assert new_find_element(self.driver, product_list.lowest_price).text == 'HK$4,090.00'


    def test_076_TUMIUAT_718(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_sortOptions1SelectBoxItText()
        product_list1.click_price_desc()
        time.sleep(1)
        assert new_find_element(self.driver,product_list.highest_price).text == 'HK$15,000.00'

    def test_077_TUMIUAT_461(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        assert len(self.driver.find_elements_by_xpath('//body/div[1]/main[1]/div[4]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]')) == 1

    def test_078_TUMIUAT_462_1(self):
        product_list1 = product_list(self.driver)
        product_list1.action_f_luggage()
        time.sleep(1)
        product_list1.click_f_luggage_all()
        time.sleep(5)
        assert new_find_element(self.driver,product_list.page_num).text == '30 件'

    def test_079_TUMIUAT_462_2(self):
        product_list1 = product_list(self.driver)
        product_list1.action_f_luggage()
        time.sleep(1)
        product_list1.click_f_luggage_all()
        time.sleep(5)
        product_list1.click_page_num()
        product_list1.click_page_60()
        time.sleep(2)
        a=self.driver.find_elements_by_link_text('快速购买')
        assert len(a) == 60

    def test_080_TUMIUAT_462_3(self):
        product_list1 = product_list(self.driver)
        product_list1.action_f_luggage()
        time.sleep(1)
        product_list1.click_f_luggage_all()
        time.sleep(5)
        product_list1.click_page_num()
        product_list1.click_page_all()
        b = new_find_element(self.driver,product_list.mergaNum).text
        time.sleep(2)
        a = self.driver.find_elements_by_link_text('快速购买')
        assert len(a) == int(b)

    def test_081_TUMIUAT_463(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        a=new_find_element(self.driver,product_list.product_name).text
        product_list1.click_buy_now()
        time.sleep(3)
        assert a == new_find_element(self.driver,product_list.b_product_name).text

    def test_082_TUMIUAT_471(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_f_compare()
        product_list1.click_s_compare()
        product_list1.click_immediately_to_compare()
        assert new_find_element(self.driver,product_list.continue_shopping).text == '继续购物'
        assert new_find_element(self.driver,product_list.mailToLink).text == '邮件结果'
        assert new_find_element(self.driver,product_list.res).text == '打印结果'
        # product_list1.click_del_product()
        # product_list1.click_f_compare()


    def test_083_TUMIUAT_472(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        # product_list1.click_f_compare()
        # time.sleep(3)
        # product_list1.click_s_compare()
        product_list1.click_immediately_to_compare()
        product_list1.click_continue_shopping()
        assert self.driver.current_url == hk_url

    def test_084_TUMIUAT_474(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_immediately_to_compare()
        product_list1.click_add_to_Cart()
        time.sleep(2)
        assert new_find_element(self.driver,product_list.gotocart).text == '前往购物车'
        self.driver.refresh()

    def test_085_TUMIUAT_1355_1(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_immediately_to_compare()
        a=new_find_element(self.driver,product_list.f_product_name).text
        product_list1.click_cart_content()
        product_list1.click_gotocart()
        print(new_find_element(self.driver,product_list.c_f_product_name).text)
        assert a == new_find_element(self.driver,product_list.c_f_product_name).text

    def test_086_TUMIUAT_1355_2(self):
        product_list1 = product_list(self.driver)
        product_list1.click_f_luggage()
        product_list1.click_s_luggage_buy()
        product_list1.click_immediately_to_compare()
        a=new_find_element(self.driver,product_list.f_product_name).text
        product_list1.click_cart_content()
        time.sleep(3)
        product_list1.click_gotocart()
        b=self.driver.find_elements_by_link_text(a)
        assert len(b) == 1




