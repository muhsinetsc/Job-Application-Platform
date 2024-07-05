import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *


@pytest.mark.usefixtures("setup")
class Test_Scenario04(functions):

    def test_contact_update(self):
        self.precondition_application()
    