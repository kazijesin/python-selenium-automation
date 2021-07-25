from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver

from app.application import Application
from support.logger import logger, MyListener

# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
#bs_user = 'kazijesin_ceSJPA'
#bs_pw = 'Wyz4ovrkC3sGMXjHYpPX'


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    #context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    #context.driver = webdriver.Chrome(executable_path='/Users/charjapadamin/Automation_2/python-selenium-automation/chromedriver')
    context.driver = webdriver.Firefox(executable_path= '/Users/charjapadamin/Automation_New/python-selenium-automation/geckodriver')
    # context.browser = webdriver.Firefox()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options)

    ###EventFiringWebDriver - log file###
    ### for drivers ###
    #context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
     ###for headless mode ###
     #context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=options), MyListener())

    ### for browerstack ###
    #desired_cap = {
         #'browser': 'Chrome',
         #'browser_version': '91',
         #'os': 'Windows',
         #'os_version': '10',
         #'name': test_name
     #}
    #url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    #context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)


    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'\nStarted step: {step}')

def after_step(context, step):
    if step.status == 'failed':
        logger.info(f'\nStep failed: {step}')

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()