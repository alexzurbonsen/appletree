#import ipaddress
import logging
#import subprocess
import unittest
import sentry_sdk

sentry_sdk.init(
    "https://292a6f85ea294d12937ec876e40dd907@o1036395.ingest.sentry.io/6005142",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

class TestSentry(unittest.TestCase) :

    def setUp(self):
        pass

    def test_sentry(self):
        sentry_sdk.capture_message("Hello World")
        logging.error("Hello Sentry")

if __name__ == '__main__':
    unittest.main()
