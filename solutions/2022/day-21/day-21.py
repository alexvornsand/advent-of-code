# advent of code 2022
# day 21

# part 1
import re

monkeys = open('input.txt', 'r').read()[:-1].split('\n')

def monkeyMath(monkeys, partTwo):
    monkeyDict = {}
    for monkey in monkeys:
        monkeyDict[monkey[:4]] = '(' + monkey[6:] + ')'

    if partTwo is False:
        root = monkeyDict['root']
        while(True):
            calls = re.findall('[a-z]{4}', root)
            if len(calls) > 0:
                call = calls[0]
                root = root.replace(call, monkeyDict[call])
            else:
                return(int(eval(root)))
    else:
        root = monkeyDict['root']
        root = root.replace('+', '==')
        monkeyDict['humn'] = '????'
        while(True):
            calls = re.findall('[a-z]{4}', root)
            if len(calls) > 0:
                call = calls[0]
                root = root.replace(call, monkeyDict[call])
            else:
                while(True):
                    expressions = re.findall('\([\d\s\*\+\/\-]*\)', root)
                    if len(expressions) > 0:
                        for expression in expressions:
                            root = root.replace(expression, str(int(eval(expression))))
                    else:
                        root = root[1:-1]
                        answer = root.split(' == ')[1]
                        expression = root.split(' == ')[0][1:-1]
                        operatorNegation = {'+': '-', '-': '+', '*': '/', '/': '*'}
                        while(expression != '????'):
                            expressionComponentsL = re.fullmatch('([\(\)\d\s\+\-\/\*\?]+)\s([\/\*\+\-])\s(\-?\d+)', expression)
                            expressionComponentsR = re.fullmatch('(\-?\d+)\s([\/\*\+\-])\s([\(\)\d\s\+\-\/\*\?]+)', expression)
                            if expressionComponentsL is not None:
                                operand1 = expressionComponentsL.groups()[0]
                                operator = expressionComponentsL.groups()[1]
                                operand2 = expressionComponentsL.groups()[2]
                                lastExpression = expression
                                lastAnswer = answer
                                expression = operand1
                                answer = '(' + answer + operatorNegation[operator] + operand2 + ')'
                            elif expressionComponentsR is not None:
                                operand1 = expressionComponentsR.groups()[0]
                                operator = expressionComponentsR.groups()[1]
                                operand2 = expressionComponentsR.groups()[2]
                                if operator == '+':
                                    lastExpression = expression
                                    lastAnswer = answer
                                    expression = operand2
                                    answer = '(' + answer + operatorNegation[operator] + operand1 + ')'
                                elif operator == '-':
                                    lastExpression = expression
                                    lastAnswer = answer
                                    expression = operand2
                                    answer = '( - (' + answer + '-' + operand1 + '))'
                                elif operator == '*':
                                    lastExpression = expression
                                    lastAnswer = answer
                                    expression = operand2
                                    answer = '(' + answer + '/' + operand1 + ')'
                                else:
                                    lastExpression = expression
                                    lastAnswer = answer
                                    expression = operand2
                                    answer = '(' + operand1 + '/' + answer + ')'
                            while(expression[0] == '(' and expression[-1] == ')'):
                                expression = expression[1:-1]
                        return(int(eval(answer)))

monkeyMath(monkeys)

# part 2
monkeyMath(monkeys, True)
