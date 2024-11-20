class IoHelper:
    def __init__(self, console):
        self._console = console

    def send_status(self, status: str):
        self._console.print(f"Cтатус пациента: '{status}'")

    def request_patient_id(self) -> int:
        patient_id = self._console.input("Введите ID пациента: ").strip()
        return int(patient_id)

    def request_command(self):
        return self._console.input("Введите команду: ").strip()

    def send_stop_application(self):
        return self._console.print("Сеанс завершён.")
