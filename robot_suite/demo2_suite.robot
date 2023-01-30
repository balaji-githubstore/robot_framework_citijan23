*** Settings ***
Library     OperatingSystem
Library    Collections

*** Test Cases ***
TC1
    Create Directory   path=C:${/}mine${/}hello
    
TC2 
    Remove Directory    path=C:${/}mine${/}hello
    Directory Should Not Exist    path=C:${/}mine${/}hello

TC3
   @{file_names}    List Files In Directory    path=C:${/}Mine
   Log To Console    ${file_names}
   Log To Console    ${file_names}[0]
    ${len}  Get Length    ${file_names}
    Log To Console    ${len}

TC4
    @{colors}   Create List     blue    green    red
    Log To Console    ${colors}
    Log To Console    ${colors}[2]

    ${len}  Get Length    ${colors}
    Log To Console    ${len}
    Append To List      ${colors}       black
    Log To Console    ${colors}
    Remove Values From List    ${colors}    green
    Log To Console    ${colors}
