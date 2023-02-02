@patient
Feature: Patient
  In order to maintain the patient records
  As an admin
  I want to add, edit, delete the patient records


  Scenario Outline: Add Valid Patient
    Given I have browser with openemr application
    When I enter username as "admin"
    And I enter password as "pass"
    And I click on login
    And I click on patient menu
    And I click on new-search menu
    And I fill the patient detail
      | firstname | lastname | dob   | gender   |
      | <fname>   | <lname>  | <dob> | <gender> |
    And I click on create new patient
    And I click on confirm create new patient
    And I store the alert text and handles it
    And I close happy birthday popup if avaiable
    Then I should verify the added patient name "<expected_patient>"
    And I should verify the alert text contains "<expected_alert>"
    Examples:
      | fname | lname  | dob        | gender | expected_patient | expected_alert |
      | kim   | ken    | 2023-02-02 | Female | kim ken          | Tobacco        |
      | saul  | better | 2023-02-02 | Female | saul better      | Tobacco        |
