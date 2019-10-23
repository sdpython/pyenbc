"""
@brief      test log(time=0s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase


class TestCodeStyle(ExtTestCase):

    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG,
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'W0703', 'W0123', 'C0302', 'W0622', 'W0107', 'C0415'),
                   skip=["Attribute 'session_params' defined outside __init__",
                         "Consider iterating the dictionary directly instead of calling .keys()",
                         "azure_transfer_api.py:20: W0231",
                         "Attribute '_service' defined outside __init__ ",
                         "magic_azure.py:303: W0612",
                         "R1720",
                         ])

    def test_style_test(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*",
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'W0511', 'W0622', 'R1710', 'E1133', 'W0107',
                                  'C0415'),
                   skip=["defined outside __init__ ",
                         "Value 'codes' is unsubscriptable",
                         "test_LONG_HTTP_jython.py:171: E1128",
                         "test_LONG_HTTP_jython.py:171: E1111",
                         "R1720",
                         ])


if __name__ == "__main__":
    unittest.main()
