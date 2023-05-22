from flask import Flask, render_template, request
import csv
import io

app = Flask(__name__)

def process_data(file):
    # Initialize variables for insights
    total_amount_sent = 0
    transaction_count = 0
    payment_methods = {}
    sending_countries = {}
    receiving_countries = {}
    transaction_statuses = {}

    # Convert bytes to string
    file_content = file.read().decode('utf-8-sig')

    # Create a StringIO object from the string
    csv_file = io.StringIO(file_content)

    # Read the CSV file
    reader = csv.DictReader(csv_file)

    # Process each row in the CSV
    for row in reader:
        # Calculate total amount sent
        total_amount_sent += float(row['Amount Sent'])

        # Count transactions
        transaction_count += 1

        # Count payment methods
        payment_method = row['Payment Method']
        payment_methods[payment_method] = payment_methods.get(payment_method, 0) + 1

        # Count sending countries
        sending_country = row['Sending Country']
        sending_countries[sending_country] = sending_countries.get(sending_country, 0) + 1

        # Count receiving countries
        receiving_country = row['Receiving Country']
        receiving_countries[receiving_country] = receiving_countries.get(receiving_country, 0) + 1

        # Count transaction statuses
        transaction_status = row['Transaction Status']
        transaction_statuses[transaction_status] = transaction_statuses.get(transaction_status, 0) + 1

    # Return the insights
    return {
        'Total Amount Sent': total_amount_sent,
        'Total Transactions': transaction_count,
        'Payment Methods': payment_methods,
        'Sending Countries': sending_countries,
        'Receiving Countries': receiving_countries,
        'Transaction Statuses': transaction_statuses
    }

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file selected')
        
        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            return render_template('index.html', error='No file selected')

        # Check if the file is a CSV
        if not file.filename.endswith('.csv'):
            return render_template('index.html', error='Invalid file format. Please upload a CSV file.')

        try:
            insights = process_data(file)
        except Exception as e:
            return render_template('index.html', error=str(e))
        
        return render_template('insights.html', insights=insights)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
