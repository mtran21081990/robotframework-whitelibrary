*** Settings ***
Library    WhiteLibrary
Suite Setup    Launch White Application For Test
Suite Teardown    Close Application
Test Teardown    Close Window
Resource    ../resource.robot
