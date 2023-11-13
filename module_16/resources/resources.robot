*** Settings ***
Library  SeleniumLibrary
Library  Collections

*** Variables ***
${browser}  chrome
${url}  https://www.demoblaze.com/
${login}    snowfallslow@gmail.com
${password}     1qa2ws3ed
${MONITOR_ELEMENT}    xpath=//*[contains(text(),'monitor')]
${PRICES_XPATH}    xpath=//*[contains(text(),'$')]
${PRODUCT_NAME}    xpath=//div[@id='tbodyid']/h2[@class='name']
${PRODUCT_PRICE}    css=#tbodyid .price-container
${ADD_TO_CART}  xpath=//div[@id='tbodyid']//a[contains(text(),'Add to cart')]
${CART_BUTTON}  xpath=//div[@class='navbar-collapse']//li/a[@id='cartur']

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
    FOR    ${price}    IN    @{prices}
        Append To List    ${prices_list}    ${price.text}
    END
    ${max_price}=    Set Variable    ${prices_list}[${prices_list.index(max(${prices_list}))}]

    ${any_price_selector}=    Set Variable    //*[contains(text(),'$')]/preceding-sibling::*[@class='card-title']/a
    ${max_price_selector}=    Set Variable    ${any_price_selector.replace('$', '${max_price}')}

    Click Element    xpath=${max_price_selector}

ValidateProductPageOpened
    reload page
    [Arguments]     ${expected_name}     ${expected_price}
    wait until element is visible  ${PRODUCT_NAME}
    element text should be  ${PRODUCT_NAME}     ${expected_name}
    element should contain   ${PRODUCT_PRICE}    ${expected_price}

ClickOnAddToCartButton
    click element  ${ADD_TO_CART}

ClickOnCartButton
    click element   ${CART_BUTTON}



