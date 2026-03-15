# ER Diagram – Ride Sharing System

RIDERS
- rider_id
- name

DRIVERS
- driver_id
- location
- available

RIDES
- ride_id
- rider_id
- driver_id
- status

Relationships

Rider 1 → N Rides  
Driver 1 → N Rides
