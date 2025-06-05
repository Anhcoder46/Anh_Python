*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser To Login Page
Suite Teardown    Close Browser

*** Variables ***
${LOGIN_URL}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}      chrome
${DELAY}        2s
${VALID_USERNAME}    Admin
${VALID_PASSWORD}    admin123
${INVALID_USERNAME}    wronguser
${INVALID_PASSWORD}    wrongpass

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Wait Until Page Contains Element    xpath=//input[@name='username']

Input Username
    [Arguments]    ${username}
    Input Text    xpath=//input[@name='username']    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    xpath=//input[@name='password']    ${password}

Submit Credentials
    Click Button    xpath=//button[@type='submit']

Welcome Page Should Be Open
    Wait Until Page Contains    Dashboard
    Page Should Contain    Dashboard

Error Message Should Be Displayed
    Wait Until Page Contains Element    xpath=//div[@class='oxd-alert-content oxd-alert-content--error']
    Page Should Contain    Invalid credentials

*** Test Cases ***
Login Successfully With Valid Credentials
    [Documentation]    Test đăng nhập thành công với thông tin hợp lệ
    Input Username    ${VALID_USERNAME}
    Input Password    ${VALID_PASSWORD}
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Click Element    xpath=//i[@class='oxd-icon bi-caret-down-fill'] 

Login Failed With Invalid Credentials
    [Documentation]    Test đăng nhập thất bại với thông tin không hợp lệ
    Input Username    ${INVALID_USERNAME}
    Input Password    ${INVALID_PASSWORD}
    Submit Credentials
    Error Message Should Be Displayed