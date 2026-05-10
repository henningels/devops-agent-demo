# Bookstore Demo

A serverless bookstore app on AWS, with CI/CD via GitHub Actions.

## Architecture

```
S3 (static hosting) → API Gateway → Lambda (Python) → DynamoDB
```

| Resource | Name |
|---|---|
| S3 Bucket | `bookstore-demo-918183255158` |
| API Gateway | `BookStoreAPI` |
| Lambda | `GetBooks` |
| DynamoDB | `Books` |

**Live URL:** http://bookstore-demo-918183255158.s3-website-us-west-2.amazonaws.com  
**API:** https://tm7id6cvkj.execute-api.us-west-2.amazonaws.com/prod/books

## CI/CD

Every push to `main` automatically:
1. Packages and deploys `lambda_function.py` to the `GetBooks` Lambda
2. Syncs `index.html` to the S3 website bucket

Requires GitHub Actions secrets: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
