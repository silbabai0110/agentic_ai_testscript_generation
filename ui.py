import streamlit as st
import os
import shutil
import subprocess
import sys


# Ensure requirements folder exists
REQUIREMENTS_FOLDER = "requirements"
os.makedirs(REQUIREMENTS_FOLDER, exist_ok=True)

st.set_page_config(page_title="Agentic AI Test Script Generator", layout="wide")
st.title("📄 Agentic AI: Requirement → Test Script Generator")

st.markdown("""
Upload your **requirement documents** (.docx or .pdf).  
They will be processed through the pipeline to generate:  
- **Features → User Stories → Test Cases**  
- **Selenium Test Scripts**  
- **Collated Output Report**  
""")

# Upload file(s)
uploaded_files = st.file_uploader("Upload Requirement Document(s)", type=["docx", "pdf"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_path = os.path.join(REQUIREMENTS_FOLDER, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        st.success(f"✅ Uploaded: {file.name}")

    if st.button("🚀 Run Pipeline"):
        with st.spinner("Running the AI pipeline... this may take a few minutes ⏳"):
            try:
                req_file = "requirements.txt"
                # Run the main.py pipeline
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
                result = subprocess.run(["python", "main.py"], capture_output=True, text=True)

                if result.returncode == 0:
                    st.success("🎉 Pipeline executed successfully!")
                    st.text_area("Logs", result.stdout, height=200)
                else:
                    st.error("⚠️ Pipeline failed.")
                    st.text_area("Error Logs", result.stderr, height=200)
            except Exception as e:
                st.error(f"Pipeline execution failed: {e}")

# Show generated outputs
st.subheader("📂 Generated Files")

if os.path.exists("GEN-TESTSCRIPTS"):
    st.markdown("### Selenium Test Scripts")
    for fname in os.listdir("GEN-TESTSCRIPTS"):
        fpath = os.path.join("GEN-TESTSCRIPTS", fname)
        with open(fpath, "r", encoding="utf-8") as f:
            st.download_button(
                label=f"⬇️ Download {fname}",
                data=f.read(),
                file_name=fname,
                mime="text/x-python"
            )

if os.path.exists("outputs"):
    st.markdown("### Collated Reports")
    for fname in os.listdir("outputs"):
        fpath = os.path.join("outputs", fname)
        with open(fpath, "rb") as f:
            st.download_button(
                label=f"⬇️ Download {fname}",
                data=f,
                file_name=fname
            )
