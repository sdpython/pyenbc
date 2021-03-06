"""
@brief      test log(time=140s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyenbc.remote.magic_azure import MagicAzure


class MockObject:
    pass


class TestMagicAzure(unittest.TestCase):

    def test_blob_path(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mg = MagicAzure()
        mg.shell = MockObject()
        mg.shell.user_ns = {"remote_azure_client": MockObject(),
                            "remote_azure_blob": MockObject()}
        mg.shell.user_ns["remote_azure_client"].account_name = "ACC"
        cmd = "/part1/part2"
        fLOG("**", cmd)
        res = mg.blob_path(cmd)
        fLOG(res)
        self.assertEqual(res, ('ACC', 'part1/part2'))
        res = mg.blob_path("part1/part2")
        fLOG(res)
        self.assertEqual(res, ('part1', 'part2'))


if __name__ == "__main__":
    unittest.main()
