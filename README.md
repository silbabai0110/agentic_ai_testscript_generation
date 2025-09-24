# 🤖 Agentic AI Test Script Generator

An **agentic AI solution** that analyzes requirements documents (PDF/DOCX), extracts **features → user stories → test cases**, and generates **Selenium test scripts** automatically using **LangGraph agents**.

Built with:
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Streamlit](https://streamlit.io/) for UI
- Python (docx, PyPDF2, reportlab, dotenv, logging)

---

## 🚀 Features
- 📂 Upload requirement documents (PDF/DOCX)
- 🔍 Extract **features** (`F-xxx`) from requirements
- 📝 Generate **user stories** (`F-xxx_US-xxx`) per feature
- ✅ Generate **test cases** (`F-xxx_US-xxx_TC-xxx`) per user story
- 🧪 Create **Selenium test scripts** for each test case
- 🛠 Validate generated scripts against standard Selenium practices
- 📑 Collate outputs into a DOCX report
- 📊 Streamlit UI with **live execution logs** and **download options**

---

## 📂 Project Structure
```
agentic_ai_testscript_generation/
│── requirement_docs/          # Input requirement documents (.docx/.pdf)
│── GEN-TESTSCRIPTS/       # Auto-generated Selenium scripts
│── outputs/               # Collated DOCX reports
│── main.py                # LangGraph pipeline (nodes + agent state)
│── requirements.txt       # Python dependencies
│── .gitignore             # Git ignore rules
│── README.md              # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/agentic_ai_testscript_generation.git
cd agentic_ai_testscript_generation
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file:
```env
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_MODEL=gpt-4o  # or any deployed model\
AZURE_OPENAI_API_VERSION=2024-12-01-preview or deployed model version
```

---

## ▶️ Usage

### Run with Streamlit UI
```bash
streamlit run main.py
```

---

## 📊 Streamlit UI Features
- Upload requirements document
- View **live execution logs**
- Automatic generation of Selenium test scripts
- Download final collated DOCX report
- Modern UI with sidebar, spinners, and progress updates

---

## ✅ Example Workflow
1. Upload `requirements.docx`
2. Pipeline runs:
   - Feature Analyzer → User Story Generator → Test Case Generator → Selenium Script Generator
3. Scripts saved in `GEN-TESTSCRIPTS/`
4. Collated report saved in `outputs/GenAI_Features_UserStories_Tescases.docx`
5. Download from UI

---

## 📌 Roadmap
- [ ] Multi-document upload & batch processing
- [ ] Dashboard view of generated test cases in UI


---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.
