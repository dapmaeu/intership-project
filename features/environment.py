from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from app.application import Application

def browser_init(context, scenario_name):
    """
    #:param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # mobile_emulation = {
    #     "deviceName": "Pixel 2"  # Choose a mobile device
    # }
    #
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # # Initialize WebDriver with mobile emulation
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)


    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # bs_user = 'mariadapello_PU8uOI'
    # bs_key = '4v4bdpMsGpRYkH3u39Bd'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "OS X",
    #     "osVersion" : "Monterey",
    #     'browserName': 'Safari',
    #     'sessionName': scenario_name,
    # }
    # #FOR MOBILE BSTACK OPTIONS
    # bstack_options = {
    #     "deviceName" : "Samsung Galaxy S22 Ultra",
    #     "platformName" : "Android",
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/sale_status.feature
    #allure serve test_results

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
    context.wait = WebDriverWait(context.driver, 10)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
