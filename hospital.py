class Hospital:
    def __init__(self, hospital_db: list, statuses_model: dict):
        self._hospital_db = hospital_db
        self._statuses_model = statuses_model

    def get_status(self, patient_id: int) -> str:
        patient_index = patient_id - 1
        status_code = self._hospital_db[patient_index]
        return self._statuses_model[status_code]

