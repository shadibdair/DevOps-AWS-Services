## CloudTrail
- CloudTrail :
    AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. ... CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.
- Need to remember what is in the CloudTrail File :
    * Who made the request.
    * When and from Where.
    * What was requested.
    * What was the response.
- Log Integrity
- Cross Account Logging

- **To remember** *CloudTrail can send data into the S3 bucket on the regular schedule OR into CloudWatch groups as a log file*

---

## Kinesis
- **Kinesis** : is a managed alternative to Apache Kafka, Apache Kafka is a streaming system.
- Great for application logs, metrics, IOT data, clickstreams.
- Great for "real-time" big data.
- Great for streaming processing freamworks(Spark, NiFi, etc...).
- Data is automatically replicated to 3 AZ.


**Kinesis Streams** : Low latency streaming ingest at scale.
**Kinesis Analytics** : Perform real-time analytics on streams using SQL.
**Kinesis Firehose** : load streams into S3, Redshift, ElasticSearch...

**[Click Streams, IOT devices, Metrics & Logs] ---> 1)Kinesis Streams 2)Kinesis Analytics 3)Kinesis Firehose ---> S3 Bucket.**

- Kinesis Streams:
    * Streams are divided in in ordered Shards/Partitions.
    * Data retention is 1 day by default, can go up to 7 days.
    * Ability to reprocess / replay data.
    * Multiple application can consume the same stream.
    * Real-time processing with scale of throughput.
    * Once data is inserted in kinesis, it can't be deleted (immutability).

- Kinesis Streams Shards:
    * One stream is made of many different shards.
    * Billing is per shard provisioned, can have as many shards as you want.
    * Batching available or per message calls.
    * The number of shards can evolve over time (reshard / merge).
    * Records are ordered per shard.

- Kinesis Data Streams Limits to know:
    * Producer:
        - 1 MB/s or 1000 messages/s at write PER SHARD.
        - "ProvisionedThroughputException" otherwise.
    * Consumer Classic:
        - 2 MB/s at read PER SHARD across all consumers.
        - 5 API calls per second PER SHARD across all consumers.
        - = if 3 different applicaiton are consuming, possibility of throttling.
    * Data Retention:
        - 24 hours data retention by default.
        - Can be extended to 7 days.
>

- Kinesis Producers:
    * Kinesis SDK 
    * Kinesis Producer Library (KPL)
    * Kinesis Agent
    * CloudWatch Logs
- Kinesis Consumers:
    * Kinesis SDK
    * Kinesis Client Library (KCL)
    * Kinesis Connector Libray
    * Kinesis Firehose
    * Kinesis AWS Lambda

>
- AWS Kinesis Client Library (KCL):
    * KCL uses DynamoDB to checkpoint offsets
    * KCL uses DynamoDB to track other workers and share the work amongst shards.
    * Great for reading in a distributed manner.

>
- **AWS Kinesis Data Firehose:**
    * Fully Managed Service, no administration.
    * Near Real Time (60 seconds latency minimum for non full batches)
    * Load data into Redshift / Amazon S3 / ElasticSearch / Splunk.
    * Data Transformation through AWS Lambda (ex: CSV => Json).
    * Support compression when target is Amazon S3 (GZIP, ZIP, SNAPPY)
    * Pay for the amount of data going through Firehose.
>
- **Kinesis Data Streams VS Firehose**
    * *Streams* :
        - Going to write custom code (producer/consumer).
        - Real time (~200 ms latency for classic).
        - Must manage scaling (Shard splitting / merging)
        - Data Storage for 1 to 7 days, replay capability, multi consumers.
        - Use with Lambda to insert data in real-time to ElasticSearch (for example).
    * *Firehose* :
        - Fully managed, send to s3, Splunk, Redshift, ElasticSearch.
        - Serverless data transformations with Lambda.
        - Near real time (lowest buffer time is 1 minute)
        - Automated Scaling
        - No data storage
>
- **AWS Kinesis Data Analytics:**
    * Perform real-time analytic on Kinesis Streams using SQL.
    * Kinesis Data Analytic:
        - Auto Scaling
        - Managed: no servers to provision.
    * Pay for actual consumption rate.
    * Can create streams out of the real-time queries.

---

## CloudWatch

**Important** *Using CloudWatch Logs Subscription Filters*
- You can use a subscription filter with kinesis, Lambda, or Kinesis Data Firehose.
    * Subscription Filters with Kinesis.
    * Subscription Filters with AWS Lambda.
    * Subscription Filters with Amazon Kinesis Data Firehode.
>

**All kind of logs**:
- Application Logs.
- Operating System Logs (Event Logs, System Logs).
- Access Logs.

**AWS Managed Logs**:
- Load Balancer Access Logs (ALB, NLB, CLB) => to S3.
- CloudTrail => to S3 and CloudWatch Logs.
- VPC Flow Logs => to S3 and CloudWatch Logs.

**What is ES (ElasticSearch)**:
- Elasticsearch is an open-source database tool that can be easily deployed and operated. ... AWS Elasticsearch makes things simpler to its users as they do not need to manually create an Elasticsearch cluster. It allows the user to visualize, analyze, and search the data in real-time.

**What is X-Ray**:
AWS X-Ray is a service that helps developers analyze and debug distributed applications. Customers use X-Ray to monitor application traces, including the performance of calls to other downstream components or services, in either cloud-hosted applications or from their own machines during development.17 ביולי 2020


---