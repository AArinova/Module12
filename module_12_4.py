import logging, unittest

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    """Тестирование Runner"""
    #is_frozen = False

    #@unittest.skipIf(is_frozen, reason="Тесты в этом кейсе заморожены!")
    def test_walk(self):
        """метод, в котором вызывается 10 раз метод walk и сравнивается атрибут distance этого объекта со значением 50."""
        try:
            runner = Runner('test_runner', -5 )
            for _ in range(10):
                runner.walk()
            logging.info('"test_walk" выполнен успешно.', exc_info=True)
            self.assertEqual(runner.distance, 50)
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            

    #@unittest.skipIf(is_frozen, reason="Тесты в этом кейсе заморожены!")
    def test_run(self):
        """метод, в котором 10 раз вызsвывается run() у объекта класса Runner и сравнивается атрибут distance этого объекта со значением 100."""
        try:
            runner = Runner(8.9, 12)
            for _ in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно.', exc_info=True)
            self.assertEqual(runner.distance, 100)
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner.", exc_info=True)
            

    #@unittest.skipIf(is_frozen, reason="Тесты в этом кейсе заморожены!")
    def test_challenge(self):
        """метод в котором создаются 2 объекта класса Runner 10 раз у объектов вызываются методы run и walk соответственно. Результаты работы методов сравниваются."""
        runner1 = Runner('test_runner1')
        runner2 = Runner('test_runner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.txt", encoding='UTF-8',
                        datefmt='%H:%M:%S', format="%(levelname)s | %(message)s)s | %(name)s " )
    unittest.main()
