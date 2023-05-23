import matplotlib
matplotlib.use('Agg')  # Use the Agg backend

from flask import Flask, render_template, request
import csv
import io
import matplotlib.pyplot as plt
import base64
from io import BytesIO

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

    # Generate graphs
    payment_methods_graph = generate_pie_chart(payment_methods, 'Payment Methods')
    sending_countries_graph = generate_bar_chart(sending_countries, 'Sending Countries')
    receiving_countries_graph = generate_bar_chart(receiving_countries, 'Receiving Countries')
    transaction_statuses_graph = generate_bar_chart(transaction_statuses, 'Transaction Statuses')

    # Return the insights and graphs
    return {
        'Total Amount Sent': format(total_amount_sent,".2f"),
        'Total Transactions': transaction_count,
        'Payment Methods': payment_methods,
        'Sending Countries': sending_countries,
        'Receiving Countries': receiving_countries,
        'Transaction Statuses': transaction_statuses,
        'Payment Methods Graph': payment_methods_graph,
        'Sending Countries Graph': sending_countries_graph,
        'Receiving Countries Graph': receiving_countries_graph,
        'Transaction Statuses Graph': transaction_statuses_graph
    }

def generate_pie_chart(data, title):
    labels = list(data.keys())
    values = list(data.values())

    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)

    # Convert the plot to base64 image
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    plt.close()

    return image_base64

def generate_bar_chart(data, title):
    labels = list(data.keys())
    values = list(data.values())

    plt.figure()
    plt.bar(labels, values)
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.title(title)

    # Convert the plot to base64 image
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    plt.close()

    return image_base64

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
