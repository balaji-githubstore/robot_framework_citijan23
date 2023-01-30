*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${BROWSER_NAME}     chrome
@{RANDOM_WORDS}     hello   john   blue    laptop
&{MY_RECORDS}       name=bala   role=trainer    mobile=192349

*** Test Cases ***
TC1 Multiple Tabs
    Open Browser     browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://www.db4free.net/
    Click Element    partial link=phpMyAdmin
    Switch Window   phpMyAdmin
    Input Text    id=input_username    hello123
    Input Password    id=input_password    welcom123
    Switch Window   db4free.net - MySQL Database for free
    Close Window
    Sleep    5s
    Close Browser

TC2 Multiple Tabs
    Open Browser     browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://www.db4free.net/
    Click Element    partial link=phpMyAdmin
    Switch Window   NEW
    Input Text    id=input_username    hello123
    Input Password    id=input_password    welcom123
    Switch Window   MAIN
    Close Window
    Sleep    5s
    Close Browser



TC3 Multiple Tabs
    Open Browser     browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://www.db4free.net/
    Click Element    partial link=phpMyAdmin
    Switch Window   phpMyAdmin
    Input Text    id=input_username    hello123
    Input Password    id=input_password    welcom123
    Click Element    id=input_go
    Element Should Contain    xpath=(//div[@role='alert'])[3]    Access denied for user
    Close Browser
