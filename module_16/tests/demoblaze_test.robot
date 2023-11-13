*** Settings ***
Library  SeleniumLibrary
Resource  ../resources/resources.robot
Test Setup  Open Browser    ${url}    ${browser}
Test Setup  LoginPreconditions

*** Test Cases ***
LoginTest
    LoginPreconditions
    ValidateWelcomeMessageText  Welcome ${login}
    close browser

AddToCartTest
    ClickOnCategory     Monitors
    ClickOnTheProductWithTheHighestPrice
    ValidateProductPageOpened   Apple monitor 24  $400
    ClickOnAddToCartButton
    ClickOnCartButton
    ValidateProductIsSuccessfullyAddedToCart       Apple monitor 24  400
