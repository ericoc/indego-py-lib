def lambda_handler(event, context):

	from indego import Indego
	import json

	# Instantiate the Indego class and get all the stations
	indego = Indego();

	# Use the ?search query string passed if there was one
	try:
		search = event['queryStringParameters']['search']
	except Exception:
		search = ''

	# Search for what ever stations were requested
	stations = indego.get_stations(search);

	# Return stations if any were found
	if len(stations) > 0:
		code = 200
	else:
		code = 204
		stations = 'No stations found'

	return {
		'statusCode': code,
		'body': json.dumps(stations)
	}
