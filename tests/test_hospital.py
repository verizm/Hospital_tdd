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

    def test_calculate_next_status(self):
        statuses = {10: "Тяжело болен", 20: "Болен", 30: "Слегка болен", 40: "Готов к выписке"}

        hospital = Hospital([10, None, 30], statuses)

        assert hospital._calculate_next_status(patient_index=2) == 40
