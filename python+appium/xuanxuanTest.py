import pytest
from appium.webdriver import webdriver

class xuanxuanTest():
    #��
    def setup_class(self):
        print("��ʼ��driver")
        cap = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "",
            "appActivity": "",
            "noReset": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)
        self.driver.implicitly_wait(10)
    #�ر�
    def teardown(self):
        print("�˳�quit")
        self.driver.quit()

    # 1.��¼
    def test_login(self):
        self.driver.find_element_by_xpath(
            "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//*[@text='ע��']").click()
        self.driver.find_element_by_xpath("//*[@text='ȷ��']").click()
        self.driver.find_element_by_xpath("//*[@text='��¼']").click()
    # 2.����������
    def test_taolunzu_Create(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("//*[@text='��������']").click()
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()

    # 3.�ղ�������
    def test_taolunzu_Shoucang(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='�ղ�']").click()

    # 4.ȡ���ղ�������
    def test_taolunzu_Shoucang(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='ȡ���ղ�']").click()

    # 5.�鿴�������Ա�б�
    def test_taolunzu_Numbers(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='��Ա�б�']").click()

    # 6.ͬ��������������Ϣ
    def test_taolunzu_news(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='ͬ���������Ϣ']").click()

    # 7.�鿴�ҵ���Ϣ
    def test_myInformation(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View").click()

    # 8.�鿴����
    def test_guanyu(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()

    # 9.�鿴��˽����
    def test_yinsitiaokuan(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()
        self.driver.find_element_by_xpath("//*[@text='��˽����']").click()

    # 10.�鿴��������
    def test_xuanxuan(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()
        self.driver.find_element_by_xpath("//*[@text='http://xuan.im']").click()

    # 11.�˳���ǰ��¼�˺�
    def test_quitXuanxuan(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//*[@text='ע��']").click()
        self.driver.find_element_by_xpath("//*[@text='ȷ��']").click()

    # 12.�鿴��ϵ�˵�����
    def test_lianxirenInformation(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]").click()
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()

    # 13.�ղ���ϵ��
    def test_shoucanglianxiren(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]").click()
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='�ղ�']").click()

    # 14.����ϵ�˷��ʼ�
    def test_sendEmail(self):
        self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()
        self.driver.find_element_by_xpath("//*[@text='Email 13618556496@163.com']").click()

    #15.��ϵ�ˣ�����
    def test_Information(self):
         self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]") \
             .click()
         self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]").click()
         self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.widget.Button[1]").click()

    #16.��ϵ�ˣ�ͬ����Ϣ
    def test_Syn(self):
         self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]").click()
         self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]").click()

    # 17.��������鰴ť�����ϵͳ
    def test_System(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]").click()

    # 18.�����飬ϵͳ���ղ�
    def test_Sysconnect(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]").click()

    # 19.�����飬ϵͳ��ȡ���ղ�
    def test_Sysnocontent(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]").click()

    # 20. �����飬ϵͳ����Ա�б�
    def test_Syslist(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button").click()

    #21.�����飬ϵͳ����Ա�б�,˽��
    def test_Syslistsend(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button").click()

    # 22.�����飬ϵͳ��ͬ����Ϣ
    def test_Groupsyn(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]").click()

    # 23.�ҵ�
    def test_About(self):
        self.driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.Button[3]").click()

    # self.driver.find_element_by_xpath("").click()
    if __name__=="__main__":
        pytest.main(["-s","xuanxuan_demo.py"])
