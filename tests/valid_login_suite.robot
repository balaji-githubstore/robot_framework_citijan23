*** Settings ***

Resource    ../resource/common_functionalities.resource

Test Setup      Launch Browser And Navigate To Url
Test Teardown   Close Browser


*** Test Cases ***
Valid Login Test
    Input Text    css=#authUser    admin
    Input Password    id=clearPass    pass
    Click Element    id=login-button
    Title Should Be    OpenEMR




