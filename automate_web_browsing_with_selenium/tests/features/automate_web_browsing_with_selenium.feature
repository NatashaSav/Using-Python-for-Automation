Feature: Automate web browsing with selenium

  Scenario: Investigation of Google Earth website
      Given I have an url
      And I open "https://earth.google.com/" page
      When I check that status code of the page is "200"
      Then I have to check that current page has title "Google Earth"
      When I click on Menu button
      Then I check that icon "https://www.gstatic.com/earth/00-favicon" is one the page
      And I see "Sign in" appeared on the page