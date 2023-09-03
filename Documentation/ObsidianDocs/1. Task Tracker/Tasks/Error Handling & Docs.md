---
SCOPE: Server
TASKTYPE: Implementation & Docs
MODULE: 
ESTTIMETOIMPLEMENT: 1.5 Hours
STATUS: In Progress - UP NEXT
PRIORITY: high
DUE: DATE
---


## Quick Description

Switching over to "raise" errors.

This switch requeires a few things

A "ErrorDefinitions.py' in each subdir, that holds the respective errors for that module
- i.e. ApiEnging.ErrorDefinitions holds error definitions for the ApiEngine.

to call an error within a .py file,
just do 'raise ERROR_CLASS_NAME'
or 'raise PATH.TO.ERROR_CLASS_NAME'

The ErrorDefinitions will take care of calling functions, along with some other info, and log it.


^^ Okay ryan turn that into docs.

## Possible Solutions/Plan


## Resources

## MindMap