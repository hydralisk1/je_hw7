# Created by Joonil at 3/3/21
Feature: Test Scenarios for adding a product into the cart on Amazon.

  Scenario: Search for Product user want and add the one that has the largest number of reviews on the first page into the cart
    Given Open Amazon page
    When The search phrase "Apple Watch" is entered
    Then Results containing "Apple Watch" are shown
    When Click on one containing "Apple Watch", which has the largest number of reviews
    Then The product page is shown, and it has an add to cart button
    And Click on the Add to Cart button
    When Click on the Cart icon
    Then Verify "Apple Watch" is in the cart