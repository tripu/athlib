# athlib
A library of functions, data and schema for Athletics (i.e. Track and Field)

We're building lots of sites for the sport of athletics.  When we find something common and testable, we aim to place it here.   This library should contain

 - static reference data, provided it's not huge nor available elsewhere
 - Python code implementing functions of general interest
 - Javascript code implementing functions of general interest

 
It is NOT intended to contain 
 - web applications, view code or database code.
 - competition management software

Things we hope to put in here:

 - standard event codes and their English names
 - UKA and other age group calculators
 - WMA age grade calculations
 - utilities for parsing and formatting performances as commonly input in athletics
 - standardised scoring functions
 - sample JSON files in line with our schemas
 - schemas to validate 

# Installation

    pip install athlib

If working on this source, you'll need to ensure the inner package (./py/athlib) is on your path, so that you can execute "import athlib"

## Age Groups
The first Python function included has been in use in our entry system for 2 years, and has a reasonable number of tests.  It just works out age groups from a competition date and birth date.   There are three supported categories: XC, ROAD and TF.

    >>> from athlib.uka.agegroups import calc_age_group
    >>> from datetime import date
    >>> calc_age_group(date(1966,3,21), date(2015,1,3), "XC", vets=False)
    'SEN'
    >>> calc_age_group(date(2000,1,1), date(2015,1,3), "XC", vets=False)
    'U15'
    >>> 

The optional vets argument says whether those over 35 should return a WMA age grade (V45 etc), or just "SEN" for senior

## IAAF scores

These are available in Javascript.  A python equivalent is coming soon.

## Next steps - 11th June
Currently we have just the IAAF scores in Javascript.

 - Add some tested Python code (e.g. UKA age group calculations)
 - Publish on PyPI
 - Work out a testing approach for the Javascript
 - Work out the best way to package and ship, and have on a CDN, for the javascript portions