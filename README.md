# <a href="https://wild-flights.herokuapp.com/">Wild Flights Web App</a>*

## Project Description

<p>This app aims to help travel lovers find flights within their budget. So, if you love travelling and your only 
limitation is your budget, you can subscribe to my Wild Flights service. All you need is to specify the city where you 
travel from, max how much you want to pay, and your email address. </p>
<p>We send emails with available flights every Monday!</p>



## Project approach

<p>When user fills the form on the website and hits Submit this sends the POST request to the database to store user's data.
Every Monday, scheduler bot runs a program that loops through each entry in the database it sends request with a corresponding
origin and max flight price to the Amadus API. </p>
<p>After the data gets received it is being reformatted and sent to the subscribed users.</p>

<p>The main language used for this app is Python.</p>
<p></p>

<h3>Framework</h3>
<p>I used Flask framework for this project. I found it easy to use, it provides a good structure and enough functionality
to create a small app.</p>
<h3>Database</h3>
<p>To store users' data I used PostgreSQL database and SQLAlchemy library. </p>
<h3></h3>
<li>Flights API: <a href="https://developers.amadeus.com/">Amadeus flight inspiration</a></li>
<li>Changing iata code to city name and vice versa: Tequila API</li>
<li>Hosting: Heroku</li>
<h3>Email notifications & API calls </h3>
<p>To build a program that sends email notifications to the users I created several classes:</p>
<p>Flight Search class is responsible for sending requests to the Amadeus API and Tequila API. This class has the following
methods:</p>
<li>flight_inspiration method. Takes two arguments: flight origin (iata code) and max price. This method sends API requiest to Amadeus
and returns a dictionary with the flight information. In case when there was an error, this method prints out the error.</li>

<li>get_city_name. This method takes one argument - iata code and returns the corresponding city name. This method is needed
because Amadeus API use iata codes and not the actual city names.</li>

<li>get_iata_code. This method takes a city name as an argument and returns an iata code. As Amadeus takes iata code for API requests,
but the user enters the actual city name, we need to turn the city name to iata code.</li>

<p>Notification manager class has one method - send_email. This method takes two arguments: recipient's email and email text.
It uses Python's smtplib module to send an email.</p>

<p>Main flight engine file makes a request to the database where the users' data is stored. For each user it makes a request
to the Amadeus with user's specified origina and max price. The received data is then used to create an email. 
The notification manager class and the send email method are used to send an email to each of the subscribed users.</p>

<h3>Security of the app</h3>
<p>In order for this app to run, I needed to use some sensitive information, such as API kyes and secrets, email address and
corresponding password.</p>
<p>To make the app secure and protect sensitive information, I stored all sensitive data as environment variables which
were added separately to Heroku so the app would work when hosted.</p>

## App screenshots

<h3>App in the browser</h3>
![My Image](wild-flights.png)

## Project dependencies

1. Install latest python version - https://www.python.org/downloads/
2. To install all other required modules from the requirements file use the following command:
`pip install -r requirements.txt`

## How to use the project

<br>To run this project locally, run the following command in the terminal:</br>
`python3 app.py`
</p>