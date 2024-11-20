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
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        console.input.side_effect = ["get status", "1", "стоп"]
        hospital = Hospital([0, 3, 2], statuses)
        commands = Commands(hospital, communication_with_user)

        Application(commands, communication_with_user).run()

        console.assert_has_calls(
            [
                call.input("Введите команду: "),
                call.input("Введите ID пациента: "),
                call.print("Cтатус пациента: 'Тяжело болен'"),
                call.input("Введите команду: "),
                call.print("Сеанс завершён."),
            ]
        )

    def test_status_up(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        console.input.side_effect = ["status up", "1", "стоп"]

        hospital = Hospital([0, 3, 2], statuses)
        commands = Commands(hospital, communication_with_user)
        Application(commands, communication_with_user).run()

        console.assert_has_calls(
            [
                call.input("Введите команду: "),
                call.input("Введите ID пациента: "),
                call.print("Новый статус пациента: Болен"),
                call.input("Введите команду: "),
                call.print("Сеанс завершён."),
            ]
        )

    def test_status_up_when_status_too_high_and_patient_not_discharged(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        console.input.side_effect = ["status up", "1", "нет", "стоп"]

        hospital = Hospital([3, 1, 2], statuses)
        commands = Commands(hospital, communication_with_user)
        Application(commands, communication_with_user).run()

        console.assert_has_calls(
            [
                call.input("Введите команду: "),
                call.input("Введите ID пациента: "),
                call.input("Желаете этого клиента выписать? (да/нет) "),
                call.print("Пациент остался в статусе 'Готов к выписке'"),
                call.input("Введите команду: "),
                call.print("Сеанс завершён."),
            ]
        )

    def test_status_up_when_status_too_high_and_patient_discharged(self):
        console = MagicMock()
        communication_with_user = CommunicationWithUser(console)
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        console.input.side_effect = ["status up", "1", "да", "стоп"]

        hospital = Hospital([3, 1, 2], statuses)
        commands = Commands(hospital, communication_with_user)
        Application(commands, communication_with_user).run()

        console.assert_has_calls(
            [
                call.input("Введите команду: "),
                call.input("Введите ID пациента: "),
                call.input("Желаете этого клиента выписать? (да/нет) "),
                call.print("Пациент выписан из больницы"),
                call.input("Введите команду: "),
                call.print("Сеанс завершён."),
            ]
        )

