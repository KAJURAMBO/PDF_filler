from flask import Flask, request, render_template, send_file
from fillpdf import fillpdfs
import os
import datetime

class PDFGenerator:
    def __init__(self, template_pdf_path, user_data):
        self.template_pdf_path = template_pdf_path
        self.user_data = user_data
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_filename = f'filled_form_{self.timestamp}.pdf'
        self.flattened_pdf_filename = f'flat_{self.output_filename}'
    
    def generate_pdf(self):
        """Generate a filled and flattened PDF based on the template and user data."""
        try:
            # Fill the form fields in the PDF
            fillpdfs.write_fillable_pdf(self.template_pdf_path, self.output_filename, self.user_data)
            fillpdfs.flatten_pdf(self.output_filename, self.flattened_pdf_filename)
            
            # Debugging: Check if the file was created successfully
            if os.path.exists(self.flattened_pdf_filename) and os.path.getsize(self.flattened_pdf_filename) > 0:
                print(f"Generated PDF: {self.flattened_pdf_filename} (size: {os.path.getsize(self.flattened_pdf_filename)} bytes)")
            else:
                print(f"Failed to generate PDF or the PDF is empty: {self.flattened_pdf_filename}")
                return None
            
            return self.flattened_pdf_filename
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return None

class FormHandler:
    def __init__(self, uploaded_file, request_form):
        self.uploaded_file = uploaded_file
        self.request_form = request_form
        self.template_path = "uploaded_template.pdf"
    
    def save_uploaded_template(self):
        """Save the uploaded PDF file temporarily."""
        if self.uploaded_file:
            self.uploaded_file.save(self.template_path)
    
    def extract_fields(self):
        """Extract form fields from the uploaded PDF."""
        if os.path.exists(self.template_path):
            fields = fillpdfs.get_form_fields(self.template_path)
            return fields
        return {}
    
    def prepare_user_data(self):
        """Prepare user data dictionary from form inputs."""
        fields = self.extract_fields()
        user_data = {field: self.request_form.get(field, '') for field in fields}
        # Special handling for checkboxes
        user_data['CheckBox1'] = 'Yes' if self.request_form.get('CheckBox1') else 'Off'
        return user_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle file upload and form submission
        uploaded_file = request.files['template_pdf']
        form_handler = FormHandler(uploaded_file, request.form)
        form_handler.save_uploaded_template()

        # Prepare user data from the form
        user_data = form_handler.prepare_user_data()

        # Generate PDF using the extracted data
        pdf_generator = PDFGenerator(form_handler.template_path, user_data)
        pdf_file = pdf_generator.generate_pdf()

        if pdf_file:
            # Send the generated PDF for download
            return send_file(pdf_file, as_attachment=True)
        else:
            return "Error generating PDF.", 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
