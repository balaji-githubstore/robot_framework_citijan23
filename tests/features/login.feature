@login
Feature: Login
  In order to maintain health records
  As a user
  I would like login to the OpenEMR portal

  @valid
  Scenario: Valid Login
    Given I have browser with openemr application
    When I enter username as "accountant"
    And I enter password as "accountant"
    And I click on login
    Then I should access the portal with title as "OpenEMR"

  @invalid    @smoke
  Scenario: Invalid Login
    Given I have browser with openemr application
    When I enter username as "john"
    And I enter password as "john123"
    And I click on login
    Then I should not access to portal with error as "Invalid username or password"

