# Build WEB API with django and python

# An API(Application Programming Interface)is a formal way to describe two computers communicating directly with one another.

# web APIs—which allow for the transfer of data over the world wide web—are structured in a RESTful (REpresentational State Transfer) pattern.

# The combination of Django and Django REST Framework is one of the most popular and customizable ways to build web APIs

# This approach of dividing services into different components is broadly known as Service-oriented architecture.

# ADVANTAGES OF USING API
# it is much more “future-proof” because a back-end API can be consumed by any JavaScript front-end. 
# it can support multiple front-ends written in different languages and frameworks.
#  an API-first approach can be used both internally and externally.

# Django REST framework is a third party app that adds further functionality to django.
# It is mature, full of features, customizable, testable, and extremely well-documented.

# The Internet is a system of interconnected computer networks that has existed since at least the 1960s.

#  Hypertext Transfer Protocol (HTTP), was the first standard, universal way to share documents over the internet
#  It ushered in the concept of web pages: discrete documents with a URL, links, and resources such as images, audio, or video.

# A URL (Uniform Resource Locator) is the address of a resource on the internet

# The request and response pattern is the basis of all web communication
# A client (typically a web browser but also a native app or really any internet-connected device) requests information and a server responds with a response.
# Since web communication occurs via HTTP these are known more formally as HTTP requests and HTTP responses

# Within a given URL are also several discrete components. Forexample,consider https://www.google.com
#  The first part, https, refers to the scheme used. It tells the web browser how to access resources at the location
#  For a website this is typically http or https, but it could also be ftp for files, smtp for email, and so on. 
#  The next section, www.google.com, is the hostname or the actual name of the site. 
#  Every URL contains a scheme and a host.
#  Many webpages also contain an optional path
#  If you go to the homepage for Python at https://www.python.org and click on the link for the “About” page you’ll be redirected to https://www.python.org/about/. The /about/ piece is the path.

# In summary, every URL like https://python.org/about/ has three potential parts:
# a scheme - https 
# a hostname - www.python.org 
# an (optional) path - /about/

# the internet procotol suite; a whole collection of other technologies must work properly(together)to connect the client with the server and load an actual webpage.

# Several things happen when a user types https://www.google.com into their web browser and hits Enter. 
#   First the browser needs to find the desired server, somewhere, on the vast internet.
#   It uses a domain name service (DNS) to translate the domain name “google.com” into an IP address 
# IP address is a unique sequence of numbers representing every connected device on the internet
#   Domain names are used because it is easier for humans to remember a domain name like “google.com” than an IP address like “172.217.164.68”.
#   After the browser has the IP address for a given domain, it needs a way to set up a consistent connection with the desired server. 
#   This happens via the Transmission Control Protocol (TCP) which provides reliable, ordered, and error-checked delivery of bytes between two application.

# To establish a TCP connection between two computers, a three-way “handshake” occurs between the client and server:
#   The client sends a SYN asking to establish a connection 
#   The server responds with a SYN-ACK acknowledging the request and passing a connection parameter 
#   The client sends an ACK back to the server confirming the connection
# Once the TCP connection is established, the two computers can start communicating via HTTP

# Every web page contains both an address(theURL) as well as a list of approved actions known as HTTP verbs

#  These four actions Create-Read-Update-Delete are known as CRUD functionality and represent the overwhelming majority of actions taken online.

# The HTTP protocol contains a number of request methods that can be used while requesting information from a server
# i.e; POST, GET, PUT, and DELETE.
# To create content you use POST, to read content GET, to update it PUT, and to delete it you use DELETE

# A website consists of web pages with HTML, CSS, images, JavaScript, and more. 
# But a web API has endpoints instead which are URLs with a list of available actions (HTTP verbs) that expose data 
#   (typically in JSON, which is the most common data format these days and the default for Django REST Framework).

# For example, we could create the following API endpoints for a new website called mysite.
#  https://www.mysite.com/api/users # GET returns all users 
#  https://www.mysite.com/api/users/<id> # GET returns a single user
#  In the first endpoint, /api/users, an available GET request returns a list of all available users
#  This type of endpoint which returns multiple data resources is known as a collection.
#  The second endpoint /api/users/<id> represents a single user. A GET request returns information about just that one user.
#  If we added POSTtothefirstendpointwecouldcreateanewuser,whileaddingDELETE to the second endpoint would allow us to delete a single user.

#  creating an API involves making a series of endpoints: URLs with associated HTTP verbs.

# A web page consists of HTML,CSS,images,and more but an end point is just away to access data via the available HTTP verbs.

# HTTP is a request-response protocol between two computers that have an existing TCP connection.
# The computer making the requests is known as the client while the computer responding is known as the server
#  a client is a web browser but it could also be an iOS app or really any internet-connected device
#  A server is a fancy name for any computer optimized to work over the internet.

# Every HTTP message consists of a status line, headers, and optional body data
# here is a sample HTTP message that a browser might send to request the Google homepage located at https://www.google.com.
# GET / HTTP/1.1, Host: google.com, Accept_Language: en-US
# The first line is the request line and it specifies the HTTP method to use(GET), the path(/), and the specific version of HTTP to use (HTTP/1.1).
# The two subsequent lines are HTTP headers: 
#    Host is the domain name and Accept_Language is the language to use, in this case American English.
# HTTP messages also have an optional third section, known as the body. 

