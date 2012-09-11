import commands
import os

from django.conf import settings
from pipeline.compilers import CompilerBase


class GameCompiler(CompilerBase):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('game.js')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return 
        return commands.getoutput(
            "%s build game" % os.path.join(settings.SITE_ROOT, 'static/limejs/bin/lime.py')
        )
