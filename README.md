# Encoder

A Streamlit-based steganography application that allows you to hide secret messages within images using LSB (Least Significant Bit) encoding.

## 🌐 Live Demo

Visit the deployed application: [https://stgnphy.streamlit.app/](https://stgnphy.streamlit.app/)

## 🚀 Features

- **Hide Images**: Encode secret images into images
- **Reveal Hidden Images**: Extract hidden images from steganographic images
- **User-Friendly Interface**: Simple web interface built with Streamlit
- **Image Processing**: Powered by PIL/Pillow for robust image handling
- **LSB Steganography**: Uses Least Significant Bit technique for minimal visual impact

## 🛠️ Technologies

- **Python 3.12+**
- **Streamlit** - Web application framework
- **Pillow (PIL)** - Image processing library
- **NumPy** - Numerical computations

## 📦 Installation

1. Clone the repository:
```bash
git clone git@github.com:abojotemi/stenography.git
cd stenography
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or using uv:
```bash
uv sync
```

## 🏃‍♂️ Running Locally

```bash
streamlit run main.py
```

The application will be available at `http://localhost:8501`

## 📝 Usage

1. **Encoding a Message**:
    - Upload an image file
    - Upload your secret image file
    - Download the encoded image

2. **Decoding a Message**:
    - Upload a steganographic image
    - Extract and view the hidden image

## 🔧 Project Structure

```
encoder/
├── main.py              # Main Streamlit application
├── encode.py     # Steganography logic
├── README.md           # Project documentation
├── pyproject.toml      # Project configuration
├── uv.lock            # Dependency lock file
└── requirements.txt    # Python dependencies
```
## 📄 License

This project is open source and available under the [MIT License](LICENSE).