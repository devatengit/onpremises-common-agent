# Devaten On-Premises MySQL Agent

## How to Install 

To run the On-Premise MySQL Agent Docker Compose File locally, you must have Git, Docker and Docker Compose installed and do the following:

1. Firstly Clone the Docker Compose file from Github using -

```ruby
git clone https://github.com/devatengit/on-premises-mysql-agent.git
``` 
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
