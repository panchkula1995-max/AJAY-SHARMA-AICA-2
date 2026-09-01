from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from config.settings import SYSTEM_LEGAL_PROMPT

class LegalService:
    @staticmethod
    def analyze_notice(document_text: str, api_key: str) -> str:
        """Executes LLM processing or triggers sandbox visualization layer."""
        if "test-key" in api_key.lower() or api_key == "dummy":
            return LegalService._get_mock_response()
            
        try:
            llm = ChatOpenAI(model="gpt-4o", temperature=0.2, openai_api_key=api_key)
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", SYSTEM_LEGAL_PROMPT),
                ("user", "Here is the extracted text of the Show-Cause Notice:\n\n{document_text}")
            ])
            chain = prompt_template | llm
            response = chain.invoke({"document_text": document_text})
            return response.content
        except Exception as e:
            raise RuntimeError(f"Engine Core failure connection metrics: {str(e)}")

    @staticmethod
    def _get_mock_response() -> str:
        """Returns structural placeholder content for localized environment testing."""
        return """### 1. Executive Summary & Parameters
- **Issuing Authority:** Office of the Assistant Commissioner of GST
- **Notice Reference Number:** GST/SCN/2026/089-A
- **Date of Issue:** 12th August 2026
- **Sections Invoked:** Section 73 of the CGST Act, 2017

### 2. Quantum of Demand (Financial Table)

| Tax Head | Tax Demand (₹) | Interest (₹) | Penalty (₹) |
| :--- | :--- | :--- | :--- |
| CGST | 5,00,000 | Applicable u/s 50 | 50,000 |
| SGST | 5,00,000 | Applicable u/s 50 | 50,000 |

### 3. Core Allegations Matrix
- **Allegation:** Mismatch between Input Tax Credit (ITC) claimed in GSTR-3B vs available in GSTR-2B.
- **Natural Justice Check:** Flagged. No personal hearing option declared in baseline order parameters.

### 4. Strategic Draft Reply Template
To,\nThe Assistant Commissioner,\n[Address]\n\n**Subject: Reply to SCN Ref No: GST/SCN/2026/089-A**\n\nRespected Sir/Madam,\nThe Assessee begs to submit that discrepancies arise from timing differences of vendors uploading invoices, which is legally protected under historical CBIC Circulars..."""
