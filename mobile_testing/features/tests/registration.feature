# created by Chepurin Ivan at 16/06/22

Feature: Registration process

  Scenario: The user can go through the registration process
    Given Input phone number
    When Press button proceed
    Then The SMS key window opens

