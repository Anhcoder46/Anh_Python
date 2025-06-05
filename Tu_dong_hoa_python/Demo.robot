*** Settings ***
Documentation     My first test suite
Library    SeleniumLibrary
Resource          resources.robot
Test Setup        Open Browser    ${URL}    ${BROWSER}
Test Teardown     Close Browser

*** Variables ***
${URL}            https://www.google.com.vn
${BROWSER}        chrome
${USERNAME}       testuser
${PASSWORD}       testpass

*** Test Cases ***
Valid Login
    [Documentation]    Test login with valid credentials
    Input Text         id=username    ${USERNAME}
    Input Text         id=password    ${PASSWORD}
    Click Button       id=login
    Page Should Contain    Welcome

*** Keywords ***
Login Application
    [Arguments]    ${username}    ${password}
    Input Text     id=username    ${username}
    Input Text     id=password    ${password}
    Click Button   id=login