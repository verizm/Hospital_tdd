from collections import Counter

from hospital_exceptions import PatientIsNotExistsError, PatientStatusTooHighError


class Hospital:
    def __init__(self, hospital_db: list, statuses_model: dict):
        self._hospital_db = hospital_db
        self._statuses_model = statuses_model

    def _convert_patient_id_to_patient_index(self, patient_id: int) -> int:
        patient_index = patient_id - 1
        if len(self._hospital_db) <= int(patient_index) or self._hospital_db[patient_index] is None:
            raise PatientIsNotExistsError
        return patient_index

    def _check_status_less_when_max_status(self, patient_index) -> bool:
        return self._hospital_db[patient_index] < max(self._statuses_model)

    def _calculate_next_status(self, patient_index: int) -> int:
        statuses_ids = list(self._statuses_model)
        current_status_id = self._hospital_db[patient_index]
        if not self._check_status_less_when_max_status(patient_index):
            raise PatientStatusTooHighError
        return statuses_ids[statuses_ids.index(current_status_id) + 1]

    def get_status(self, patient_id: int) -> str:
        patient_index = self._convert_patient_id_to_patient_index(patient_id)
        status_code = self._hospital_db[patient_index]
        return self._statuses_model[status_code]

    def status_up(self, patient_id: int):
        patient_index = self._convert_patient_id_to_patient_index(patient_id)
        self._hospital_db[patient_index] = self._calculate_next_status(patient_index)

    def can_status_up(self, patient_id: int):
        patient_index = self._convert_patient_id_to_patient_index(patient_id)
        return self._check_status_less_when_max_status(patient_index)

    def discharge(self, patient_id: int):
        patient_index = self._convert_patient_id_to_patient_index(patient_id)
        self._hospital_db[patient_index] = None

    def _exclude_discharged_patients(self) -> list:
        return list(filter(lambda item: item is not None, self._hospital_db))

    def calculate_total_count_patients(self):
        return len(self._exclude_discharged_patients())

    def calculate_statistic(self):
        statistic = Counter(self._exclude_discharged_patients())

        statistic_with_statuses_values = {

            self._statuses_model[status_id]: count_patients for status_id, count_patients in sorted(statistic.items())
        }
        return statistic_with_statuses_values
