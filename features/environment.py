from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#init driver

def browser_init(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


#from sample_script import driver


def browser_init(context):
    """
    :param context:behave context
    """
    #context.driver = webdriver.Chrome(executable_path = '/Users/raihanamin/Automation/python-selenium-automation/chromedriver')
    context.driver.maximize_window()
    #context.browser = webdriver.Safari())'
    #context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.browser.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
