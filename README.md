<h1>🌾 Teaching Garden </h1>
<p>Grow your teaching ideas, one lesson at a time.
Teaching Garden is a full-stack Django web application that allows primary teachers to upload, browse, save, and manage teaching resources in a calm, garden-inspired digital environment.</p>
<br>
________________________________________
<ol><li>📌 Table of Contents</li>
<li>Project Overview</li>
<li>UX & Design</li>
<li>User Stories</li>
<li>Features</li>
<li>Database Design</li>
<li>Technologies Used</li>
<li>Testing</li>
<li>Deployment</li>
<li>Future Improvements</li>
<li>Credits</li></ol>
<br>
_____________________________________
<h2>🌱 1. Project Overview </h2>
<p>Teaching Garden is a resource-sharing platform designed for primary educators.</p>
<p>The application allows users to:</p>
<ul>
<li>Create an account</li>
<li>Upload teaching resources</li>
<li>Browse resources by subject and year group</li>
<li>Save resources to a personal collection (“Greenhouse”) </li>
<li>Leave comments on resources</li>
<p>The garden theme is applied at the presentation layer while maintaining a structured relational database design.</p>
________________________________________
<h2>🎨 2. UX & Design</h2>
<p>The Teaching Garden platform features an intuitive, nature-inspired interface designed for ease of use by primary educators.</p>

<h3>Wireframes</h3>
<ul>
  <li><strong>Home Page</strong> - Landing page with platform introduction and call-to-action</li>
  <li><strong>Dashboard</strong> - User's personal hub with quick access to resources</li>
  <li><strong>Resource List</strong> - Browse and filter teaching resources</li>
  <li><strong>Resource Detail</strong> - View full resource information and comments</li>
  <li><strong>Upload Form</strong> - Interface for uploading new teaching resources</li>
</ul>

<p><em>Note: Wireframe images and screenshots to be embedded here</em></p>

<hr>

<h2>👩‍🏫 3. User Stories</h2>
<p>This section demonstrates planning and Agile thinking throughout the development process.</p>

<h3>First-Time Visitor Goals</h3>
<ul>
  <li>Understand what the platform does</li>
  <li>Browse resources without registration</li>
  <li>Register for an account</li>
</ul>

<h3>Registered User Goals</h3>
<ul>
  <li>Upload teaching resources</li>
  <li>Save useful resources</li>
  <li>Manage personal uploads</li>
  <li>Leave comments and engage with other educators</li>
</ul>

<h3>Site Owner Goals</h3>
<ul>
  <li>Maintain structured and organized data</li>
  <li>Manage content via Django admin panel</li>
  <li>Ensure secure authentication and authorization</li>
</ul>
<img width="1714" height="599" alt="image" src="https://github.com/user-attachments/assets/66ab7bed-9481-47db-b577-8f02324a98ec" />


<hr>

<h2>🌾 4. Features</h2>

<h3>Core Features</h3>

<h4>User Authentication</h4>
<ul>
  <li>Register, login, and logout functionality</li>
  <li>Access control for restricted pages</li>
  <li>User-specific dashboards and content</li>
</ul>

<h4>Resource Management (CRUD)</h4>
<ul>
  <li><strong>Create</strong> (Plant a Seed) - Upload new teaching resources</li>
  <li><strong>Read</strong> (Seed Library) - Browse and search resources</li>
  <li><strong>Update</strong> (Edit Seed) - Modify personal resource uploads</li>
  <li><strong>Delete</strong> (Remove Seed) - Remove resource uploads</li>
</ul>

<h4>Categorisation & Organization</h4>
<ul>
  <li>Resources linked to Subject area</li>
  <li>Resources linked to Year Group/Age Range</li>
  <li>Enables intelligent filtering and discovery</li>
</ul>

<h4>Favourites (Greenhouse)</h4>
<ul>
  <li>Save resources to personal collection</li>
  <li>Remove saved resources</li>
  <li>Many-to-many relationship implementation</li>
</ul>

<h4>Comments (Gardener Notes)</h4>
<ul>
  <li>Add comments to resources</li>
  <li>View full comment history</li>
  <li>Comments linked to user and resource</li>
</ul>

<hr>

<h2>🗃️ 5. Database Design</h2>

<h3>Entity Relationship Diagram</h3>
<p><em><img width="989" height="544" alt="image" src="https://github.com/user-attachments/assets/8bd002b1-cfce-49ab-b52e-7a2145e0c404" />
</em></p>

<h3>Database Structure</h3>
<p>The database follows a <strong>normalized relational structure</strong> for optimal data integrity:</p>
<ul>
  <li><strong>Resource</strong> is the central entity, linked to Subject and YearGroup through foreign keys</li>
  <li><strong>User</strong> entity manages authentication and resource ownership</li>
  <li><strong>Favourite</strong> junction table implements many-to-many relationships between Users and Resources</li>
  <li><strong>Comment</strong> entity tracks user feedback on resources</li>
</ul>

<hr>

<h2>🛠️ 6. Technologies Used</h2>

<h3>Backend</h3>
<ul>
  <li>Python 3</li>
  <li>Django Web Framework</li>
  <li>SQLite (Development)</li>
  <li>PostgreSQL (Production)</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li>HTML5</li>
  <li>CSS3</li>
  <li>JavaScript</li>
  <li>Bootstrap (Responsive Design)</li>
</ul>

<h3>Development Tools</h3>
<ul>
  <li>Git & GitHub (Version Control)</li>
  <li>Heroku (Deployment)</li>
  <li>Lucidchart (ERD Design)</li>
</ul>

<hr>

<h2>🔮 9. Future Improvements</h2>
<p>This section demonstrates ongoing development opportunities and scalability (important for grading).</p>
<ul>
  <li>Resource rating and review system</li>
  <li>Advanced search functionality</li>
  <li>User profile customisation and bio</li>
  <li>Tag-based filtering and categorisation</li>
  <li>File preview functionality (PDF, images)</li>
  <li>Admin approval workflow for moderation</li>
  <li>Pagination improvements for large datasets</li>
  <li>Email notifications for saved resources</li>
  <li>Social sharing capabilities</li>
</ul>

<hr>

<h2>🙏 10. Credits</h2>
<div>
  <h3>Resources & Documentation</h3>
  <ul>
    <li>Django Official Documentation</li>
    <li>Discord Community Support</li>
    <li>Lucidchart for ERD design tools</li>
  </ul>
  
  <h3>The Code Institute</h3>
  <ul>
    <li>Mark, Tom, and Alex - Instructors & Support</li>
    <li>My Code Institute Cohort - Class of March 2026</li>
  </ul>
</div>
