*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${BROWSER_NAME}     chrome
${URL}      https://demo.openemr.io/b/openemr

*** Keywords ***
Launch Browser And Navigate To Url
    Open Browser    browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    Go To    url=${url}


Take Screenshot And Close Browser
    Capture Page Screenshot
    Close Browser

