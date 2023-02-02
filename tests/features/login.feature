@login
Feature: Login
  In order to maintain health records
  As a user
  I would like login to the OpenEMR portal

  @invalid    @smoke
  Scenario: Invalid Login
    Given I have browser with openemr application
    When I enter username as "john"
    And I enter password as "john123"
    And I click on login
    Then I should not access to portal with error as "Invalid username or password"

  @valid
  Scenario Outline: Valid Login1
    Given I have browser with openemr application
    When I enter username as "<username>"
    And I enter password as "<password>"
    And I click on login
    Then I should access the portal with title as "<expected_title>"
    Examples:
      | username     | password     | expected_title |
      | accountant   | accountant   | OpenEMR        |
      | receptionist | receptionist | OpenEMR        |


