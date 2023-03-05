Feature: Scraping Club

  Background:
    Given I have an url
    And I open the main page

  Scenario: Login to the website
    When I check that status code of the page is "200"
    Then I check that current page has title "Recursively Scraping pages | ScrapingClub"
    Then I check that all product names, prices and pictures are available on the pages

  Scenario: Checking buttons from the navigation bar
    When I click on Home button
    And I check that status code of the page is "200"
    Then I check that "Learn Web Scraping Using Python For Free" is appeared on current page
    And I see container with name "Donation"
    Then I need to make sure that container has "rgb(24, 188, 156)" color
    When I click on Blog button
    And I check that status code of the page is "200"
    Then I check that "/media/images/scrapy-tutorial-10-header.original.original.jpg" picture is on the page
    When I click on About button
    And I check that status code of the page is "200"
    When I click on Contact button
    And I check that status code of the page is "200"
    When I click on eBook button
    And I check that status code of the page is "200"
    When I click on Subscribe button
    And I check that status code of the page is "200"
    Then I check that current page has "ScrapingClub Newsletter" title
