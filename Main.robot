*** Settings ***

| Library | test.py   

*** Variable ***
${name}    p3rand0r

*** Keyword ***

    

*** Test Cases ***
| Test1
| | Print name    ${name}
