\# BlogNest 📝



BlogNest is a Django-based blog web application that allows users to create, read, edit, and delete blog posts with secure user authentication.



\## Features



\- User registration

\- User login and logout

\- User authentication

\- Create blog posts

\- View individual posts

\- Edit your own posts

\- Delete your own posts

\- Blog post categories

\- Author and publication date

\- Responsive web interface

\- Django admin panel



\## Technologies Used



\- Python

\- Django

\- HTML5

\- CSS3

\- SQLite

\- Git \& GitHub



\## Project Structure



```text

BlogNest/

│

├── blog/

│   ├── migrations/

│   ├── templates/

│   │   └── blog/

│   │       ├── create\_post.html

│   │       ├── delete\_post.html

│   │       ├── edit\_post.html

│   │       ├── home.html

│   │       ├── login.html

│   │       ├── post\_detail.html

│   │       └── register.html

│   ├── admin.py

│   ├── models.py

│   ├── views.py

│   └── tests.py

│

├── config/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── manage.py

├── .gitignore

└── README.md

```



\## How to Run



\### 1. Clone the repository



```bash

git clone https://github.com/jasleen-data/BlogNest.git

cd BlogNest

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



Activate it on Windows:



```bash

venv\\Scripts\\activate

```



\### 3. Install Django



```bash

pip install django

```



\### 4. Apply database migrations



```bash

python manage.py migrate

```



\### 5. Start the development server



```bash

python manage.py runserver

```



Open:



```text

http://127.0.0.1:8000/

```



\## User Workflow



1\. Create an account.

2\. Log in.

3\. Create a blog post.

4\. View the published post.

5\. Edit or delete your own posts.

6\. Log out.



\## Authentication



BlogNest uses Django's built-in authentication system for registration, login, logout, session management, and restricting post management to authenticated users.



\## Purpose



This project demonstrates core Django concepts including models, views, templates, URL routing, authentication, database operations, and CRUD functionality.



\## Author



\*\*Jasleen Kaur\*\*



GitHub: https://github.com/jasleen-data

