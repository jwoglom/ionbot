# Copyright (C) 2013 Fox Wilson, Peter Foley, Srijay Kasturi, Samuel Damashek and James Forcier
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from config import CMDCHAR
from inspect import getdoc

args = ['modules', 'nick', 'connection']


def cmd(send, msg, args):
    if msg:
        if msg[0] == CMDCHAR:
            msg = msg[1:]
        if len(msg.split()) > 1:
            send("One argument only")
            return
        if msg not in args['modules']:
            send("Not a module.")
            return
        else:
            doc = getdoc(args['modules'][msg].cmd)
            if doc is None:
                send("No documentation found.")
            else:
                send(doc)
    else:
        modules = sorted(args['modules'])
        num = int(len(modules) / 2)
        cmdlist1 = ' !'.join([x for x in modules[:num]])
        cmdlist2 = ' !'.join([x for x in modules[num:]])
        args['connection'].privmsg(args['nick'], 'Commands: !' + cmdlist1)
        args['connection'].privmsg(args['nick'], '!' + cmdlist2)
