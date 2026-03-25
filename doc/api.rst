discid API
==========

.. automodule:: discid
   :synopsis: Python binding of Libdiscid

Constants
---------
At the module level there are these constants available:

.. autodata:: LIBDISCID_VERSION_STRING
   :annotation:
.. autodata:: FEATURES
   :annotation:
.. autodata:: FEATURES_IMPLEMENTED

Functions
---------
These functions are used to create a :class:`Disc` object.

.. autofunction:: read
.. autofunction:: put

You can get the device that is used as a default with

.. autofunction:: get_default_device

Disc object
-----------
.. autoclass:: Disc
   :undoc-members:

   .. autoproperty:: id
   .. autoproperty:: freedb_id
   .. autoproperty:: submission_url
   .. autoproperty:: toc_string

      .. versionadded:: 1.1

   .. autoproperty:: cddb_query_string

      .. versionadded:: 1.3

   .. autoproperty:: first_track_num
   .. autoproperty:: last_track_num
   .. autoproperty:: sectors
   .. autoproperty:: length
   .. autoproperty:: seconds
   .. autoproperty:: mcn
   .. autoproperty:: tracks

Track object
------------
.. autoclass:: Track
   :undoc-members:

   .. autoproperty:: number
   .. autoproperty:: offset
   .. autoproperty:: sectors
   .. autoproperty:: length
   .. autoproperty:: seconds
   .. autoproperty:: isrc

Exceptions
----------
The discid module includes a custom exception to handle specific problems:

.. autoexception:: DiscError
   :show-inheritance:
.. autoexception:: TOCError
   :show-inheritance:
