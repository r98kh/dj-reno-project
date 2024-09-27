
# DJ Reno Project

## Description
The DJ Reno Project is a Django-based web application designed for online shopping and product management. It integrates various modules that provide functionality such as product catalog management, user authentication, blog handling, shopping cart management, and more. This project serves as a foundation for building e-commerce websites.

## Modules
- **Product Module:** Manages product listings, categories, and details.
- **User Module:** Handles user registration, login, profile management, and authentication.
- **Cart Module:** Manages the shopping cart, allowing users to add, remove, and view items in their cart.
- **Comment Module:** Allows users to post and view comments on products and blog posts.
- **Blog Module:** Handles blog creation and management.
- **Contact Us Module:** Provides a form for users to contact the site administrators.
- **About Us Module:** Displays information about the company or website.
- **Admin Interface:** Django's built-in admin panel for managing the site's content.


## Technologies Used
- **Django**: As the web framework.
- **SQLite**: For the database.
- **HTML/CSS**: For frontend design.
- **JavaScript**: For interactive elements and dynamic content.
- **Python**: Backend logic.
  
## Installation

### Prerequisites
- Python 3.x
- Django 4.x

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/r98kh/dj-reno-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd dj-reno-project
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open the application by visiting `http://127.0.0.1:8000` in your browser.

## Usage
- **Admin Panel**: Navigate to `http://127.0.0.1:8000/admin` and log in with your admin credentials to manage site content.
- **Product Pages**: Products can be added and viewed through the admin interface, and customers can browse them on the main site.
- **Shopping Cart**: Users can add items to their cart, view the cart, and proceed to checkout.
- **User Management**: Users can register, log in, and manage their profiles.

## Contributing
Feel free to fork the repository and submit pull requests. Please make sure your code adheres to the style guide and includes relevant tests.

## License
This project is licensed under the MIT License.

## Contact
For any issues or feature requests, please create an issue in the GitHub repository or contact the developer at [rasool.khorshidi1998@gmail.com].
