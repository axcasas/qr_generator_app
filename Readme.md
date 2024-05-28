# Free QR Image Generator App

About This Project
==

Most of the websites to generate QR images requires you to create a new account or to pay for a QR image.  

Those that are "free" only allow users to create a single QR image or last a certain period of time.

This project aims to provide a simple and free QR code generation tool accessible through a user-friendly web interface. 

With this app, users can create QR codes for various purposes, such as sharing URLs, contact information, or product details. 

## Objectives

- Develop an easy and free user interface to create QR images.
- To create an app with customization options.
- To create a GUI that allows users to create as many QR images as they want.

## About This Repository

```
└── gui
|   ├── layout.py <- app's layout
|   ├── sidebar.py <- app's sidebar
└── qr_generator
|   ├── main.py <- create_qr_code function
├── README.md
├── app.py <- Streamlit app 
├── .gitignore 
├── requirements.txt 
```

Requirements 
===

Python version > 3.10

- qrcode==7.4.2
- streamlit==1.29.0
- pillow==9.5.0

Run the app 
===
```
streamlit run app.py
```