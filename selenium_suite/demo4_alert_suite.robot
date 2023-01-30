*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${BROWSER_NAME}     chrome

*** Test Cases ***
TC1 Alert
    Open Browser     browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm
    Click Element    xpath=//img[@alt='Go']
    ${alert_text}   Handle Alert    action=ACCEPT   timeout=20s
    Log To Console    ${alert_text}
    Should Be Equal  ${alert_text}  Customer ID${SPACE}${SPACE}cannot be left blank.