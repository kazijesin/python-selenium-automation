# Created by raihanamin at 6/13/21

Feature: Test Amazon cart
  # Enter feature description here

  Scenario: User can add product to Amazon cart
  Given Open Amazon page1
  When Input table in search field
  When Click on Amazon search icon
  When Click on first product
  And Click add to cart button

   Then Verify cart has one item
