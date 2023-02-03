*** Settings ***
Library    RequestsLibrary
Library    OperatingSystem

Suite Setup      Create Session      alias=petshop     url=https://petstore.swagger.io/v2
#Suite Teardown  DELETE On Session

Test Template       Delete Valid Pet Template

*** Test Cases ***
TC1   101
TC2   102

*** Keywords ***
Delete Valid Pet Template
    [Arguments]     ${pet_id}
    &{headers}      Create Dictionary     api_key=abc123

    ${response}     DELETE On Session   alias=petshop   url=pet/${pet_id}
    ...  headers=${headers}
    Log    ${response.json()}
    Log    ${response.json()}[message]
    Status Should Be    200

