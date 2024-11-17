# CollabSphere: Smart Collaboration Platform
A versatile, team-focused communication tool designed for efficient collaboration in both professional and casual environments. The platform offers features such as:

## Features
- **User Authentication**:
  - Secure signup, login, and logout.
  - Profile management.

- **Room-Based Chat**:
  - Create or join public/private chat rooms.
  - Real-time messaging with persistent history.

- **Private Messaging**:
  - Direct, one-on-one conversations.
  - Message read receipts and typing indicators.

## Technologies Used
### Backend:
- **Framework**: Django
- **Database**: PostgreSQL
- **WebSockets**: Django Channels# ChatMe: A Simple Real-Time Chat Application

ChatMe is a user-friendly chat application designed for seamless real-time communication. Users can create or join chat rooms and privately message friends or colleagues.

## Features
- **User Authentication**:
  - Secure signup, login, and logout.
  - Profile management.

- **Room-Based Chat**:
  - Create or join public/private chat rooms.
  - Real-time messaging with persistent history.

- **Private Messaging**:
  - Direct, one-on-one conversations.
  - Message read receipts and typing indicators.

## Technologies Used
### Backend:
- **Framework**: Django
- **Database**: PostgreSQL
- **WebSockets**: Django Channels/Socket.IO

### Frontend:
- **Framework**: React.js
- **WebSocket Library**: Socket.IO Client
- **Styling**: CSS/Bootstrap

## Installation and Setup
### Prerequisites
- Python 3.9+
- Node.js 14+
- PostgreSQL/MongoDB

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatme.git
   cd chatme
2. Set up the backend:
   
```
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

3. Set up the frontend:
```
cd frontend
npm install
npm start
Access the app at http://localhost:3000.
```

Contributing
Feel free to open issues or submit pull requests to enhance ChatMe. Contributions are always welcome!
