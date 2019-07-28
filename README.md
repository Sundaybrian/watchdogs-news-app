# WatchDogs News App

#### 26/07/2019

#### By **[Sunday Brian](https://github.com/Sundaybrian)**

## Description

This is a flask web application that allows users to access news from all the globe.The app fetches various news sources and sorts them based on the categories.

## Behaviour Driven Development

1.Feature Select A News Source

**Scenario:Selecting a news Source**

    Given There is/are news sources availabe
    When i click on a source
    Then i i will be redirected to that news source
    And i will see articles from that source

2.Feature Select an Article

**Scenario:Clicking an article**

    Given there are multiple articles
    When i click i on the articles's title
    Then i should be redirected to the articles news source page

3.Feature Clicking the watchdogs brand

**Scenario:Clicking the brand name**

    Given there is a brand name
    When i click the brand
    Then i should be redirected to the home page
    And i should see the various news sources

## Prerequisites

- Download and install Python3.6

## Setup/Installation

- visit
- Clone [this repository](https://github.com/Sundaybrian/python-pass-locker)
- Open a terminal window navigate to the app folder and type `./run.py` to run the application
-
- Enjoy

## Known Bugs

No known bugs
No Search feature has been implemented
The NewsAPi shuts down if request exceed 250 in a given day

## Technologies Used

- Python3.6
- Flask
- Html5
- Bootstrap
- Css

### License

MIT (c) 2019 **[Sunday Brian](https://github.com/Sundaybrian)**
