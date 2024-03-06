from __future__ import absolute_import

import logging
import sys
import time
import traceback

import pytest

try:
    from urlparse import urlparse
    from urlparse import urlunparse
    from urlparse import ParseResult
except ImportError:
    # Python3 compatibility
    from urllib.parse import urlparse
    from urllib.parse import urlunparse
    from urllib.parse import ParseResult

LOG = logging.getLogger(__name__)


class BrowserInterface(object):
    def __init__(self, host):
        from selenium import webdriver
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

        from framework.core import browser

        url = urlparse(host)
        parsed_host = url.netloc if url.scheme else url.path.split("/")[0]
        schema = url.scheme if url.scheme else 'https'
        # noinspection PyArgumentList
        new_parsed = ParseResult(scheme=schema, netloc=parsed_host,
                                 path='', params='', query='',
                                 fragment='')
        host = urlunparse(new_parsed)

        capabilities = DesiredCapabilities.CHROME.copy()

        capabilities['e34:auth'] = "sx9469pnzb6637qd"
        capabilities['e34:video'] = True
        capabilities['chromeOptions'] = {
            'args': [
                '--disable-extensions',
                '--disable-gpu',
                '--disable-infobars',
                '--start-maximized'
            ],
            'prefs': {
                'download.prompt_for_download': False,
                'plugins.always_open_pdf_externally': True,
                'safebrowsing_for_trusted_sources_enabled': False
            }
        }

        self.current_browser = None
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        # to run tests on local
        pytest.BROWSER = webdriver.Chrome()

        self.current_browser = None
        try:
            self.current_browser = pytest.BROWSER
            LOG.info("Started browser session id {}".format(self.current_browser.session_id))
            self.current_browser.get(host)
            # wait for page to load
            time.sleep(3)

            self.host = host
        except Exception:
            if self.current_browser:
                self.current_browser.quit()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            ex_string = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
            raise Exception("Initial setup failed. {}".format(ex_string))

    def now_on(self, page_class):
        self.current_page = page_class()
        return self.current_page
