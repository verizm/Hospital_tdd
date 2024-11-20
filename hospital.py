from collections import Counter


class Hospital:
    def __init__(self, hospital_db: list, statuses_model: dict):
        self._hospital_db = hospital_db
        self._statuses_model = statuses_model

    def _calculate_next_status(self, patient_index: int) -> int:
        statuses_ids = list(self._statuses_model)
        current_status_id = self._hospital_db[patient_index]
        return statuses_ids[statuses_ids.index(current_status_id) + 1]

    def get_status(self, patient_id: int) -> str:
        patient_index = patient_id - 1
        status_code = self._hospital_db[patient_index]
        return self._statuses_model[status_code]

    def status_up(self, patient_id: int):
        patient_index = patient_id - 1

        self._hospital_db[patient_index] = self._calculate_next_status(patient_index)

    def can_status_up(self, patient_id: int):
        patient_index = patient_id - 1
        return self._hospital_db[patient_index] < max(self._statuses_model)

    def discharge(self, patient_id: int):
        patient_index = patient_id - 1
        self._hospital_db[patient_index] = None

    def _exclude_discharged_patients(self) -> list:
        return list(filter(lambda item: item is not None, self._hospital_db))

    def calculate_total_count_patients(self):
        return len(self._exclude_discharged_patients())

    def calculate_statistic(self):
        current_patients = self._exclude_discharged_patients()
        statistic = dict(Counter(current_patients))

        statistic_with_statuses_values = {
            self._statuses_model[status_id]: count_patients for status_id, count_patients in statistic.items()
        }
        return statistic_with_statuses_values
