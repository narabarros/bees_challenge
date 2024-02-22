Feature: Login
  Scenario: Successfully login
    Given User open bees web page
    When User sign in as "email" and "password"
    When User click in submit button

