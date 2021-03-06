#!/usr/bin/env python

# This file is part of the Printrun suite.
#
# Printrun is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Printrun is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Printrun.  If not, see <http://www.gnu.org/licenses/>.

import sys

try:
    import wx  # NOQA
except:
    print("wxPython is not installed. This program requires wxPython to run.")
    if sys.version_info.major >= 3:
        print("""\
As you are currently running python3, this is most likely because wxPython is
not yet available for python3. You should try running with python2 instead.""")
        sys.exit(-1)
    else:
        raise

from printrun.pronterface import PronterApp
from wxPython._misc import wxLogNull

if __name__ == '__main__':
    nullTarget = wxLogNull()
    app = PronterApp(False)
    try:
        app.MainLoop()
    except KeyboardInterrupt:
        pass
    del app
