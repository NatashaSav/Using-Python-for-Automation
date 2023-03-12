Feature: Quoters to scrape

  Background:
    Given I have an url
    And I open the main page

  Scenario: Login to the website
    When I check that status code of the page is "200"
    Then I check that current page has title "Quotes to Scrape"
    Then I have Login button
    When I click on Login button to get to the site
    Then I enter username "Natalia91"
    And  I enter password "434708"
    Then I click on Login button and get to the site as authorised user


  Scenario: Get values for the first quote
    When I see that first quote has text "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"
    Then I expect to see "Albert Einstein" author name
    And I want to be sure that "change", "deep-thoughts", "thinking" and "world" tags are in the first quote
