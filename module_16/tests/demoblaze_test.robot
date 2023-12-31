*** Settings ***
Library  SeleniumLibrary
Resource  ../resources/resources.robot
Test Setup  Open Browser    ${url}    ${browser}
Test Teardown   Close Browser


*** Test Cases ***
LoginTest
    ClickLogInButton
    ValidateLoginAndPasswordFieldsArePresented
    LoginToApplication
    CheckLogOutButtonIsVisible
    ValidateWelcomeMessageText  Welcome ${login}

AddToCartTest
    [Setup]    LoginPreconditions
    ClickOnCategory     Monitors
    ClickOnTheProductWithTheHighestPrice
    ValidateProductPageOpened   Apple monitor 24  $400
    ClickOnAddToCartButton
    ClickOnCartButton
    ValidateProductIsSuccessfullyAddedToCart       Apple monitor 24  400


