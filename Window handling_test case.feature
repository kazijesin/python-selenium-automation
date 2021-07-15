
Feature: Open and switch back to Amazon Help page

  Scenario: User can open and close Amazon Help page

  Given Open Amazon T&C 508008 page
    When Store original window
    When Click on Amazon Privacy Notice link
    When Switch to the newly opened window
    Then Verify Amazon Privacy Notice pages is opened
    When User can close new window
    When switch back to original
