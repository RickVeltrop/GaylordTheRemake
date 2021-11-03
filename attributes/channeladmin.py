lockchannel = {
    'aliases': ['l', 'lock'],
    'brief': 'Keep users from sending messages.',
    'description': 'Stops non-admin users from sending messages in the specified channel.',
    'enabled': True,
    'hidden': False,
    'usage': '#channel*'
}

unlock = {
    'aliases': ['u', 'unl'],
    'brief': 'Unlocks channel.',
    'description': 'Lets non-admin users send messages in a previously locked server.',
    'enabled': True,
    'hidden': False,
    'usage': '#channel*'
}

purge = {
    'aliases': ['p', 'purgechannel'],
    'brief': 'Purges a channel.',
    'description': 'Purges a channel of all messages unless an amount or user is specified.',
    'enabled': True,
    'hidden': False,
    'usage': 'amount(number or inf)* @user* #channel*'
}

spam = {
    'aliases': ['s', 'sendspam'],
    'brief': 'Spams a message.',
    'description': 'Spams the entered message a certain amount.',
    'enabled': True,
    'hidden': False,
    'usage': 'amount "msg" channel*'
}
