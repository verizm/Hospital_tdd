from unittest.mock import (
    MagicMock,
    call,
)

from application import Application
from io_helper import IoHelper
from hospital import Hospital
from commands import Commands


class TestHospitalApplication:

    def test_get_status_command(self):
        console_mock = MagicMock()
        io_helper = IoHelper(console_mock)
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        console_mock.input.side_effect = ["get status", "1", "стоп"]
        hospital = Hospital([0, 3, 2], statuses)
        commands = Commands(hospital, io_helper)

        Application(commands, io_helper).run()

        console_mock.assert_has_calls(
            [
                call.input("Введите команду: "),
                call.input("Введите ID пациента: "),
                call.print("Cтатус пациента: 'Тяжело болен'"),
                call.input("Введите команду: "),
                call.print("Сеанс завершён."),
            ]
        )
