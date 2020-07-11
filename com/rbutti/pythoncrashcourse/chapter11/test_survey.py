import unittest
from survey import Survey

class TestSurvey(unittest.TestCase):

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = Survey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_response(self):
        self.my_survey.responses.append(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    if __name__ == '__main__':
        unittest.main()