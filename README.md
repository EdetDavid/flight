# Flight Booking System

This is a Django-based web application that allows users to book flights. The system checks if a flight has been approved before proceeding with the booking process, retrieves flight pricing from Amadeus API, and confirms flight orders.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [API Integration](#api-integration)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [License](#license)

---

## Features

- **Flight Booking**: Users can book approved flights, ensuring flight details such as departure date, return date, class, and passenger count match the approved criteria.
- **Flight Approval System**: Flights are only bookable if they have been pre-approved.
- **Amadeus API Integration**: Integrates with the Amadeus API to retrieve real-time flight prices and confirm bookings.
- **Passenger Information**: Automatically includes passenger details (e.g., name, contact information, documents) in flight booking requests.
- **Email Notifications**: Sends booking confirmation emails to the user with flight details.

---

## Technologies Used

- **Django**: Web framework used to build the application.
- **Python**: Core programming language.
- **Amadeus API**: For accessing flight offers, prices, and booking flights.
- **SQLite/PostgreSQL**: Used for database management.
- **HTML/CSS**: Frontend design.
- **Bootstrap**: Used for styling templates.
- **Requests Library**: For making HTTP requests to external APIs.
- **Logger**: For logging errors and system information.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flight-booking-system.git
   cd flight-booking-system
