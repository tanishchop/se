# Software Requirements Specification (SRS)
## College Event Management System

---

## Table of Contents
1. Introduction
   1.1 Aim
   1.2 Document Conventions
   1.3 Intended Audience and Reading Suggestions
   1.4 Product Scope
   1.5 References
2. Overall Description
   2.1 Product Perspective
   2.2 Product Functions
   2.3 User Classes and Characteristics
   2.4 Operating Environment
   2.5 Design and Implementation Constraints
   2.6 User Documentation
   2.7 Assumptions and Dependencies
3. External Interface Requirements
   3.1 User Interfaces
   3.2 Hardware Interfaces
   3.3 Software Interfaces
   3.4 Communications Interfaces
4. System Features
   4.1 Event Management
   4.2 Schedule Management
   4.3 User Registration
   4.4 Authentication
   4.5 Admin Panel
5. Other Nonfunctional Requirements
   5.1 Performance Requirements
   5.2 Safety Requirements
   5.3 Security Requirements
   5.4 Software Quality Attributes
   5.5 Business Rules

---

## 1. Introduction

### 1.1 Aim
To develop a web-based College Event Management System for organizing, scheduling, and registering college events.

### 1.2 Document Conventions
- Requirements are numbered (FRx for functional, NFRx for non-functional).
- “System” refers to the College Event Management System.

### 1.3 Intended Audience and Reading Suggestions
- Developers, testers, project managers, stakeholders.
- Section 2 for overview, Section 4 for features, Section 5 for constraints.

### 1.4 Product Scope

The College Event Management System provides a reliable online platform for college organizers to create, manage, and schedule events, while allowing students and staff to browse, view, and register for available event slots. Organizers can specify event details, manage schedules, and monitor registrations. Participants can filter events by date, category, and location, and register for available slots directly through the system. The platform also incorporates an admin role for overseeing event management, user registrations, and system monitoring. By integrating DevOps tools such as Git for version control and Docker for deployment, the system ensures continuous integration, streamlined testing, efficient deployment, and reliable monitoring for improved performance and scalability.

### 1.5 References
- Django Documentation
- Docker Documentation
- Git Documentation

---

## 2. Overall Description

### 2.1 Product Perspective
Standalone web application, deployable via Docker, versioned with Git.

### 2.2 Product Functions
- User authentication and registration
- Event and schedule management
- User registration for schedules
- Admin panel for CRUD operations

### 2.3 User Classes and Characteristics
- Admin: Full access
- Organizer: Event/schedule management
- User: Event viewing and registration

### 2.4 Operating Environment
- Windows, macOS, Linux (Docker)
- Python 3.11+, Django 4.2+
- Modern web browsers

### 2.5 Design and Implementation Constraints
- Uses SQLite by default
- Django framework
- Docker containerization

### 2.6 User Documentation
- README.md with setup instructions

### 2.7 Assumptions and Dependencies
- Users have internet access
- Docker and Python installed for deployment

---

## 3. External Interface Requirements

### 3.1 User Interfaces
- Web-based UI for all users
- Admin panel for management

### 3.2 Hardware Interfaces
- No special hardware required

### 3.3 Software Interfaces
- Django ORM for database
- Docker for deployment

### 3.4 Communications Interfaces
- HTTP/HTTPS for web access

---

## 4. System Features

### 4.1 Event Management
- FR1: Organizers can create, edit, delete events
- FR2: Events have title, date, location, description

### 4.2 Schedule Management
- FR3: Organizers can add, edit, delete schedules
- FR4: Schedules have title, time, description, slots

### 4.3 User Registration
- FR5: Users can register for schedules
- FR6: Registration status is shown

### 4.4 Authentication
- FR7: Login and registration forms
- FR8: Only authenticated users can manage schedules

### 4.5 Admin Panel
- FR9: Full CRUD for users, events, schedules

---

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements
- NFR1: System should support 50+ concurrent users

### 5.2 Safety Requirements
- NFR2: Data backup and recovery procedures

### 5.3 Security Requirements
- NFR3: User data must be protected
- NFR4: CSRF and form validation

### 5.4 Software Quality Attributes
- NFR5: Usability for desktop users
- NFR6: Reliability and maintainability

### 5.5 Business Rules
- Only organizers can manage events/schedules
- Users can only register for available slots
