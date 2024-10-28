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
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):

    def setUpClass(self):
        """создаётся атрибут класса в котором хранятся результаты всех тестов."""
        self.all_results = dict()

    def setUp(self):
        """создаются 3 объекта Runner"""
        r1 = Runner("Усэйн", 10)
        r2 = Runner("Андрей", 9)
        r3 = Runner("Ник", 3)
        print('setup')

    def tearDownClass(self):
        """вывод результатов"""
        for i_result in self.all_results:
            print(i_result)

    def start(self):
        return self.all_results

    def test_race(self, *args):
        self.setUp()
        tourney = Tournament(90, *args)
        for runner in args:
            self.all_results = tourney.start()
            #self.all_results[runner.name] = tourney.full_distance / runner.speed
            print(runner.name, self.all_results)

        max_key = max(self.all_results, key=self.all_results.get)
        print("Highest value of key in dict:", max_key, self.all_results[max_key])
        self.assertTrue(self.all_results[max_key], self.all_results[len(self.all_results)])


if __name__ == "__main__":
     unittest.main()
#     {1: Усэйн, 2: Ник}
#     {1: Андрей, 2: Ник}
#     {1: Андрей, 2: Усэйн, 3: Ник}