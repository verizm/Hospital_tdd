class Commands:
    def __init__(self, hospital, console_helper):
        self._hospital = hospital
        self._console_helper = console_helper

    def get_status(self):
        patient_id = self._console_helper.request_patient_id()
        status = self._hospital.get_status(patient_id)
        self._console_helper.send_message(status)

