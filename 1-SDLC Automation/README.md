# 🙂😊😀😁😍😀🙌🐠🐟🐡🦈🐬🐳🐋🙈🙉🙊!
# New Part - CodeCommit | CICD

- CI/CD
- CodeCommit
- Repository | HTTPS | clone | add | commit | push | Branches | PullRequest | SecuringTheRepository&Branches | Trigger&Notification | AWSLambda

* **CodeCommit** : Store Code in private Git repository.
* **Repository** : A repository is your whole project (directories and files) that you clone on your computer-(Where I saved the my source code.) 
* **Branches** : A branch is a version of your repository, or in other words, an independent line of development. A repository can contain multiple branches, which means there are multiple versions of the repository
* **Pull request & Push** : A "pull request" is you requesting the target repository to please grab your changes. A "push request" would be the target repository requesting you to push your chang

----------

# New Part - CodeBuild

- CodeBuild = Our code in CodeCommit we need to deploy it onto a Web Server 
    In CodeCommit we want to fetch and test our Branch Master index.html , and to test if i.g: The word "Congratulation" is exits onto html.index File.
    *Service Role* : Is what will allow CodeBuild to do what it needs to do

    * **Buildspec.yml File** | Docker, ECR | Environment variables & Parameter store
    * **Inside of Buildspec.yml** : we can run some varaiables i.g= (printenv) This will print all the environment variables.

    **Important** *Using parameter store is the secure way to provide environment variables into your CodeBuild Project*

    * Code Build **Artificts & S3** :
        - What is Artifacts = If you use CodeBuild  for running tests , We don't really build anything (We just running test) ... CodeBuild can be used to build stuff, And when we build stuff we generate new falls out of it. *i.g* If you have a Java project you would generate Java files ... So this built output is an artificat and that artifiact **Needs to be uploded somewhere i.g: In S3, to be consumed by other programs and deployed wherever you want**

        artifacts:
            files:
                - '**/*'  #Here we saying any files that is in our repository will become artificats
            name: my-webapp-artifacts  #What is the name of the artifacts

    * Code Build - **CloudWatch Events, CloudWatch Logs, CloudWatch Metrics & Trigger.**
        - What if you wanted to test our project every hour? **We could allow CloudWatch *Events***
            We choosed **Schedule** option , and choose every one hour you are going to emit a new event 
            AND Choose the target i.g = CodeBuild project and the Project ARN

            Also I can create an event that report to me if something failed or success or or or or .... And sent a notification 

    * CodeBuild - Validating CodeCommit Pull Request  

----------

# New Part - CodeDeploy

- *AWS CodeDeploy* : We want to deploy our application automatiaclly to many instances so that they go from V1 to V2 ... There are several ways to handle the deployments using a person's such (Ansible | Terraform | Chef | Puppets) ... We can use the managed service AWS CodeDeploy 

    ### How It works : 
    * Each EC2 Machine (or On Premise machine) must be running CodeDeploy Agent.
    * The agent is continuously polling AWS CodeDeploy for work to do 
    * CodeDeploy sends appspec.yml file to the instances.
    * Application is pulled from Github | S3.
    * EC2 will run the deployment instructions
    * CodeDeploy Agent will report of success / failure of deployment on the instance

    ## Important things : 
    > Source code.

    > appspec.yml File.
    
    ## More info:
    * EC2 instances are grouped by deployment group (dev/test/prod)
    * Lots of flexibility to define any kind of deployment
    * CodeDeploy can be chained into CodePipline and use artifacts from there
    * CodeDeploy can re-use existing setup tools, works with any application, auto scaling integration
    * Note: Blue/Green only works with EC2 instances (not on premise)
    * Support for AWS Lambda deployment , EC2 
    * CodeDeploy does not provision resources

---
    > EC2 Setup

    > Application

    > Deployment Group : A deployment group is the AWS CodeDeploy entity for grouping EC2 instances or AWS Lambda functions in a CodeDeploy deployment. For EC2 deployments, it is a set of instances associated with an application that you target for a deployment. | A deployment group is a logical set of deployment target machines that have agents installed on each one. Deployment groups represent the physical environments; for example, "Dev", "Test", or "Production" environment. In effect, a deployment group is just another grouping of agents, much like an agent pool.

        * CodeDeployDefault.AllAtOnce
        * CodeDeployDefault.HalfAtATime
        * CodeDeployDefault.OneAtATime		

    > Deployment Group Discussion

    > Deployment Configuration

    > appspec.yml (DeepDive)
        * Hooks & Environment Variables
            - ApplicationStop
            - DownloadBundle
            - BeforeInstall
            - Install
            - AfterInstall
            - ApplicationStart
            - ValidateService

    > CloudWatch Events, CloudWatch Logs, CloudWatch Alarm, Trigger

    > Roolback

    > On-premise instance setup  = An on-premises instance is any physical device that is not an Amazon EC2 instance that can run the CodeDeploy agent and connect to public AWS service endpoints.

    > Deploy to AWS 
        * Canary - one then all 
        * Linear - step by step


---

----------

# New Part - CodePipline

- CodePipline is to orchestrate our entire CICD pipline

    - CloudFormation can create automatically a CodePipeline and choose the source repository in different branch.

* How to CodeCommit & CodeDeploy together
* Adding CodeBuild
* Artifiacts, Encryption and S3
* Manual Approval Steps
* CloudWatch Event Integration
* Stage Action , sequential & Paralle
* All Integration
* Custom Action Jobs with AWS Lambda

----------

# New Part - CodeStar

* **CodeStar** : is integrated environment you can Quickly develop, build, and deploy applications on AWS. (CodeCommit & CodeBuild & CodeDeploy & CodePipeline) all together.
    - CodeStar template.yml File


----------

# New Part - Jenkins on AWS 

* Jenkins with Code Pipeline: Jenkins replaces CodeBuild and is invoked by CodePipeline
* Jenkins Setup EC2
