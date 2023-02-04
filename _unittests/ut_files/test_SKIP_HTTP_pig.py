"""
@brief      test log(time=203s)
"""
import os
import unittest
import random
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor
from pyenbc.filehelper import download_java_standalone, is_java_installed
from pyenbc.filehelper.pig_helper import run_pig, download_pig_standalone


class TestPig (unittest.TestCase):

    @unittest.skipIf(True, reason="PIG not maintained anymore")
    def test_simple_pig(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            return

        download_java_standalone()
        assert is_java_installed()

        try:
            download_pig_standalone(fLOG=fLOG)
        except FileNotFoundError:
            # for some unknown reason, it requires to be done twice
            # due to FileNotFoundError: [Errno 2] No such file or directory:
            # 'pyenbc\\src\\pyenbc\\filehelper\\pigjar\\pig-0.15.0\\contrib\\
            # piggybank\\java\\build\\classes\\org\\apache
            # \\pig\\piggybank\\storage\\IndexedStorage$IndexedStorageInputFormat$
            # IndexedStorageRecordReader$IndexedStorageRecordReaderComparator.class'
            download_pig_standalone(fLOG=fLOG)

        # it does not work for the time being
        this = os.path.abspath(os.path.dirname(__file__))
        temp = os.path.join(this, "temp_pig")
        if not os.path.exists(temp):
            os.mkdir(temp)

        rnd = os.path.join(temp, "random.sample.txt")
        with open(rnd, "w") as f:  # pylint: disable=W1514
            for _ in range(0, 1000):
                x = random.random()
                f.write(str(x) + "\n")

        pg = os.path.normpath(os.path.join(temp, "..", "p1.pig"))
        tf = "file:/" + rnd.replace("\\", "/")
        with open(pg, "w", encoding="utf8") as f:
            f.write('''
                        values = LOAD '%s' USING PigStorage('\t') AS (x:double);
                        values_h = FOREACH values GENERATE x, ((int)(x / 0.1)) * 0.1 AS h ;
                        hist_group = GROUP values_h BY h ;
                        hist = FOREACH hist_group GENERATE group, COUNT(values_h) AS nb ;
                        STORE hist INTO '%s' USING PigStorage('\t') ;
                        '''.replace("                        ", "") %
                    (tf, tf + ".out.txt"))

        out, err = run_pig(pg, fLOG=fLOG, logpath=temp)
        if "first try with pig" not in out:
            raise AssertionError("--OUT--\n{0}\n--ERR--\n{1}".format(out, err))


if __name__ == "__main__":
    unittest.main()
