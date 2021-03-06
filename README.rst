DJCron Agent
============

This project is a component of the `DJCron Project`_, a Distributed Cron application.

The goal of the DJCron Agent is to run a task and return the results and some statistics about the result.


STATUS
------

=================  ================  ==================  ===========  ==============
PACKAGE            VERSION           DOWNLOADS           TESTS        COVERAGE
=================  ================  ==================  ===========  ==============
`DJCron Agent`_    |pip version a|   |pip downloads a|   |travis a|   |coveralls a|
=================  ================  ==================  ===========  ==============

Still under development, but already usable. Lots of features still to be added.

You can browse the code in the repository_.



Installation
------------

Just use pip:

.. code::

    pip install djcron-agent


It is already configured with basic settings to allow you to start using it. Just execute:

.. code::

     python manage.py celery worker --config=djcron_agent/settings --autoreload --queues=cron.agent

Easy!



Advisement
----------

Remember this is just an agent. The `DJCron Server`_ is required in order to make any action.


.. _`DJCron Project`: https://github.com/djcron-project
.. _`DJCron Server`: https://github.com/djcron-project/djcron-server
.. _`DJCron Agent`: https://github.com/djcron-project/djcron-agent
.. _`repository`: https://github.com/djcron-project/djcron-agent
.. _`Celery`: http://www.celeryproject.org/
.. _`RabbitMQ`: http://www.rabbitmq.com/
.. _`Redis`: http://redis.io/
.. _`MongoDB`: http://www.mongodb.org/
.. _`Django`: https://www.djangoproject.com/


.. |pip version a| image:: https://pypip.in/v/djcron-agent/badge.png
    :target: https://pypi.python.org/pypi/djcron-agent
    :alt: Latest PyPI version

.. |pip downloads a| image:: https://pypip.in/d/djcron-agent/badge.png
    :target: https://pypi.python.org/pypi/djcron-agent
    :alt: Number of PyPI downloads

.. |travis a| image:: https://travis-ci.org/djcron-project/djcron-agent.png
    :target: `Travis a`_
    :alt: Travis results

.. |coveralls a| image:: https://coveralls.io/repos/djcron-project/djcron-agent/badge.png
    :target: `Coveralls a`_
    :alt: Coveralls results

.. _`Travis a`: https://travis-ci.org/djcron-project/djcron-agent
.. _`Coveralls a`: https://coveralls.io/r/djcron-project/djcron-agent
