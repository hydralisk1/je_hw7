# Created by Joonil at 3/3/21
Feature: Test Scenarios for opening Sign in page and verifying Shopping Cart is empty

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify 'Sign-In' page is opened

  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Amazon Cart is empty' text present