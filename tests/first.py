import unittest

from functions import get_formatted_name


class AnonymousSurvey:
    def __init__(self, question):
        pass


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)

        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
