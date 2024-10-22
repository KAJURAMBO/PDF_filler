# PDF Form Filler Web Application

This web application allows users to upload a PDF form, fill it with data, and download the filled and flattened PDF. It uses Flask as the web framework and the `fillpdf` library to manage PDF form fields.

## Features
- Upload a PDF form and automatically extract form fields.
- Submit user input to fill the form fields of the uploaded PDF.
- Flatten the filled PDF to make the fields non-editable.
- Download the generated PDF.

## Requirements

- Python 3.x
- Flask
- fillpdf
- os
- datetime

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/KAJURAMBO/PDF_filler.git
    cd pdf-form-filler
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the application**:
   Open your web browser and go to:http://127.0.0.1:5000/


3. **Upload PDF Template**:
 - Select a PDF file that contains form fields.
 - Fill out the form with your desired data.
 - Submit the form to generate a filled and flattened PDF.

4. **Download the Filled PDF**:
 - The filled PDF will be provided for download.

## File Structure

- `app.py`: The main Flask application code.
- `templates/index.html`: The HTML form for uploading PDFs and filling out form fields.

## Customization

- To handle different PDF templates, you can modify the `FormHandler` class to select different templates based on certain criteria (e.g., form type).
- Adjust the form field mappings in the `prepare_user_data` method to suit the field names of your PDF.

## Troubleshooting

- If the form fields do not appear correctly or the PDF does not get generated, check the console for error messages.
- Ensure that your PDF form has fillable fields by checking it with a PDF reader.

## License

This project is licensed under the MIT License.

