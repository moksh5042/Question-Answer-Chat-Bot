# Question-Answer Chat Bot: Answer Evaluator

This project is an AI-powered tool for evaluating student answers to questions, supporting both text and image inputs. It uses OCR to extract text from images, then leverages LLMs (like Ollama and Groq) to automatically grade answers based on the question and a maximum mark.

## Features

- **Text & Image Input:** Enter questions and answers as text or upload images (handwritten or printed).
- **OCR Integration:** Uses PaddleOCR to extract text from uploaded images.
- **LLM Grading:** Grades answers using LLMs (Ollama or Groq) based on accuracy, relevance, and completeness.
- **Streamlit UI:** Simple web interface for uploading, input, and result display.

## How It Works

1. **Input:** Provide question and answer as text or image.
2. **OCR:** If images are uploaded, PaddleOCR extracts the text.
3. **Grading:** The extracted or input text is sent to an LLM, which returns a numeric score.
4. **Output:** The score is displayed in the UI.

## Setup

### Requirements

- Python 3.8+
- See [`requirements.txt`](requirements.txt) or [`requirements_cpu.txt`](requirements_cpu.txt) for dependencies.

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd Question-Answer-Chat-Bot

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies (choose one)
pip install -r requirements.txt
# or for CPU-only
pip install -r requirements_cpu.txt
```

### Environment Variables

Create a `.env` file for any required API keys (e.g., Groq, Anthropic).  
Example:
```
GROQ_API_KEY=your_groq_api_key
```

### Running the App

```bash
streamlit run main.py
```

## File Structure

- `main.py` - Main Streamlit app, OCR, and grading logic.
- `OCR_test.py` - Standalone OCR test script.
- `test_ollama.py` - LLM grading test script.
- `requirements.txt` - Dependencies (GPU).
- `requirements_cpu.txt` - Dependencies (CPU).
- `HLD.md` - High-level design notes.
- `Img/` - Directory where uploaded images are saved.

## Example Usage

1. Start the app: `streamlit run main.py`
2. Enter or upload a question and answer.
3. Set the maximum marks.
4. Click **Run** to get the evaluated score.

## Notes

- Only one input method (text or image) per field is allowed at a time.
- Images are saved in the `Img/` directory.
- LLM models and OCR may require additional setup or API keys.
- For best OCR results, ensure images are clear and well-lit.

## License

[MIT](LICENSE) (add your license file if needed)