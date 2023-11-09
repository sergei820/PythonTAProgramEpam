*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.demoblaze.com/
${login}    snowfallslow@gmail.com
${password}     1qa2ws3ed

*** Test Cases ***
LoginTest
    Open Browser    ${url}    ${browser}
    ClickLogInButton
    ValidateLoginAndPasswordFieldsArePresented
    LoginToApplication
    checkLogOutButtonIsVisible
    validateWelcomeMessageText  Welcome ${login}
    close browser


*** Keywords ***
ClickLogInButton
    click element    id:login2

ValidateLoginAndPasswordFieldsArePresented
    Wait Until Element Is Visible  id:loginusername
    element should be visible  id:loginusername
    element should be visible  id:loginpassword

LoginToApplication
    input text  id:loginusername    ${login}
    Input Text    id:loginpassword    ${password}
    Click Element    xpath://div[@class='modal-footer']/button[text()='Log in']

checkLogOutButtonIsVisible
    Wait Until Element Is Visible  id:logout2
    element should be visible  id:logout2

validateWelcomeMessageText
    [Arguments]     ${message}
    element should contain  id:nameofuser   ${message}