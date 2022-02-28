import pytest
import urllib3
from selenium import webdriver

user_name = "yogalakshmipandu"
app_key = "NO64PZzTLaQF8YimOWY3nhxI9JJ4iuPZDBOa81Ri1S3kzN539T"

LIST = [
    ['chrome_build','Windows 10','chrome','80.0'],
    ['firefox_build', 'Windows 7','firefox','82.0'],
    [ 'Edge_build', 'macOS Sierra', 'MicrosoftEdge''87.0'],
    ['IE_build', 'Windows 10','Internet Explorer','11.0' ],   
]

@pytest.fixture(parameters=LIST)
def setup(request):
    parameter_1, parameter_2, parameter_3, parameter_4 = request.parameters
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    #remote_url = "https://panabakamnoothan:nTJGmEd5ONboKwHcZiC0TrsNoGtqsTfrks2UCrYwQmYMiZPLSM@hub.lambdatest.com/wd/hub"
    capabilities = {
        "build": parameter_1,
        "platform": parameter_2,
        "browserName": parameter_3,
        "version": parameter_4,
    }

    web_driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=capabilities)
    request.cls.driver = web_driver

