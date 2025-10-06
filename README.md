# Phoenix_2025_nasa

  TerraQuest

TerraQuest is a hybrid scientific–artistic platform that transforms 25 years of NASA Terra satellite data into an interactive, data-driven, and animated storytelling experience.
It bridges the gap between data science and human experience, turning raw environmental observations into tools for understanding, empathy, and action.

---
 Features

* Interactive Web Platform
  Built with HTML, CSS, JavaScript, designed for an intuitive and cinematic interface.

* Temporal Visualization of Terra Data

  * Over 9,000 Terra datasets processed.
  * Representative days: [15, 46, 74, 105, 135, 166, 196, 227, 258, 288, 319, 349].
  * Converted into aligned PNG map frames using Python.

* GIF & Timeline Animation

  * Flask backend (`asdfg.py`) generates GIFs for any year range.
  * JavaScript timeline controller enables smooth navigation through years.

* AI Chatbot Assistant

  * Backend (`chatbot.py`) powered by OpenAI.
  * Provides answers about Terra, its instruments, and environmental science.

* Machine Learning Classifier

  * (`app.py`) loads a trained rainfall classification model.
  * Flask interface for interactive predictions.

* AI Video Generation

  * (`2.py`) integrates Diffusion models (Zeroscope) for generating cinematic videos.
  * Converts user prompts into short analytical or narrative clips.

* Artistic Layer

  * Creative film with AI tools (Sora, Hailuo AI, ChatGPT).
  * Story of a water droplet witnessing drought and learning how satellite data protects Earth.

---

Tech Stack

* Frontend: HTML, CSS, JavaScript
* Backend: Flask (Python)
* Data Processing: Python, Pillow, NumPy, Pandas
* ML Model: Scikit-learn / XGBoost (rainfall classifier)
* AI APIs: OpenAI GPT, Diffusers (Hugging Face)
* Visualization: GIF generation, interactive timeline
* Deployment: Local Flask apps (modular structure)

---

📂 Project Structure
├── 1.png                          # Example/sample image  
├── asdfg.py                       # Flask app for assembling PNG frames into GIF timelapses  
├── chatbot.py                     # Flask app for chatbot (OpenAI API integration)  
├── Untitled-1 (2).html            # Main HTML front-end (can be renamed to index.html)  
├── frames/                        # Processed PNG frames (aligned Terra satellite maps)  
├── Video_Generator_Model/         # AI video generator (Diffusion models + UI)  
│   ├── Video_Generator_Model.py   # Flask app for AI video generation  
│   ├── templates/                 # Front-end templates for video generator  
│   └── static/                    # Static assets (CSS, JS, images)  
├── app/                           # Rainfall prediction web app  
│   ├── templates/                 # Front-end templates for rainfall prediction  
│   ├── static/                    # Static assets (CSS, JS)  
│   └── app.py                     # Flask app for rainfall prediction (ML model)  
└── README.md                      # Project documentation  


  Usage
 1. Clone repository

git clone https://github.com/yourusername/TerraQuest.git
cd TerraQuest

 2. Install dependencies

pip install -r requirements.txt

 3. Run individual modules

* GIF Generator

    python asdfg.py
  

  Open browser at http://127.0.0.1:5055/make_gif?start=2000&end=2005&fps=6

* Chatbot

    python chatbot.py
  

  POST to /ask with JSON: {"question": "What is Terra?"}

* Rainfall Classifier

    python app.py
  

  Web form for interactive prediction at http://127.0.0.1:5055

* AI Video Generator

    python 2.py
  

  Enter a prompt → generates video in static/videos/output.mp4.

---
 Example Workflow

1. Explore historical Terra data through the interactive timeline.
2. Generate GIF animations of rainfall/temperature trends.
3. Use the chatbot to ask scientific questions.
4. Run the classifier to analyze rainfall conditions.
5. Create narrative videos to combine science with storytelling.

---

 Scalability

* Current demo focuses on one region.
* Framework is fully scalable to global datasets.
* Future expansion: education, citizen science, and environmental policy tools.

---
 Acknowledgements

* NASA Terra Mission (MODIS, ASTER, MISR, MOPITT, CERES instruments)
* OpenAI (ChatGPT, Sora)
* Hailuo AI
* Hugging Face Diffusers (Zeroscope)

---

---
 Film

> TerraQuest includes a short AI-animated film where a water droplet learns about 
Earth’s changing climate, making science emotional and accessible.
>
https://drive.google.com/file/d/1puFOI74vEI66FFQNcvtSVMrPUSGCxQqC/view?usp=drive_link
