import logging
import allure
from selenium.webdriver.common.by import By



def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):

        from page.base_page import BasePage

        # 弹框处理的定位列表
        # 黑名单处理
        _black_list = [(By.XPATH, "//*[@text='确认']"),
                       (By.XPATH, "//*[@text='确定']"),
                       (By.XPATH, "//*[@text='下次再说']"),
                       (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")]

        _max_num = 3
        _error_num = 0
        instance:BasePage = args[0]

        try:
            logging.info("run "+func.__name__ + "\n args: \n"+repr(args[1:])+"\n"+repr(kwargs))

            element = func(*args, **kwargs)
            # 找到之前 _erro_num归零
            _error_num = 0
            # 还原会之前的隐式等待
            instance._driver.implicitly_wait(10)
            return element

        except Exception as e:
            instance.screenshot("tmp.png")

            with open("tmp.png", "wb") as f:
                content = f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)

            logging.error("element not found,hand_black list")
            # 出现异常，将隐式等待设置小一点，快速处理弹框
            instance._driver.implicitly_wait(1)
            # 判断异常处理次数
            if _error_num > _max_num:
                raise e
            else:
                _error_num += 1
            # 处理黑名单里面的弹框
            for ele in _black_list:
                elelist = instance._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完成，再去查找目标元素
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
