````markdown
# 🌐 Personal Portfolio Website

A personal portfolio built with **Django** and deployed on **Render**, showcasing my projects, resume, and journey as a developer.  
This portfolio highlights my skills in web development and provides an easy way to connect with me.

---

## 🚀 Features
- 🖼️ Responsive and modern UI  
- 📂 Projects showcase with descriptions  
- 📄 Downloadable resume  
- 📧 Contact section  
- 🎨 Static assets (CSS, JS, Images) managed via **Whitenoise**  
- 🌍 Live deployment on [Render](https://shreya-portfolio-62wx.onrender.com/)  

---

## ⚙️ Tech Stack
- **Backend:** Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (default for demo, can be swapped)  
- **Deployment:** Render  
- **Static Files:** Whitenoise  

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shreyasaraf01/shreya-portfolio.git
   cd shreya-portfolio
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Collect static files**

   ```bash
   python manage.py collectstatic --noinput
   ```

6. **Run the server locally**

   ```bash
   python manage.py runserver
   ```

---

## 📬 Contact

* **LinkedIn:** [Shreya Saraf](https://www.linkedin.com/in/shreya-saraf-797440257)
* **Email:** [shreyasaraf765@gmail.com](mailto:shreyasaraf765@gmail.com)

---

⭐ If you found this project interesting, feel free to fork, star, and connect!
