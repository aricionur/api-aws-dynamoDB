import boto3

dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

resp = dynamodb.execute_statement(
    # Statement="INSERT INTO Books value {\'Author\': \'Antje Barth\', \'Title\': \'Data Science on AWS\',\'Category\': \'Technology\', \'Formats\': { \'Hardcover\': \'J4SUKVGU\', \'Paperback\': \'D7YF4FCX\' } }"
    Statement="INSERT INTO Books value {'Author': 'Julien Simon', 'Title': 'Learn Amazon SageMaker','Category': 'Technology', 'Formats': { 'Hardcover': 'Q7QWE3U2','Paperback': 'ZVZAYY4F', 'Audiobook': 'DJ9KS9NM' } }"

    # Statement='SELECT * FROM Books WHERE Author = \'Antje Barth\' AND Title = \'Data Science on AWS\''
)
print(resp)
