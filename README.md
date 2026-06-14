# Serverless REST API on AWS

A fully serverless REST API built with AWS Lambda, API Gateway, and DynamoDB — provisioned entirely with Terraform.

## Architecture
Client (Postman / Frontend)

|

v

API Gateway          <- receives HTTP requests

|

v

AWS Lambda           <- runs business logic (Python 3.12)

|

v

DynamoDB             <- stores data (NoSQL)
## Tech Stack

| Service | Purpose |
|---|---|
| AWS API Gateway | HTTP endpoint - routes requests to Lambda |
| AWS Lambda | Serverless compute - runs on trigger only |
| AWS DynamoDB | NoSQL database - stores items |
| AWS IAM | Permissions - least privilege access |
| Terraform | Infrastructure as Code - provisions all resources |
| Python 3.12 | Lambda runtime |

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /items | Fetch all items |
| GET | /items/{id} | Fetch single item by ID |
| POST | /items | Create new item |
| DELETE | /items/{id} | Delete item by ID |

## Deploy

```bash
git clone https://github.com/Prabhnoor186/serverless-rest-api.git
cd serverless-rest-api
terraform init
terraform plan
terraform apply
```

## Destroy

```bash
terraform destroy
```

## Key Design Decisions

**Lambda over EC2** - Lambda runs only when triggered, no idle cost. For an API with unpredictable traffic this is more cost efficient and operationally simpler.

**DynamoDB over RDS** - Serverless, no connection management, scales automatically. Fits the stateless Lambda model.

**Terraform** - All infrastructure is version controlled and reproducible. No manual console clicks.

**Least privilege IAM** - Lambda has only the DynamoDB actions it needs (GetItem, PutItem, DeleteItem, Scan). Nothing more.

## Region

Deployed in eu-north-1 (Stockholm) on AWS Free Tier.
