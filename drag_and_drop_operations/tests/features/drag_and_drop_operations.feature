Feature: Drag and drop operations

  Scenario: Drag and drop capital to city
      Given I have an url
      And I open the main page
      When I check that status code of the page is "200"
      Then I have to check that current page has title "Demo 2: Drag and drop"
      When I check that "Washington" is in list of capitals
      And "United States" is in list of countries
      Then I drag capital name and move it to country name
      And I verify that capital background is "rgb(0, 255, 0)"



