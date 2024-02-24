Feature: Login
  Scenario: Successfully login
    Given User open bees web page
    When User sign in as "email" and "password"
    When User click in submit button
    When User open items page
    When User click in new item button
    When User open the new item page
    When User insert in the form
   | name     | height  | width | weight |
   | pepsi    |     56  | 40    | 90     |
    When User click in create item button