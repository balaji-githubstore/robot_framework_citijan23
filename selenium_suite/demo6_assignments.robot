*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC1 Salesforce Signup
    Open Browser    browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://www.salesforce.com/in/form/signup/freetrial-sales/
#1.	Enter first name as “John”
    Input Text    name=UserFirstName    abi

#2.	Enter last name as “wick”
    Input Text    name=UserLastName    kar

#3.	Select Job title as “IT Manager”
#    Select From List By Label    name=UserTitle     IT Manager
    Select From List By Value    name=UserTitle     IT_Manager_AP
#4. click on start my trial
    Click Element    name=start my free trial