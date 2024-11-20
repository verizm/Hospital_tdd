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

    def discharge(self, patient_id: int):
        patient_index = patient_id - 1
        self._hospital_db[patient_index] = None

