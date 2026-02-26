<img width="412" height="80" alt="image" src="https://github.com/user-attachments/assets/8c5320af-5f86-4ed1-a5d7-134114b2ecfc" />

# 🌱 The Teaching Garden

The Teaching Garden is a full-stack Django web application designed as a supportive, moderated community hub for primary educators. Users can upload teaching resources, write reflective posts, and comment on content. Admin moderation ensures a safe and professional space. It uses HTML, CSS and Django.

**Live site:** https://theteachinggarden-9c7919705954.herokuapp.com/ 

**Repository:** https://github.com/aimeelittle1708-hub/theteachinggarden

SUPERUSER CREDENTIALS:  
username - admin  
password - abc123 

  These will be needed to access all features on the site.

---

## Table of Contents
1. [Project Goals](#project-goals)
2. [UX & Accessibility](#ux--accessibility)
3. [Agile Development](#agile-development)
4. [Features](#features)
5. [Data Model](#data-model)
6. [Authentication & Permissions](#authentication--permissions)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Installation](#installation)
10. [Technologies Used](#technologies-used)
11. [AI Tools](#ai-tools)
12. [Reflection](#reflection)
13. [Future Developement](#future-dev)
14. [Credits](#credits)

---

## Project Goals

### Primary Objectives
- Provide a clean, responsive platform for teachers to:
  - Share downloadable resources (Cloudinary storage)
  - Create posts and discussions
  - Leave comments with moderation controls
- Implement role-based permissions:
  - Users can manage their own content (CRUD)
  - Staff/admin can moderate and manage all content

### Target Audience
- Primary school teachers and trainees
- SEND practitioners
- Teachers seeking evidence-based strategies and community support

---

# UX & Accessibility


## Design

### Design Philosophy

The Teaching Garden was designed to reflect:

- 🌿 Calm professionalism  
- 📚 Educational credibility  
- 🤝 Community and collaboration  
- ♿ Accessibility and clarity  

The visual style avoids clutter and prioritises readability, consistency, and intuitive navigation.

Design decisions were guided by:

- UX best practice
- Accessibility considerations (WCAG awareness)
- Audience expectations (primary educators)
- Simplicity over decoration

---

### Colour Palette

The colour scheme is intentionally soft, natural, and education-focused.

| Colour | Hex Code | Usage | Rationale |
|--------|----------|--------|------------|
| Deep Green | `#2d6a4f` | Headings, brand accents | Represents growth, calm, and the “garden” theme |
| Success Green | Bootstrap Success | Buttons, CTAs | Familiar UI convention for positive actions |
| Light Background | `#f8f9fa` | Page backgrounds, footer | Clean and neutral without harsh white contrast |
| Dark Text | `#212529` | Body text | Strong contrast for readability |
| Muted Text | `#6c757d` | Secondary information | Reduces visual noise while maintaining clarity |

### Why Green?

Green was selected because:

- It aligns with the “Teaching Garden” concept.
- It conveys growth, development and calmness.
- It avoids the urgency of red or the corporate tone of blue.
- It supports a reflective and supportive educational environment.

## Accessibility Considerations

- High contrast between text and background.
- Buttons use strong, accessible colour contrast.
- Focus outlines preserved for keyboard navigation.
- Hero buttons adjusted for improved accessibility.
- Semantic HTML used throughout templates.

*(Optional: Insert Lighthouse accessibility screenshot here)*

---

## Typography

Typography was selected for clarity, legibility, and professionalism.

### Primary Font: System / Bootstrap Default (e.g., Helvetica / Arial / system-ui)

- Clean and widely supported.
- Highly legible across devices.
- Reduces load time (no external font dependency).
- Maintains a professional educational tone.

### Heading Styling

- Bold weight for hierarchy.
- Consistent spacing for readability.
- Clear visual separation between sections.

### Design Principle Applied

- Body text prioritises readability over decoration.
- Avoided overly stylised fonts to maintain accessibility.
- Line spacing and padding adjusted for comfortable reading on desktop and mobile.

---

## Layout & Structure

The layout follows a predictable and user-friendly structure:

- Persistent navigation bar
- Clear hero section on homepage
- Card-based content layout
- Consistent page margins using Bootstrap containers
- Footer with structured navigation and copyright

Bootstrap 5 Grid and Flexbox were used to:

- Ensure responsiveness
- Maintain layout integrity on mobile
- Prevent content overlap
- Provide consistent spacing

---

## Responsive Design

The site was designed mobile-first and tested across:

- Desktop
- Tablet
- Mobile

Bootstrap breakpoints ensure:

- Navigation collapses into a hamburger menu on smaller screens
- Cards stack vertically on mobile devices
- Buttons maintain touch-friendly sizing (~44px minimum height)
- Content spacing adjusts fluidly without layout breakage
- Mobile phones
<br>
<br>
<img width="420" height="761" alt="image" src="https://github.com/user-attachments/assets/a9d0570b-a250-450d-8bb4-efe87f722d41" />
<br>
<br>
- Tablets and small screens
<br>
<br>
<img width="501" height="719" alt="image" src="https://github.com/user-attachments/assets/35512d4d-60a2-4442-942e-4f784949adb0" />
<br>
<br>
- Laptops and Medium sized screens
<br>
<br>
<img width="1156" height="678" alt="image" src="https://github.com/user-attachments/assets/bfa95527-14cb-41a3-a98c-d3580ce913c1" />
<br>
<br>
-Large screen desktops
<br>
<br>
<img width="1166" height="726" alt="image" src="https://github.com/user-attachments/assets/8862c71a-9eaa-4889-a9ce-5b72d0000b24" />
<br>
<br>

---

## Wireframes

Wireframes were created during the planning stage to map:

- Page layout hierarchy
- Navigation placement
- User flow between resources and posts
- Comment placement and moderation visibility

### Wireframe Screenshots

Homepage Wireframes
<br>
<img width="216" height="579" alt="image" src="https://github.com/user-attachments/assets/adc4231b-72b5-4766-ba04-a58e2f680612" /> 
<br>
<br>
<img width="876" height="678" alt="image" src="https://github.com/user-attachments/assets/4b1415d9-2f49-4c7d-b77d-fb0bb54f191a" />
<br>
<br>
Resources Page Wireframes
<br>
<br>
<img width="831" height="710" alt="image" src="https://github.com/user-attachments/assets/c9f6cc97-dfd4-44dc-90a9-7f6efab47437" /> 
<br>
<br>
<img width="215" height="585" alt="image" src="https://github.com/user-attachments/assets/c5dd6ba2-bc83-4cf2-851a-9d82300a3e8e" />
<br>
<br>
Post page Wireframes
<br>
<br>
<img width="244" height="597" alt="image" src="https://github.com/user-attachments/assets/85fb3e42-f009-43be-8936-cf673aa92e45" />
<br>
<br>
<img width="828" height="703" alt="image" src="https://github.com/user-attachments/assets/60cd33db-4afa-4b5d-900f-fabfbb5d7ca3" />

### Design Evolution

During development:

- The hero section spacing was refined for improved accessibility.
- A footer was added to improve structural completeness.
- Button contrast was adjusted following accessibility testing.
- Button labels added for improved accessibility with screen readers.
- Comment moderation visibility influenced layout decisions.
- Pending comments were separated visually from approved comments.

This demonstrates that the UX process was iterative and responsive to development findings.

---

##  Consistency

Design consistency was maintained through:

- Reusable card components
- Standardised button classes
- Shared template inheritance (`base.html`)
- Centralised custom CSS file
- Consistent spacing and padding rules

---

### Accessibility
Implemented:
- Semantic HTML structure and Bootstrap components
- High-contrast button styling
- Clear focus targets and spacing (especially in hero CTA buttons)
- Form labels and validation feedback
  
---

## Agile Development

This project was planned and tracked using an Agile workflow:
- User stories were written, prioritised, and moved across workflow stages (To Do → In Progress → Done).
- Each major feature maps to a user story and an LO requirement.

**Agile Tool Evidence (add):**
- Kanban board link: [The Teaching Garden Project Link](https://github.com/aimeelittle1708-hub/theteachinggarden/projects?query=is%3Aopen)
- Screenshot of your board: <img width="1714" height="599" alt="image" src="https://github.com/user-attachments/assets/66ab7bed-9481-47db-b577-8f02324a98ec" />

### Key User Stories (examples)
**Resources**
- As a user, I can upload a teaching resource so others can download it.
- As a user, I can filter resources by subject/year group.
- As an admin, I can approve resources before they are visible publicly.

**Posts**
- As a user, I can create and edit a post.
- As a user, I can comment on a post.
- As an admin, I can approve or delete posts/comments to maintain standards.

---

## Features

### ✅ Authentication
- Register / login / logout
- Login state reflected in navbar (“Hi, {{ user.name }}”)
- Conditional navigation links (Upload appears only when authenticated)
- <img width="429" height="759" alt="image" src="https://github.com/user-attachments/assets/f944aef7-a2f9-4d86-a5d2-11087dfb0341" />


### ✅ Resources
- Upload resource (Cloudinary raw upload)
- Filter: subject + year group
- Search: keyword matches title/description
- Detail page: view + download link
  <br>
<img width="1818" height="866" alt="image" src="https://github.com/user-attachments/assets/1492092a-cbc1-41f1-84ef-c0e2ac2479d6" />
<br>
<br>
<img width="1738" height="586" alt="image" src="https://github.com/user-attachments/assets/9f931fe4-d497-491e-8d2a-af921b24c3a8" />
<br>
<br>
- Commenting and moderation workflow
- <br>
  <br>
<img width="592" height="750" alt="image" src="https://github.com/user-attachments/assets/4ebfef60-6087-453e-bd0b-50ab89689200" />

### ✅ Posts
- Posts feed + detail page
 <img width="1818" height="864" alt="image" src="https://github.com/user-attachments/assets/6f68cca9-6201-4967-a21b-a6577987b035" />
 <br>

- Commenting and moderation workflow
  <br>
 <br> <img width="1730" height="886" alt="image" src="https://github.com/user-attachments/assets/e629dcca-be0c-4dc0-af30-e1d7aab96100" />


### ✅ Comments (Posts + Resources)
- Users can create comments
- Users can see their *own pending comments*
- Users can edit/delete their own comments
- Editing re-triggers approval (if moderation enabled)

### ✅ Admin Moderation
- Approve resources/posts/comments via Django admin
- Staff users can edit/delete other users’ content when needed

### ✅ About Page
- Includes contact form with Bootstrap confirmation alert

### ✅ UI Feedback
- Django messages framework to confirm actions:
  - Upload success
  - <br>
  <br>
  <img width="421" height="766" alt="image" src="https://github.com/user-attachments/assets/64b524d1-4e51-416b-a7ea-4ce48c692a58" />
<br>
<br>
  - Comment submitted
  <br>
  <br>
    <img width="1772" height="365" alt="image" src="https://github.com/user-attachments/assets/679894f7-8ef6-404a-9df4-63cedd02fe9b" />
 <br>
  <br>
  - Delete confirmations
  <br>
<br>
  <img width="432" height="760" alt="image" src="https://github.com/user-attachments/assets/deffe332-5f52-4515-885d-66519a838fcc" />
<br>
<br>
  - Update confirmations
<br>
<br>
  - <img width="419" height="763" alt="image" src="https://github.com/user-attachments/assets/3961b9bc-342e-457d-98e7-44050041c1da" />
<br>
<br>

---

## Data Model

The database design uses Django ORM with a custom user model and relational models for resources, posts, and comments.

### Custom User Model
Fields include:
- email (USERNAME_FIELD)
- name
- is_staff / is_superuser

### Resource
- Uploaded file stored in Cloudinary
- Linked to user via ForeignKey
- Moderation fields: is_approved, approved_by, approved_at

### Post
- Linked to user via ForeignKey
- Moderation fields

### Comment
- Can belong to **either** a post or a resource
- Linked to user via ForeignKey
- Moderation fields

## Entity Relationship Diagram
<p><img width="989" height="544" alt="image" src="https://github.com/user-attachments/assets/8bd002b1-cfce-49ab-b52e-7a2145e0c404" />
- Short explanation of relationship choices (FK + related_name)

---

## Authentication & Permissions

### Role-Based Access
- Anonymous users:
  - Can browse approved resources/posts
  - Cannot upload/create/comment
- All Logged-in users:
  - Can upload resources and create posts
  - Can edit/delete their own content
  - Can create comments (pending until approved)
- Staff/admin users:
  - Can see unapproved content
  - Can edit/delete/moderate content from other users
  - Can approve items in admin panel
  - Can Add, edit and upload posts to the blog section

### Access Control Examples
- `@login_required` used for upload/post/comment actions
- Ownership checks enforced:
  - Users can edit/delete only their own content
  - Staff can override



---

## Testing

Testing was completed via manual testing across core user journeys.

### Manual Test Table (example)

| Feature | Test | Expected | Result |
|--------|------|----------|--------|
| Register | Submit valid form | User created + logged in | Pass |
| Login | Submit valid credentials | User logged in | Pass |
| Upload resource | Upload file | Resource saved, pending approval message shown | Pass |
| Resources filter | Filter by year/subject | Only matching resources shown | Pass |
| Comment | Submit comment | Success message, comment pending approval | Pass |
| Comment edit | Edit own comment | Comment reverts to pending | Pass |
| Permissions | Non-owner edit URL | Forbidden/blocked | Pass |

### CSS Validation
- <img width="1790" height="858" alt="image" src="https://github.com/user-attachments/assets/a9ec355b-6ca8-465e-9517-a133b30fd1f2" />
No Errors found.
<br>
<br>
### HTML validation from W3C
<img width="1771" height="670" alt="image" src="https://github.com/user-attachments/assets/5debb601-316c-417f-a662-45439bd864af" />
No Errors found on all pages.

### Ligthouse test
Lighthouse testing shows good performance and best practises.
<img width="586" height="721" alt="image" src="https://github.com/user-attachments/assets/8f862d14-4ebd-4341-acc7-6204fa37c634" />

---

## Deployment

The application is deployed using Heroku.

### Environment Variables (Heroku Config Vars)
- `SECRET_KEY`
- `DATABASE_URL`
- `CLOUDINARY_URL`

### Deployment Steps
1. Create Heroku app
2. Set config vars
3. Ensure `DEBUG=False`
4. Install dependencies:
   - `gunicorn`
   - `whitenoise`
   - `dj-database-url`
5. Configure WhiteNoise and static files
6. Add Procfile:

7. web: gunicorn theteachinggarden.wsgi

7. Deploy from GitHub (manual or automatic)
8. Run migrations on Heroku:

heroku run python manage.py migrate


### Security Measures
- No secrets committed
- `.gitignore` used
- Deployment uses env vars
- DEBUG disabled on Heroku

---

## Installation

### Local Setup
1. Clone:

git clone <REPO URL>
cd theteachinggarden


2. Create and activate venv:

python -m venv .venv
.venv\Scripts\activate


3. Install:

pip install -r requirements.txt


4. Create `env.py` or `.env` with:
- SECRET_KEY
- DATABASE_URL (optional if using sqlite locally)
- CLOUDINARY_URL

5. Migrate:

python manage.py migrate


6. Create superuser:

python manage.py createsuperuser


7. Run:

python manage.py runserver

---

## Technologies Used

### Languages
- Python
- HTML5
- CSS3

### Frameworks / Libraries
- Django
- Bootstrap 5
- Cloudinary
- WhiteNoise
- Gunicorn
- dj-database-url

### Tools
- Git + GitHub
- Heroku
- Chrome DevTools
- Django Admin

---

## AI Tools

AI tools were used to support development in ways aligned with the project goals. Used for Debugging and content generation.

### AI Used For:
- Drafting example content (teacher voice posts)
- Debugging Django template syntax issues
- Supporting view/model refactoring decisions
- Improving UX messaging and accessibility improvements

### Reflection (brief, distinction-friendly)
AI accelerated development by reducing time spent on debugging repetitive syntax errors and by helping restructure views/models in a maintainable way. I validated AI suggestions by cross-checking Django documentation and testing changes incrementally in local development before committing.
As a novice developer I did make the mistake of pushing my secret key to GitHub, but was able to change the key and have secured the new one in the env.py file which was then ignored and not pushed by using .gitignore.

---
## Future Development
This was the first iteration of The Teaching Garden. In future iterations I would like to implement the following features to the website:

  -Resource rating and review system
  
  -More advanced search functionality
  
  -User profile customisation and bio
  
  -Tag-based filtering and categorisation
  
  -File preview functionality (PDF, images)
  
  -Admin approval workflow for moderation
  
  -Pagination improvements for large datasets
  
  -Email notifications for saved resources
  
  -Social sharing capabilities

  -Games section to aid teachers and students in their lessons.

---
## Credits (#credits)
- Django documentation
- Bootstrap documentation
- Cloudinary documentation
- Heroku deployment documentation
- Django Official Documentation
- Discord Community Support
- Lucidchart for ERD design tools
-The Code Institute
  -Mark, Tom, and Alex - Instructors & Support
  -My wonderful Code Institute Cohort - Class of March 2026
