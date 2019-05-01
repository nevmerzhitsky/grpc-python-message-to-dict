# A converter of proto3 message to a Python dictionary

It can be terrible to work with ProtoBuffers 3 messages in a read-only mode. This solution simplify
this task by converting any kind of message to a well-known Python dictionary.

It use Docker for demonstration: just run `build-and-run.sh`. It will output a server and a client
logs to STDOUT. You will see how the server converts input messages to dictionaries.

To re-use the solution just copy-paste content of `converter.py` module.
