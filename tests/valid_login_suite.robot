*** Settings ***

Resource    ../resource/common_functionalities.resource

Test Setup      Launch Browser And Navigate To Url
Test Teardown   Close Browser

Test Template   Valid Login Template

*** Test Cases ***
TC1     admin   pass    OpenEMR
TC2     physician   physician   OpenEMR
Valid Login Test For Accountant    accountant   accountant   OpenEMR


*** Keywords ***
Valid Login Template
    [Arguments]    ${username}      ${passsword}      ${expected_title}
    Input Text    css=#authUser    ${username}
    Input Password    id=clearPass    ${passsword}
    Click Element    id=login-button
    Title Should Be    ${expected_title}






