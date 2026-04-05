# 🤖 Smart Number Guessing AI

This is a Python-based project where the computer intelligently guesses the number you are thinking of using a smart search strategy.

---

## 🧠 How It Works

* You think of a number within a given range (default: 1 to 100)
* The computer makes a guess
* You give feedback:

  * `h` → Guess is too high
  * `l` → Guess is too low
  * `c` → Guess is correct
* Based on your response, the program narrows down the range and makes a better guess

👉 This approach is based on the **Binary Search Algorithm**, which is a fundamental concept in computer science and AI problem-solving.

---

## 🎯 Features

* Intelligent guessing using binary search
* Fast and optimized (guesses in very few attempts)
* Input validation for user responses
* Detects inconsistent inputs
* Displays total number of attempts

---

## 🖥️ Example

```bash
Think of a number between 1 and 100

Is your number 50?
(h/l/c): l

Is your number 75?
(h/l/c): h

Is your number 62?
(h/l/c): c

🎉 Yay! I guessed your number!
Guessed in 3 attempts
```

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/smart-calculator.git
```

2. Navigate to the project folder:

```bash
cd smart-calculator
```

3. Run the program:

```bash
python your_file_name.py
```

---

## 📚 What I Learned

* Binary Search Algorithm
* Problem-solving using logic and optimization
* Handling user input and validation
* Writing clean and structured Python code

---

## 🔮 Future Improvements

* Allow custom range input (user-defined min & max)
* Add GUI version (using Tkinter or web interface)
* Add voice interaction (advanced)

---


## ⭐ If you like this project

Give it a star on GitHub ⭐
