# @Author ：黄贝尔
# @Time ：2021/2/9__13:39
# #coding:utf-8
from base_page import page
import time
from HK_001_homepage import homepage

class my_account(page):

    #查看个人信息
    view_my_info=('xpath',"//body/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/ul[2]/li[1]/a[1]")

    #查看我的账号
    view_my_account=('xpath','//header/div[3]/div[3]/div[3]/a[1]')
    #更新个人信息
    update_my_info=('xpath',"//a[contains(text(),'Update personal information')]")
    #地址簿
    my_address=('xpath',"//a[contains(text(),'My address book')]")
    #更新密码
    update_my_password=('xpath',"//a[contains(text(),'Update Password')]")
    #附近门店
    nearby_stores=('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/a[1]')
    #返回门店搜索
    store_search=('xpath',"//a[contains(text(),'< Back To Search')]")
    #个性化输入框
    diy_Input=('id','monogram.initials')
    #个性化按钮
    diy_btn=('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]/span[1]')
    #更新个人信息用户名输入框
    account_username=('id','profile.userName')
    #更新个人信息称呼
    account_call =('id','profile.titleSelectBoxIt')
    #小姐称呼
    call_miss = ('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[2]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[3]/span[1]/ul[1]/li[2]/a[1]')
    #更新个人信息邮箱
    account_email=('id','profile.email')
    #更新保存按钮
    account_save_btn=('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[2]/div[2]/form[1]/div[3]/button[1]')
    #取消保存按钮
    no_save=('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[2]/div[2]/form[1]/div[3]/a[1]')
    #个人中心logo
    account_logo=('xpath','//body/div[1]/section[1]/div[4]/div[1]/a[1]/img[1]')
    #用户名报错
    userName_errors=('id','userName.errors')
    #称呼报错
    titleCode_errors=('id','titleCode.errors')
    #称呼-请选择
    call_null=('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[2]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[3]/span[1]/ul[1]/li[1]/a[1]')
    #切换到地址簿
    address_book_btn=('xpath',"//a[contains(text(),'我的地址簿')]")
    #新增地址
    creat_new_address=('xpath',"//span[contains(text(),'添加收货地址')]")
    #地址-收货人输入框
    address_consignee=('id','addressEditTo')
    #地址-手机号输入框
    address_phone=('id','addressEditMobile')
    #地址-点击地区
    address_region=('id','addressEditCityarea')
    #地址-北京
    address_beijing=('xpath',"//a[contains(text(),'北京')]")
    #地址-区
    address_qu=('xpath',"//a[contains(text(),'东城区')]")
    #地址-详细地址输入框
    address_Detailed=('id','addressEditDetail')
    #地址-保存
    address_save=('xpath','//body/div[1]/main[1]/div[2]/div[4]/div[2]/div[1]/div[1]/form[1]/div[7]/button[1]')
    #地址-编辑
    address_edit=('xpath','//body/div[1]/main[1]/div[2]/div[4]/div[2]/div[1]/section[2]/div[2]/a[1]')
    #地址-删除
    address_del=('xpath','//body/div[1]/main[1]/div[2]/div[4]/div[2]/div[1]/section[2]/div[2]/a[2]')
    #地址-收货人姓名
    address_name=('xpath',"/html[1]/body[1]/div[1]/main[1]/div[2]/div[4]/div[2]/div[1]/section[2]/div[1]/ul[1]/li[1]")
    #地址-收货人报错
    nameErrors=('id','name.errors')
    #地址-手机号报错
    phoneErrors=('id','phone.errors')
    #地址-设为默认地址
    default_address=('xpath',"//label[contains(text(),'设为默认地址')]")
    #地址-固定电话-区号
    addressEditAreaCode=('id','addressEditAreaCode')
    #地址-固定电话-电话号
    addressEditTelphone=('id','addressEditTelphone')
    #地址-固定电话报错
    areaPhone_errors=('id','areaPhone.errors')
    #更新密码-当前密码
    now_password=('id','profile.currentPassword')
    #更新密码-新密码
    new_password=('id','profile-newPassword')
    #更新密码-确认新密码
    confirm_new_password=('id','profile.checkNewPassword')
    #更新密码-保存新密码
    save_new_password=('xpath','//body/div[1]/main[1]/div[2]/div[4]/div[2]/div[1]/div[1]/form[1]/div[4]/button[1]')
    #密码修改成功
    modifly_password_successful=('xpath','//body/div[1]/main[1]/div[2]/div[3]/div[1]')
    #修改密码-当前密码报错
    nowPassword_errors=('id','currentPassword.errors')
    #修改密码-新密码报错
    newPassword_errors=('id','newPassword.errors')
    #修改密码-确认密码报错
    checkNewPassword_errors=('id','checkNewPassword.errors')

    my_account_title = ('xpath', "//h2[contains(text(),'My Account')]")
    store_name = ('xpath', "//body/div[1]/main[1]/div[1]/div[2]/div[3]/div[1]/h2[1]")
    store_type = ('xpath', "//div[contains(text(),'Store Type')]")
    diy_title = ('xpath', "//p[contains(text(),'Click on each slots to enter an alphabet, number o')]")



    def __init__(self,driver):
        page.__int__(self, driver)
    def go_to_my_info(self):
        self.click(homepage.login_register_btn)
        time.sleep(1)
        self.input_text(homepage.phone, text='90000001')
        self.input_text(homepage.password, text='1111qqqq')
        self.click(homepage.login_btn)
        time.sleep(1)
        self.click(self.view_my_info)

    def click_account_logo(self):
        self.click(self.account_logo)

    def move_to_logo(self):
        self.action(self.account_logo)
    def go_to_my_account(self):
        homepage1=homepage(self.driver)
        homepage1.login()
        time.sleep(1)
        self.click(self.view_my_account)
        self.driver.refresh()

    def go_to_my_account2(self):
        homepage1=homepage(self.driver)
        homepage1.login2()
        time.sleep(1)
        self.click(self.view_my_account)
        self.driver.refresh()

    def click_nearby_stores(self):
        self.click(self.nearby_stores)

    def click_store_search(self):
        self.click(self.store_search)

    def input_diy(self):
        self.input_text(self.diy_Input,text='1')

    def click_diy_btn(self):
        self.action(self.diy_btn)
        self.click(self.diy_btn)

    def click_update_my_info(self):
        self.click(self.update_my_info)

    def clear_account_username(self):
        self.clear_loc(self.account_username)

    def clear_account_email(self):
        self.clear_loc(self.account_email)

    def input_account_username(self):
        self.input_text(self.account_username,text='测试')

    def click_account_call(self):
        self.click(self.account_call)

    def click_call_miss(self):
        self.click(self.call_miss)

    def input_account_email(self):
        self.input_text(self.account_email,text='testtest@qq.com')

    def click_account_save_btn(self):
        self.click(self.account_save_btn)

    def click_call_null(self):
        self.click(self.call_null)

    def click_no_save(self):
        self.click(self.no_save)

    def click_address_book_btn(self):
        self.click(self.address_book_btn)

    def click_creat_new_address(self):
        self.click(self.creat_new_address)

    def input_address_consignee(self):
        self.input_text(self.address_consignee,text='测试测试')

    def input_address_phone(self):
        self.input_text(self.address_phone,text='17311111111')

    def input_address_phone2(self):
        self.input_text(self.address_phone,text='27311111111')

    def click_address_region(self):
        self.click(self.address_region)

    def click_address_beijing(self):
        self.click(self.address_beijing)

    def click_address_qu(self):
        self.click(self.address_qu)

    def input_address_Detailed(self):
        self.input_text(self.address_Detailed,text='测试地址')

    def click_address_save(self):
        self.click(self.address_save)

    def click_address_edit(self):
        self.click(self.address_edit)

    def click_address_del(self):
        self.click(self.address_del)

    def clear_address_consignee(self):
        self.clear_loc(self.address_consignee)

    def click_default_address(self):
        self.click(self.default_address)

    def input_addressEditAreaCode(self):
        self.input_text(self.addressEditAreaCode,text='021')

    def input_addressEditTelphone(self):
        self.input_text(self.addressEditAreaCode,text='55555555')

    def click_update_my_password(self):
        self.click(self.update_my_password)

    def input_now_password(self):
        self.input_text(self.now_password,text='gxjy541')

    def input_now_password2(self):
        self.input_text(self.now_password,text='1qaz2wsx')

    def input_new_password(self):
        self.input_text(self.new_password,text='1qaz2wsx')

    def input_new_password2(self):
        self.input_text(self.new_password,text='gxjy541')

    def input_confirm_new_password(self):
        self.input_text(self.confirm_new_password,text='1qaz2wsx')

    def input_confirm_new_password2(self):
        self.input_text(self.confirm_new_password,text='gxjy541')

    def click_save_new_password(self):
        self.click(self.save_new_password)














