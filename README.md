# Archicad Python Interface

## Project Description

This is the official Python binding for the Archicad JSON command interface.

This package provides a convenient way to write simple scripts to support your Archicad workflow, e.g. by automating repetitive tasks.

The set of available commands will increase with each release.

## Requirements

* Archicad 24 beta 3 or later.
* Python 3.7 or later (Tcl/Tk is recommended)

## Getting started

* Install the package with pip
* *Optional: Enable the experimental Python palette in Archicad*
* Run your own scripts either from the command line or directly from ARCHICAD

### Documentations

* [Reference Manual](https://archicadapi.graphisoft.com/archicadPythonPackage)
* [Documentation of Archicad's new JSON interface](https://archicadapi.graphisoft.com/JSONInterfaceDocumentation/#Introduction)
* [Official website](https://graphisoft.com/downloads/python)

## Release notes

### 26.3000

* Archicad 26 release
* More navigator item types are handled
* New attribute related commands (folder handling) are introduced
* Property handling: return info on property default values
* Removed those attribute types which are not attributes in Archicad reality
* Classification systems are introduced
* Property groups are now available
* Selected elements' identifiers can be queried

### 25.3000

* More properties became available. For example the dynamic enum typed built-in properties (like Structural Function, Position and Renovation Status) are available from AC25. Those can be retrieved and modified.

### 25.2255

* ExecuteAddOnCommand and IsAddOnCommandAvailable commands require command namespace instead of developerId and localId.

### 25.1100

* Preparation for ARCHICAD 25 release.
* New commands were introduced.

### 25.326

* Preparation for Archicad 25 release.
* New commands were introduced.

### 24.3000

* An unexpected Runtime Error is fixed.

### 24.2310b3

* Beta release. Compatible with the official Archicad beta 3.
* Doesn't compatible with earlier (preview) versions.
