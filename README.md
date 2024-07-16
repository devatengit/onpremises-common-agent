# Devaten On-Premises

## How to Install 

To run the On-Premise MySQL Agent Docker Compose File locally, you must have Git, Docker and Docker Compose installed and do the following:

1. Firstly Clone the Docker Compose file from Github using -

```ruby
git clone https://github.com/devatengit/onpremises-common-agent.git
```
**Configure docker-compose.yml:**

Once the cloning process is complete, you will see the ‘onpremises-common-agent’ folder. Open the ‘docker-compose.yml’ file in that folder using any text editor, such as Notepad or VS Code.

Here is a step-by-step guide to update the fields in your docker-compose.yml file

1. Locate the openai.apiKey Field:

&nbsp;&nbsp;openai.apiKey: Enter-your-openai-key

&nbsp;&nbsp;Replace Enter-your-openai-key with your actual OpenAI API key.

 &ensp;2. Set the openai.apiurl Field:

&nbsp;&nbsp;openai.apiurl: Enter-open-ai-api-url

&nbsp;&nbsp;Replace Enter-open-ai-api-url with the appropriate URL
3. Define the openai.responsemodel Field:

&nbsp;&nbsp;openai.responsemodel: Enter-open-ai-responsemodel

&nbsp;&nbsp;Replace Enter-open-ai-responsemodel with the model name.
&nbsp;&nbsp;Use ‘gpt-3.5-turbo’ or ‘gpt-4’ for the response model.
4. Specify the openai.server Field:

&nbsp;&nbsp;openai.server: Enter-open-ai-server
&nbsp;&nbsp;Replace Enter-open-ai-server with the appropriate server name.
&nbsp;&nbsp;For Azure, use ‘azure’.
&nbsp;&nbsp;For open-source, use ‘openai’.
 5. Adjust the openai.timeintervalinseconds Field:

&nbsp;&nbsp;openai.timeintervalinseconds: 0

&nbsp;&nbsp;Field Name: openai.timeintervalinseconds
&nbsp;&nbsp;Description: This field specifies the interval, in seconds, between consecutive OpenAI API calls. It ensures that the calls to the OpenAI API are made with &nbsp;&nbsp;a defined pause between them, avoiding potential rate limiting or excessive usage.
&nbsp;&nbsp;Current Value: 0
&nbsp;&nbsp;Implications: Setting this value to 0 means there is no delay between consecutive OpenAI API calls. This could lead to rapid successive calls, potentially &nbsp;&nbsp;hitting rate limits or causing performance issues.
6. Set the scheduler.fixed-delay Field:

 &nbsp;&nbsp;scheduler.fixed-delay: 15000

&nbsp;&nbsp;Field Name: scheduler.fixed-delay
&nbsp;&nbsp;Description: This field defines the delay, in milliseconds, between updates to the Devaten live metric page. It controls how often session data, graphs, and other metrics are refreshed &nbsp;&nbsp;on the live metric page.
&nbsp;&nbsp;Current Value: 15000
&nbsp;&nbsp;Implications: Setting this value to 15000 means the live metric page will update every 15 seconds. This frequent updating ensures that users see near-real-time data and metrics, &nbsp;&nbsp;providing a current view of sessions and graphs.
7. Configure the scheduler.cpu.collertor-type Field:

&nbsp;&nbsp;Options include OFF, AGENT, or CLIENT_TABLE.
&nbsp;&nbsp;Replace AGENT with your desired collector type.
8. Enter Details for Azure DevOps:

&nbsp;&nbsp;azure.devops.organization: your-organisation
&nbsp;&nbsp;azure.devops.project: your-project
&nbsp;&nbsp;azure.devops.tickettype: task
&nbsp;&nbsp;azure.devops.pat: your-token-for-api-calls

&nbsp;&nbsp;Replace Enter-your-organisation with your Azure DevOps organization name.
&nbsp;&nbsp;Replace Enter-your-project with your Azure DevOps project name.
&nbsp;&nbsp;Replace enter task with your desired ticket type .
&nbsp;&nbsp;Replace Enter-your-token-for-api-calls with your Azure DevOps personal access token.
9. Set Up SMTP Configuration:

&nbsp;&nbsp;smtp.host: smtp.example.com
&nbsp;&nbsp;smtp.email: your-email@example.com
&nbsp;&nbsp;smtp.password: your-password

&nbsp;&nbsp;Replace [HOST_URL] with your SMTP host URL.
&nbsp;&nbsp;Replace [EMAILID] with your SMTP email address.
&nbsp;&nbsp;Replace [PASSWORD] with your SMTP password.
Once you have updated all the fields with your actual data, your docker-compose.yml file should be ready for use.

## Note:

* This document has been written for ``` Ubuntu ```

* Windows users and the Linux users who access the terminals with ``` root ``` access they do not need to type ``` sudo ``` in front of Docker commands. ``` e.g. docker-compose pull ```

## How to Run

2. You will see the 'on-premises-mysql-agent' folder as soon as the clone is complete. Go to that folder, open terminal and run the following commands:

```ruby
sudo docker-compose pull
```

 &ensp; This will download the docker images locally.

3. To run Docker Images mentioned in Docker Compose File, Write the following command:

```ruby
sudo docker-compose up
```

 &nbsp; This command starts all the docker containers.

4. Once the docker image is running, go to your browser and hit the http://localhost:8081/ URL. Your Devaten dashboard will open. After opening the dashboard add your agent, add the application and database of your application and you are ready to use the application.

5. If you want to stop the running containers, type

```ruby
sudo docker-compose pause
```

 &nbsp; command in your terminal. It will stop your application.

6. If you want to resume the stopped containers, type 

``` ruby
sudo docker-compose unpause 
```

 &nbsp; command in your terminal. It will start your application again.

7. If you want to check the logs of any of the running containers use this command- 

```ruby 
sudo docker logs -f Container_Name 
```

8. To remove all the running containers of the on-premise dashboard docker image use this command- 

```ruby 
sudo docker-compose down 
``` 

 &nbsp; It will stop all running containers and delete all the containers.
