from flask import Flask, render_template, request, send_file
from fillpdf import fillpdfs
import os
import datetime

app = Flask(__name__)

# Function to generate the PDF
def generate_pdf(template_pdf_path, user_data):
    # Generate a unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f'filled_form_{timestamp}.pdf'
    
    # Create the PDF
    fillpdfs.write_fillable_pdf(template_pdf_path, output_filename, user_data)
    fillpdfs.flatten_pdf(output_filename, f'flat_{output_filename}')
    
    return f'flat_{output_filename}'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Gather user data from the form
        user_data = {
            'Text1': request.form.get('Text1'),
            'Text2': request.form.get('Text2'),
            'Text3': request.form.get('Text3'),
            'Text4': request.form.get('Text4'),
            'CheckBox1': 'Yes' if request.form.get('CheckBox1') else 'Off',
            'Signature1': request.form.get('Signature1')
        }
        
        # Generate the PDF
        pdf_file = generate_pdf('template_3.pdf', user_data)
        
        return send_file(pdf_file, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
