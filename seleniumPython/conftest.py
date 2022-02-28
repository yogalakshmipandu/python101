import pytest
import urllib3
from selenium import webdriver

user_name = "panabakamnoothan"
app_key = "nTJGmEd5ONboKwHcZiC0TrsNoGtqsTfrks2UCrYwQmYMiZPLSM"

TERMS_LIST = [
    ['chrome', 'Windows 10', '80.0', 'sample'],
    ['firefox', 'Windows 7', '82.0', 'sample'],
    ['MicrosoftEdge', 'macOS Sierra', '87.0', 'sample'],
    ['Internet Explorer', 'Windows 10', '11.0', 'sample']
]


# ["chrome", "firefox", "MicrosoftEdge", "Internet Explorer"]
@pytest.fixture(params=TERMS_LIST)
def setup(request):
    param_one, param_2, param_3, param_4 = request.param
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    #remote_url = "https://panabakamnoothan:nTJGmEd5ONboKwHcZiC0TrsNoGtqsTfrks2UCrYwQmYMiZPLSM@hub.lambdatest.com/wd/hub"
    capabilities = {
        "build": param_4,
        "platform": param_2,
        "browserName": param_one,
        "version": param_3,

    }

    web_driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=capabilities)
    request.cls.driver = web_driver

