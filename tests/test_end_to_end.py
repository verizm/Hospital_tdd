from unittest.mock import (
    MagicMock,
    call,
)

from application import Application
from communication_with_user import CommunicationWithUser
from hospital import Hospital
from commands import Commands


class TestHospitalApplication:

    def test_get_status_command(self):
        console_mock = MagicMock()
        communication_with_user = CommunicationWithUser(console_mock)
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        console_mock.input.side_effect = ["get status", "1", "стоп"]
        hospital = Hospital([0, 3, 2], statuses)
        commands = Commands(hospital, communication_with_user)

        Application(commands, communication_with_user).run()

        console_mock.assert_has_calls(
            [
                call.input("Введите команду: "),
                call.input("Введите ID пациента: "),
                call.print("Cтатус пациента: 'Тяжело болен'"),
                call.input("Введите команду: "),
                call.print("Сеанс завершён."),
            ]
        )
