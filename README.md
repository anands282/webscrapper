# Creating a Web Scraper
Web scrapers are tools or programs used to extract data from websites. They can be written in various programming languages like Python, Java, or JavaScript, and typically involve making HTTP requests to a website, parsing the HTML or other content, and then extracting the desired information.

# Why Scrape Google Maps
Google Maps offers a wealth of business profile data, including addresses, ratings, phone numbers, and website addresses. Scraping Google Maps can yield a comprehensive data directory for business intelligence and market analysis. Additionally, it can be used for lead generation by providing access to business contact details.

Also as a proof of concept this project can have immediate practical uses, the other day I wanted to get my bike serviced and wasnt sure which service centre would be most suited. With this project we can enter a shop or an establishment category and location to get a list of businesses in and around the location selected. We can also fetch the details such as average ratings and contact information from this.
There are a couple of ways this can be implemented.

## Tools we need
* Python installation 3.7 or greater
* Any IDE of your choice(I have used PyCharm Community edition)
* A cup of Tea or Coffee
## Python packages used
* argparse: The argparse module provides a way to handle command-line arguments, making it easier to write scripts that can accept user input directly from the command line. This can be incredibly useful for creating tools, utilities, and applications that require user configuration or input.
* playwright:Playwright is a powerful tool for automating web browsers. Developed by Microsoft, it is designed to be reliable, fast, and capable of handling modern web applications. Playwright supports multiple programming languages, including JavaScript, Python, C#, and Java, and can interact with all major browser engines: Chromium, Firefox, and WebKit. This makes it an excellent choice for cross-browser testing and automation.I have used Chromium browser for this project.
* dataclasses: This module provides a decorator and functions for automatically adding special methods to user-defined classes. These special methods include __init__(), __repr__(), __eq__(), and more. The primary purpose of dataclasses is to simplify the creation of classes that are primarily used to store data.
* pandas: Pandas is a powerful and widely-used open-source library in Python for data manipulation and analysis. It provides data structures and functions needed to work on structured data seamlessly. Built on top of NumPy, Pandas is particularly well-suited for handling tabular data, such as data stored in spreadsheets or databases.