## CloudFormation in AWS
- CloudFormation: *Create and Manage Resources with Templates* , is a declartive way of outlining your AWS Infrastructure, for any resources (most of them are supported)
- For example, with CloudFormation template you say:
    * I want a Security group.
    * I want two EC2 machines using this security group.
    * I want two Elastic IPs for these EC2 machines
    * I want an S3 bucket
    * I want a load balancer (ELB) in front of these machines

    **The CloudFormation creates those for you, in the right order, with the exact configuration that you specify**

- CloudFormation:
    * Create Stack.
    * Update & Delete stack
    * Yaml Crash
    * Parameters
    * Resources
    * Mapping
    * Outputs
    * Conditions
    * Intrinsic Function
    * User Date 
    * cfn-init
    * cfn-signal & wait condition
    * cfn-signal failure troubleshooting
    * Rollbacks
    * Nested Stacks
    * Change Sets
    * DeletionPolicy
    * TerminationProtection
    * Parameter from SSM:
        - *What is SSM* : Amazon EC2 Simple Systems Manager (SSM) is an Amazon Web Services tool that allows an IT professional to automatically configure virtual servers in a cloud or in on-premises data center. ... An instance must be launched with an AWS Identity and Access Management role to grant required permissions. || AWS Systems Manager (formerly known as SSM) is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources.
    * Public parameters from SSM
    * DependOn
    * Deploying lambda function
    * Custom Resources
    * Drift Detection
    * Status Codes (Deep Dive)
    * InsufficientCapabilitiesException (It's an error)
    * cfn-hup & cfn-metadata
    * Stack Policies

---

## Elastic Beanstalk - EB 
- **What is Elastic Beanstalk** : Elastic Beanstalk (EB) is a service used to deploy, manage, and scale web applications and services. You can use Elastic Beanstalk from the AWS Management console or from the command line using the Elastic Beanstalk Command Line Interface (EB CLI).
    - **Remember - Beanstack is just CloudFormation in the end or using CloudFormation at least to be managed**
    * AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, . ... You can simply upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring.


* EB CLI
* Saved Configuration
* .ebextension for configs
    - Precedence from Highest to Lowest:
        * Settings applied directly to the environment.
        * Saved configuration
        * Configuration Files (.ebextentions)
        * Default value
* .ebextension for resources
* RDS In or Out of environment
* .ebextension for commands & container commands
>--
* Rolling updates strategies:
    - Beanstack Deployment Option for updates:
        1) **All at once (Deploy all in one go)** : Fastest, but instances aren't available to serve traffic for a bit (DOWNTIME).
        2) **Rolling**: Update a few instances at a time (bucket), and then move onto the next bucket once the first bucket is healthy.
        3) **Rolling with additional batches**: Like rolling, but spins up new instances to move the batch (so that the old application is still available).
        4) **Immutable**: spins up new instances in a new ASG, deploys version to these instances, and then swaps all the instances when everything is healthy.

    **All at once**:
        - Fastest deployment.
        - Application has downtime.
        - Great for quick iteration in development environment.
        - No additional cost
    **Rolling**:
        - Application is running below capacity
        - Can set the bucket size
        - Application is running both versions simultaneously
        - No additional cost
        - Long deployment
    **Rolling with additional batches**:
        - Application is running at capacity
        - Can set the bucket size
        - Application is running both versions simultaneously
        - Small additional cost
        - Additional batch is removed at the end of the deployment
        - Longer deployment
        - Good for Production
    **Immutable**:
        - Zero DownTime
        - New Code is deployed to new instances on a temporary ASG 
        - High cost, double capacity
        - Quick rollback in case of failure (just terminate new ASG)
        - Greate for Production
>--
* Swap URL(blue/green)
* Worker environment:
    * Worker environment can do two thing:
        - It can pull from a queue and do jobs that gets submitted from a queue
        - It can do schedule tasks using cron.yaml and that is a feature that is only available to the worker environment 
* Multi docker integration

**Important to remember** *There are two environment in Beanstack*
    1) Prod env: One is for serving web.
    2) Worker env: One is for processing long running jobs.
        * The Worker environment also allows us to have current jobs defined cron.yaml File
    
    **One of the Reason of why we want to use Docker on Beanstack** : *Is to be able to standardize our deployment to any kind of language or any kind of application that we want*

---

## Lambda
-  What is Lambda : AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you. You can use AWS Lambda to extend other AWS services with custom logic, or create your own back end services that operate at AWS scale, performance, and security.

* Source and Use cases
* Security , environment Variables , KMS(Encrypt) and SSM(Store Value as plaintext)
    - SSM & KMS : Both services can leverage AWS KMS to encrypt values. ... SSM Parameter provides an option to store values in plaintext or encrypt it with a KMS key. AWS Secrets Manager only stores encrypted data (otherwise it would not be a secret if the value was stored in plaintext; it would be an unsecured parameter)

* Versions, Aliases and Canary Routing
* SAM Framework
    - SAM : The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings.
    - The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications. ... SAM CLI provides a Lambda-like execution environment that lets you locally build, test, and debug applications defined by SAM templates or through the AWS Cloud Development Kit (CDK).

* SAM and CodeDeploy : AWS SAM is an open-source framework for building serverless applications. ... Creates your CodeDeploy application and deployment group. Creates two Lambda functions that execute deployment validation tests during CodeDeploy lifecycle hooks. Detects when your Lambda function is updated.


---

