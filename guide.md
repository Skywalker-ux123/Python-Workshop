# 📖 The Python Pipeline: Step-by-Step Guide

Welcome to the companion guide! If you attended the presentation, you know that Python is basically a superpower that lets you automate the web, analyze data, run AI, and build web servers.

Below is the documentation for each mini-project in this repository. Follow the steps to fill in the blanks (`TODO`s) and get your code working!

---

### **Act I: The Book Scraper**

**Goal:** Write a script that secretly reads a bookstore website and extracts the titles and prices of every book on the page.

**Step-by-Step:**

1. **Find the Container:** The template already downloads the website and finds all the "book" containers for you using `soup.find_all("article", class_="product_pod")`.
2. **Extract the Title:** Look closely at the HTML structure of the website. The title is hidden inside an `<h3>` tag, inside an `<a>` (link) tag, under the attribute `title`.
* *Replace the first TODO with:* `title = book.h3.a["title"]`


3. **Extract the Price:** The price is inside a `<p>` (paragraph) tag that has a specific CSS class called `price_color`.
* *Replace the second TODO with:* `price = book.find("p", class_="price_color").text`


4. **Run it:** Type `python 01_scraping_template.py` in your terminal and watch the data pour in!

---

### **Act I (Part B): The Automation Robot**

**Goal:** Take over a Google Chrome browser, navigate to Fast.com, wait for the test to finish, and print your internet speed.

**Step-by-Step:**

1. **Navigate the Web:** Tell the Selenium webdriver to go to the specific URL.
* *Replace the first TODO with:* `driver.get("https://fast.com")`


2. **Wait for the Result:** Fast.com takes a few seconds to run. We need to wait until the final speed pops up. If you inspect the website, the speed number is inside an element with the ID `speed-value`. When it finishes, it gains the class `succeeded`.
* *Replace the second TODO with:* `"#speed-value.succeeded"`


3. **Run it:** Type `python 02_automation_template.py` and take your hands off the keyboard. Watch the ghost in the machine take over!

---

### **Act II: The Data Analyst**

**Goal:** Take a raw dataset of student grades, calculate the classroom average using pandas, and graph it using Matplotlib.

**Step-by-Step:**

1. **Calculate the Average:** We need to access the `Math_Score` column in our DataFrame and find the mean (average).
* *Replace the first TODO with:* `df["Math_Score"].mean()`


2. **Plot the Chart:** A bar chart needs an X-axis (the names) and a Y-axis (the scores).
* *Replace the second TODO with:* `plt.bar(df["Name"], df["Math_Score"], color='skyblue')`


3. **Run it:** Type `python 03_data_template.py` and a clean, visual graph will pop up on your screen.

---

### **Act III: The AI Vision System**

**Goal:** Load an industry-standard neural network (YOLOv8) and hook it up to your webcam to detect objects in real-time.

**Step-by-Step:**

1. **Load the Brain:** We need to tell the `YOLO` library which pre-trained model to use. We are using the "nano" version because it is incredibly fast.
* *Replace the first TODO with:* `YOLO("yolov8n.pt")`


2. **Feed the AI:** Inside the `while` loop, your webcam is capturing frames. We need to hand that `frame` over to our model so it can do the math.
* *Replace the second TODO with:* `model(frame, stream=True)`


3. **Draw the Boxes:** The model returns results. We need to tell it to plot those results (draw the bounding boxes) onto our video frame.
* *Replace the third TODO with:* `result.plot()`


4. **Run it:** Type `python 04_vision_template.py`. Hold up your phone, a cup, or a book to the camera!

---

### **Act IV: The Web Server (Vibe Court)**

**Goal:** Turn your Python code into a real web server that judges a user's inputs based on custom logic.

**Step-by-Step:**

1. **Build the Homepage:** When someone visits your server, they need to see something. Let's return a simple HTML string.
* *Replace the first TODO with:* `"<h1 style='font-family: sans-serif;'>⚖️ Welcome to Vibe Court API</h1>"`


2. **Build the Logic (Good Vibes):** If the user types "pizza" or "sleep", we want to return a good verdict.
* *Replace the second TODO with:* `"NOT GUILTY"`


3. **Build the Logic (Bad Vibes):** If the user types "homework" or "traffic", we want to roast them.
* *Replace the third TODO with:* `"GUILTY"`


4. **Run it:** Type `python 05_flask_template.py`. Open your web browser and go to `http://127.0.0.1:5000/judge/pizza` to see your API in action!