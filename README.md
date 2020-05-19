# DevOpsProject2
## Project:Complete Automation of Web-Application Deployment and Testing
![](images/0.png)
## Description:
#### 1. Create container image that’s has Jenkins installed using dockerfile.
#### 2. When we launch this image, it should automatically starts Jenkins service in the container.
#### 3. Create a job chain of job1, job2, job3 and job4 using build pipeline plugin in Jenkins.
#### 4. Job1 : Pull the Github repo automatically when some developers push repo to Github.
#### 5. Job2 : By looking at the code or program file, Jenkins should automatically start the respective language interpreter install image container to deploy code ( eg. If code is of PHP, then Jenkins should start the container that has PHP already installed ).
#### 6. Job3 : Test your app if it is working or not. If app is not working , then send email to developer with error messages.
#### 7. Job4 : If container where app is running. fails due to any reson then this job should automatically start the container again.

### Step1: Git and GitHub
  * Create a repository on GitHub, initialize with read me, and then clone it on your local Git.

### Step2: RedHat OS
  * Run Docker services in your Redhat OS.
  * Create a volume in your redhat os to link with the container afterwards
  ![](images/1.jpg)
  * Create a Dockerfile to build container image that has jenkins installed it it and all its     dependencies.
  ![](images/2.png)
  * Build this image using this command
  ![](images/3.png)
  * Launch the container, It will start Jenkins service automatically inside the container.
  ![](images/4.jpg)

### Step3:Setup Jenkins Jobs
#### Job1: For fetching repo from GitHub
This job will copy repository from github whenever developer pushes the code to Github. This job has a build trigger Poll SCM enabled in it that will check every minute if there is any update in github.
![](images/5.png)
#### Job2: For launching container
This job is interesting it will check the code/program file then automatically launch container having the respective language interpreter installed in it. This job is also chainnned with Job1. It will run only when Job1 is successfully build.
![](images/6.png)
#### Job3: For Testing
This job tests our web application. If its running then the job will build successfully otherwise it will fail and it will send email to developer that the job is failed.
![](images/7.png)
![](images/8.png)
#### Job4: For monitoring container
This Job will automatically launch the container if for some reason container is down
![](images/8.png)

### Dashboard
![](images/0.png)
