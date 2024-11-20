from unittest.mock import MagicMock
from communication_with_user import CommunicationWithUser


class TestCommunicationWithUser:

    def test_send_status(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)

        communication_with_user.send_status('Болен')
        console.print.assert_called_with("Cтатус пациента: 'Болен'")

    def test_request_patient_id(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)
        console.input.return_value = "1"

        patient_id = communication_with_user.request_patient_id()
        console.input.assert_called_with("Введите ID пациента: ")
        assert patient_id == 1

    def test_request_command(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)
        console.input.return_value = " get status "

        cmd = communication_with_user.request_command()

        console.input.assert_called_with("Введите команду: ")
        assert cmd == "get status"

    def test_send_stop_application(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)

        communication_with_user.send_stop_application()

        console.print.assert_called_with("Сеанс завершён.")

    def test_send_new_status(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)

        communication_with_user.send_new_status('Болен')

        console.print.assert_called_with("Новый статус пациента: Болен")

    def test_request_need_to_discharge(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)
        console.input.return_value = " да "

        assert communication_with_user.request_need_to_discharge()

    def test_send_status_not_changed(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)

        communication_with_user.send_status_not_changed("Готов к выписке")

        console.print.assert_called_with("Пациент остался в статусе 'Готов к выписке'")

