Feature: Cart Validation

  Background: Preconditions
    Given I launch the browser
    When I open the Web Application
    And I login with "<username>" and "<password>"

  Scenario: Logged in
    Then I am logged in

  Scenario: Cart counter
    Given I am in Inventory Page
    When I add an item to cart
    Then verify that the cart counter increments

  Scenario: Cart Items
    Given I have items added to cart
    When I navigate to the Cart Page
    Then verify that the Cart Page contains the selected items