## AWS Step Function Use Cases
* Step Function : Are used when you have a very complex workflow and you need to isolate some functions of your workflow and probably make it more visual and intuitive.

**Important** : *The Step Function are used to orchestrate things as workflows*

---

## API Getway 
- What is API Getway : Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. ... 
    Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications.

* Integration with lambda
* Stages and Deployment 
* Canary Deployment
* Deployment and canary testing 
* Throttles : Each account has a concurrency limit in Lambda. This limit specifies the number of function invocations that can be running at the same time. Each function can reserve a chunk of the account's concurrency limit, guaranteeing the function exactly that much concurrency.
* Fronting Step Function

---

## ECS - Elastic Container Service
- What is ECS : Amazon Elastic Container Service (ECS) is a highly scalable, high performance container management service that supports Docker containers and allows you to easily run applications on a managed cluster of Amazon EC2 instances.
- **Docker** : 
    * Docker is a software development platform to deploy apps
    * Apps are packaged in container that can be run on any OS
    * Apps run the same, regardless of where they're run:
        - Any machine.
        - No compatibility issue
        - Predictable behavior
        - Less work closely with
        - Easier to maintain and deploy
        - Works with any language, any OS, any technology
    * ?? Where Docker images are stored:
        - Docker images are stored in Docker Repository:
            * Public: Docker Hub (https://hub.docker.com/)
            * Private: Amazon ECR (Elastic Container Registry)
        **DockerFile -->(Build): Docker Image -->(run): Docker Container**
        *These images docker we have to store them , So we can push them into 1(DockerHub) OR 2(ECR) and we can Pull them also to docker image from dockerHub || ECR.
    
    * Docker Containers Management:
        - To manage container we need a container management platform:
            * 1) ECS: Amazon own platform.
            * 2) Fargate: Amazon own Serveless platform
            * 3) EKS: Amazon managed Kubernetes (open source)

- ECS Clusters Overview:
    - ECS clusters are logical grouping of EC2 instances.
    - EC2 instances run the ECS agent (Docker container)
    - The ECS agents registers the instance to the ECS cluster 
    - The EC2 instances run a special AMI, made specifically for ECS

- Task Definition:
    * ECS Task Definitions:
        - Tasks definitions are metadata in JSON form to tell ECS how to run a Docker Container
        - It contains crucial information around:
            * Image Name.
            * Port Building for container and host.
            * Memory and CPU required.
            * Environment variable.
            * Networknig information.
- ECS Service:
    - ECS Service help define how many tasks should run and how they should be run.
    - They ensure that the number of tasks desired is running across our fleet of EC2 instances.
    - They can be linked to ELB / NLB / ALB if needed.
- ECS Service with Load Balancer

- **ECR**: Is a private Docker image repository.
    * Is a private Docker image repository.
    * Access is controlled through IAM (permission errors => policy).
    * To Push & Pull, you need to run some commands:
        - $(aws ecr get-login --no-include-email --region us-west-2)
        - docker push 1234567890.dkr.ecr.us-west-2.amazonaws.com/demo:latest
        - docker pull 1234567890.dkr.ecr.us-west-2.amazonaws.com/demo:latest

- **Fargate**:
    * With Fargate, it's all Serverless !
    * We don't provision EC2 instances.
    * We just Task Definition, and AWS will run our containers for us.
    * To scale, just increase the task number. Simple! No more EC2.


---

## Elastic Beanstack (EB) + Elastic Container Service (ECS)
**You can run Elastic Beanstack in single & Multi Docker Container mode**
**Multi Docker helps run multiple container per EC2 instance in EB**
**This will create for you:**
    *ECS Cluster*
    *EC2 instances, configured to used the ECS Cluster*
    *Load Balancer(in high availability mode)*
    *Task Definition and execution*
**Requires a config file Dockerrun.aws.json at the root of source code**
**Your Docker images must be pre-built and stored in ECR for example**

- When you create your EB environment, It creates a load balancer ... It will also create an Auto Scaling Group & ECS Clustrer in it will be EC2 instances will be created and automatically registered to the ECS cluster.

- ECS IAM Roles
    * In the ECS Classic when we have two instances, you will have two Roles:
        - 1) The EC2 Role.
        - 2) The Task Role.
    * In the Fargate because there is no EC2 instances being managed then only The tasks have Role.

- ECS Auto Scaling
- ECS CloudWatch Integration
- ECS CodePipeline CI/CD

---

## OpsWorks 
- **OpsWorks**: AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. ... OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments.

* OpsWorks Stak:
    - Load Balancer
    - Application Server Instance
    - Amazon RDS Instance

* OpsWorks Lifecycle Events:
    - Chef Recipes
        * Setup : This event occurs after a started instance has finished booting.
        * Configure :
            * This event occurs on all of the stack's instances when one of the following occurs:
                - An instance enters or leaves the online state.
                - You associate an Elastic IP address with an instance or disassociate one from an instance.
                - You attach an Elastic Load Balancing load balancer to a layer, or detach one from a layer.

        * Deploy : This event occurs when you run a Deploy command
        * Undeploy : This event occurs when you delete an app or run an Undeploy command to remove an app from a set of application server instances.
        * Shutdown : This event occurs after you direct AWS OpsWorks Stacks to shut an instance down but before the associated Amazon EC2 instance is actually terminated.

* **Summary** Need to remember:
    - 1) That we create Stacks
    - 2) And each Stack a set of instances
    - 3) Then these instances can be 24/7 or Time or Load based 