# Distributed Communication Project: CECS 327

This project demonstrates a small distributed system with custom-designed communication protocols, implemented as part of the CECS 327 – Intro to Networks and Distributed Computing course.

## Table of Contents

- [Overview](#overview)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Testing](#testing)
- [Monitoring](#monitoring)
- [Contributors](#contributors)
- [Acknowledgments](#acknowledgments)

## Overview

This distributed system consists of multiple server nodes connected via custom communication protocols:

- Broadcast Protocol
- Anycast Protocol
- Multicast Protocol (optional)

The system is containerized using Docker for easy setup and replication.

## Installation and Setup

### Prerequisites

- Docker
- Docker Compose

### Steps:

1. **Clone the Repository:**

   ```bash
   git clone <repository-link>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd distributed_project
   ```

3. **Build and Start the Containers:**
   ```bash
   docker-compose up --build
   ```

## Usage

After starting the containers, the master server node will be accessible at port 5000 (or your chosen port).

To interact with the system, [describe any client-side operations, HTTP calls, scripts, or UI, if any].

For example:

```bash
curl http://localhost:5000/api_endpoint
```

## Testing

We have implemented various test cases to validate the communication protocols.

To run the tests, [provide specific steps or commands, if any].

## Monitoring

Network activities among the nodes can be monitored using [your chosen tool, e.g., built-in logging, Wireshark, etc.].

Logs capturing all required fields such as Time, Source_IP, Destination_IP, etc., can be found at [specify the location, e.g., `logs/communication.log`].

## Contributors

[List names, roles, and contributions of all team members]

- **Toan Le** - Lead Protocol Design, Docker Setup, Videographer, tester
- ...

## Acknowledgments

We utilized [mention any existing protocol design or libraries you've used] for the initial setup of the communication protocols. All sources have been cited in the source code as per the project guidelines.

---
