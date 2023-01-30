*** Settings ***
Library     SeleniumLibrary
Library     FakerLibrary

*** Variables ***
${BROWSER_NAME}     chrome
@{RANDOM_WORDS}     hello   john   blue    laptop
&{MY_RECORDS}       name=bala   role=trainer    mobile=192349

*** Test Cases ***
TC1 Multiple Tabs
    ${username}     First Name
    ${password}     Password
    Open Browser     browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://www.db4free.net/
    Click Element    partial link=phpMyAdmin
    Switch Window   NEW
    Input Text    id=input_username    ${username}
    Input Password    id=input_password    ${password}
    Click Element    id=input_go
    Element Should Contain    xpath=(//div[@role='alert'])[3]    Access denied for user
    Close Browser
