*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC1
    Open Browser    url=https://facebook.com/       browser=chrome
    ${title}    Get Title
    Log To Console    ${title}
    Log    ${title}
    Close Browser

TC2
    Open Browser    url=https://facebook.com/       browser=chrome
    Input Text    locator=id:email    text=demo123@gmail.com

TC3
    Open Browser    url=https://facebook.com/       browser=chrome
    Input Text    id:email    demo123@gmail.com

TC4
    Open Browser    url=https://facebook.com/       browser=chrome
    Input Text    id=email    demo123@gmail.com
    Input Password    id=pass    welcom123
    Click Element    name=login

TC5
    Open Browser     browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://facebook.com/
    Click Element    link=Create new account
    Input Text    name=firstname    Balaji
    Select From List By Label    id=day     20
    Select From List By Label    id=month   Oct
    Select From List By Label    id=year    2000
    Click Element    xpath=//input[@value='-1']
    Click Element    name=websubmit

TC7
    Open Browser    url=https://facebook.com/       browser=chrome
    Input Text    css=#email    demo123@gmail.com
    Input Password    css=#pass    welcom123
    Click Element    css=button[name='login']