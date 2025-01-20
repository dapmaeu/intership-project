# Created by marud at 1/19/2025
Feature: Tests for main page features

  Scenario: User can click on verifications settings option and verify the right page opens
    Given Open Reelly main page
    When Log in to the page
    When Click on "settings" on left side menu
    When Click on the verification option
    And  Verify the verification page opens
    Then Verify “upload image” and “Next step” buttons are available