# However we only see a body message with HTTP responses containing data.
# let’s assume that the Google homepage only contained the HTML “Hello, World!” 
# This is what the HTTP response message from a Google server might look like.
#  HTTP/1.1 200 OK 
#  Date: Wed, 17 Feb 2020 23:26:07 GMT 
#  Server: gws 
#  Accept-Ranges: bytes 
#  Content-Length: 13 Content-Type: text/html; charset=UTF-8
#  Hello, world!
# The top line is the response line and it specifies that we are using HTTP/1.1
# The status code 200 OK indicates the request by the client was successful 
# The next eight lines are HTTP headers. And finally after a line break there is our actual body content of “Hello, world!”.

# Every HTTP message, whether a request or response, therefore has the following format:
#   Response/request line 
#   Headers
#   (optional) Body

# Most web pages contain multiple resources that require multiple HTTP request/responsecycles
# If a web page had HTML, one CSS file, and an image,three separate trips back-and-forth between the client and server would be required before the complete web page could be rendered in the browser.

# Once your web browser has executed an HTTP Request on a URL there is no guarantee things will actually work! 
# Thus there is a quite lengthy list of HTTP Status Codes available to accompany each HTTP response.
#  -2xx Success - the action requested by the client was received, understood, and accepted 
#  -3xx Redirection - the requested URL has moved 
#  -4xx Client Error - there was an error, typically a bad URL request by the client 
#  -5xx Server Error - the server failed to resolve a request
#  -200 (OK)
#  -201 (Created)
#  -301 (Moved Permanently)
#  -404 (Not Found)
#  -500 (Server Error)

#  there are only four potential outcomes to any given HTTP request: 
#    it worked (2xx), 
#    it was redirected somehow (3xx), 
#    the client made an error (4xx), 
#    the server made an error (5xx).
# These status codes are automatically placed in the request/response line at the top of every HTTP message.

#  HTTP is a stateless protocol
# stateless protocol means each request/response pair is completely independent of the previous one. 
# There is no stored memory of past interactions, which is known as state in computer science.
# State is how a website remembers that you’ve logged in and how an ecommerce site manages your shopping cart. 
# It’s fundamental to how we use modern websites, yet it’s not supported on HTTP itself.


# REpresentational State Transfer (REST)  is an approach to building APIs on top of the web, which means on top of the HTTP protocol.
# .Every RESTful API:
#  -is stateless, like HTTP 
#  -supports common HTTP verbs (GET, POST, PUT, DELETE, etc.) 
#  -returns data in either the JSON or XML format

# Any RESTful API must, at a minimum, have these three principles. 
# The standard is important because it provides a consistent way to both design and consume web APIs

# a web API is a collection of endpoints that expose certain parts of an underlying database. 

# As developers we control the URLs for each endpoint, what underlying data is available, and what actions are possible via HTTP verbs

# We cannot build a web API with only Django Rest Framework; it always must be added to a project after Django itself has been installed and configured.
# Django creates websites containing webpages
# Django REST Framework creates web APIs which are a collection of URL endpoints containing available HTTP verbs that return JSON.

# A traditional Django website consists of a single project and one (or more) apps representing discrete functionality

#  __init__.py is a Python way to treat a directory as a package; it is empty
#      Each app has a __init__.py file identifying it as a Python package 
#  settings.py contains all the configuration for our project 
#  urls.py controls the top-level URL routes
#  wsgi.py stands for web server gateway interface and helps Django serve the eventual web pages 
#  manage.py executes various Django commands such as running the local web server or creating a new app.

# We run migrate to sync the data base with Django’s default settings

# admin.py is a configuration file for the built-in Django Admin app 
# apps.py is a configuration file for the app itself
# the migrations/ directory stores migrations files for database changes
# models.py is where we define our database models 
# tests.py is for our app-specific tests
# views.py is where we handle the request/response logic for our web app

# Typically developers will also create an urls.py file within each app too for routing.

# We always add new apps at the bottom since Django will read them in order and we want the built-in core Django apps like admin and auth to already be loaded before it loads ours.

# Each web page in traditional Django requires several files: a view, url, and template. But first we need a database model 

# We include a __str__ method in the models so that the title of a book will display in the admin later on.

# Inorder to expose it as a web page we need to create views, URLs, and template files. 

# views.py file controls how the data base model content is displayed

# template file controls the lay out the actual web page.

# Django REST Framework is added just like any other third-party app

# The api app will not have its own database models 
# so there is no need to create a migration file and update the database as we normally would.

# A serializer translates data into a format that is easy to consume over the internet, typically JSON, 
# and is displayed at an API endpoint

# Since we are not bothering to build out web pages for this project, there is no need for website URLs,views,ortemplates.
#All we need is a model and Django REST Framework will take care of the rest.

#  the implicit default settings are designed so that developers can jump in and start working quickly in a local development environment.
# The default settings are not appropriate for production though.
# So typically we will make a number of changes to them over the course of a project

#  we will update three files that are Django REST Framework specific to transform our database model into a web API: urls.py, views.py, and serializers.py

# URLs the entry-point for our API end points. 

#  with Django REST Frame work we need to add a serializers.py file and we do not need a templates file

# Whenever a client interacts with an API hosted on a different domain (mysite.com vs yoursite.com) or port (localhost:3000 vs localhost:8000) there are potential security issues.
# CORS( Cross-Origin Resource Sharing) requires the server to include specific HTTP headers that allow for the client to determine if and when cross-domain requests should be allowed.

# An API exists to communicate with another program













