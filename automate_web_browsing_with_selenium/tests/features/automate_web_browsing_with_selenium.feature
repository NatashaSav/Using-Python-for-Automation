Feature: Automate web browsing with selenium

  Scenario: Investigation of Google Earth website
      Given I have an url
      And I open the main page
      When I check that status code of the page is "200"
      Then I have to check that current page has title "Google Earth"
      And I check that icon "https://www.gstatic.com/earth/00-favicon" is one the page
      Then I click on Menu button