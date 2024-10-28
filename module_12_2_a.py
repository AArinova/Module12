import unittest
import pprint

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
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """создаётся атрибут класса в котором хранятся результаты всех тестов."""
        self.all_results = dict()

    def setUp(self):
        """создаются 3 объекта Runner"""
        self.r1 = Runner("Усэйн", 10)
        self.r2 = Runner("Андрей", 9)
        self.r3 = Runner("Ник", 3)
        #print('setup')

    def tearDownClass(self):
        """вывод результатов"""
        for i_result in self.all_results:
            print(i_result)

    def start(self):
        return self.all_results

    def test_race1(self):
        self.setUp()
        tourney = Tournament(90, self.r1, self.r3)
        self.all_results = tourney.start()
        print(self.all_results)

        max_key = max(self.all_results, key=self.all_results.get)
        print("Highest value of key in dict:", max_key, self.all_results[max_key])
        self.assertTrue(self.all_results[max_key], "Ник")

    def test_race2(self):
        self.setUp()
        tourney = Tournament(90, self.r2, self.r3)
        self.all_results = tourney.start()
        print(self.all_results)

        max_key = max(self.all_results, key=self.all_results.get)
        print("Highest value of key in dict:", max_key, self.all_results[max_key])
        self.assertTrue(self.all_results[max_key], "Ник")

    def test_race3(self):
        self.setUp()
        tourney = Tournament(90, self.r1, self.r2, self.r3)
        self.all_results = tourney.start()
        print(self.all_results)

        max_key = max(self.all_results, key=self.all_results.get)
        print("Highest value of key in dict:", max_key, self.all_results[max_key])
        self.assertTrue(self.all_results[max_key], "Ник")

if __name__ == "__main__":
     unittest.main()
#     {1: Усэйн, 2: Ник}
#     {1: Андрей, 2: Ник}
#     {1: Андрей, 2: Усэйн, 3: Ник}