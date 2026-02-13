<h1>🌾 Teaching Garden </h1>
Grow your teaching ideas, one lesson at a time.
Teaching Garden is a full-stack Django web application that allows primary teachers to upload, browse, save, and manage teaching resources in a calm, garden-inspired digital environment.
________________________________________
📌 Table of Contents
1.	Project Overview
2.	UX & Design
3.	User Stories
4.	Features
5.	Database Design
6.	Technologies Used
7.	Testing
8.	Deployment
9.	Future Improvements
10.	Credits
________________________________________
🌱 1. Project Overview
Teaching Garden is a resource-sharing platform designed for primary educators.
The application allows users to:
•	Create an account
•	Upload teaching resources
•	Browse resources by subject and year group
•	Save resources to a personal collection (“Greenhouse”)
•	Leave comments on resources
The garden theme is applied at the presentation layer while maintaining a structured relational database design.
________________________________________
🎨 2. UX & Design
(Insert the Design & UX section we wrote earlier here.)
You can also add:
Wireframes
Include:
•	Home page
•	Dashboard
•	Resource list
•	Resource detail
•	Upload form
(Upload images and embed them in your README.)
________________________________________
👩‍🏫 3. User Stories
This section shows planning and Agile thinking.
First-Time Visitor Goals
•	Understand what the platform does
•	Browse resources
•	Register for an account
Registered User Goals
•	Upload teaching resources
•	Save useful resources
•	Manage personal uploads
•	Leave comments
Site Owner Goals
•	Maintain structured data
•	Manage content via Django admin
•	Ensure secure authentication
________________________________________
🌾 4. Features
Break this into sections:
Core Features
User Authentication
•	Register, login, logout
•	Access restricted pages
•	User-specific dashboards
Resource Management (CRUD)
•	Create (Plant a Seed)
•	Read (Seed Library)
•	Update (Edit Seed)
•	Delete (Remove Seed)
Categorisation
•	Resources linked to Subject
•	Resources linked to Year Group
Favourites (Greenhouse)
•	Save resources
•	Remove saved resources
•	Many-to-many relationship implementation
Comments (Gardener Notes)
•	Add comments
•	View comment history
•	Linked to user and resource
________________________________________
🗃️ 5. Database Design
Entity Relationship Diagram
(Insert your ERD image here)
Brief explanation:
The database follows a normalized relational structure.
Resource is the central entity, linked to Subject and YearGroup through foreign keys.
Many-to-many relationships are handled using a junction table (Favourite).
________________________________________
🛠 6. Technologies Used
Backend
•	Python
•	Django
•	SQLite (development)
•	PostgreSQL (production, if used)
Frontend
•	HTML5
•	CSS3
•	JavaScript (if used)
•	Bootstrap (if used)
Tools
•	Git
•	GitHub
•	Heroku
•	Lucidchart (ERD design)
🔮 9. Future Improvements
This section is VERY important for grading.
Examples:
•	Resource rating system
•	Search functionality
•	User profile customisation
•	Tag-based filtering
•	File preview functionality
•	Admin approval workflow
•	Pagination improvements
________________________________________
🙏 10. Credits
•	Django Documentation
•	Discord
•	Lucidchart
•	Mark, Tom and Alex from The Code Institute
•	My Code Institute Cohort- Class of March 2026.
________________________________________
