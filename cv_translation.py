from deep_translator import GoogleTranslator
import subprocess


cv_data = {
    "role_title": "Master of Science in Computer Science",
    "degree_program": "Diplôme d'Ingénieur program - Expected in 2027",
    
    "section_profile": "Profile",
    "profile_text": """Versatile and results-oriented Engineering student 
specializing in Computer Science and Electronics. Proficient in cross-functional 
problem-solving and full lifecycle project development, with proven experience in 
integrating disparate technologies to deliver robust, scalable solutions. Seeking 
to apply skills in system architecture design and performance optimization to help 
companies tackle complex challenges and contribute to innovative projects.""",
    
    "section_education": "Education",
    "edu_1_degree": "Diplôme d'Ingénieur (Master's Degree equiv.)",
    "edu_1_desc": "Specializing in Electronics, Computer Science, and Telecommunications.",
    "edu_1_date": "Sept 2022 -- July 2027 (Expected)",
    "edu_2_degree": "Exchange Semester",
    "edu_2_desc": "Technological Engineering coursework conducted entirely in English.",
    "edu_2_date": "Feb 2024 -- July 2024",

    "section_skills": "Technical Skills",
    "cat_ai": "AI & Machine Learning",
    "cat_embedded": "Embedded & Electronics",
    "cat_software": "Software Development",
    "cat_web": "Web & Cloud",
    "cat_network": "Networking & Cybersecurity",
    "cat_soft": "Soft Skills",
    "val_soft": "Ownership & Proactivity, Communication, Teamwork, Problem-solving, Adaptability",
    "cat_lang": "Languages",
    "val_lang": "French (Native), English (C1 - Full Professional Proficiency), Spanish (B1 - Intermediate)",

    "section_exp": "Professional Experience",
    
    "exp_1_role": "AI & Embedded Systems Intern",
    "exp_1_org": "SGA - Ministry of Defence",
    "exp_1_date": "Sept 2025 -- Present",
    "exp_1_desc1": "Designing and developing an innovative device for defense applications, integrating embedded Artificial Intelligence on a dedicated hardware card.",
    "exp_1_desc2": "Responsible for the full project lifecycle, from hardware/software architecture design to AI model selection and optimization for embedded constraints.",
    "exp_1_desc3": "Implementing robust connectivity solutions with a focus on data security and confidentiality.",

    "exp_2_role": "Founder & Operator (Self-Employed)",
    "exp_2_org": "CleanGenius",
    "exp_2_date": "Oct 2024 -- Present",
    "exp_2_desc1": "Launched and manage a cleaning service company for private and public sector clients.",
    "exp_2_desc2": "Oversee all business operations, including client acquisition, service delivery, and administrative management, demonstrating strong organizational and entrepreneurial skills.",

    "exp_3_role": "Train Commercial Service Agent (ASCT)",
    "exp_3_org": "SNCF Voyageurs",
    "exp_3_date": "Summer 2023",
    "exp_3_desc1": "Ensured the safety, security, and service quality for thousands of passengers on regional trains (TER), holding a sworn officer status from the Angers Judicial Court.",
    "exp_3_desc2": "Completed a rigorous 1.5-month certification in safety protocols, security procedures, equipment management, and commercial operations.",

    "section_lead": "Leadership & Volunteering",
    "lead_1_title": "Member, Student Union (BDE) & Sports Office",
    "lead_1_desc": "Co-organize student life events and support school-wide initiatives.",
    "lead_2_title": "Member, Unit Against Harassment & Violence",
    "lead_2_desc": "Provide confidential support to students and contribute to prevention campaigns.",

    "section_awards": "Awards & Certifications",
    "award_1": "1st Prize Winner, Public Speaking Competition",
    "award_2": "Certified in Project Management",
    "award_3": "Aeronautical Initiation Certificate"
}

