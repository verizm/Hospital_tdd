class CommunicationWithUser:
    def __init__(self, console):
        self._console = console

    def request_patient_id(self) -> int:
        patient_id = self._console.input("Введите ID пациента: ").strip()
        return int(patient_id)

    def request_command(self):
        return self._console.input("Введите команду: ").strip()

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
