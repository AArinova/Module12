import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, reason="Тесты в этом кейсе заморожены!")
    def test_walk(self):
        """метод, в котором вызывается 10 раз метод walk и сравнивается атрибут distance этого объекта со значением 50."""
        runner = Runner('test_runner')
        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, reason="Тесты в этом кейсе заморожены!")
    def test_run(self):
        """метод, в котором 10 раз вызsвывается run() у объекта класса Runner и сравнивается атрибут distance этого объекта со значением 100."""
        runner = Runner('test_runner')
        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, reason="Тесты в этом кейсе заморожены!")
    def test_challenge(self):
        """метод в котором создаются 2 объекта класса Runner 10 раз у объектов вызываются методы run и walk соответственно. Результаты работы методов сравниваются."""
        runner1 = Runner('test_runner1')
        runner2 = Runner('test_runner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


