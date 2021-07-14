# Created by charjapadamin at 19/6/21
Feature:Test Amazon cart


 Scenario: User can add product to Amazon cart
 Given Open Amazon page
 When Search for coffee mug
 When Click on first product
 And Click add to cart button
 Then Verify cart has 1 item