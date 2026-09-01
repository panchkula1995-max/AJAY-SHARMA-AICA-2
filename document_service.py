from pypdf import PdfReader

class DocumentService:
    @staticmethod
    def extract_text(uploaded_file) -> str:
        """Extracts plain text out of a binary PDF input framework stream."""
        if not uploaded_file:
            return ""
            
        pdf_reader = PdfReader(uploaded_file)
        extracted_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
        return extracted_text
