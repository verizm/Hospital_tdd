from unittest.mock import MagicMock

from hospital_use_cases import HospitalUseCases
from hospital import Hospital
from hospital_exceptions import (
    PatientIdIsNotPositiveIntegerError,
    PatientIsNotExistsError,
)


class TestHospitalUseCases:

    def test_get_status(self):
        user_interaction = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}
        hospital = Hospital([0, 3, None], statuses)
        use_cases = HospitalUseCases(hospital, user_interaction)

        user_interaction.request_patient_id = MagicMock(return_value=2)
        use_cases.get_status()

        user_interaction.send_status.assert_called_with('Готов к выписке')

    def test_status_up(self):
        user_interaction = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([2, 0, 1], statuses)
        use_cases = HospitalUseCases(hospital, user_interaction)

        user_interaction.request_patient_id = MagicMock(return_value=1)
        use_cases.status_up()

        user_interaction.send_new_status.assert_called_with('Готов к выписке')
        assert hospital._hospital_db == [3, 0, 1]

    def test_status_up_when_patient_id_is_not_positive_integer(self):
        user_interaction = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([2, 0], statuses)
        use_cases = HospitalUseCases(hospital, user_interaction)
        user_interaction.request_patient_id = MagicMock(side_effect=PatientIdIsNotPositiveIntegerError())

        use_cases.status_up()

        user_interaction.send_message.assert_called_with(PatientIdIsNotPositiveIntegerError().message)

    def test_status_up_when_patient_not_exists(self):
        user_interaction = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([2, 0], statuses)
        use_cases = HospitalUseCases(hospital, user_interaction)
        user_interaction.request_patient_id = MagicMock(return_value=3)

        use_cases.status_up()

        user_interaction.send_message.assert_called_with(PatientIsNotExistsError().message)

    def test_status_up_when_status_too_high_and_patient_discharged(self):
        user_interaction = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([3, 0, 1], statuses)
        use_cases = HospitalUseCases(hospital, user_interaction)

        user_interaction.request_patient_id = MagicMock(return_value=1)
        user_interaction.request_need_to_discharge = MagicMock(return_value=True)
        use_cases.status_up()

        user_interaction.send_patient_discharged.assert_called()
        assert hospital._hospital_db == [None, 0, 1]

    def test_status_up_when_status_too_high_and_patient_not_discharged(self):
        user_interaction = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([3, 0, 1], statuses)
        use_cases = HospitalUseCases(hospital, user_interaction)

        user_interaction.request_patient_id = MagicMock(return_value=1)
        user_interaction.request_need_to_discharge = MagicMock(return_value=False)
        use_cases.status_up()

        user_interaction.send_status_not_changed.assert_called_with('Готов к выписке')
        assert hospital._hospital_db == [3, 0, 1]

    def test_calculate_statistic(self):
        user_interaction = MagicMock()
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([None, 3, 2, 0, 2, 3], statuses)
        use_cases = HospitalUseCases(hospital, user_interaction)
        statistic = {"Тяжело болен": 1, "Слегка болен": 2, "Готов к выписке": 2}

        use_cases.calculate_statistic()

        user_interaction.send_statistic.assert_called_with(5, statistic)
