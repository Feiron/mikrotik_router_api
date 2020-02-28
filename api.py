#!/usr/bin/python

import configparser
import os
import sys
import routeros_api

iniPath = 'settings.ini'

if os.path.exists(iniPath):

    #
    # if error
    # cant cancat str in bytes error
    # in routeros_api/sentence.py #58 ADD
    # if type(value) == str:
    #    value = str.encode(value)
    #

    arAvailableCommands = ['enable', 'disable']

    config = configparser.ConfigParser()
    config.read(iniPath)

    user = config.get('Main', 'user')
    password = config.get('Main', 'password')
    host = config.get('Main', 'host')
    port = int(config.get('Main', 'port'))
    device = config.get('Main', 'device')

    command = 'disable'

    args = sys.argv

    if len(sys.argv) > 1:
        command = sys.argv[1]

    if len(command) == 0 or (command not in arAvailableCommands):
        command = 'disable'

    if len(sys.argv) > 2:
        device = sys.argv[2]

    if len(device) == 0:
        raise Exception('NO_DEVICE')

    if len(user) == 0:
        user = 'admin'

    if len(password) == 0:
        password = ''

    if len(host) == 0 or port <= 0:
        raise Exception('NO_HOST')

    connection = routeros_api.RouterOsApiPool(
        host,
        username=user,
        password=password,
        port=port,
        plaintext_login=True,  # Добавил вчера
        use_ssl=False,
        ssl_verify=False,
        ssl_verify_hostname=False,
        ssl_context=None,
    )

    api = connection.get_api()
    api.get_binary_resource('/interface/ethernet').call(command, {'numbers': device})

    connection.disconnect()

else:
    print('INI_NOT_SET')
