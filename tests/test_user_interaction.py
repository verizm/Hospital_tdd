from unittest.mock import (
    MagicMock,
    call,
)

import pytest

from hospital_exceptions import PatientIdIsNotPositiveIntegerError
from user_interaction import UserInteraction


class TestUserInteraction:

    def test_send_status(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)

        user_interaction.send_status('Болен')
        console.print.assert_called_with("Cтатус пациента: 'Болен'")

    def test_request_patient_id(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)
        console.input.return_value = "1"

        patient_id = user_interaction.request_patient_id()
        console.input.assert_called_with("Введите ID пациента: ")
        assert patient_id == 1

    @pytest.mark.parametrize("input_value", ["0.1", "-1", "0", "один"])
    def test_request_patient_id_when_id_is_not_positive_integer(self, input_value):
        console = MagicMock()
        user_interaction = UserInteraction(console)
        console.input.return_value = input_value

        with pytest.raises(PatientIdIsNotPositiveIntegerError):
            user_interaction.request_patient_id()

    def test_request_command(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)
        console.input.return_value = " get status "

        cmd = user_interaction.request_command()

        console.input.assert_called_with("Введите команду: ")
        assert cmd == "get status"

    def test_send_stop_application(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)

        user_interaction.send_stop_application()

        console.print.assert_called_with("Сеанс завершён.")

    def test_send_new_status(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)

        user_interaction.send_new_status('Болен')

        console.print.assert_called_with("Новый статус пациента: Болен")

    def test_request_need_to_discharge(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)
        console.input.return_value = " да "

        assert user_interaction.request_need_to_discharge()

    def test_send_status_not_changed(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)

        user_interaction.send_status_not_changed("Готов к выписке")

        console.print.assert_called_with("Пациент остался в статусе 'Готов к выписке'")

    def test_send_patient_discharged(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)

        user_interaction.send_patient_discharged()

        console.print.assert_called_with("Пациент выписан из больницы")

    def test_send_statistic(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)

        user_interaction.send_statistic(total_count_patients=6, statistic={"Тяжело болен": 3, "Слегка болен": 3})

        console.assert_has_calls(
            [
                call.print("В больнице на данный момент находится 6 чел., из них:"),
                call.print("- в статусе 'Тяжело болен': 3 чел."),
                call.print("- в статусе 'Слегка болен': 3 чел.")
            ]
        )

    def test_send_message(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)

        user_interaction.send_message("Random message")

        console.print.assert_called_with("Random message")

    def test_request_command(self):
        console = MagicMock()
        user_interaction = UserInteraction(console)
        console.input.return_value = "get status"

        assert user_interaction.request_command() == "get_status"
        console.input.assert_has_calls("Введите команду: ")

    @pytest.mark.parametrize(
        "command, command_type",
            [
                ("get status", "get_status"),
                ("узнать статус пациeнта", "get_status"),
                ("стоп", "stop"),
                ("STOP", "stop"),
                ("status up", "status_up"),
                ("рассчитать статистику", "calculate_statistic"),

            ]
        )
    def test_convert_command_to_command_type(self, command, command_type):
        console = MagicMock()
        user_interaction = UserInteraction(console)

        assert user_interaction._convert_command_to_command_type(command) == command_type
