getuser = {
    'aliases': ['mention', 'user'],
    'brief': 'Mentions a user',
    'description': 'Mentions the user who\'s ID was entered',
    'enabled': True,
    'hidden': False,
    'usage': 'Params: "User ID"'
}

getperms = {
    'aliases': ['g', 'perms'],
    'brief': 'Gets a user\'s perms.',
    'description': 'Gets all of a specified user\'s perms, requires manage roles.',
    'enabled': True,
    'hidden': False,
    'usage': 'Params: @user*',
}

lockchannel = {
    'aliases': ['l', 'lock'],
    'brief': 'Keep users from sending messages.',
    'description': 'Stops non-admin users from sending messages in the specified channel.',
    'enabled': True,
    'hidden': False,
    'usage': 'Params: #channel*'
}

unlock = {
    'aliases': ['u', 'unl'],
    'brief': 'Unlocks channel.',
    'description': 'Lets non-admin users send messages in a previously locked server.',
    'enabled': True,
    'hidden': False,
    'usage': 'Params: #channel*'
}

kick = {
    'aliases': ['k', 'kickmember'],
    'brief': 'Kicks user from the server,',
    'description': 'Kicks the specified user from the server.',
    'enabled': True,
    'hidden': False,
    'usage': 'Params: "reason" @user'
}

ban = {
    'aliases': ['b', 'banmember'],
    'brief': 'Bans user from the server',
    'description': 'Bans the specified user from the server for undetermined time',
    'enabled': True,
    'hidden': False,
    'usage': 'Params: "reason" @user'
}

warn = {
    'aliases': ['w', 'warnuser'],
    'brief': 'Formally warns a user',
    'description': 'Formally warns specified user for the given reason.',
    'enabled': True,
    'hidden': False,
    'usage': 'Params: "reason" @user'
}

showwarns = {
    'aliases': ['s', 'warns', 'show'],
    'brief': 'Shows warns for a user',
    'description': 'Shows all warns for the specified user',
    'enabled': True,
    'hidden': False,
    'usage': 'Params: @user'
}
