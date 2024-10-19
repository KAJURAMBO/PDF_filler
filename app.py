import streamlit as st
from fillpdf import fillpdfs
import os
import datetime

def generate_pdf(template_pdf_path, user_data):
    # Generate a unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f'filled_form_{timestamp}.pdf'
    
    # Create the PDF
    fillpdfs.write_fillable_pdf(template_pdf_path, output_filename, user_data)
    fillpdfs.flatten_pdf(output_filename, f'flat_{output_filename}')
    
    return output_filename

# Streamlit UI
st.title("PDF Form Generator")

# File uploader for the PDF template
uploaded_file = st.file_uploader("Upload your PDF template", type="pdf")

# Only show the form if a file has been uploaded
if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("uploaded_template.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Input fields for the form
    user_data = {
        'Text1': st.text_input("Enter value for Text1:"),
        'Text2': st.text_input("Enter value for Text2:"),
        'Text3': st.text_input("Enter value for Text3:"),
        'Text4': st.text_input("Enter value for Text4:"),
        'CheckBox1': st.checkbox("CheckBox1", value='Off'),  # You might want to adjust the value here based on your needs
        'Signature1': st.text_input("Enter value for Signature1:")
    }

    if st.button("Generate PDF"):
        # Generate PDF and display a success message
        pdf_file = generate_pdf("uploaded_template.pdf", user_data)
        st.success("PDF has been generated successfully!")
        
        # Provide a download link for the generated PDF
        with open(pdf_file, "rb") as f:
            st.download_button("Download PDF", f, file_name=pdf_file)

        # Optional: Remove the generated PDF after download (if desired)
        # os.remove(pdf_file)
        
    # Optional: Display the uploaded PDF template (for verification)
    st.subheader("Uploaded PDF Template:")
    st.write("Preview of uploaded PDF:")
    st.write("Note: PDF preview may not be available in Streamlit.")

# Clean up: Remove the temporary file after generating the PDF if desired
# os.remove("uploaded_template.pdf")  # Uncomment if you want to delete it after processing
