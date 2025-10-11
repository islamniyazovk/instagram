# Instagram Clone

A full-stack Instagram clone built to simulate the core functionalities of Instagram. This project allows users to register, login, upload photos, follow other users, like and comment on posts, and explore a feed of posts from followed users.

## Features

* User authentication (Sign up / Login / Logout)
* User profiles with editable information and profile pictures
* Follow/unfollow other users
* Post images with captions
* Like and comment on posts
* Explore feed showing posts from followed users
* Search for users by username
* Responsive design for mobile and desktop

## Tech Stack

**Frontend:**

* React / Vue / Angular (уточни, какой именно используешь)
* Tailwind CSS / Bootstrap / Material UI

**Backend:**

* Python + FastAPI / Django / Node.js + Express
* REST API / GraphQL API

**Database:**

* PostgreSQL / MySQL / SQLite
* SQLAlchemy / Django ORM / Prisma

**Storage:**

* Local file storage / AWS S3 / Cloudinary

**Other:**

* JWT authentication
* Docker for containerization (optional)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/instagram-clone.git
cd instagram-clone
```

2. Create a virtual environment (Python example):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/instagram_clone
SECRET_KEY=your_secret_key
```

5. Run migrations:

```bash
alembic upgrade head  # for FastAPI/SQLAlchemy
python manage.py migrate  # for Django
```

6. Start the server:

```bash
uvicorn main:app --reload  # FastAPI
python manage.py runserver   # Django
```

7. Start the frontend (if separate):

```bash
npm install
npm run dev
```

## Usage

* Register a new account or login with an existing account
* Upload photos with captions
* Follow other users and see their posts in your feed
* Like and comment on posts

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
