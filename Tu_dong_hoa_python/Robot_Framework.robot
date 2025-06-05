*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.google.com
${BROWSER}    Chrome

*** Test Cases ***
Search with Google
    Open Browser    ${URL}    ${BROWSER}
    Input Text    name=q    Robot Framework
    Press Key    name=q    ENTER
    Wait Until Element Is Visible    xpath://textarea  timeout=5s
    Capture Page Screenshot
    Close Browser