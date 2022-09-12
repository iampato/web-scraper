# Web poll bot
a bot to fill a poll using python

! CAUTION this repository is only for educational purposes only


### Pseudo - code

- Get the poll url
- Using chrom dev tools get the `input` of type radio id for the person you want to flood with responses
- click it with `selenium` browser
- find the `vote` button id and click it with selenium driver
- Create a loop to do this multiple times

## Technologies used
* [Python3](https://www.python.org/downloads/) Intially I had begun with `golang` but the webcrawler packages did not provide a chrome instance that I need the DOM to tap on html elements
* [Selenium WebDriver](https://www.selenium.dev/) Browser based testing of sites
* [Webdriver manager](https://pypi.org/project/webdriver-manager/) - Simplifies developers work of managing of chrom binary drivers for different browsers and OS. initially I was manually downloading and setting up the executable bianry before I found this

