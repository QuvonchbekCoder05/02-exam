## ENG

## This project is built using Django REST Framework and includes multiple models such as Team Members, Services, News, Publications, Reviews, and Search functionality. It also includes custom validators for phone numbers and emails and utilizes Swagger and Redoc for API documentation.

## Technologies Used:
- **Python**
- **Django**: Python web framework
- **Django REST Framework**: For building RESTful APIs
- **drf-yasg**: For API documentation with Swagger and Redoc
- **Django Filter**: Filtering and search functionality
- **SQLite**: Default database used in development


## Features:
- CRUD operations for models such as Team Members, Services, News, Publications, Reviews, and About.
- Custom validation for phone numbers (supports Uzbek format) and emails.
- Full-text search across multiple models using filters.
- Automatic timestamping with `created_time` and `updated_time` fields.
- Comprehensive API documentation using Swagger and Redoc.
- Admin panel for managing data.

## Models:
- **TeamMember**: Stores team member details (first name, last name, position, etc.).
- **Service**: Information related to services offered.
- **Publication**: Publications related to the team members.
- **Review**: Stores reviews for services.
- **Search**: Provides search functionality.
- **ContactInformation**: Stores contact details such as phone numbers and emails.
- **About**: Provides general information about the platform.

## Key API Endpoints:

- `GET /about/` - Fetches a list of "about" content.
- `GET /contact-information/` - Fetches contact information.
- `GET /contact/` - Fetches a list of contact entries.
- `POST /contact/` - Creates a new contact entry.
- `GET /news/` - Fetches a list of news items.
- `GET /news/{slug}/` - Fetches detailed news by slug.
- `GET /partners/` - Fetches a list of partners.
- `GET /publications/` - Fetches a list of publications.
- `GET /publications/{slug}/` - Fetches publication details by slug.
- `GET /reviews/` - Fetches a list of reviews.
- `GET /search/` - Searches across multiple content types.
- `GET /services/` - Fetches a list of services.
- `GET /services/{slug}/` - Fetches service details by slug.
- `GET /team-member/` - Fetches a list of team members.
- `GET /team-member/{slug}/` - Fetches team member details by slug.

## Libraries Used:
- Django
- Django REST Framework
- drf-yasg (for Swagger/Redoc)
- Django Filter
- SQLite


## Installation:
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## API Documentation:
- **Swagger UI**: `/swagger/`
- **Redoc**: `/redoc/`

## UZB

## Ushbu loyiha Django REST Framework yordamida qurilgan va bir nechta modellarni, jumladan, jamoa a'zolari, xizmatlar, yangiliklar, nashrlar, sharhlar va qidiruv funksiyalarini o'z ichiga oladi. Bundan tashqari, telefon raqamlari va elektron pochta uchun maxsus validatorlar ham mavjud. API hujjatlari Swagger va Redoc orqali taqdim etilgan.

## Foydalanilgan texnologiyalar:
- **Python**
- **Django**: Python veb-freyvorki
- **Django REST Framework**: RESTful API yaratish uchun
- **drf-yasg**: Swagger va Redoc bilan API hujjatlarini yaratish uchun
- **Django Filter**: Filtrlash va qidiruv funksiyalari uchun
- **SQLite**: Ishlab chiqish jarayonida ishlatiladigan ma'lumotlar bazasi


## Xususiyatlar:
- Jamoa a'zolari, xizmatlar, yangiliklar, nashrlar, sharhlar va "About" bo'limlari uchun CRUD amallari.
- O'zbek formatidagi telefon raqamlari va elektron pochta uchun maxsus validatsiya.
- Bir nechta modellar bo'yicha to'liq matnli qidiruv imkoniyati.
- Avtomatik vaqt belgilash (`created_time` va `updated_time` maydonlari).
- Swagger va Redoc orqali keng qamrovli API hujjatlari.
- Ma'lumotlarni boshqarish uchun admin panel.

## Modellar:
- **TeamMember**: Jamoa a'zolarining ma'lumotlarini saqlaydi (ism, familiya, lavozim va boshqalar).
- **Service**: Taklif etilayotgan xizmatlar haqida ma'lumot.
- **Publication**: Nashrlar va ularga tegishli jamoa a'zolari haqida ma'lumot.
- **Review**: Xizmatlar bo'yicha sharhlarni saqlaydi.
- **Search**: Kontent bo'yicha qidiruv funksiyasi.
- **ContactInformation**: Telefon raqamlari va elektron pochta manzillarini saqlaydi.
- **About**: Platforma haqida umumiy ma'lumot beradi.

## Muhim API manzillari:

- `GET /about/` - "About" bo'limini ro'yxatlash.
- `GET /contact-information/` - Kontakt ma'lumotlarini olish.
- `GET /contact/` - Kontaktlar ro'yxatini olish.
- `POST /contact/` - Yangi kontakt yaratish.
- `GET /news/` - Yangiliklar ro'yxatini olish.
- `GET /news/{slug}/` - Yangiliklarning batafsil ma'lumotlarini olish.
- `GET /partners/` - Hamkorlar ro'yxatini olish.
- `GET /publications/` - Nashrlar ro'yxatini olish.
- `GET /publications/{slug}/` - Nashrlar bo'yicha batafsil ma'lumot olish.
- `GET /reviews/` - Sharhlar ro'yxatini olish.
- `GET /search/` - Qidiruv funksiyasi orqali turli kontentni qidirish.
- `GET /services/` - Xizmatlar ro'yxatini olish.
- `GET /services/{slug}/` - Xizmatning batafsil ma'lumotlarini olish.
- `GET /team-member/` - Jamoa a'zolari ro'yxatini olish.
- `GET /team-member/{slug}/` - Jamoa a'zolarining batafsil ma'lumotlarini olish.

## Foydalanilgan kutubxonalar:
- Django
- Django REST Framework
- drf-yasg (Swagger/Redoc uchun)
- Django Filter
- SQLite


## O'rnatish:
1. Repodan klon qiling.
2. Zaruriy kutubxonalarni o'rnating: `pip install -r requirements.txt`
3. Migratsiyalarni ishga tushiring: `python manage.py migrate`
4. Dastur serverini ishga tushiring: `python manage.py runserver`

## API Hujjatlari:
- **Swagger UI**: `/swagger/`
- **Redoc**: `/redoc/`

