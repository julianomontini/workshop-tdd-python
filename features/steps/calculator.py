from behave import given, when, step, then

class Calculator:
    def __init__(self):
        self.numbers = []
        self.operation = None

    def input_number(self, number):
        self.numbers.append(number)

    def set_operation(self, operation):
        self.operation = operation

    def calculate(self):
        a, b = self.numbers[0], self.numbers[1]
        if self.operation == '+':
            return a + b
        if self.operation == '-':
            return a - b
        raise Exception('Operation not implemented')

@given("I have a calculator")
def step_impl(context):
    context.calculator = Calculator()


@when("I input {number}")
def step_impl(context, number):
    context.calculator.input_number(int(number))


@step("I press {operation}")
def step_impl(context, operation):
    context.calculator.set_operation(operation)


@then("The result should be {result}")
def step_impl(context, result):
    assert context.calculator.calculate() == int(result)