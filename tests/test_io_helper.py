from unittest.mock import MagicMock
from io_helper import IoHelper


class TestIoHelper:

    def test_send_status(self):
        mock = MagicMock()
        io_helper = IoHelper(mock)

        io_helper.send_status('Болен')
        mock.print.assert_called_with("Cтатус пациента: 'Болен'")

    def test_request_patient_id(self):
        mock = MagicMock()
        io_helper = IoHelper(mock)
        mock.input.return_value = "1"

        patient_id = io_helper.request_patient_id()
        mock.input.assert_called_with("Введите ID пациента: ")
        assert patient_id == 1

    def test_request_command(self):
        mock = MagicMock()
        io_helper = IoHelper(mock)
        mock.input.return_value = " get status "

        cmd = io_helper.request_command()

        mock.input.assert_called_with("Введите команду: ")
        assert cmd == "get status"

    def test_send_stop_application(self):
        mock = MagicMock()
        io_helper = IoHelper(mock)

        io_helper.send_stop_application()

        mock.print.assert_called_with("Сеанс завершён.")

