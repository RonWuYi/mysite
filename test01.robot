
# *** Test Cases ***
# First Case
#     Log    Hello World!    warn
 
# Second Case
#     ${res}    Evaluate    1+2+3
#     # Should Be Equal    ${res}    6
#     Should Be Equal    ${res}    ${6}
 
# Third Case
#     ${res}    Evaluate    'i'*3
#     Length Should Be    ${res}


*** Variables ***
${var1}          value
@{list1}           a    b    c    ${var1}
&{dict1}          key1=sf   key2=${list1}
 
*** Test Cases ***
First Case
    Log to console    ${var1}    
    Log to console    @{list1}    
    # Log to console    &{dict1}  
 
Second Case
    ${res}    Evaluate    1+2+3
    Should Be Equal    ${res}    ${6}
 
Third Case
    ${res}    Evaluate    'i'*3
    Length Should Be    ${3}