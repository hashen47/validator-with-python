import unittest


from ..exceptions import RuleInvalidArgumentException, RuleValidationException
from ..rules import AlphaNumericRule, LowerCaseRule, MaxRule, MinRule, NumericRule, PasswordRule, Rule, SpecialCharacterRule, UpperCaseRule
from ..tests import testcases


class TestRules(unittest.TestCase):
    def test_raise_if_attrname_empty_method(self):
        with self.assertRaises(RuleInvalidArgumentException):
            Rule.raiseIfAttrNameEmpty('')


    def test_min_rule(self):
        data_should_pass = testcases.lenEightOrMorePasswords
        data_should_fail = testcases.lenLessThanEightPasswords 

        for testcase in data_should_pass:
            self.assertEqual(MinRule.validate('title', testcase, 8), None)

        with self.assertRaises(RuleValidationException):
            for testcase in data_should_fail:
                self.assertEqual(MinRule.validate('title', testcase, 8), None)

        for testcase in data_should_fail:
            try:
                MinRule.validate('title', testcase, 8)
            except RuleValidationException as e:
                self.assertEqual(str(e), 'title at least should have 8 characters')
                self.assertNotEqual(str(e), 'title at least should have 7 characters')
                self.assertNotEqual(str(e), 'title at least should have 9 characters')
                self.assertNotEqual(str(e), 'titlee at least should have 8 characters')
                self.assertNotEqual(str(e), 'titl at least should have 8 characters')
                self.assertNotEqual(str(e), 'titl at least should have 0 characters')

        with self.assertRaises(RuleInvalidArgumentException):
            MinRule.validate('title', 'sdsfdfs')

        with self.assertRaises(RuleInvalidArgumentException):
            MinRule.validate('title', 'sdsfdfs', 0)


    def test_max_rule(self):
        data_should_pass = testcases.lenLessOrEqualTenPasswords
        data_should_fail = testcases.lenMoreThanTenPasswords 

        for testcase in data_should_pass:
            self.assertEqual(MaxRule.validate('title', testcase, 10), None)

        with self.assertRaises(RuleValidationException):
            for testcase in data_should_fail:
                self.assertEqual(MaxRule.validate('title', testcase, 10), None)

        for testcase in data_should_fail:
            try:
                MaxRule.validate('title', testcase, 10)
            except RuleValidationException as e:
                self.assertEqual(str(e), 'title cannot have more than 10 characters')
                self.assertNotEqual(str(e), 'title cannot have more than 0 characters')
                self.assertNotEqual(str(e), 'title cannot have more than 9 characters')
                self.assertNotEqual(str(e), 'titl cannot have more than 10 characters')
                self.assertNotEqual(str(e), 'titlle cannot have more than 10 characters')
                self.assertNotEqual(str(e), 'titl cannot have more than -7 characters')

        with self.assertRaises(RuleInvalidArgumentException):
            MaxRule.validate('title', 'sdsfdfs')

        with self.assertRaises(RuleInvalidArgumentException):
            MaxRule.validate('title', 'sdsfdfs', 0)

        with self.assertRaises(RuleInvalidArgumentException):
            MaxRule.validate('', 'sdsfdfs', 5)


    def test_numeric_rule(self):
        data_should_pass = testcases.numericValues
        data_should_fail = testcases.lenMoreThanTenPasswords 

        for testcase in data_should_pass:
            self.assertEqual(NumericRule.validate('title', testcase), None)

        with self.assertRaises(RuleValidationException):
            NumericRule.validate('title', '-234343242342')
            NumericRule.validate('title', '234343242342.090')
            for testcase in data_should_fail:
                self.assertEqual(NumericRule.validate('title', testcase), None)

        for testcase in data_should_fail:
            try:
                NumericRule.validate('title', testcase)
            except RuleValidationException as e:
                self.assertEqual(str(e), 'title should contains all numeric values')
                self.assertNotEqual(str(e), 'titlee should contains all numeric values')
                self.assertNotEqual(str(e), 'titli should contains all numeric values')
                self.assertNotEqual(str(e), 'titleee should contains all numeric values')
                self.assertNotEqual(str(e), 'titlse should contains all numeric values')
                self.assertNotEqual(str(e), 'tit should contains all numeric values')

        with self.assertRaises(RuleValidationException):
            NumericRule.validate('title', '', 5)


    def test_lowercase_rule(self):
        data_should_pass = testcases.lowercaseWords
        data_should_fail = testcases.lenMoreThanTenPasswords 

        for testcase in data_should_pass:
            self.assertEqual(LowerCaseRule.validate('title', testcase), None)

        with self.assertRaises(RuleValidationException):
            LowerCaseRule.validate('word', '-234343242342')
            LowerCaseRule.validate('word', '234343242342.090')
            for testcase in data_should_fail:
                self.assertEqual(LowerCaseRule.validate('word', testcase), None)

        for testcase in data_should_fail:
            try:
                LowerCaseRule.validate('password', testcase)
            except RuleValidationException as e:
                self.assertEqual(str(e), 'word should contains only lowercase characters')
                self.assertNotEqual(str(e), 'words should contains only lowercase characters')
                self.assertNotEqual(str(e), 'ords should contains only lowercase characters')
                self.assertNotEqual(str(e), 'wwords should contains only lowercase characters')
                self.assertNotEqual(str(e), 'w0ords should contains only lowercase characters')


    def test_uppercase_rule(self):
        data_should_pass = testcases.uppercaseWords
        data_should_fail = testcases.lenMoreThanTenPasswords 

        for testcase in data_should_pass:
            self.assertEqual(UpperCaseRule.validate('uppercase', testcase), None)

        with self.assertRaises(RuleValidationException):
            LowerCaseRule.validate('tset', 'this is the test')
            LowerCaseRule.validate('dsfs', 'UPPER CASE')
            for testcase in data_should_fail:
                self.assertEqual(LowerCaseRule.validate('word', testcase), None)

        for testcase in data_should_fail:
            try:
                LowerCaseRule.validate('password', testcase)
            except RuleValidationException as e:
                self.assertEqual(str(e), 'word should contains only lowercase characters')
                self.assertNotEqual(str(e), 'words should contains only lowercase characters')
                self.assertNotEqual(str(e), 'ords should contains only lowercase characters')
                self.assertNotEqual(str(e), 'wwords should contains only lowercase characters')
                self.assertNotEqual(str(e), 'w0ords should contains only lowercase characters')


    def test_special_character_rule(self):
        data_should_pass = testcases.specialCharacterWords
        data_should_fail = testcases.lenMoreThanTenPasswords

        for testcase in data_should_pass:
            self.assertEqual(SpecialCharacterRule.validate('special_chars', testcase), None)

        with self.assertRaises(RuleValidationException):
            for testcase in data_should_fail: 
                SpecialCharacterRule.validate('special_chars', testcase)

        for testcase in data_should_fail:
            try:
                for testcase in data_should_fail: 
                    SpecialCharacterRule.validate('special_chars', testcase)
            except RuleValidationException as e:
                self.assertEqual(str(e), 'special_chars should only contains special characters')
                self.assertNotEqual(str(e), 'special_charss should only contains specials characters')
                self.assertNotEqual(str(e), 'special_charss should only contains specials characters')
                self.assertNotEqual(str(e), 'sspecial_charss should only contains specials characters')
                self.assertNotEqual(str(e), 'special-charss should only contains specials characters')


    def test_alpha_numeric_rule(self):
        data_should_pass = testcases.alphaNumericWords
        data_should_fail = testcases.lenMoreThanTenPasswords

        for testcase in data_should_pass:
            self.assertEqual(AlphaNumericRule.validate('alphanumeric', testcase), None)

        with self.assertRaises(RuleValidationException):
            for testcase in data_should_fail:
                AlphaNumericRule.validate('alphanumeric', testcase)

        for testcase in data_should_fail:
            try:
                AlphaNumericRule.validate('alphanumeric', testcase)
            except RuleValidationException as e:
                self.assertEqual(str(e), 'alphanumeric can only contains alphanumeric values')
                self.assertNotEqual(str(e), 'alphanumerics can only contains alphanumeric values')


    def test_password_rule(self):
        data_should_pass = testcases.validPasswords
        data_should_fail = testcases.lenLessThanEightPasswords

        for testcase in data_should_pass:
            self.assertEqual(PasswordRule.validate('password', testcase), None)

        for testcase in testcases.lengthFiveWords:
            self.assertEqual(PasswordRule.validate('password', testcase, 5), None)

        with self.assertRaises(RuleValidationException):
            for testcase in data_should_fail:
                PasswordRule.validate('password', testcase)

        with self.assertRaises(RuleValidationException):
            for testcase in testcases.lengthFiveWords:
                PasswordRule.validate('password', testcase, 6)
                PasswordRule.validate('password', testcase, 7)
                PasswordRule.validate('password', testcase)

        try:
            for testcase in data_should_fail:
                PasswordRule.validate('password', testcase)
        except RuleValidationException as e:
            self.assertEqual(str(e), "password at least should have 8 characters")

        try:
            for testcase in testcases.numericValues:
                PasswordRule.validate('password', testcase)
        except RuleValidationException as e:
            self.assertEqual(str(e), "password should contains at least one special character")

        try:
            for testcase in testcases.specialCharacterWords:
                PasswordRule.validate('password', testcase)
        except RuleValidationException as e:
            self.assertEqual(str(e), "password should contains at least one lowercase character")

        try:
            for testcase in testcases.lenEightOrMorePasswords:
                PasswordRule.validate('password', testcase.lower())
        except RuleValidationException as e:
            self.assertEqual(str(e), "password should contains at least one uppercase character")

        try:
            for testcase in testcases.nonNumericPasswords:
                PasswordRule.validate('password', testcase)
        except RuleValidationException as e:
            self.assertEqual(str(e), "password should contains at least one numeric character")

        with self.assertRaises(RuleInvalidArgumentException):
            PasswordRule.validate('password', 'dfdf', 3)

        try:
            PasswordRule.validate('password', 'dfdf', 3)
        except RuleInvalidArgumentException as e:
            self.assertEqual(str(e), "password length should be greater than or equal to 4 (default 8)")
