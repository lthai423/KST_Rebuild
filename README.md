KST Content Management and Website Rebuild
===========================================

Migration of Web Applications
-----------------------------
Due to NDA, the code base for all propietary web applications have been moved to a private repository on Github.  Applications including Remote View, Content Delivery and Deliverable Management System, and the User Authentication System models have all been migrated back to Boeing's server and must remain there during development until UAS is deployed.  If you have any issues contact [**Lawrence Thai - SWE Intern and PL for KST_Rebuild**](mailto:lthai@kellyspace.com) or [**Jason Lee - Director of Operations**](mailto:jlee@kellyspace.com).

About this Project
------------------

The aim of the project is to develop a central codebase that can be used by future developers to quickly modify the front-end, back-end, and to create new web applications as needed. It will provide a central database for storing information necessary for user authentication, web applications, etc. To ensure future developers can easily maintain this project, the popular [**Python**](https://docs.python.org/3/) programming language was chosen.

This codebase utilizes the [**Django**](https://docs.djangoproject.com/en/1.9/) webframework, with built-in support for the [**Django Templating Language (DTL)**](https://docs.djangoproject.com/en/1.9/topics/templates/) HTML templating engine. Website data is stored in a [**PostgreSQL**](http://www.postgresql.org/docs/) database. Manipulation of the database is done through the Django's built-in wrapper. Database migrations are done using [**Django Migrations**](https://docs.djangoproject.com/en/1.9/topics/migrations/).

For easier styling, we will be using [**Bootstrap**](http://bootstrapdocs.com/v3.0.3/docs/css/), the most popular responsive, mobile friendly front-end framework available.  To ensure visual cohesion, developers are encouraged to use available templates already created and implemented.  Developers are advised to stick to the coding conventions and practices that are already used to ensure the project is extensible for all future developers.

Developers
----------

* Lawrence Thai *lthai423* [lthai@kellyspace.com](mailto:lthai@kellyspace.com)

Getting Involved
----------------

[Get in contact with the KST Webmaster](mailto:lthai@kellyspace.com) to get added to the GitHub team. If added, you will get write access to the repository.

Requirements
------------

* Linux or Mac OS X (using Homebrew to install *python* and *pip*)
* python 3.4.x
* python-virtualenv 12.1.x
* git 2.4.x
* pip 6.1.x
* postgresql 9.4.x
* (the remaining requirements will be installed below using *pip*)

**Note:** Pay close attention to the package names for your distro of Linux...

* For example, on Ubuntu Server you'd use ```python3 virtualenv git python3-pip postgresql```.
* On Manjaro (an Arch-derivative), you'd use ```python python-virtualenv git python-pip postgresql```.

Setting Up
----------

### Mac OSX via Command Line

Check Back Soon

Ongoing Work
------------

* Always begin your day by pulling the latest revisions from GitHub

* To run the site locally after install, run the following command "python manage.py runserver"


Developer notes
---------------




Contributions
	
	README was templated from a modified version of CSUSB CSE Club's Website Project README.
