# Guide to Generate a PDF CV in a Specific Language

This guide explains how to generate my CV in PDF format from a Python script and a LaTeX template, in the language of your choice.

---

## 1. Prerequisites

Make sure you have the following installed:

- **Python 3**
- Required Python libraries:
```bash
    pip install deep-translator
```
- To compile LaTeX into PDF :
```bash
    # macOS
    brew install --cask mactex

    # Ubuntu
    sudo apt-get install texlive-full
```
- Compile the PDF : 
```bash
    pdflatex name_cv.tex
```


## 2. Project Structure

.
├── README.md
├── cv_English/
├── cv_Français/
└── cv_translation

## 3. Contributing

Feel free to fork this repository, suggest improvements, or submit pull requests. Feedback is always welcome!

## 4. Thanks & Credits

A big thank you to:

- TeX Live / MacTeX team for providing excellent LaTeX distributions.

- Deep-Translator developers for easy translation APIs.

- The authors of ModernCV / Awesome-CV templates for inspiring professional CV designs.