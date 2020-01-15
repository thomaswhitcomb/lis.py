#!/bin/sh
zip lispy.zip *py
aws lambda create-function \
  --function-name lispy \
  --handler cli.lambda_handler \
  --runtime "python2.7" \
  --memory 512 \
  --timeout 10 \
  --role arn:aws:iam::079759702379:role/lambda_exec_role \
  --zip-file fileb://./lispy.zip

