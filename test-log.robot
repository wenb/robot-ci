*** Settings ***
Library           Selenium2Library
Library           OperatingSystem

*** Test Cases ***
test
    [Setup]    run    taskkill /f/ /pid chromedriver.exe
    Open Browser    http://www.baidu.com    chrome
    Wait Until Page Contains    百度    15
    Close Browser
    log  for demo
