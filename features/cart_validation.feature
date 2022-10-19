Feature: Cart Validation

  Background: Preconditions
    Given I launch the browser
    When I open the Web Application
    And I enter username "standard_user" and "secret_sauce"
    Then I log in

  Scenario: Cart functionality
    Given I am in Inventory Page
    When I add an item to cart
    Then verify that the cart counter increments
    And I navigate to the Cart Page
    And verify that the Cart Page contains the selected items

