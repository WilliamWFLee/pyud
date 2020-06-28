pyud
====

A simple wrapper for the Urban Dictionary API in Python.

Features
--------

- Synchronous and asynchronous clients for the API
- Definition objects for object-style access to definition attributes, and includes all fields
- Full coverage of the known API

Requirements
------------

- **Python 3.5.3 or higher.** Python 2 is not supported.
- `aiohttp <https://docs.aiohttp.org/en/stable/>`_, version 3.6.2

Quick Examples
--------------

Synchronous Example
~~~~~~~~~~~~~~~~~~~

.. code:: py

    import pyud

    ud = pyud.Client()
    definition = ud.define("hello")
    print(definition.word) # Outputs "hello"

Asynchronous Example
~~~~~~~~~~~~~~~~~~~~

.. code:: py

    import asyncio

    import pyud


    async def example():
        ud = pyud.AsyncClient()
        definition = await ud.define("hello")
        print(definition.word) # Outputs "hello"


    async def main():
        await example()

    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

License
-------

`GNU GPL v3 <https://www.gnu.org/licenses/gpl-3.0.en.html>`_