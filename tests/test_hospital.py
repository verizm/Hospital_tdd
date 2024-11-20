from hospital import Hospital


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

        assert hospital.can_status_up(patient_id=3) == True

    def test_can_status_up_when_status_too_high(self):
        statuses = {10: "Тяжело болен", 20: "Болен", 30: "Слегка болен", 40: "Готов к выписке"}

        hospital = Hospital([10, None, 40], statuses)

        assert hospital.can_status_up(patient_id=3) == False

    def test_calculate_next_status(self):
        statuses = {10: "Тяжело болен", 20: "Болен", 30: "Слегка болен", 40: "Готов к выписке"}

        hospital = Hospital([10, None, 30], statuses)

        assert hospital._calculate_next_status(patient_index=2) == 40

    def test_discharge(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

        hospital = Hospital([1, 0, 3], statuses)

        hospital.discharge(patient_id=1)

        assert hospital._hospital_db == [None, 0, 3]
