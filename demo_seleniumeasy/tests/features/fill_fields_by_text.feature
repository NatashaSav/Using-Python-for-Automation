Feature:  Form demo scenarios

  Background:
       Given I have an url
      And I open "https://demo.seleniumeasy.com/basic-first-form-demo.html" page


    Scenario Outline: Fill input fields by text
      When the user type "<typed_phrase>"
      Then the user find the "Show Message" button in the single input field
      And the user click Show Message button
      Then "<appeared_phrase>" message is displayed on page
      Examples:
        | typed_phrase   | appeared_phrase |
        | Hello world    |  Hello world    |
        | Saturday       | Saturday        |
        | image          | image           |


      Scenario: Fill two input fields by text
        When the user type "10" in field named a
        And the user type "25" in field named b
        Then the user find the "Get Total" button in the two input fields
        And the user click on Get Total button
        Then "35" number is displayed on the page

