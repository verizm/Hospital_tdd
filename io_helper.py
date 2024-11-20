class IoHelper:
    def __init__(self, console):
        self._console = console

    def send_status(self, status: str):
        self._console.print(f"Cтатус пациента: '{status}'")

    def request_patient_id(self) -> int:
        patient_id = self._console.input("Введите ID пациента: ").strip()
        return int(patient_id)
