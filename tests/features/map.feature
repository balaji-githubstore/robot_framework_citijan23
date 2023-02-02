@map
Feature: Map

  Scenario: Connect Cities
    Given I have browser with map application
    When I connect the cities
      | city | statecode |
      | hyd  | 78        |
      | ban  | 98        |
      | del  | 88        |
    Then I should see the map with connect cities