#STACK: *FASTAPI, MYSQL, REACTJS*

# Setting Up
* Install FastAPI
```
pip install fastapi
```
* Setup mysql database
* Get an api key from newsapi.org
* Edit the config.py 
```
# database configurations
user = ''
password = ''
host = ''
port = 
database_name = ''
# newsApi key
key = ''
```

* Clone this repository
```
git clone https://github.com/maxwell150/topHeadlines
```
* 
```
cd newsAPP
```
*
```
npm install
```



# React Application
The React application seamlessly interacts with the backend, meticulously constructed using the fastAPI framework and supported by a robust MySQL database. This backend architecture facilitates the retrieval of articles, a process initiated by the React application, which subsequently renders the obtained articles within its user interface.

  Additionally, the application incorporates a dedicated page designed for the generation of API keys catering to developers. This functionality empowers developers with a streamlined process for obtaining the necessary credentials, enhancing the overall accessibility and integration capabilities of the application

  # API

  ## Introduction

  This API provides functionality to retrieve articles.

  ## Base URL

  The base URL for this API is `/articles`.

  ## Endpoints

  ### 1. Get All Articles

  #### `GET /articles/`

  **Description:** Retrieve a list of all articles.

  **Response:**
  - Status Code: 200 OK
  - Response Body: List of articles in JSON format.

  ### 2. Get All Articles with API Key

  #### `GET /articles/apiKey={apikey}`

  **Description:** Retrieve a list of all articles using an API key for authentication.

  **Path Parameters:**
  - `apikey` (string): API key for authentication.

  **Response:**
  - Status Code: 200 OK
  - Response Body: List of articles in JSON format.

  ### 3. Get Latest Article

  #### `GET /articles/latest`

  **Description:** Retrieve details of the latest article.

  **Response:**
  - Status Code: 200 OK
  - Response Body: Details of the latest article in JSON format.

  ## Examples

  ### 1. Retrieve All Articles

  ```bash
  curl -X GET http://api-base-url/articles/
  ```

  ## Generatating API keys

  ## Base URL

  The base URL for this API is `/apikeys`.

  ## Endpoints

  ### 1. Generate API Key

  #### `GET /apikeys/generate_api_key`

  **Description:** Generate a new API key.

  **Response:**
  - Status Code: 200 OK
  - Response Body: JSON object containing the generated API key.

  ## Examples

  ### 1. Generate API Key

  ```bash
  curl -X GET http://api-base-url/apikeys/generate_api_key
  ```
  ```json
  {
    "api_key": "generated-api-key-here"
  }
  ```

