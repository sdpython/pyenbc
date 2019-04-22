"""
@brief      test log(time=140s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyenbc.remote import ASSHClient


class TestLsFormat(unittest.TestCase):

    def test_ls(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        line = "-rw-rw-r-- 1 xavierdupre xavierdupre 21546346 Sep 27 11:18 ConfLongDemo_JSI.txt"
        out = ASSHClient.parse_lsout(line, False)
        self.assertEqual(out.shape, (1, 9))
        fLOG(out)
        fLOG(out.columns)


if __name__ == "__main__":
    unittest.main()
