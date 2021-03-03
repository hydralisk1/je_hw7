# HW7
## 0. Repeat everything I coded during the class.
## 0. Interview QQQQ! : Interview Q&A

## 0. Read about behave context
## 0. Watch: Page Object: You are doing it wrong

## 0*. Official Page Object documentation for Python: https://selenium-python.readthedocs.io/page-objects.html


## 1. Rewrite these scenarios with Page Object pattern: ```./features/amazon.feature```

```
- Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened
    
- Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Shopping Cart is empty.' text present
```

## 2*. Rewrite “Add a product to cart” scenario using Page Object pattern. ```./features/amazon_add_to_cart.feature```

