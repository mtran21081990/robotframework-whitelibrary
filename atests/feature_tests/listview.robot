*** Settings ***
Library     WhiteLibrary
Resource    ../resource.robot
Suite Setup    Setup for Tab 2 Tests
Suite Teardown    Select Tab Page    tabControl    Tab1

*** Test Cases ***
Row Verification
    Listview Row Should Contain    list_view2    Title    Bible    ligious
    Listview Row Should Not Contain    list_view2    Title    Robinson Crusoe    Scienc
    Listview Row In Index Should Contain    list_view2    2    Programming
    Listview Row In Index Should Not Contain    list_view2    1    Donald

Cell Verification
    Listview Cell Text Should Be    list_view2    Title    2    The Art of Computer Programming
    Listview Cell Text Should Not Be    list_view2    Title    2    Robinson Crusoe
    Listview Cell Text In Index Should Be   list_view2    2    1    The Art of Computer Programming
    Listview Cell Text In Index Should Not Be    list_view2    2    1    Robinson Crusoe

    Listview Cell Should Contain    list_view2    Title    2    omputer P
    Listview Cell Should Not Contain    list_view2    Title    2    obinson
    Listview Cell In Index Should Contain    list_view2    2    1    omputer
    Listview Cell In Index Should Not Contain    list_view2    2    1    obinson

Unsuccessful Row Verification
    Run Keyword And Expect Error    Row defined by cell 'Title'='Bible' did not contain text 'abcd'
    ...                             Listview Row Should Contain    list_view2    Title    Bible    abcd
    Run Keyword And Expect Error    Row defined by cell 'Title'='Robinson Crusoe' should not have contained text 'Fiction'
    ...                             Listview Row Should Not Contain    list_view2    Title    Robinson Crusoe    Fiction
    Run Keyword And Expect Error    Row 2 did not contain text 'abcd'
    ...                             Listview Row In Index Should Contain    list_view2    2    abcd
    Run Keyword And Expect Error    Row 1 should not have contained text 'igious'
    ...                             Listview Row In Index Should Not Contain    list_view2    1    igious

Unsuccessful Cell Verification
    Run Keyword And Expect Error    Cell text should have been 'Hello', found 'The Art of Computer Programming'
    ...                             Listview Cell Text Should Be    list_view2    Title    2    Hello

    Run Keyword And Expect Error    Cell text should not have been 'The Art of Computer Programming'
    ...                             Listview Cell Text Should Not Be    list_view2    Title    2    The Art of Computer Programming

    Run Keyword And Expect Error    Cell (2, 1) text should have been 'Hello', found 'The Art of Computer Programming'
    ...                             Listview Cell Text In Index Should Be   list_view2    2    1    Hello

    Run Keyword And Expect Error    Cell (2, 1) text should not have been 'The Art of Computer Programming'
    ...                             Listview Cell Text In Index Should Not Be    list_view2    2    1    The Art of Computer Programming

    Run Keyword And Expect Error    Cell did not contain text 'obinson'
    ...                             Listview Cell Should Contain    list_view2    Title    2    obinson

    Run Keyword And Expect Error    Cell should not have contained text 'omputer'
    ...                             Listview Cell Should Not Contain    list_view2    Title    2    omputer

    Run Keyword And Expect Error    Cell (2, 1) did not contain text 'obinson'
    ...                             Listview Cell In Index Should Contain    list_view2    2    1    obinson

    Run Keyword And Expect Error    Cell (2, 1) should not have contained text 'omputer'
    ...                             Listview Cell In Index Should Not Contain    list_view2    2    1    omputer

Get Text From ListView
    ${expected}    Create List    Donald Knuth    The Art of Computer Programming    Science
    ${actual}    Get Listview Row Text    list_view2    Category    Science
    Should Be Equal    ${actual}    ${expected}

    ${expected}    Create List    Daniel Defoe    Robinson Crusoe    Fiction
    ${actual}    Get Listview Row Text By Index    list_view2    0
    Should Be Equal    ${actual}    ${expected}

    ${actual}    Get Listview Cell Text    list_view2    Author    0
    Should Be Equal    ${actual}    Daniel Defoe

    ${actual}    Get Listview Cell Text By Index    list_view2    2    2
    Should Be Equal    ${actual}    Science

ListView Select
    Select ListView Row By Index    list_view    1
    Bible Should Be Selected
    Select ListView Row By Index    list_view    2
    The Art of Computer Programming Should Be Selected
    Select ListView Row    list_view    Title    Robinson Crusoe
    Robinson Crusoe Should Be Selected

ListView Right Click
    Repeat Keyword    2    Right Click Listview Cell    list_view2    Title    1
    Bible Should Be Right Clicked
    Repeat Keyword    2    Right Click Listview Cell    list_view2    Author    0
    Daniel Defoe Should Be Right Clicked