import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="server selection"
    )


@pytest.fixture(scope="session")     # Runs once before whole execution begins
def user_credentials(request):
    return request.param


@pytest.fixture
def browserInstance(playwright, request):                   # request -> common fixture available which comes under global Pytho fixture
    # global browser
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":                          # elif -> same as elseif in Java
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    #page.goto(url_name)
    yield page                                              # yield -> It will return back this page value, like return
    context.close()
    browser.close()
#2 times, 1st run opened browser and completed, homepage