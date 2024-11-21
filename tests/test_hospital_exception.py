from hospital_exceptions import (
    PatientIdIsNotPositiveIntegerError,
    PatientIsNotExistsError,
)


class TestHospitalException:

    def test_patient_id_is_not_positive_integer_error(self):
        assert PatientIdIsNotPositiveIntegerError().message == "Ошибка. ID пациента должно быть числом (целым, положительным)"

    def test_patient_is_not_exists_error(self):
        assert PatientIsNotExistsError().message == "Ошибка. В больнице нет пациента с таким ID"
