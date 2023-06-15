# Remittances Analysis Tool

This is a data science model/software solution for analyzing remittance transactions.

## Description

The Remittances Analysis Tool is designed to provide insights and analysis on remittance transactions. It takes a CSV file containing remittance data as input and generates various statistics, visualizations, and trends to help understand the patterns and characteristics of the remittance transactions.

## Problem

The problem identified is the need for better analysis and understanding of remittance transactions. Remittances play a significant role in global economies, and analyzing the data can help identify trends, patterns, and insights that can assist in making informed decisions and policies related to remittances.

## Requirements

- Python 3.9 or higher
- Docker (optional)

## Usage

1. Clone the repository:

```bash
git clone https://github.com/shoanchikato/remittances-analysis.git
```

2. Navigate to the project directory:

```bash
cd remittances-analysis
```

3. (Optional) Create a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare your remittance data in a CSV file with the following columns: Date, Amount Sent, Name, Surname, Transaction Status, Time, Payment Method, Reason for Transfer, Sending Country, Receiving Country, Delivery Method.

2. Run the Flask application:

```bash
python app.py
```

3. Open your web browser and go to http://localhost:5000.

4. Upload the remittance data CSV file using the provided form.

5. The application will process the data and display insights and visualizations on the webpage.

## Docker

Alternatively, you can use Docker to run the application. Make sure you have Docker installed and running.

1. Build the Docker image:

```bash
docker build -t remittances-analysis .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 remittances-analysis
```

3. Open your web browser and go to http://localhost:5000.

## Running Bash Commands

To run bash commands, open your terminal or command prompt and navigate to the project directory.

To start the Flask application without Docker:

```bash
python app.py
```

To stop the Flask application, press Ctrl+C in the terminal.

## Docker Bash Commands

To run Docker bash commands, open your terminal or command prompt and navigate to the project directory.

To build the Docker image:

```bash
docker build -t remittances-analysis .
```

To run the Docker container:

```bash
docker run -p 5000:5000 remittances-analysis
```

To stop the Docker container:

```bash
docker stop <container-id>
```

To remove the Docker container:

```bash
docker rm <container-id>
```

To remove the Docker image:

```bash
docker rmi remittances-analysis
```

## License

This project is licensed under the MIT License.