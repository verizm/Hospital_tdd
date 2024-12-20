from hospital_exceptions import (
    PatientIsNotExistsError,
    PatientIdIsNotPositiveIntegerError,
)


class HospitalUseCases:
    def __init__(self, hospital, user_interaction):
        self._hospital = hospital
        self._user_interaction = user_interaction

    def get_status(self):
        patient_id = self._user_interaction.request_patient_id()
        status = self._hospital.get_status(patient_id)
        self._user_interaction.send_status(status)

    def status_up(self):
        try:
            patient_id = self._user_interaction.request_patient_id()
            if self._hospital.can_status_up(patient_id):
                self._hospital.status_up(patient_id)
                status = self._hospital.get_status(patient_id)
                self._user_interaction.send_new_status(status)
            else:
                if self._user_interaction.request_need_to_discharge():
                    self._hospital.discharge(patient_id)
                    self._user_interaction.send_patient_discharged()
                else:
                    status = self._hospital.get_status(patient_id)
                    self._user_interaction.send_status_not_changed(status)
        except (PatientIsNotExistsError, PatientIdIsNotPositiveIntegerError) as error:
            self._user_interaction.send_message(error.message)

    def calculate_statistic(self):
        total_count_patients = self._hospital.calculate_total_count_patients()
        statistic = self._hospital.calculate_statistic()
        self._user_interaction.send_statistic(total_count_patients, statistic)

