*** Settings ***
Library     ${root}/lib/Example.py

*** Test Cases ***
My Test
    Should be equal     void        void
    Should be equal     ExampleLib.void_command()       void
# *** Keywords ***
# The result of ${calculation} should be ${expected}
#     ${result} =    Calculate    ${calculation}
#     Should Be Equal    ${result}     ${expected}