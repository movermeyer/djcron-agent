DJCron Agent
============

This project is a component of the `DJCron Project`_, a Distributed Cron application.

The goal of the DJCron Agent is to run a task and return the results and some statistics about the result.


STATUS
------

Still under development, but already usable. Lots of features still to be added.

You can browse the code in the repository_.


Installation
------------

Just use pip:

..code::

    pip install djcron-agent


It is already configured with basic settings to allow you to start using it. Just execute:

..code::

     python manage.py celery worker --config=agent_settings --autoreload --queues=cron.agent

Easy!


Advisement
----------

Remember this is just an agent. The `DJCron Server`_ is required in order to make any action.


-- _`DJCron Project`: https://github.com/djcron-project
-- _`DJCron Server`: https://github.com/djcron-server
.. _`repository`: https://github.com/djcron-project/djcron-agent
.. _`Celery`: http://www.celeryproject.org/
.. _`RabbitMQ`: http://www.rabbitmq.com/
.. _`Redis`: http://redis.io/
.. _`MongoDB`: http://www.mongodb.org/
.. _`Django`: https://www.djangoproject.com/
