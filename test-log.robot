*** Settings ***
Library           Selenium2Library
Library           OperatingSystem

*** Test Cases ***
test
    [Setup]    run    taskkill /f/ /pid chromedriver.exe
    log    hello world
    Open Browser    http://www.baidu.com    chrome
    Wait Until Page Contains    百度    15
    Close Browser
