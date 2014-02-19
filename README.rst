Plumage
=======

Colourful syntax for your Pelican.


Uhh, what?
----------

This is a `Jinja2`_ extension to allow you to render a `Pygments`_
fragment against an ``.html``-formatted Pelican article. Typically
only ``rST`` files implement the Pygments Directive.


Installation
-----------

Requires the `html_jinja2`_ Pelican plugin.

Add this module to your ``pelicanconf.py`` settings:

::

  JINJA_EXTENSIONS = ['plumage.plumage.CodeHighlight',]


Usage
-----

Adds support for a new Jinja2 tag

With language arg (passed to Pygment's lexer lookup)::

  {% syntax 'python' %}
  import this
  {% endsyntax %}


Or without for plain, but preformatted text::

  {% syntax %}
  >> $('body').find('a');
  ...
  {% endsyntax %}


Known Issues
------------

If you use `Typogrify`_ you'll need to disable it as it rewrites
single quotes in the tag to HTML entities.

A workaround or fix is currently #TODO.


License
-------

As this work conveys modified source from `Pelican`_ itself, it is licensed
under the same terms; The GNU Affero General Public License, v3.


.. _`Jinja2`: http://jinja.pocoo.org/
.. _`Pygments`: http://pygments.org/
.. _`html_jinja2`: https://github.com/mattoc/html_jinja2
.. _`Typogrify`: https://github.com/mintchaos/typogrify
.. _`Pelican`: https://github.com/getpelican/pelican
