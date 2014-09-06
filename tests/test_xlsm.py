import os
from base import PyexcelXlsBase


class TestXLSXReader(PyexcelXlsBase):
    def setUp(self):
        """
        Declare the test xlsx  file.

        It is pre-made as csv file:

        1,1,1,1
        2,2,2,2
        3,3,3,3
        """
        self.testfile = os.path.join("tests", "testxlsm.xlsm")
        self.rows = 3