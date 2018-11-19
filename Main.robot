*** Settings ***

| Library | test.py   

*** Variable ***
${name}    p3rand0r
${url}     https://webhook.site/6b49f467-104d-46e0-ad47-
${id}      c32ece3312ba
*** Keyword ***

    

*** Test Cases ***
| Test1
| | Print name    ${name}
    
| Test2
| | Make request to     ${url}     ${id}
