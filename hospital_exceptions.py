class PatientIdIsNotPositiveIntegerError(Exception):
    def __init__(self):
        self.message = "Ошибка. ID пациента должно быть числом (целым, положительным)"
        super().__init__()


class PatientIsNotExistsError(Exception):
    def __init__(self):
        self.message = "Ошибка. В больнице нет пациента с таким ID"
        super().__init__()


class PatientStatusTooHighError(Exception):
    def __init__(self):
        super().__init__()
