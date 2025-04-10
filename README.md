# BlockTrust 🔗

A **Blockchain-Based Trust Simulation using Game Theory**  
This project simulates trust and reputation evolution in a decentralized blockchain network. Nodes behave either honestly or dishonestly over several rounds, and their actions affect their trust scores, reputations, and penalties. The system models game-theoretical behavior to study how cooperation or defection plays out in decentralized systems.

---

## 🚀 Features

- 🎮 Game Theory-Based Trust Model
- 📊 Animated Charts for Node Trust & Reputation
- ⏳ Live Progress Bar for Simulation
- 📅 Downloadable Results as CSV
- 💻 Interactive UI using HTML, CSS, JavaScript
- 🧠 Backend Logic with Python

---

## 💠 Technologies Used

| Component     | Tech Stack                     |
|---------------|-------------------------------|
| Frontend      | HTML, CSS, JavaScript         |
| Backend       | Python                        |
| Visualization | Chart.js                      |
| Server Comm   | Flask (for backend API calls) |
| CSV Export    | FileSaver.js                  |

---

## 🤩 Project Structure

```
TrustChain/
│
├── backend/
│   └── blockchain_simulation.py      # Core simulation logic (Python)
│
├── frontend/
│   ├── index.html                    # Main UI
│   ├── style.css                     # Stylesheet
│   ├── script.js                     # JS logic for UI interaction
│   ├── chart.js                      # Animated trust charts
│   └── FileSaver.min.js              # For CSV export
│
├── results/
│   └── simulation.csv                # Output data
│
└── README.md                         # This file
```

---

## 🧪 How to Run

### Backend (Python)

```bash
cd backend
python blockchain_simulation.py
```

> Or if using Flask:
```bash
flask run
```

### Frontend (Open UI)

Open `index.html` in your browser. Or run a simple server:

```bash
cd frontend
python -m http.server
# Then open http://localhost:8000
```

---

## 📅 Output

- Real-time node status:
  - Action (Honest/Dishonest)
  - Trust Score
  - Reputation
  - Penalty
- Chart Visualization of Trust Evolution
- Option to Download Results as CSV

---

