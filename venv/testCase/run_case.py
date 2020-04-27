__author__ = "starry"

from HtmlTestRunner import HTMLTestRunner
import unittest
import time
import os
import sys
from testCase import send_email

test_list = sys.path[0]
print(test_list)

result = "./Result"

# create a test suit
def Creatsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_list, pattern='test_*.py', top_level_dir=None)
    print (discover)
    for test_suit in discover:
        for case_name in test_suit:
            testunit.addTest(case_name)
            print (case_name)
        print (testunit)
    return testunit

test_case = Creatsuite()
try:
    runner = HTMLTestRunner(report_title=u'SkyDRM SERVER UI Automation Test Report', combine_reports=True,
                            report_name="SERVER UI Automation TEST REPORT", failfast=False)
    runner.run(test_case)
    folder = "./reports/"
    files = os.listdir(folder)
    file_name = files[len(files) - 1].title()
    print(file_name)

    file_path = folder + file_name

    send = send_email.send()
    send.send_to_user(file_path)
except AssertionError as a:
    print(a)

except Exception as e:
    print(e)
    assert False


