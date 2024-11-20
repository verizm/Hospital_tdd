from unittest.mock import (
    MagicMock,
    call,
)

from hospital import Hospital


class TestHospitalApplication:

    def test_get_status_command(self):
        console_mock = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        console_mock.input.side_effect = ["get status", "1", "стоп"]
        hospital = Hospital([0, 3, 2], statuses)

        Application(hospital, console_mock).run()

        console_mock.assert_has_calls(
            [
                call.input("Введите команду: "),
                call.input("Введите ID пациента: "),
                call.print("Cтатус пациента: Тяжело болен"),
                call.input("Введите команду: "),
                call.print("Сеанс завершён."),
            ]
        )
