# Created by julianomontini at 12/02/21
Feature: Calculator
  I'm a user and I want to have a calculator to sum and subtract numbers

  Scenario: Sum two numbers
    Given I have a calculator
    When  I input 3
    And   I press +
    And   I input 4
    Then  The result should be 7

  Scenario: Subtract two numbers
    Given I have a calculator
    When  I input 4
    And   I press -
    And   I input 3
    Then  The result should be 1

  Scenario Outline: Operate two numbers
    Given I have a calculator
    When  I input <n1>
    And   I press <op>
    And   I input <n2>
    Then  The result should be <res>

    Examples:
      | n1 | op | n2 | res |
      | 2  | +  | 3  | 5   |
      | 5  | -  | 3  | 2   |