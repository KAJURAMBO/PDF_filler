from flask import Flask, request, render_template, send_file
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
    try:
        fillpdfs.write_fillable_pdf(template_pdf_path, output_filename, user_data)
        filled_pdf = f'flat_{output_filename}'
        fillpdfs.flatten_pdf(output_filename, filled_pdf)

        # Debugging: Check if the file was created
        if os.path.exists(filled_pdf) and os.path.getsize(filled_pdf) > 0:
            print(f"Generated PDF: {filled_pdf} (size: {os.path.getsize(filled_pdf)} bytes)")
        else:
            print(f"Failed to generate PDF or the PDF is empty: {filled_pdf}")
        
        return filled_pdf
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Save the uploaded file temporarily
        uploaded_file = request.files['template_pdf']
        if uploaded_file:
            template_path = "uploaded_template.pdf"
            uploaded_file.save(template_path)

            # Extract the form fields from the uploaded PDF
            fields = fillpdfs.get_form_fields(template_path)

            # Prepare user_data dictionary
            user_data = {field: request.form.get(field, '') for field in fields}
            user_data['CheckBox1'] = 'Yes' if request.form.get('CheckBox1') else 'Off'

            # Generate PDF
            pdf_file = generate_pdf(template_path, user_data)

            if pdf_file:
                # Provide the generated PDF for download
                return send_file(pdf_file, as_attachment=True)
            else:
                return "Error generating PDF.", 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)