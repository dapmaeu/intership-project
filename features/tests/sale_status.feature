# Created by marud at 11/5/2024
Feature: Tests for Reelly Sales Status

  Scenario: User can filter by Secondary Deals
    Given Open Reelly main page
    When Log in to the page
    When Click on “Secondary” button
    And Verify the right page opens
    When Click on Filters button
    And  Filter the products by "Want to sell"
    And Click on Apply Filter
    Then Verify all cards have "for sale" tag

  Scenario: User can filter by Secondary Deals on mobile
    Given Open Reelly main page
    When Log in to the page
    #When Close Popup banner
    When Click on “Secondary” button on the top menu
    And Verify the right page opens
    When Click on Filters button
    And  Filter the products by "Want to sell"
    And Click on Apply Filter
    Then Verify all cards have "for sale" tag

  Scenario: User can filter the off plan products by Unit price range
    Given Open Reelly main page
    When Log in to the page
    When Click on “off plan” at the left side menu
    And Verify the off plan page opens
    When Filter the products by price range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range (1200000 - 2000000)