import runner, tournament
import unittest

"""Создание теста"""
runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)