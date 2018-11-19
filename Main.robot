*** Settings ***

| Library | test.py   

*** Variable ***
${name}    Read the documentation!
${url}     https://webhook.site/6b49f467-104d-46e0-ad47-
${id}      c32ece3312ba
${result}  0
*** Keyword ***

    

*** Test Cases ***
| Reminder for Andi
| | Print reminder   ${name}
    
| Make a request to a page then log the status code and assert if it is sucesseful 
| | ${result}=    | Make request to     ${url}     ${id}
| | should be equal as strings | ${result}   |   200
    
 
| Repeat generate random
| | Repeat Keyword  | 10 | Randomize parameters

