@cucumber-basket
Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all.

  Background:
    Given the basket has "5" cucumbers


  @add
  Scenario Outline: Add cucumbers to a basket
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers
  Examples:
    | some | total |
    |  4   |   9   |
    |  1   |   6   |
    |  3   |   8   |

@remove
  Scenario Outline: Remove cucumbers from a basket
    When "<some>" cucumbers are removed from the basket
    Then the basket contains "<total>" cucumbers
  Examples:
     | some | total |
     |  3   |   2   |
     |  1   |   4   |
     |  5   |   0   |
