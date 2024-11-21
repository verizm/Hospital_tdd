from hospital_exceptions import PatientIdIsNotPositiveIntegerError


class UserInteraction:
    def __init__(self, console):
        self._console = console
        self._commands_storage = {
            "get_status": ["get status", "узнать статус"],
            "status_up": ["status up", "повысить статус"],
            "statistic": ["calculate statistic", "рассчитать статистику"],
            "stop": ["stop", "стоп"],
        }

    def request_patient_id(self) -> int:
        patient_id = self._console.input(f"Введите ID пациента: ").strip()

        if not patient_id.isdigit() or int(patient_id) <= 0:
            raise PatientIdIsNotPositiveIntegerError
        return int(patient_id)

    def request_command(self):
        command = self._console.input("Введите команду: ").strip()
        return self._convert_command_to_command_type(command)

    def _convert_command_to_command_type(self, command: str) -> str:
        command = command.lower()

        for command_type, commands in self._commands_storage.items():
            if command in commands:
                return command_type
        return "unknown_command"

    def send_status(self, status: str):
        self._console.print(f"Cтатус пациента: '{status}'")

    def send_stop_application(self):
        return self._console.print("Сеанс завершён.")

    def send_new_status(self, status: str):
        return self._console.print(f"Новый статус пациента: {status}")

    def request_need_to_discharge(self) -> bool:
        answer = self._console.input("Желаете этого клиента выписать? (да/нет) ").strip()
        return answer.lower() == "да"

    def send_status_not_changed(self, status):
        self._console.print(f"Пациент остался в статусе '{status}'")

    def send_patient_discharged(self):
        self._console.print("Пациент выписан из больницы")

    def send_statistic(self, total_count_patients: int, statistic: dict):
        self._console.print(f"В больнице на данный момент находится {total_count_patients} чел., из них:")
        for status, count_patients in statistic.items():
            self._console.print(f"- в статусе '{status}': {count_patients} чел.")

    def send_message(self, message: str):
        self._console.print(message)

    def send_unknown_command(self):
        self._console.print("Неизвестная команда! Попробуйте ещё раз")
