*** Settings ***
Library     DateTime
Library    String

*** Test Cases ***
TC1
    Log To Console  message=Balaji Dinakaran
    Log To Console    hello! everyone

TC2
    Log To Console    hi

TC3
    ${my_name}     Set Variable    Balaji
    Log To Console    My name is ${my_name}
    ${u_name}   Convert To Upper Case   ${my_name}
    Log To Console    ${u_name}
    

TC4
    ${curr_date}    Get Current Date
    Log To Console    ${curr_date}

TC5
    Log To Console    C:\\mine\\nello.txt
    Log To Console    ${/}
    Log To Console    C:${/}mine${/}nello.txt
    Log To Console    ${CURDIR}
    Log To Console    ${OUTPUT_DIR}
    Log To Console    ${TEST_NAME}
    Log To Console    ${SUITE_NAME}