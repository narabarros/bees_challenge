Feature: Deposits
Scenario: Successfully new deposit created
  Given User open bees web page
  When User sign in as "email" and "password"
  When User click in submit button
  When User open the deposit page
  When User click in new deposit button
  When User open the new deposit page
  When I insert in the form
   | name     | address         | city    | state    | zipcode |
   | Nara     | rua das acacias | campinas| sp       | 12345   |
    When User click in create deposit button