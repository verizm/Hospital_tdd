from unittest.mock import MagicMock

from commands import Commands
from hospital import Hospital


class TestCommands:

    def test_get_status(self):
        communication_with_user = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}
        hospital = Hospital([0, 3, None], statuses)
        cmd = Commands(hospital, communication_with_user)

        communication_with_user.request_patient_id = MagicMock(return_value=2)
        cmd.get_status()

        communication_with_user.send_status.assert_called_with('Готов к выписке')

    def test_status_up(self):
        communication_with_user = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([2, 0, 1], statuses)
        cmd = Commands(hospital, communication_with_user)

        communication_with_user.request_patient_id = MagicMock(return_value=1)
        cmd.status_up()

        communication_with_user.send_new_status.assert_called_with('Готов к выписке')
        assert hospital._hospital_db == [3, 0, 1]
