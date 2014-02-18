from jinja2 import nodes
from jinja2.ext import Extension
from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
import six

import pelican.settings as pys


class CodeHighlight(Extension):
    tags = set(['syntax'])

    def parse(self, parser):
        lineno = parser.stream.next().lineno

        # get language, if set
        if parser.stream.current.test('string'):  # no lang supplied
            args = [parser.parse_expression()]
        else:  # format as plain text
            args = [nodes.Const(None)]

        body = parser.parse_statements(['name:endsyntax'], drop_needle=True)

        return nodes.CallBlock(self.call_method('_pygmentize', args),
                               [], [], body).set_lineno(lineno)

    def _pygmentize(self, name, caller):
        self.options = {}

        try:
            lexer = get_lexer_by_name(name)
        except ValueError:
            lexer = TextLexer()
        content = caller()

        # Fetch the defaults
        if pys.PYGMENTS_RST_OPTIONS is not None:
            for k, v in six.iteritems(pys.PYGMENTS_RST_OPTIONS):
                # Locally set options overrides the defaults
                if k not in self.options:
                    self.options[k] = v

        if ('linenos' in self.options and
                self.options['linenos'] not in ('table', 'inline')):
            if self.options['linenos'] == 'none':
                self.options.pop('linenos')
            else:
                self.options['linenos'] = 'table'

        for flag in ('nowrap', 'nobackground', 'anchorlinenos'):
            if flag in self.options:
                self.options[flag] = True

        # noclasses should already default to False, but just in case...
        formatter = HtmlFormatter(noclasses=False, **self.options)
        parsed = highlight(content, lexer, formatter)

        return parsed
