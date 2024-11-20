class Commands:
    def __init__(self, hospital, io_helper):
        self._hospital = hospital
        self.io_helper = io_helper

    def get_status(self):
        patient_id = self.io_helper.request_patient_id()
        status = self._hospital.get_status(patient_id)
        self.io_helper.send_status(status)

