Feature: Instructor Register
@dynamicRegister
  Scenario: Successful instructor registration with dynamic email
    Given user navigates to register page
    When user registers as instructor with valid name and password
    Then registration should be completed successfully
