.. currentmodule:: pyud

Usage
=====

This gives a brief usage guide to the library. If you haven't installed pyud already, then check out the section on :ref:`installation`.

Overview
--------

The current `Urban Dictionary`_ API exposes three features that are all implemented in pyud:

- Fetching definitions for a certain term
- Fetching a specific definition by the integer ID of that definition
- Retrieving random definitions

pyud supports both synchronous and asynchronous usage of the library, and this is shown in the following examples.

Examples
--------

The examples show pyud being used to retrieve a definition for the word *hello*.

Synchronous example
~~~~~~~~~~~~~~~~~~~

The following code gives an example in "regular", synchronous programming:

.. code-block:: py

    import pyud

    ud = pyud.Client()
    definitions = ud.define("hello")
    print(definitions[0].word)

First, we import pyud into Python. If you get an error while importing, then check the :ref:`installation` section to make sure you have installed it correctly.

Next, we create a new instance of :class:`Client`. This is used to access the features of the API wrapper, and connect with Urban Dictionary.

Then, we retrieve the definitions for the word *hello* using the :meth:`Client.define` method. This returns a list, with each element in the list being an instance of :class:`Definition`, or :data:`None` if no definitions are found. Because *hello* is such a common word, we can reasonably assume that there are definitions for this word.

Finally, we take the first definition, ``definitions[0]``, from the list and print the :attr:`~Definition.word` attribute from that :class:`Definition`. This is a string of the word we wanted the definition for.

Running the above code, gives us::

    hello

which is exactly what we expected.

Asychronous example
~~~~~~~~~~~~~~~~~~~

There may be cases where you may want to use pyud asynchronously, such as for event-based applications. For this reason, pyud has an asynchronous equivalent of the :class:`Client` called :class:`AsyncClient`.

The following example gives an example using :class:`AsyncClient`:

.. code-block:: py

    import asyncio

    import pyud


    async def example():
        ud = pyud.AsyncClient()
        definitions = await ud.define("hello")
        print(definitions[0].word)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())


Running this example, we get the same result as with the first.

You should be familiar with the concepts of using the :mod:`asyncio` module in order to understand this example. If not, then you can refer to the Python documentation on `coroutines and tasks`_ for a quick rundown of the concepts.

.. _coroutines and tasks: https://docs.python.org/3/library/asyncio-task.html
.. _Urban Dictionary: https://urbandictionary.com
