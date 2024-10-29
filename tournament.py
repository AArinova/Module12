import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(self):
        """создаётся атрибут класса в котором хранятся результаты всех тестов."""
        self.all_results = dict()

    def setUp(self):
        """создаются 3 объекта Runner"""
        self.r1 = Runner("Усэйн", 10)
        self.r2 = Runner("Андрей", 9)
        self.r3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        """вывод результатов"""
        for i_result in cls.all_results:
            print(i_result)

    def start(self):
        return self.all_results

    @unittest.skipIf(is_frozen == True, reason="Тесты в этом кейсе заморожены!")
    def test_race1(self):
        tourney = Tournament(90, self.r1, self.r3)
        self.all_results = tourney.start()
        max_key = max(self.all_results.keys())
        self.assertTrue(self.all_results[max_key], "Ник")

    @unittest.skipIf(is_frozen, reason="Тесты в этом кейсе заморожены!")
    def test_race2(self):
        tourney = Tournament(90, self.r2, self.r3)
        self.all_results = tourney.start()
        max_key = max(self.all_results.keys())
        self.assertTrue(self.all_results[max_key], "Ник")

    @unittest.skipIf(is_frozen, reason="Тесты в этом кейсе заморожены!")
    def test_race3(self):
        tourney = Tournament(90, self.r1, self.r2, self.r3)
        self.all_results = tourney.start()
        max_key = max(self.all_results.keys())
        self.assertTrue(self.all_results[max_key], "Ник")

