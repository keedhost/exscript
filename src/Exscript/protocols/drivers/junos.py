# Copyright (C) 2007-2010 Samuel Abels.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""
A driver for devices running JunOS (by Juniper).
"""
import re
from driver import Driver

_user_re     = re.compile(r'[\r\n]login: $')
_password_re = re.compile(r'[\r\n]Password: $')
_prompt_re   = re.compile(r'(?:[\r\n]\[edit\])?[\r\n][\w\-]+@[\-\w+\.]+[>#] $')
_junos_re    = re.compile(r'\bjunos\b', re.I)

class JunOSDriver(Driver):
    def __init__(self):
        Driver.__init__(self, 'junos')
        self.user_re     = _user_re
        self.password_re = _password_re
        self.prompt_re   = _prompt_re

    def check_head_for_os(self, string):
        if _junos_re.search(string):
            return 80
        if _user_re.search(string):
            return 35
        return 0

    def init_terminal(self, conn):
        conn.execute('set cli screen-length 0')
        conn.execute('set cli screen-width 0')
        conn.execute('set cli terminal ansi')