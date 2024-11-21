from application import Application
from hospital import Hospital
from hospital_use_cases import HospitalUseCases
from user_interaction import UserInteraction
from console import Console

if __name__ == '__main__':
    data_base = [1 for _ in range(200)]
    statuses_model = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    user_interaction = UserInteraction(Console())

    hospital = Hospital(data_base, statuses_model)
    commands = HospitalUseCases(hospital, user_interaction)

    Application(commands, user_interaction).run()
