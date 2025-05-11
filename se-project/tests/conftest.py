
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser",action="store",default="chrome",help="Send 'chrome' or 'firefox' as parameter for execution"
    )

@pytest.fixture()
def driver(request):
    browser=request.config.getoption("--browser")
    driver=""
    options=Options()
    options.add_argument("--headless")
    #setup
    print(f"\nSetting up:{browser} driver")
    if browser=="chrome":
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    elif browser=="firefox":
        driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.implicitly_wait(10)
    yield driver
    print(f"\nTear down: {browser} driver")
    driver.quit()