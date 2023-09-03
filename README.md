# DoRoad

## Why DoRoad?
"DoRoad" is an AI-powered day trip planner designed to provide families with a seamless experience in planning their day trips and effortless create family-friendly itineraries. By leveraging the power of OpenAI, "DoRoad" creates a full-featured, family-friendly itinerary based on user-provided parameters like the departure location, destination, number of persons, and the date of the trip to generate a comprehensive intinerary, ensuring an unforgettable journey. The objective behind this project is to use AI to enhance the trip planning process, making it more efficient, personalized, and enjoyable.:
- **Efficiency**: Use the latest weather and traffic data to plan routes and activities.
- **Personalization**: Based on the number of adults and children, the AI crafts an itinerary that's suitable for everyone.
- **Simplicity**: Instead of spending hours researching places to visit, get a detailed itinerary in seconds.


## DoRoad in Action
Imagine planning a day trip for your family. The endless research on local attractions, family-friendly activities, and the best routes can be overwhelming to ensure every member of the family, including children, have an engaging experience. "DoRoad" simplifies this process. With just a few inputs, such as departure location, destination, number of adults, and children, and the date of the trip, "DoRoad" crafts a detailed itinerary for a day filled with a mix of adventure, cultural exploration and relaxation. Whether you're exploring the scenic beauty of Vincy or embarking on an adventure in the Netherlands, "DoRoad" ensures you discover the unexpected, effortlessly.


## Getting Started Self-Hosting

### 1. Installation Process

- Clone the repository to your local machine.

```
git clone https://github.com/Gyarbij/DoRoad.git
```
- Navigate to the project directory.

```
cd DoRoad
```
- Virtual Environment: Consider using a virtual environment to isolate the dependencies for the project. This can help avoid conflicts between different versions of libraries. You can create a virtual environment using:

```
python3 -m venv doroad
source doroad/bin/activate
```

### 2. Software Dependencies
- Ensure you have Python and Flask installed.
- Install the required packages using ```pip install -r requirements.txt``` (Note: `requirements.txt` should contain Flask and other necessary libraries).


### 3. Environment Variable via file

Before starting the server using the environment variable file, follow these steps:

1. Copy the `.envEXAMPLE` provided in the repository to a new file named `.env`:
```
cp .envEXAMPLE .env
```
2. Edit the `.env` file with the appropriate values for your setup:
- Replace `openai_api_type` with the api type of 'azure' or 'openai'.
- Replace `penai_api_version` with the api version. For Azure, use e.g. '2023-08-01-preview'. For OpenAI, use '2020-04-01' (I haven't tested OpenAI as yet). 
- Replace `your_openai_api_key` with your actual Azure/OpenAI API key.
- Replace `https://YOURENDPOINT.openai.azure.com/` with your actual OpenAI API endpoint. For OpenAI, use `https://api.openai.com/`.
- Replace `your_deployment_name` with the name of your deployment. For Azure, use the name of your deployment. For OpenAI, use 'playground'.

3. Use the `python-dotenv` library to automatically load the environment variables from the `.env` file. If you haven't installed it yet, do so with:
```
pip install python-dotenv
```
4. Ensure that your Flask application is set up to use the `python-dotenv` library. If you're using the default Flask setup, it will automatically load the `.env` file. If not, you can manually load the `.env` file in your application with the following code:
```
from dotenv import load_dotenv
load_dotenv()
```
The application will now use the environment variables specified in the `.env` file.


### 4. Environment Variable using the `export` command:
```
export OPENAI_API_TYPE=azure
export OPENAI_API_VERSION=2023-08-01-preview
export OPENAI_API_KEY=#your_openai_api_key
export OPENAI_API_BASE=#your_api_base
export DEPLOYMENT_NAME=#your_deployment_name

```

### 5. How to Run the Application
- Set up your environment variables for the OpenAI API.
- Navigate to the project directory in your terminal.
- Run the command `python3 doroad.py`.
- Open a browser and navigate to `http://localhost:5000` to access the application.


## Build and Test
To build and test the application:

1. **Building the Application**:
   - Ensure all dependencies are installed.
   - Set up your environment variables.
   - Modify the application to turn on debug mode in Flask.
   - Make any necessary changes to the application.
   - Run the application using `python3 doroad.py`.

2. **Testing the Application**:
   - Navigate to the home page.
   - Fill in the required details such as departure location, destination, number of adults, children, and the date.
   - Click on the "do road" button.
   - Wait for the AI to generate your itinerary and display it in the "your itinerary" section.
   - Monitor the Flask debug logs for any errors.


## Latest Releases
- Check the releases section of the repository for the latest stable version.


## API References
- The application uses the OpenAI API with the hosted version using Azure. Ensure you have your API keys set up as environment variables.


