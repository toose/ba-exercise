# Exercise 1 - Containerized Web Application

## Getting Started:

Clone the repo: 

`git clone https://github.com/toose/ba-exercise`

Change directory to cloned repo:

`cd /path/to/ba-exercise`

Build/run containers from docker-compose.yml:

`docker-compose up -d --build`

Open a web browser and navigate to http://localhost to see that you are automatically redirected to a secured endpoint located at https://localhost.

Use `curl -k https://localhost -H "User-Agent: h4ck3r" -w "\n%{http_code}\n"` to see that a 403 Forbidden response code is returned when sending requests with user-agent headers configured as `h4ck3r`.

# Exercise 2 - Log Parse

## Getting started

Change directory to cloned repo:

`cd /path/to/ba-exercise`

Run the python script, using the URI as an argument:

`./log_parse.py https://bit.ly/3hFzUzs`

# Exercise 3 - CI/CD
* Untested code is broken by design, so first and foremost we would write a unit test suite for this application. 
* This suite would test components such as response codes, known page content, templates used, database models etc. for each route of the application.
* Once there exists a working test suite, we can choose and configure a CI/CD tool to build and deploy the application, such as Jenkins, AWS CodePipeline, or GitHub Actions.
* Next, we would want to plan for a multi environment strategy, where you might have one or more of the following: staging, qa, production.
* These tools usually have multiple phases, some of which include build and deploy.
* During the build phase, test suites are run and the app is compiled (if the programming language is not interpreted) into artifacts and saved for later deployment.
* If the test suite and/or compilation fails, the deployment fails. Notificaitons are sent to the team responsible for executing the deployment.
* Pending a passing test suite and successful compilation, the application is deployed to one or more of the previously mentioned environments, e.g. staging.
* Pending the acceptance of the new features, or changes, the application is then deployed to the production environment.