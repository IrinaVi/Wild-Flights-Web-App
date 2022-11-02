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

<li>Framework: Flask</li>
<li>Database: PostgreSQL, SQLalchemy</li>
<li>Flights API: <a href="https://developers.amadeus.com/">Amadeus flight inspiration</a></li>
<li>Hosting: Heroku</li>
<h3>Email notifications. </h3>
<p>To build a program that sends email notifications to the users I created several classes:</p>
<li>Flight Search class is responsible for sending requests to the Amadeus API</li>



