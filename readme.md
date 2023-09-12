markdown
Copy code
# Vartapratikriya API Documentation

Welcome to the Vartapratikriya API documentation. This API allows you to retrieve news sources based on a given name. You can use it to fetch the source of news articles.

## Base URL
The base URL for this API is:
https://vartapratikriya-backend-rdkz.vercel.app/

shell
Copy code

## Endpoint

### Get News Source by Name

#### Endpoint

GET /?name={name}

bash
Copy code

#### Description

This endpoint allows you to retrieve the source of news articles based on the provided name.

#### Parameters

- `name` (string): The name of the news source you want to retrieve.

#### Example

```bash
curl -X GET "https://vartapratikriya-backend-rdkz.vercel.app/?name=example_news_source"
Response
json
Copy code
{
  "source": "Example News Source",
  "url": "https://www.example.com"
}
source (string): The name of the news source.
url (string): The URL of the news source.
Error Handling
If the specified name is not found, the API will return a 404 Not Found response.
Usage
To use this API, make a GET request to the appropriate endpoint with the required parameters.

javascript
Copy code
fetch("https://vartapratikriya-backend-rdkz.vercel.app/?name=example_news_source")
  .then((response) => response.json())
  .then((data) => {
    console.log("News Source:", data.source);
    console.log("Source URL:", data.url);
  })
  .catch((error) => console.error("Error:", error));