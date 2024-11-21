import pytest

from hospital import Hospital
from hospital_exceptions import PatientIsNotExistsError

class TestHospital:

    def test_get_status(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([1, None, 2], statuses)
        assert hospital.get_status(patient_id=1) == "Болен"

    def test_status_up(self):
        statuses = {10: "Тяжело болен", 20: "Болен", 30: "Слегка болен", 40: "Готов к выписке"}

        hospital = Hospital([10, None, 30], statuses)
        hospital.status_up(patient_id=3)

        assert hospital._hospital_db == [10, None, 40]

    def test_can_status_up(self):
        statuses = {1: "Тяжело болен", 2: "Болен", 3: "Слегка болен", 4: "Готов к выписке"}

        hospital = Hospital([1, None, 3], statuses)

        assert hospital.can_status_up(patient_id=3)

    def test_can_status_up_when_status_too_high(self):
        statuses = {10: "Тяжело болен", 20: "Болен", 30: "Слегка болен", 40: "Готов к выписке"}

        hospital = Hospital([10, None, 40], statuses)

        assert not hospital.can_status_up(patient_id=3)

    def test_calculate_next_status(self):
        statuses = {10: "Тяжело болен", 20: "Болен", 30: "Слегка болен", 40: "Готов к выписке"}

        hospital = Hospital([10, None, 30], statuses)

        assert hospital._calculate_next_status(patient_index=2) == 40

    def test_discharge(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([1, 0, 3], statuses)

        hospital.discharge(patient_id=1)

        assert hospital._hospital_db == [None, 0, 3]

    def test_calculate_total_count_patients(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([None, 1, 0,  3, None], statuses)
        hospital.calculate_total_count_patients()

        assert hospital.calculate_total_count_patients() == 3

    def test_exclude_discharged_patient(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([None, 1, 0, None,  3, None], statuses)

        assert hospital._exclude_discharged_patients() == [1, 0,  3]

    def test_calculate_statistic(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([3, 1, 3, 0, 1, None], statuses)
        expected_statistic = {"Тяжело болен": 1, "Болен": 2, "Готов к выписке": 2}

        assert hospital.calculate_statistic() == expected_statistic

    def test_convert_patient_id_to_patient_index(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([1, 0, 3], statuses)

        assert hospital._convert_patient_id_to_patient_index(patient_id=1) == 0

    def test_convert_patient_id_to_patient_index_when_patient_discharged(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([None, 0, 3], statuses)
        with pytest.raises(PatientIsNotExistsError):
            hospital._convert_patient_id_to_patient_index(patient_id=1)

    def test_convert_patient_id_to_patient_index_when_patient_not_exists(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([1, 0, 3], statuses)
        with pytest.raises(PatientIsNotExistsError):
            hospital._convert_patient_id_to_patient_index(patient_id=4)
