#!/usr/bin/env bash
set -eu

# Demonstrates curl and the public JSONPlaceholder API.
curl --version
printf '\n--- Fetch a web page ---\n'
curl -L http://example.com
printf '\n--- Fetch JSON posts ---\n'
curl https://jsonplaceholder.typicode.com/posts
printf '\n--- Response headers only ---\n'
curl -I https://jsonplaceholder.typicode.com/posts
printf '\n--- Simulated POST request ---\n'
curl -X POST -d 'title=foo&body=bar&userId=1' https://jsonplaceholder.typicode.com/posts
printf '\n'
