import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru", help="Language for autotests")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language not in ["ru", "en-GB", "es", "fr"]:
        raise pytest.UsageError("Select an existing language")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.user_language = language

    yield browser

    print("\nquit browser..")
    browser.quit()
