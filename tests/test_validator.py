from unittest import TestCase

from ..exceptions import RuleInvalidArgumentException
from ..validator import Validator
from ..tests import testcases


class TestValidator(TestCase):
    def test_validator(self):
        for testcase in testcases.lengthFiveWords:
            validator = Validator({ "title": ["min:4", "password:5"]})
            self.assertEqual(validator.validate({ "title": testcase }), None)

        for testcase in testcases.lengthFiveWords:
            validator = Validator({'title': ['min:6', 'max:8', 'password:5']})
            validator.validate({ "title": testcase })

        with self.assertRaises(RuleInvalidArgumentException):
            for testcase in testcases.lengthFiveWords:
                validator = Validator({'title': ['min:-1']})
                validator.validate({ "title": testcase })
                validator = Validator({'title': ['max:-1']})
                validator.validate({ "title": testcase })

        for testcase in testcases.lengthFiveWords:
            validator = Validator({'title': ['min:5', 'max:8', 'password:6']})
            validator.validate({ "title": testcase })
            self.assertEqual(validator.errors(), {'title': ["title at least should have 6 characters"]})

        for testcase in testcases.numericValues:
            validator = Validator({'title': ['numeric']})
            validator.validate({ "title": testcase })
            self.assertEqual(validator.errors(), {'title': []})

        for testcase in testcases.lengthFiveWords:
            validator = Validator({'title': ['numeric']})
            validator.validate({ "title": testcase })
            self.assertEqual(validator.errors(), {'title': ["title should contains all numeric values"]})

        for testcase in testcases.lengthFiveWords:
            validator = Validator({
                'title': ['min:6', 'max:8', 'password:8'],
                'name': ['min:4', 'max:5', 'password:5'],
                'age': ['numeric']
            })
            validator.validate({ "title": testcase, "name": testcase + "df", "age": "23" })
            self.assertEqual(validator.errors(), {
                'title': ["title at least should have 6 characters", "title at least should have 8 characters"],
                'name': ["name cannot have more than 5 characters"],
                'age': [],
            })
