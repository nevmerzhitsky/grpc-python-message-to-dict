# A converter of proto3 message to a Python dictionary

It can be terrible to work with ProtoBuffers 3 messages in a read-only mode. This solution
simplifies this task by converting any kind of message to a well-known Python dictionary.

It uses Docker for demonstration: just run `build-and-run.sh`. It will output a server and a client
logs to STDOUT. You will see how the server converts input messages to dictionaries.

To re-use the solution just copy-paste the content of `converter.py` module.

Note that `converter.message_to_dict.pythonify_value()` contains specific conditions for casting.
You can remove them or extend.
