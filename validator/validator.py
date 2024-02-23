from typing import Dict, List, Type

from ..exceptions import RuleValidationException, ValidationInvalidArgumentException
from ..rules import AlphaNumericRule, LowerCaseRule, MaxRule, MinRule, NumericRule, PasswordRule, Rule, SpecialCharacterRule, UpperCaseRule 


class Validator:
    rulesNotNeedLength: Dict[str, Type[Rule]] = {
            NumericRule.NAME         : NumericRule,
            LowerCaseRule.NAME       : LowerCaseRule,
            UpperCaseRule.NAME       : UpperCaseRule,
            SpecialCharacterRule.NAME: SpecialCharacterRule,
            AlphaNumericRule.NAME    : AlphaNumericRule,
     }

    rulesNeedLength: Dict[str, Type[Rule]] = {
            MinRule.NAME             : MinRule,
            MaxRule.NAME             : MaxRule,
            PasswordRule.NAME        : PasswordRule
    }


    def __init__(self, validationExpressions: Dict[str, List[str]]):
        self.validationExpressions: Dict[str, List[str]] = validationExpressions 
        self.__createErrorBag()


    def validate(self, inputs: Dict[str, str]):
        for inputName, ruleExpressions in self.validationExpressions.items():
            for ruleExpression in ruleExpressions:
                ruleParts = ruleExpression.split(':')
                ruleName = ruleParts[0]
                try:
                    rule: Type[Rule]|None = Validator.rulesNeedLength.get(ruleName, None)
                    if rule is None:
                        rule = Validator.rulesNotNeedLength.get(ruleName, None)
                        if rule is None:
                            raise ValidationInvalidArgumentException(f"Invalid rule name called '{ruleName}'")
                    else:
                        rule = Validator.rulesNeedLength.get(ruleName, None)
                        if rule is None:
                            raise ValidationInvalidArgumentException(f"Invalid rule name called '{ruleName}'")

                        if len(ruleParts) == 1:
                            raise ValidationInvalidArgumentException(f'{ruleName} rule should contains the input length after colon')

                    input = inputs.get(inputName, None) or ''
                    if len(ruleParts) > 1:
                        rule.validate(inputName, input, ruleParts[1])
                    else:
                        rule.validate(inputName, input)

                except RuleValidationException as e:
                    inputError = self.__errors.get(inputName, None)
                    if inputError is not None:
                        self.__errors[inputName].append(str(e))
                    else:
                        self.__errors[inputName] = [str(e)]


    def errors(self) -> Dict[str, List[str]]:
        return self.__errors


    def __createErrorBag(self):
        self.__errors: Dict[str, List[str]] = {} 
        for inputName, _ in self.validationExpressions.items():
            if inputName.strip(' ') == '':
                raise ValidationInvalidArgumentException('input name cannot be empty')
            self.__errors[inputName] = []

