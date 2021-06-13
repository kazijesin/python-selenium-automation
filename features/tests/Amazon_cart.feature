# Created by raihanamin at 6/13/21

Feature: Test Amazon cart
  # Enter feature description here

  Scenario: User can add product to Amazon cart
  Given Open Amazon page
  When Input table on search field
  When Click on the second product
  And Click add to cart button

   Then Verify cart has the item
