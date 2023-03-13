# DJANGO SETTINGS

This is just a short intro I have made to familiarise myself with the django settings file but if you want to find more about django settings file click below it will take you to the official documentation 🙂

click here - [DJANGO SETTINGS](https://docs.djangoproject.com/en/4.1/topics/settings/)

A django settings file contains all the configurations of your django installation.
It is just a python module with module-level variables
The following below are a couple of example settings

ALLOWED\_HOST = ['www.example.com']
Debug = False
DEFAULT\_FROM\_EMAIL = 'example@gmail.com'

And because this file is just a normal python module, the following also apply to it
1) It does not allow Python syntax errors

2) It can assign settings dynamically using normal Python syntax3) It can import values from other settings files just like other modules

## DESIGNNATING THE SETTINGS
### DJANGO\_SETTINGS\_MODULE
When you use django you have to tell it which you are using exactly Do this by using an environment variable, DJANGO\_SETTING\_MODULE

The vlaue of DJANGO\_SETTINGS\_MODULE should be in python path syntax eg mysite.settings