latex_template = r"""
\documentclass[letterpaper,11pt]{{article}}
\usepackage{{latexsym}}
\usepackage[empty]{{fullpage}}
\usepackage{{titlesec}}
\usepackage{{marvosym}}
\usepackage[usenames,dvipsnames]{{color}}
\usepackage{{verbatim}}
\usepackage{{enumitem}}
\usepackage[hidelinks]{{hyperref}}
\usepackage{{fancyhdr}}
\usepackage[english]{{babel}}
\usepackage{{tabularx}}
\input{{glyphtounicode}}

\pagestyle{{fancy}}
\fancyhf{{}} 
\fancyfoot{{}}
\renewcommand{{\headrulewidth}}{{0pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\addtolength{{\oddsidemargin}}{{-0.5in}}
\addtolength{{\evensidemargin}}{{-0.5in}}
\addtolength{{\textwidth}}{{1in}}
\addtolength{{\topmargin}}{{-.5in}}
\addtolength{{\textheight}}{{1.0in}}
\urlstyle{{same}}
\raggedbottom
\raggedright
\setlength{{\tabcolsep}}{{0in}}

\titleformat{{\section}}{{
  \vspace{{-4pt}}\scshape\raggedright\large
}}{{}}{{0em}}{{}}[\color{{black}}\titlerule \vspace{{-5pt}}]

\newcommand{{\resumeItem}}[1]{{
  \item\small{{
    {{#1 \vspace{{-2pt}}}}
  }}
}}

\newcommand{{\resumeSubheading}}[4]{{
  \vspace{{-2pt}}\item
    \begin{tabular*}{{0.97\textwidth}}[t]{{l@{{\extracolsep{{\fill}}}}r}}
      \textbf{{#1}} & #2 \\
      \textit{{\small#3}} & \textit{{\small #4}} \\
    \end{tabular*}\vspace{{-7pt}}
}}

\newcommand{{\resumeProjectHeading}}[2]{{
    \item
    \begin{tabular*}{{0.97\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
      \small#1 & #2 \\
    \end{tabular*}\vspace{{-7pt}}
}}

\newcommand{{\resumeSubHeadingListStart}}{{\begin{{itemize}}[leftmargin=0.15in, 
label={{}}]}}
\newcommand{{\resumeSubHeadingListEnd}}{{\end{{itemize}}}}
\newcommand{{\resumeItemListStart}}{{\begin{{itemize}}}}
\newcommand{{\resumeItemListEnd}}{{\end{{itemize}}\vspace{{-5pt}}}}

\begin{{document}}

\begin{{center}}
    \textbf{{\Huge \scshape Louis BAFFOUR}} \\ \vspace{{3pt}}
    \textbf{{\large {role_title}}} \\ \vspace{{1pt}}
    \small {degree_program} \\ \vspace{{5pt}}
    \small
    
\href{{mailto:Louis.baffour@reseau.eseo.fr}}{{\underline{{Louis.baffour@reseau.eseo.fr}}}} 
$|$ 
    
\href{{https://linkedin.com/in/louis-baffour}}{{\underline{{linkedin.com/in/louis-baffour}}}} 
$|$
    \href{{https://github.com/SlashFR1}}{{\underline{{github.com/SlashFR1}}}} $|$
    +33 7 66 44 00 89
\end{{center}}

\section{{{section_profile}}}
\small{{
{profile_text}
}}
\vspace{{5pt}}

\section{{{section_education}}}
  \resumeSubHeadingListStart
    \resumeSubheading
      {{ESEO | {edu_1_degree}}}{{Angers, France}}
      {{{edu_1_desc}}}{{{edu_1_date}}}
    \resumeSubheading
      {{KU Leuven | {edu_2_degree}}}{{Leuven, Belgium}}
      {{{edu_2_desc}}}{{{edu_2_date}}}
  \resumeSubHeadingListEnd

\section{{{section_skills}}}
 \begin{{itemize}}[leftmargin=0.15in, label={{}}]
    \small{{\item{{
     \textbf{{{cat_ai}}}}{{: TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy}} \\
     \textbf{{{cat_embedded}}}}{{: C, C++, VHDL, STM32, ARM Cortex-M, RISC-V, 
FPGA, LTspice}} \\
     \textbf{{{cat_software}}}}{{: Python, Java, JavaScript, SQL, Bash, Git}} \\
     \textbf{{{cat_web}}}}{{: React, Node.js, HTML/CSS, MySQL, Docker, Microsoft 
Azure}} \\
     \textbf{{{cat_network}}}}{{: Wireshark (Packet Analysis), TCP/IP Suite 
(HTTP/S, DNS, TCP/UDP)}} \\
     \textbf{{{cat_soft}}}}{{: {val_soft}}} \\
     \textbf{{{cat_lang}}}}{{: {val_lang}}}
    }}}}
 \end{{itemize}}

\section{{{section_exp}}}
  \resumeSubHeadingListStart

    \resumeSubheading
      {{{exp_1_role}}}{{Paris, France}}
      {{{exp_1_org}}}{{{exp_1_date}}}
      \resumeItemListStart
        \resumeItem{{{exp_1_desc1}}}
        \resumeItem{{{exp_1_desc2}}}
        \resumeItem{{{exp_1_desc3}}}
      \resumeItemListEnd

    \resumeSubheading
      {{{exp_2_role}}}{{Angers, France}}
      {{{exp_2_org}}}{{{exp_2_date}}}
      \resumeItemListStart
        \resumeItem{{{exp_2_desc1}}}
        \resumeItem{{{exp_2_desc2}}}
      \resumeItemListEnd

    \resumeSubheading
      {{{exp_3_role}}}{{Nantes, France}}
      {{{exp_3_org}}}{{{exp_3_date}}}
      \resumeItemListStart
        \resumeItem{{{exp_3_desc1}}}
        \resumeItem{{{exp_3_desc2}}}
      \resumeItemListEnd

  \resumeSubHeadingListEnd

\section{{{section_lead}}}
  \resumeSubHeadingListStart
    \resumeProjectHeading
        {{\textbf{{{lead_1_title}}} $|$ \emph{{ESEO}}}}{{2024 -- Present}}
        \resumeItemListStart
          \resumeItem{{{lead_1_desc}}}
        \resumeItemListEnd
    \resumeProjectHeading
        {{\textbf{{{lead_2_title}}} $|$ \emph{{ESEO}}}}{{2024 -- Present}}
        \resumeItemListStart
          \resumeItem{{{lead_2_desc}}}
        \resumeItemListEnd
  \resumeSubHeadingListEnd

\section{{{section_awards}}}
  \resumeSubHeadingListStart
    \resumeProjectHeading
        {{\textbf{{{award_1}}} $|$ \emph{{ESEO}}}}{{Jan 2025}}
    \resumeProjectHeading
        {{\textbf{{{award_2}}} $|$ \emph{{MOOC Gestion de Projet}}}}{{Feb 2023}}
    \resumeProjectHeading
        {{\textbf{{{award_3}}} $|$ \emph{{Brevet d'Initiation 
Aéronautique}}}}{{Jun 2021}}
  \resumeSubHeadingListEnd

\end{{document}}
"""

