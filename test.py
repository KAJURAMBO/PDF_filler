import fillpdf
from fillpdf import fillpdfs

Input_entry=fillpdfs.get_form_fields("template_3.pdf")##without filling
print(Input_entry)
# Example input dictionary
input_entry = {
    'Text1': '',
    'Text2': '',
    'Text3': '',
    'Text4': '',
    'CheckBox1': 'Off',
    'Signature1': ''
}

# Function to update the dictionary with user input
def update_entry_with_user_input(input_entry):
    for key in input_entry.keys():
        # Simulating user input (you can replace this with actual user input retrieval)
        user_input = input(f"Enter value for {key}: ")
        
        # Update the dictionary value for the corresponding key
        input_entry[key] = user_input if user_input else input_entry[key]  # Keep old value if input is empty

    return input_entry

# Call the function to update the input_entry dictionary
updated_entry = update_entry_with_user_input(input_entry)

# Print the updated dictionary
# print("Updated Entry:", updated_entry)

data_dict = updated_entry
fillpdfs.write_fillable_pdf('template_3.pdf', 'new.pdf', data_dict)
fillpdfs.flatten_pdf('new.pdf', 'newflat.pdf')







from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import fillpdf
from fillpdf import fillpdfs
import os
from datetime import datetime

app = Flask(__name__)

# Directory to save the generated PDFs
OUTPUT_DIR = 'generated_pdfs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Route for the main form
@app.route('/')
def index():
    return render_template('index.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        'Text1': request.form.get('Text1'),
        'Text2': request.form.get('Text2'),
        'Text3': request.form.get('Text3'),
        'Text4': request.form.get('Text4'),
        'CheckBox1': 'Yes' if request.form.get('CheckBox1') else 'Off',
        'Signature1': request.form.get('Signature1')
    }

    # Path to input PDF
    input_pdf_path = 'template_3.pdf'
    
    # Create a unique filename using the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_pdf_path = os.path.join(OUTPUT_DIR, f'filled_pdf_{timestamp}.pdf')
    flattened_pdf_path = os.path.join(OUTPUT_DIR, f'flattened_pdf_{timestamp}.pdf')

    # Write and flatten the PDF
    fillpdfs.write_fillable_pdf(input_pdf_path, output_pdf_path, user_data, flatten=False)
    fillpdfs.flatten_pdf(output_pdf_path, flattened_pdf_path)

    return redirect(url_for('download_file', filename=f'flattened_pdf_{timestamp}.pdf'))

# Route for downloading the generated PDF
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
