# Phone-Tracker Wiki

Welcome to the Phone-Tracker Wiki! This documentation provides an overview of the project's features, setup instructions, usage guide, and details about its main components.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Authentication & User Management](#authentication--user-management)
- [Tracking Functionality](#tracking-functionality)
- [Key Components](#key-components)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
Phone-Tracker is an application designed to monitor and track mobile device locations securely. It provides real-time location updates, user authentication, and a dashboard for managing tracked devices.

## Features
- Tracking the approximate location of the device via GOOGLE open libraries

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LorenzoColitta/Phone-Tracker.git
   cd Phone-Tracker
   ```
2. **Install dependencies**
   ```bash
   # Example for Node.js projects
   pip install -r dependencies.txt
   ```
3. **Run the application**
   ```bash
   python main.py
   ```

## Usage
- Add a device to track by entering its phonr number. No account required.
- View the dashboard for real-time location updates and history.

## Authentication & User Management
No Accounts = No UAM

## Mandatory Telemetry
- The package saves the phone number used in a log using MD5 HASH. This data is not sent to any servers and is encrypted by using encryption keys hosted on Cloudflare Workers in a secure manner.

## Contributing

Interested in improving Phone-Tracker? Make a pull request!

## License

This project is licensed under the MIT License.

---