def fill_template(template, data):
    """Remplacer manuellement les clés pour éviter les conflits avec LaTeX"""
    text = template
    for key, value in data.items():
        # On remplace {clé} par la valeur
        text = text.replace("{" + key + "}", str(value))
    return text

def generate_translated_cv(target_lang='fr'):
    print(f" Translating to: {target_lang} ...")
    
    translated_data = {}
    translator = GoogleTranslator(source='auto', target=target_lang)

    # Traduction de chaque champ
    for key, text in cv_data.items():
        try:
            if not text or len(text) < 2:
                translated_data[key] = text
            else:
                translated_data[key] = translator.translate(text)
        except Exception as e:
            print(f"Translation error on {key}: {e}")
            translated_data[key] = text

    # Génération du LaTeX traduit
    final_latex = fill_template(latex_template, translated_data)
    
    filename = f"cv_louis_baffour_{target_lang}.tex"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_latex)
    
    print(f" File generated successfully: {filename}")
    
    # Important : on retourne le texte pour la compilation PDF
    return final_latex

if __name__ == "__main__":
    langue = input("Which language? (fr = French, es = Spanish, de = German, en = English): ").strip()
    
    final_latex = ""

    if langue == 'en':
        # En anglais, pas besoin de traduction
        final_latex = fill_template(latex_template, cv_data)
        with open("cv_louis_baffour_en.tex", "w", encoding="utf-8") as f:
            f.write(final_latex)
        print(" English file generated.")
    else:
        # Autres langues : traduction
        final_latex = generate_translated_cv(langue)
        
    # Écriture du fichier temporaire pour compilation
    if final_latex:
        with open("cv.tex", "w", encoding="utf-8") as f:
            f.write(final_latex)

        print(" Compiling PDF...")
        try:
            # Compilation deux fois pour les références si nécessaire (optionnel)
            subprocess.run(["pdflatex", "-interaction=nonstopmode", "cv.tex"], check=True)
            print(" PDF Compiled successfully (cv.pdf)")
        except subprocess.CalledProcessError:
            print(" Error during PDF compilation. Check cv.log.")
    else:
        print(" Error: No LaTeX content generated.")
