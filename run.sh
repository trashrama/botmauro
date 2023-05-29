#!/bin/bash
rm -R cache.json
rm -R replies.json
~/.fly/bin/flyctl ssh sftp get /bot/cache.json cache.json
~/.fly/bin/flyctl ssh sftp get /bot/replies.json replies.json

