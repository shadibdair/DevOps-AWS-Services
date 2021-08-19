## Auto Scaling group (ASG)
- **What is Launch Configuration**
    * A launch configuration is a template that an EC2 Auto Scaling group uses to launch EC2 instances. When you create a launch configuration, you specify information for the instances such as the ID of the Amazon Machine Image (AMI), the instance type, a key pair, one or more security groups, and a block device mapping.

?? If you want to specify a mix of OnDeamand and spot instances for your ASG ?
    * Then you need to use a launch template and you need to use the option *Combine purchase option and instances*

- **Launch templates** : *Give us the ability to specify a mix of instances, a mix of OnDemand or spots for purchase options*

- **What is on Demand and spot instances?** *A Spot Instance is an instance that uses spare EC2 capacity that is available for less than the On-Demand price. Because Spot Instances enable you to request unused EC2 instances at steep discounts, you can lower your Amazon EC2 costs significantly. The hourly price for a Spot Instance is called a Spot price.*

- **Scheduled Actions** : *Able to schedule in advance how your orders can group should behave based on patterns you can predict in advance*

- **Suspending processes** : *If you suspend either the Launch or Terminate process types, it can prevent other process types from functioning properly. For more information, see Suspending and resuming scaling processes in the Amazon EC2 Auto Scaling User Guide. To resume processes that have been suspended, call the ResumeProcesses API.*

- **Lifecycle Hooks** : *Lifecycle hooks allow you to control what happens when your Amazon EC2 instances are launched and terminated as you scale out and in. For example, you might download and install software when an instance is launching, and archive instance log files in Amazon Simple Storage Service (S3) when an instance is terminating.*

    **The Notification Option**
        - Using CLoudWatch Event
        - Using Amazon SNS
        - Using Amazon SQS

    (Qusetion) **Can you have this to launch a script on an EC2 instance?**
        - The answer is *YES* Using Auto Scaling lifecycle hooks -> Lambda -> EC2 Run Commnad 

---

## DynamoDB

---

## Multi Region Services:
    * DynamoDB Global Tables (multi-way replication, enabled by Streams)
    * AWS Config Aggregators (multi region & multi account)
    * RDS Cross Region Read Replicas (used for Read & DR(Disaster Recovery))
    * Auurora Global Database (one region is a master, other is for Read & DR(Disaster Recovery))
    * EBS volumes snapshots, AMI, RDS snapshots can be copied to other regions
    * VPC peering to allow private traffic between regions
    * Route53 uses a global network of DNS servers
    * S3 cross region Replication
    * CloudFront for Global CDN at the Edge Locations
    * Lambda@Edge for Global Lambda function at Edge Locations (A/B testing)

- **Multi Region with Route53** :
    - *Health Check => automated DNS failovers:*
        * 1) Health checks that monitor an endpoint (application, server, other AWS resources)
        * 2) Health checks that monitor other health checks (calculated health checks)
        * 3) Health checks that monitor CloudWatch alarms (full control !!) - e.g. thottles of DynamoDB, custom metrics, etc..


---

## CloudFormation StackSets:

 * Create, update, or delete stacks across multiple accounts and regions with a single opeation.
 * Administrator account to create StackSets
 * Trusted accounts to create, update, delete stack instances from StackSets.
 * When you update a stack set, all associated stack instances are updated throughout all accounts and regions.
 * Ability to set a maximum concurrent actions on targets (# or %)
 * Ability to set failure tolerance (# or %)


 ---

 ## Disaster Recovery :
 * Any Event that has a negative impact on a company business continuity or finances is a disaster.
* Disaster recovery (DR) is about preparing for and recovering from a disaster.
* What kind of disaster recovery?
    - On-Premise => On-Premise:traditional DR, and very expensive.
    - On-Premise => AWS Cloud:hybrid recovery
    - AWS Cloud Region A => AWS Cloud Region B.
* Need to define two terms:
    - RPO: Recovery Point Objective.
    - RTO: Recovery Time Objective.

- **Disaster Recovery Strategies**
    * Backup and Restore
    * Pilot Light
    * Warm Standby
    * Hot Site / Multi Site Approach

---- 
Notes