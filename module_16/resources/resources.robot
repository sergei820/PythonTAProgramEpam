*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.demoblaze.com/
${login}    snowfallslow@gmail.com
${password}     1qa2ws3ed
${MONITOR_ELEMENT}    xpath=//*[contains(text(),'monitor')]
${PRICES_XPATH}    xpath=//*[contains(text(),'$')]

*** Keywords ***
ClickLogInButton
    Wait Until Element Is Visible  id:login2
    click element    id:login2

ValidateLoginAndPasswordFieldsArePresented
    Wait Until Element Is Visible  id:loginusername
    element should be visible  id:loginusername
    element should be visible  id:loginpassword

LoginToApplication
    Wait Until Element Is Visible  id:loginusername
    input text  id:loginusername    ${login}
    Input Text    id:loginpassword    ${password}
    Click Element    xpath://div[@class='modal-footer']/button[text()='Log in']

checkLogOutButtonIsVisible
    Wait Until Element Is Visible  id:logout2
    element should be visible  id:logout2

validateWelcomeMessageText
    [Arguments]     ${message}
    element should contain  id:nameofuser   ${message}

ClickOnCategory
    reload page
    [Arguments]     ${category}
    Wait Until Element Is Visible  xpath://div[@class='list-group']/a[text()='${category}']
    click element  xpath://div[@class='list-group']/a[text()='${category}']

ClickOnTheProductWithTheHighestPrice
    Wait Until Page Contains Element    ${MONITOR_ELEMENT}
    ${prices}=    Get WebElements    ${PRICES_XPATH}
    ${prices_list}=    Create List
#    :FOR    ${price}    IN    @{prices}
#    \    ${price_value}=    Evaluate    int("${price.text.replace('$', '')}")
#    \    Append To List    ${prices_list}    ${price_value}
#    ${max_price}=    Set Variable    ${prices_list}[${prices_list.index(max(${prices_list}))}]
#
#    ${any_price_selector}=    Set Variable    //*[contains(text(),'$')]/preceding-sibling::*[@class='card-title']/a
#    ${max_price_selector}=    Set Variable    ${any_price_selector.replace('$', '${max_price}')}
#
#    Click Element    xpath=${max_price_selector}


