*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${BROWSER_NAME}     edge

*** Keywords ***
Launch Browser And Navigate To Url
    [Arguments]     ${url}
    Open Browser    browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    Go To    url=${url}


*** Test Cases ***
TC1 
    Launch Browser And Navigate To Url    url=https://www.online.citibank.co.in/
#    Run Keyword And Ignore Error    Click Element    xpath=//a[@title='Close123']
    Run Keyword And Ignore Error    Click Element    xpath=//a[@title='Close']
    Click Element    xpath=//span[text()='Login']
    Switch Window   Citibank India
    Click Element    xpath=//div[contains(text(),'Forgot User')]
    Click Element    link=select your product type
    Click Element    link=Credit Card
    Input Text    id=citiCard1    7877
#    Input Text    id=bill-date-long    14/04/2022
    Execute Javascript      document.querySelector('#bill-date-long').value='14/04/2000'
#    Press Keys      NONE    ARROW_DOWN

