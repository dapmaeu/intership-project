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

