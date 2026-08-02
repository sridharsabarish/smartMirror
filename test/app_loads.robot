*** Settings ***
Library    SeleniumLibrary
Library    Process

Suite Setup       Start Flask App
Suite Teardown    Stop Flask App

*** Variables ***
${URL}    http://127.0.0.1:8000
${BROWSER}    Chrome

*** Keywords ***
Start Flask App
    Start Process    python3    app.py    cwd=${EXECDIR}/src
    Sleep    5s

Stop Flask App
    Terminate All Processes    kill=True

*** Test Cases ***
Verify Flask App Loads
    Open Browser    ${URL}    ${BROWSER}

    Maximize Browser Window
    Sleep    5s
    Wait Until Page Contains Element    tag:body    30s

    ${title}=    Get Title
    Log    Page title is: ${title}

    Capture Page Screenshot

    [Teardown]    Close All Browsers