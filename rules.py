from abc import ABC, abstractmethod
import re

from .exceptions import RuleInvalidArgumentException, RuleValidationException


class Rule(ABC):
    NAME = None

    @staticmethod
    @abstractmethod
    def validate(attrname: str, value: str, *args):
        pass

    @staticmethod
    def raiseIfAttrNameEmpty(value: str):
        if len(value.strip()) < 1:
            raise RuleInvalidArgumentException("attribute can't be empty")


class MinRule(Rule):
    NAME = 'min'

    @staticmethod
    def validate(attrname: str, value: str, *args):
        Rule.raiseIfAttrNameEmpty(attrname)

        if len(args) == 0:
            raise RuleInvalidArgumentException('min value should be given')

        try:
            length = int(args[0])
        except ValueError:
            raise RuleInvalidArgumentException('min value should be integer value')

        if length < 1:
            raise RuleInvalidArgumentException('min value at least should be one')

        if len(value) < length:
            raise RuleValidationException(f'{attrname} at least should have {length} characters')


class MaxRule(Rule):
    NAME = 'max'

    @staticmethod
    def validate(attrname: str, value: str, *args):
        Rule.raiseIfAttrNameEmpty(attrname)

        if len(args) == 0:
            raise RuleInvalidArgumentException('max value should be given')

        try:
            length = int(args[0])
        except ValueError:
            raise RuleInvalidArgumentException('max value should be integer value')

        if length < 1:
            raise RuleInvalidArgumentException('max value should at least should be one')

        if len(value) > length:
            raise RuleValidationException(f'{attrname} cannot have more than {length} characters')


class NumericRule(Rule):
    NAME = 'numeric'

    @staticmethod
    def validate(attrname: str, value: str, *args):
        Rule.raiseIfAttrNameEmpty(attrname)

        if re.search(r'^[\d]{1,}$', value) is None:
            raise RuleValidationException(f'{attrname} should contains all numeric values')


class LowerCaseRule(Rule):
    NAME = 'lowercase'

    @staticmethod
    def validate(attrname: str, value: str, *args):
        Rule.raiseIfAttrNameEmpty(attrname)


        if re.search(r'[a-z]{1,}', value) is None:
            raise RuleValidationException(f'{attrname} should contains at least one lowercase character')


class UpperCaseRule(Rule):
    NAME = 'uppercase'

    @staticmethod
    def validate(attrname: str, value: str, *args):
        Rule.raiseIfAttrNameEmpty(attrname)

        if re.search(r'[A-Z]{1,}', value) is None:
            raise RuleValidationException(f'{attrname} should contains only lowercase characters')


class SpecialCharacterRule(Rule):
    NAME = 'specialchars'

    @staticmethod
    def validate(attrname: str, value: str, *args):
        Rule.raiseIfAttrNameEmpty(attrname)

        if re.search(r'^[`!@#$%^&*_\-+<>/?\|:;]{1,}$', value) is None:
            raise RuleValidationException(f'{attrname} should only contains special characters')


class AlphaNumericRule(Rule):
    NAME = 'alphanumeric'

    @staticmethod
    def validate(attrname: str, value: str, *args):
        Rule.raiseIfAttrNameEmpty(attrname)

        if re.search(r'^[a-zA-Z0-9]+$', value) is None:
            raise RuleValidationException(f'{attrname} can only contains alphanumeric values')


class PasswordRule(Rule):
    NAME = 'password'

    @staticmethod
    def validate(attrname: str, value: str, *args):
        Rule.raiseIfAttrNameEmpty(attrname)

        if len(args) == 0:
            passwordLength: int = 8
        else:
            try:
                passwordLength = int(args[0])
                if passwordLength < 4:
                    raise ValueError('')
            except ValueError:
                raise RuleInvalidArgumentException(f'{attrname} length should be greater than or equal to 4 (default 8)')

        MinRule.validate(attrname, value, passwordLength)

        if re.search(r'(?=[`!@#$%^&*_\-+<>/?\|:;]{1,})', value) is None:
            raise RuleValidationException(f'{attrname} should contains at least one special character')

        if re.search(r'(?=[a-z]{1,})', value) is None:
            raise RuleValidationException(f'{attrname} should contains at least one lowercase character')

        if re.search(r'(?=[A-Z]{1,})', value) is None:
            raise RuleValidationException(f'{attrname} should contains at least one uppercase character')

        if re.search(r'(?=[0-9]{1,})', value) is None:
            raise RuleValidationException(f'{attrname} should contains at least one numeric character')

