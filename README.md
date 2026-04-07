# AI Student Drop-off Predictor

**AI-powered dashboard to predict student drop-off and improve retention in edtech platforms.**

---

## 📌 Overview

This project is an interactive **Streamlit app** that predicts whether a student is likely to stay active or drop off using a machine learning model. The app provides **confidence scores, actionable insights, and engagement analytics** to help improve student retention.

---

## 🚀 Features

- **Prediction with Confidence Score** – Know the model’s certainty.  
- **Interactive Inputs** – Adjust sessions, time spent, last active days, and quiz score.  
- **Student Summary** – Quick overview of student activity.  
- **Engagement Trends** – Line chart showing sessions attended vs. average time spent.  
- **Drop-off Distribution** – Bar chart of active vs. inactive students.  
- **Key Insights & Suggestions** – Recommendations to improve engagement.  

---

## 💻 Tech Stack

- Python  
- Streamlit  
- Pandas & NumPy  
- Scikit-learn (ML model)  
- Pickle (save/load trained model)  

---

## 🏗 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/itsmeshalu-24/Student-dashboard.git
cd Student-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```


Open in browser: http://localhost:8501

## 📁 File Structure


├─ app.py # Streamlit app
├─ model.py # ML model training script
├─ model.pkl # Trained model
├─ students.csv # Dataset for charts & trends
├─ requirements.txt # Required Python packages
└─ README.md # Project documentation


---

## 🧠 Key Insights

- Students with more sessions are less likely to drop off.  
- High inactivity increases the risk of dropout.  
- Better quiz scores improve retention.  
- Provides actionable suggestions for engagement improvement.  

---

## 🌟 Next Steps

- Deploy on **Streamlit Community Cloud** for live access.  
- Add **risk meter and color indicators** for premium UX.  
- Integrate more **interactive dashboards and analytics**.  

---

## ✅ Usage Tips

- Click **Predict** to get the latest output.  
- Refresh the app after any code update.  
- Retrain the model if the dataset changes.  

---

## 🎯 Outcome

- **AI usage & predictive analytics** ✅  
- **Product thinking & business insights** ✅  
- **Interactive, real-world dashboard** ✅
