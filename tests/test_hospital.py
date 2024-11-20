from hospital import Hospital


class TestHospital:

    def test_get_status(self):
        statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}
        hospital = Hospital([1, None, 2], statuses)
        assert hospital.get_status(patient_id=1) == "Болен"
