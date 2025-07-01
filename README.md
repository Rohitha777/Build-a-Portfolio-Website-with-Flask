Build a Portfolio Website with Flask
#  Portfolio Website (Flask)

This is a personal portfolio website built using **Flask**, **HTML/CSS**, and **Flask-Mail**. It showcases my academic background, technical skills, projects, certifications, and includes a working contact form that dynamically sends emails to any recipient

---

## 🌐 Live Features

- Clean and professional landing page with profile image
- Sections: About Me, Skills, Projects, Certifications, Hobbies
- Responsive contact form that:
  - Sends a confirmation email to the user
  - Sends the message to the specified recipient
  - Optionally notifies the site owner (me!)
- Styled with custom CSS for a modern and friendly look

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Flask-Mail  
- **Frontend**: HTML5, CSS3  
- **Templating**: Jinja2  
- **Email Service**: Gmail SMTP (via app password)

- **🔧 How It Works**
Visitors can view information about me and my work
On the Contact page, users can fill out a form
An email is sent to:
The recipient entered in the form
Me (for my records)
After sending, users are redirected to a Thank You page


## 📁 Project Structure
project/
│
├── app.py # Main Flask app
├── templates/
│ ├── index.html # Home page
│ ├── contact.html # Contact form
│ └── thankyou.html # Success page
├── static/
│ ├── style.css # Stylesheet
│ └── profile.jpg # Profile picture
└── README.md # This file

**🚀 How to Run**
**.Install Dependencies**
pip install flask flask-mail

**Configure Email (in app.py)**
Update these values with your own Gmail app password:
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'
🔐 Note: Use an App Password if 2-step verification is enabled.

**Run the App**
Then open http://localhost:5000 in your browser.



