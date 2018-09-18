MongoDB - NoSQL database
========================

`Mongo DB`_ (from "humongous") is a scalable, high-performance
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
   - Includes mongo-tools_ (via package management) - a collection of tools for
     administering MongoDB servers.
   - Includes MongoDB PHP7.0 bindings (mongodb_). Note, for use with PHP, you
     may wish to also install the `MongoDB PHP Library`_
   - Includes MongoDB Python3 bindings and iPython3.
   - Bundled with Nginx webserver.

- Note: as of v15.0 this appliance no longer ships with a built-in Mongo UI
  for web based administration (previous versions had RockMongo). Unfortunately
  RockMongo is no longer maintained and not compatible with PHP7.0. There are
  numerous UI options avaialble, some suggestions are provided on the applaince
  landing page.

- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**

.. _Mongo DB: https://www.mongodb.org/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _mongo-tools: https://github.com/mongodb/mongo-tools
.. _mongodb: https://secure.php.net/mongodb
.. _mongo-php-library: https://github.com/mongodb/mongo-php-library
