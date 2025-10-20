# 🍽️ Django QR Code Generator

A simple Django web application that generates a **QR code** for restaurant menus or other use cases.  
Users can enter the restaurant name and select a QR color, then download or view the generated QR code.

---

## 🚀 Features
- Generate custom QR codes for restaurant menus  
- Choose QR color dynamically using a color picker  
- Automatically save generated QR codes in the `/media` folder  
- Clean and simple UI  
- Download and view generated QR codes instantly  

---
## Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **QR Code Generation:** `qrcode` Python library  
- **Image Processing:** Pillow (PIL)  
- **Database:** SQLite (default Django DB)  
- **Version Control:** Git & GitHub  

---


## 🏗️ Project Structure
myproject/
│
├── manage.py
├── db.sqlite3
│
├── myproject/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── views.py
│ ├── forms.py
│ ├── asgi.py
│ └── wsgi.py
│
├── templates/
│ ├── generate_qr_code.html
│ └── qr_result.html
│
├── media/
│ └── demo_restaurant_menu.png
│
