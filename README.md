[![Build Status](https://travis-ci.org/KapsonLabs/Andela-iReporter.svg?branch=api)](https://travis-ci.org/KapsonLabs/Andela-iReporter) [![Coverage Status](https://coveralls.io/repos/github/KapsonLabs/Andela-iReporter/badge.svg?branch=master)](https://coveralls.io/github/KapsonLabs/Andela-iReporter?branch=master) [![Maintainability](https://api.codeclimate.com/v1/badges/5ecd878a2235b47e603a/maintainability)](https://codeclimate.com/github/KapsonLabs/Andela-iReporter/maintainability)

# iREPORTER PROJECT #

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

## ABOUT ##
A) User

- User Registration
- User login
- User can create a red-flag record.
- User can create an intervention record.
- User can delete a red-flag or intervention record.
- User can add images to either red-flag or intervention record.
- User can add videos to either red-flag or intervention record.
- User can add geolocation to either a red-flag or intervention record.

User profile has the following features
- List of all his/her red-flag/intervention records.
- The number of red-flag/intervention records that has been resolved.
- The number of red-flag/intervention records that are yet to be resolved.
- The number of red-flag/intervention records that have been rejected.

B) Admin

- An Admin can Change the status of a red-flag/intervention records.
- AnAdmin can view a list of all red-flag/intervention records created by all users.

## Technology Stack ##
- HTML
- CSS
- JS
- Python

### API Endpoints

HTTP Method|Endpoint|Functionality
-----------|--------|-------------
POST|api/v1/red-flags|Create an incident
GET|api/v1/red-flags/id|Fetch a specific incident
GET|api/v1/red-flags|Fetch all incidents
DELETE|api/v1/red-flags/id|Delete a specific red-flag/incident
