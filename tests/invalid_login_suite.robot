*** Settings ***

Resource    ../resource/common_functionalities.resource

Library     DataDriver      file=../test_data/openemr_data.xlsx     sheet_name=InvalidLoginTest

Test Setup      Launch Browser And Navigate To Url
Test Teardown   Close Browser

Test Template       Invalid Login Template

*** Test Cases ***
TC1

*** Keywords ***
Invalid Login Template
    [Arguments]     ${username}     ${password}     ${expected_error}
    Input Text    css=#authUser    ${username}
    Input Password    id=clearPass    ${password}
    Click Element    id=login-button
    Element Text Should Be    //div[contains(text(),'Invalid')]    ${expected_error}