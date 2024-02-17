# WeSellClothes

WeSellClothes is a mock e-commerce store developed using Django. The project simulates an online clothing store where users can browse, select, and "purchase" clothing items. It includes features such as adding items to a shopping cart, selecting sizes, 
and completing the "purchase" process, sending email confirmations and verifications.

## Website

https://wesellclothes.herokuapp.com/

Presentation video: https://youtu.be/EGxmlptydVE

## Features

- **User Authentication**: Users can sign up, log in, and log out of their accounts.
- **Email Verification and Confirmation**: Account registration includes email verification to ensure the validity of user accounts.
- **Product Listings**: The app displays a catalog of clothing items available for purchase.
- **Shopping Cart**: Users can add items to their shopping cart and view the items before "purchasing."
- **Customization**: Users can select sizes and colors for clothing items before adding them to their cart.
- **Checkout Process**: Simulates the checkout process where users can review their order and complete the "purchase" (no real transactions involved).
- **Responsive Design**: Developed using Django's built-in templates and CSS for a responsive design that works across various devices.

## Tech Stack

- **Framework**: Django
- **Database**: Django ORM with SQLite (can be easily swapped with other databases supported by Django, such as PostgreSQL or MySQL)
- **Frontend**: HTML, CSS (with Django's template engine)
- **Email Verification**: Django's built-in email verification features or third-party libraries such as Django-allauth or Django-registration
