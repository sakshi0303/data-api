Approach to test the service:

1. Examples - https://mkyong.com/spring/curl-post-request-examples/ 
2. curl http://localhost:5000
3. Remove whitespace - https://codebeautify.org/remove-extra-spaces
4. Escape JSON - https://www.freeformatter.com/json-escape.html#before-output
5. Read the json content in python - https://stackabuse.com/how-to-get-and-parse-http-post-body-in-flask-json-and-form-data/ 

AWS cli setup - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
1. https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html 
2. aws configure
Default region name [None]: us-west-2
Default output format [None]: json
3. Test by running - aws s3 ls
4. You should see a s3 bucket name

curl -H "Content-Type: application/json" -X POST -d {\"namespace\":\"dataset1\",\"content\":\"rawcontent\", \"fileName\": \"part0.json\"} http://localhost:5000/upload

curl -H "Content-Type: application/json" -X POST -d "{\"namespace\":\"dataset1\",\"content\":\"[ { \\\"name\\\": \\\"John\\\", \\\"age\\\": 30, \\\"cars\\\": [ \\\"Ford\\\", \\\"BMW\\\", \\\"Fiat\\\" ] }, { \\\"name\\\": \\\"John1\\\", \\\"age\\\": 30, \\\"cars\\\": [ \\\"Ford\\\", \\\"BMW\\\", \\\"Fiat\\\" ] } ]\", \"fileName\": \"part0.json\"}" http://localhost:5000/upload


