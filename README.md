# Mobile App Automation
Repository for exploration and implementations on how to test mobile applications using automation

## Node
Required for Appium
https://nodejs.org/en/download/

`npm i -g appium@next`

## Appium
https://appium.github.io/appium/docs/en/2.0/quickstart

Appium runs the services which the test framework uses to execute commands against the simulated devices
We make use of a python module Appium-Python-Client to define and execute UI tests against the simulated devices.

https://pypi.org/project/Appium-Python-Client/

`python -m pip install appium-python-client`

Specific applications are specified in the "capabilities" of the test suite along with the device, platform, language etc.

The selenium framework is used for navigation and searching of elements

The pytest module is used to handle the testing capabilities for the automation files.

### Appium Drivers
 - https://appium.io/docs/en/drivers/android-uiautomator2/index.html
 - https://appium.io/docs/en/drivers/ios-xcuitest/index.html

## Android Studio
This is used to host the application code and create and manage the simulated devices for Android. This can be done in different ways and devices can be run in headless mode on platforms like CircleCI etc.

## XCode
This is the IOS equivalent of Android Studio which enable device simulation. Similarly this has been containerized on platforms like CircleCI for use in CI/CD pipelines.
