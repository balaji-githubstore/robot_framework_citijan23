Feature: Login
  In order to maintain health records
  As a user
  I would like login to the OpenEMR portal


  Scenario: Valid Login
    Given I have browser with openemr application
    When I enter username as "accountant"
    And I enter password as "accountant"
    And I click on login
    Then I should access the portal with title as "OpenEMR"



