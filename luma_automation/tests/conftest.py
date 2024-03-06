
import logging
import os
import sys

import pytest
from py.xml import html

# append automation folder to path
automation_folder = os.path.dirname(os.path.abspath(__file__))
while not automation_folder.endswith('luma_automation'):
    automation_folder = os.path.dirname(automation_folder)
if automation_folder not in sys.path:
    sys.path.append(automation_folder)

LOG = logging.getLogger(__name__)


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Test Case', class_="sortable testcase", col="testcase"))
    cells.insert(2, html.th('Bug ID', class_="sortable bugid", col="bugid"))
    cells.insert(2, html.th('Current Location', class_="sortable currentlocation", col="currentlocation"))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    # add testcase id column
    if hasattr(report, 'testcase'):
        testcase_id = str(report.testcase)
    else:
        testcase_id = ""
    cells.insert(2, html.td(testcase_id, class_='col-testcase'))
    # add current location column
    if hasattr(report, 'current_location'):
        current_location = str(report.current_location)
    else:
        current_location = ""
    cells.insert(2, html.td(str(current_location), class_='col-currentlocation'))
    cells.pop()


def get_screenshot_html(screenshot_path_relative_to_report):
    return f'<div><a href="{screenshot_path_relative_to_report}"><img src="{screenshot_path_relative_to_report}" ' \
           f'alt="screenshot" style="width:320px;" onclick="window.open(this.src)" align="right"/></a></div>'


def get_pytest_html_report_directory_path(html_path):
    pytest_html_directory_path = os.sep.join(html_path.split(os.sep)[:-1]) or '.'
    return os.path.abspath(pytest_html_directory_path)


def get_screenshot_path_relative_to_report(pytest_report_dir, screenshot_location):
    return screenshot_location.split(f"{pytest_report_dir}{os.sep}")[-1]


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    # runs at setup, call and teardown
    print(call.when, item.name)
    outcome = yield
    report = outcome.get_result()
    report.testcase = get_test_testcase(item)
    if hasattr(item, "rep_status"):
        current_status = item.rep_status.passed
    else:
        current_status = report.failed
    setattr(item, "rep_status", report or current_status)

    extra = getattr(report, 'extra', [])
    pytest_report_dir = get_pytest_html_report_directory_path(pytest.html_path)

    if item.rep_status.failed:
        # if stage is failed, take screenshot and add it to report
        screenshot_location = getattr(item, "screenshot", '')
        current_url = getattr(item, "current_location", '')
        if not screenshot_location:
            try:
                from framework.core import browser
                screenshot_location = browser.take_screenshot()
                current_url = browser.get_current_location()
            except Exception:
                pass
            setattr(item, "current_location", current_url)
            setattr(item, "screenshot", screenshot_location)

        screenshot_path_relative_to_report = get_screenshot_path_relative_to_report(
            pytest_report_dir=pytest_report_dir, screenshot_location=screenshot_location)
        report.current_location = current_url
        report.screenshot = screenshot_path_relative_to_report
        pytest_html = item.config.pluginmanager.getplugin('html')
        screenshot_html = get_screenshot_html(screenshot_path_relative_to_report)
        extra.append(pytest_html.extras.html(screenshot_html))
        report.extra = extra


def get_test_testcase(item):
    """
    Returns testcase if it was added to the test using pytestmark marker or it is present in the
    parameters list when parametrize was used
    :param item: Function Item responsible for setting up and executing a Python test function
    :return: str
    """
    if hasattr(item.function, "pytestmark"):
        for marker in item.function.pytestmark:
            if marker.name == "testcase":
                return marker.args[0]
            if marker.name == 'parametrize' and 'testcase' in item.callspec.params:
                return item.callspec.params['testcase']
    return ""


def pytest_addoption(parser):
    parser.addoption("--host", required=False,default="https://magento.softwaretestingboard.com/", help="Host address where Candid NB API server is running.")
    parser.addoption("--open_dev_tools", default=False)

def pytest_configure(config):
    pytest.host = config.getoption('host')
    pytest.open_dev_tools = config.getoption('open_dev_tools')
    pytest.html_path = config.option.htmlpath

@pytest.fixture(scope='module', autouse=False)
def base_ui():
    from framework.pages import landing
    base_ui = landing.LandingPage()
    return base_ui

@pytest.fixture(scope='module', autouse=True)
def setup(base_ui,request):
    from framework.core import BrowserInterface
    browser = BrowserInterface(pytest.host)
    base_ui.perform_login()

    def teardown():
        if browser:
            base_ui.perform_logout()
            browser.current_browser.quit()

    request.addfinalizer(teardown)
    return browser
