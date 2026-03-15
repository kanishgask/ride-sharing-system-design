# 🚗 Ride Sharing System Design

System Design Project – Large Scale Mobility Platform

---

# Problem Statement

Design a ride sharing platform similar to Uber where riders can request rides and drivers can accept them.

---

# Functional Requirements

- Rider requests ride
- Driver accepts ride
- Match nearby drivers
- Track trip status

---

# Non Functional Requirements

- Low latency driver matching
- High availability
- Real-time location updates
- Horizontal scalability

---

# Core Concepts

• Geolocation matching  
• Real-time updates  
• Trip lifecycle management  
• Distributed services  

---

# High Level Architecture

Rider App
 ↓
API Gateway
 ↓
Ride Service
 ↓
Matching Service
 ↓
Driver Service
 ↓
Database
