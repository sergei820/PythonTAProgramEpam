*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
LoginTest
    Open Browser    https://www.demoblaze.com/    chrome
    click element    id:login2
    Wait Until Element Is Visible  id:loginusername
    input text  id:loginusername    snowfallslow@gmail.com
    Input Text    id:loginpassword    1qa2ws3ed
    Click Element    xpath://div[@class='modal-footer']/button[text()='Log in']
