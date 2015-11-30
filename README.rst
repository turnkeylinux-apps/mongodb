MongoDB - NoSQL database
========================

`MongoDB`_ (from "humongous") is a scalable, high-performance
document-oriented NoSQL database system. Instead of storing data in
tables as is done in a "classical" relational database, MongoDB stores
structured data as JSON-like documents with dynamic schemas, making
integration with certain types of applications easier and faster.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- MongoDB configurations:
   
   - MongoDB installed and maintained through the package management
     system (mongodb package).
   - Configured with auth enabled (security).
   - Configured to bind to all network interfaces (convenience).
   - Includes MongoDB PHP bindings.
   - Includes MongoDB Python bindings and iPython.

- RockMongo for web based administration:
   
   - Installed from upstream source code to /var/www/rockmongo.
   - RockMongo is powered by Lighttpd with SSL support out-of-the-box.

- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**


.. _MongoDB: http://www.mongodb.org/
.. _TurnKey Core: https://www.turnkeylinux.org/core
