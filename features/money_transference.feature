# Created by julianomontini at 12/02/21
Feature: Money Transference
  I am a user and I want to transfer money to other accounts

  Background:
    Given The source account exists
      And The target account exists

  Scenario Outline: Money transference succeeds
    Given The source account balance is <source_acc_balance>
      And The target account balance is <target_acc_balance>
    When  I transfer <amount>
    Then  The source account balance should be <source_acc_final_balance>
     And  The target account balance should be <target_acc_final_balance>
     And  The operation message is <message>

    Examples:
      | source_acc_balance | target_acc_balance | amount | source_acc_final_balance | target_acc_final_balance | message           |
      | 10                 | 15                 | 5      | 5                        | 20                       | Success           |
      | 10                 | 15                 | 15     | 10                       | 15                       | Not enough founds |
