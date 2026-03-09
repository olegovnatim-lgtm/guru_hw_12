import pytest
from selene import browser, have
from selene.support.shared import config


@pytest.fixture(scope='function')
def setup_browser():
    config.browser_name = 'chrome'
    config.remote_url = 'https://user1:1234@selenoid.autotests.cloud/wd/hub'
    config.timeout = 10

    yield browser
    browser.quit()


# # Тест
# def test_login(setup_browser):
#     browser.open("https://example.com/login")
#     browser.element("#username").type("user123")
#     browser.element("#password").type("pass456")
#     browser.element("button[type='submit']").click()
#
#     # Проверка
#     browser.element(".welcome").should(have.text("Welcome"))
#     browser.should(have.url("https://example.com/dashboard"))




# import os
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selene import Browser, Config
# from dotenv import load_dotenv
#
# from utils import attach
#
# DEFAULT_BROWSER_VERSION = "100.0"
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser_version',
#         default='128.0'
#     )
#
#
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()
#
#
# @pytest.fixture(scope='function')
# def setup_browser(request):
#     browser_version = request.config.getoption('--browser_version')
#     browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": browser_version,
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#
#     login = os.getenv('LOGIN')
#     password = os.getenv('PASSWORD')
#
#     driver = webdriver.Remote(
#         command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#     browser = Browser(Config(driver))
#
#     yield browser
#
#     attach.add_html(browser)
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_video(browser)
#     browser.quit()
