*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://the-internet.herokuapp.com/login
${USERNAME}    tomsmith
${PASSWORD}    SuperSecretPassword!

*** Test Cases ***
Đăng nhập thành công
    [Documentation]    Kiểm tra đăng nhập thành công với thông tin hợp lệ
    Open Browser ${URL} Chrome
    Go To ${URL}
    Input Text    username    ${USERNAME}
    Input Text    password    ${PASSWORD}

    TRY
        Click Element    //*[@id='login']/button/i
    EXCEPT
        Log to console    Không tìm thấy nút bấm
    END

    # $(status)    $(message)=   Run Keyword And Ignore Error   Page Should Contain        Welcome
    # IF   '${status}' == 'PASS'
    #     Log to console    Đăng nhập thành công
    # ELSE
    #     Log to console    Đăng nhập thất bại: ${message}
    # END 

    # Kiểm tra 
    Page Should Contain    Welcome
    Log To Console    Đăng nhập thành công

    #Đăng nhập thất bại
    [Documentation]    Kiểm tra đăng nhập thất bại với thông tin không hợp lệ
    Open Browser    ${URL}    chrome
    Input Text    id=username    ${WRONG_USER}
    Input Text    id=password    ${WRONG_PASS}
    Click Button    xpath=//*[@id="login"]/button
    Wait Until Page Contains    Your username is invalid!    timeout=5s
    Page Should Contain    Your username is invalid!
    Log To Console    Đăng nhập thất bại như mong đợi
    Close Browser



#     *** Settings ***
# Library    SeleniumLibrary

# *** Variables ***
# ${URL}           https://the-internet.herokuapp.com/login
# ${USERNAME}      tomsmith
# ${PASSWORD}      SuperSecretPassword!
# ${WRONG_USER}    wronguser
# ${WRONG_PASS}    wrongpassword

# *** Test Cases ***
# Đăng nhập thành công
#     [Documentation]    Kiểm tra đăng nhập thành công với thông tin hợp lệ
#     Open Browser    ${URL}    chrome
#     Input Text    id=username    ${USERNAME}
#     Input Text    id=password    ${PASSWORD}
#     Click Button    xpath=//*[@id="login"]/button
#     Wait Until Page Contains    Welcome to the Secure Area    timeout=5s
#     Page Should Contain    Welcome to the Secure Area
#     Log To Console    Đăng nhập thành công
#     Close Browser

# Đăng nhập thất bại
#     [Documentation]    Kiểm tra đăng nhập thất bại với thông tin không hợp lệ
#     Open Browser    ${URL}    chrome
#     Input Text    id=username    ${WRONG_USER}
#     Input Text    id=password    ${WRONG_PASS}
#     Click Button    xpath=//*[@id="login"]/button
#     Wait Until Page Contains    Your username is invalid!    timeout=5s
#     Page Should Contain    Your username is invalid!
#     Log To Console    Đăng nhập thất bại như mong đợi
#     Close Browser
