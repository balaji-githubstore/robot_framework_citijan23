@patient
Feature: Patient
  In order to maintain the patient records
  As an admin
  I want to add, edit, delete the patient records


  Scenario: Add Valid Patient
    Given I have browser with openemr application
    When I enter username as "admin"
    And I enter password as "pass"
    And I click on login
    And I click on patient menu
    And I click on new-search menu
    And I fill the patient detail
      | firstname | lastname | dob        | gender |
      | john      | wick     | 2023-02-02 | Male   |
    And I click on create new patient
    And I click on confirm create new patient
    And I store the alert text and handles it
    And I close happy birthday popup if avaiable
    Then I should verify the added patient name
    And I should verify the alert text contains "Tobacco"