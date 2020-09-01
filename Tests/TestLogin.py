from appium import webdriver

"""
Desired Capabilities
"""

desired_cap = {
    "platformName": "Android",
    "deviceName": "Galaxy A6",
    "udid": "52005246586a65fb",
    "appPackage": "vieon.phim.tv",
    "appActivity": "vieon.phim.tv.MainActivity",
    "automationName": "uiautomator2"
}

# Create the driver instances
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(20)

# close the popup
driver.find_element_by_xpath("//android.widget.TextView[@text='Cho phép']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text ='Bỏ qua']").click()
driver.implicitly_wait(20)

# select Individual and Login button
driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc='ProfileSetting']/android.widget.ImageView").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='Đăng nhập']").click()
driver.implicitly_wait(20)

# Input Login form
driver.find_element_by_xpath("//android.widget.EditText[@text='Số điện thoại']").send_keys("0966080747")
driver.find_element_by_xpath("//android.widget.EditText[@text='Mật khẩu']").send_keys("123456")
driver.implicitly_wait(20)
driver.find_element_by_xpath("//android.widget.TextView[@text='Đăng nhập']").click()
#submitButton = driver.find_element_by_xpath("//android.widget.TextView[@text='Đăng nhập']")
#driver.execute_script("arguments[0].click();", submitButton)
