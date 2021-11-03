getuser = {
    'aliases': ['mention', 'user'],
    'brief': 'Mentions a user',
    'description': 'Mentions the user who\'s ID was entered',
    'enabled': True,
    'hidden': False,
    'usage': '"User ID"'
}

getperms = {
    'aliases': ['g', 'perms'],
    'brief': 'Gets a user\'s perms.',
    'description': 'Gets all of a specified user\'s perms, requires manage roles.',
    'enabled': True,
    'hidden': False,
    'usage': '@user*',
}

kick = {
    'aliases': ['k', 'kickmember'],
    'brief': 'Kicks user from the server,',
    'description': 'Kicks the specified user from the server.',
    'enabled': True,
    'hidden': False,
    'usage': '"reason" @user'
}

ban = {
    'aliases': ['b', 'banmember'],
    'brief': 'Bans user from the server',
    'description': 'Bans the specified user from the server for undetermined time',
    'enabled': True,
    'hidden': False,
    'usage': '"reason" @user'
}

warn = {
    'aliases': ['w', 'warnuser'],
    'brief': 'Formally warns a user',
    'description': 'Formally warns specified user for the given reason.',
    'enabled': True,
    'hidden': False,
    'usage': '"reason" @user'
}

showwarns = {
    'aliases': ['warns', 'show'],
    'brief': 'Shows warns for a user',
    'description': 'Shows all warns for the specified user',
    'enabled': True,
    'hidden': False,
    'usage': '@user'
}
