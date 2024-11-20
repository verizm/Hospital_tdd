class Commands:
    def __init__(self, hospital, communication_with_user):
        self._hospital = hospital
        self._communication_with_user = communication_with_user

    def get_status(self):
        patient_id = self._communication_with_user.request_patient_id()
        status = self._hospital.get_status(patient_id)
        self._communication_with_user.send_status(status)

    def status_up(self):
        patient_id = self._communication_with_user.request_patient_id()
        if self._hospital.can_status_up(patient_id):
            self._hospital.status_up(patient_id)
            status = self._hospital.get_status(patient_id)
            self._communication_with_user.send_new_status(status)
        else:
            if self._communication_with_user.request_need_to_discharge():
                self._hospital.discharge(patient_id)
                self._communication_with_user.send_patient_discharged()
            else:
                status = self._hospital.get_status(patient_id)
                self._communication_with_user.send_status_not_changed(status)
