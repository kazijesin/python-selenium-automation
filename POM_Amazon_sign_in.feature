# Created by charjapadamin at 10/7/21
Feature: Logged out users sees sign in page


  Scenario: Logged out users sees sign in page when clicking Orders
  Given Open Amazon page
  When Click Amazon Orders link
  Then Verify page has Sign-In


