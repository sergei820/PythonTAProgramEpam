*** Settings ***
Library  SeleniumLibrary
Resource  ../resources/resources.robot



*** Test Cases ***
LoginTest
    Open Browser    ${url}    ${browser}
    ClickLogInButton
    ValidateLoginAndPasswordFieldsArePresented
    LoginToApplication
    CheckLogOutButtonIsVisible
    ValidateWelcomeMessageText  Welcome ${login}
    close browser

# make set up as precondition -> as a keyword -> test setup -> вынести в *** settings *** как отдельного теста
AddToCartTest
    Open Browser    ${url}    ${browser}
    ClickLogInButton
    ValidateLoginAndPasswordFieldsArePresented
    LoginToApplication
    CheckLogOutButtonIsVisible
    ClickOnCategory     Monitors
    ClickOnTheProductWithTheHighestPrice
    ValidateProductPageOpened   Apple monitor 24  $400
    ClickOnAddToCartButton
    ClickOnCartButton
#   step 4: Click on Cart button
#   expected result: product is successfully added to cart; {product_name} and {product_price} are presented
