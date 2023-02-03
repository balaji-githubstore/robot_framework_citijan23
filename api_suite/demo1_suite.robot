*** Settings ***
Library    RequestsLibrary
Library    OperatingSystem

Suite Setup      Create Session      alias=petshop     url=https://petstore.swagger.io/v2
#Suite Teardown  DELETE On Session

*** Test Cases ***
TC1 Find Pet By Id
    ${response}     GET On Session  alias=petshop   url=pet/2005   expected_status=200
    Log     ${response}
    Status Should Be    200
    Log     ${response.json()}
    Log     ${response.json()}[id]
    Log     ${response.json()}[name]
    ${expected_id}      Convert To Integer    2005
    Should Be Equal    ${response.json()}[id]    ${expected_id}
    Should Be Equal    ${response.json()}[name]    doggie-2005

TC2 Find Invalid Pet By Id
    ${response}     GET On Session  alias=petshop   url=pet/2005    expected_status=404
    Log     ${response}
    Log     ${response.json()}
    Status Should Be    404
    Should Be Equal    ${response.json()}[message]    Pet not found

TC3 Find Pet By Status
    ${response}     GET On Session      alias=petshop
    ...  url=pet/findByStatus?status=sold
    ...  expected_status=200
    Log    ${response}
    Log    ${response.json()}
    Log    ${response.json()}[0]
    Log    ${response.json()}[0][id]

TC4 Add a pet to store
    ${json}     Get Binary File     ${EXECDIR}${/}test_data${/}new_pet.json
#    Log   ${json}
    &{headers}      Create Dictionary     Content-Type=application/json       Cache-Control=no-cache

    ${response}     POST On Session     alias=petshop   url=pet
    ...  headers=${headers}      data=${json}    expected_status=200
    
    Log    ${response.json()}
    Status Should Be    200

TC5 Delete Valid Pet
    &{headers}      Create Dictionary     api_key=abc123

    ${response}     DELETE On Session   alias=petshop   url=pet/20051
    ...  headers=${headers}

    Log    ${response.json()}
    Log    ${response.json()}[message]
    Status Should Be    200

TC6 Delete Invalid Pet
    &{headers}      Create Dictionary     api_key=abc123

    ${response}     DELETE On Session   alias=petshop   url=pet/998
    ...  headers=${headers}     expected_status=404

    Log    ${response.reason}
    Status Should Be    404
    Should Be Equal    ${response.reason}    Not found

TC5 Update a pet to store
    ${json}     Get Binary File     ${EXECDIR}${/}test_data${/}new_pet.json
#    Log   ${json}
    &{headers}      Create Dictionary     Content-Type=application/json       Cache-Control=no-cache

    ${response}     PUT On Session     alias=petshop   url=pet
    ...  headers=${headers}      data=${json}    expected_status=200

    Log    ${response.json()}
    Status Should Be    200
