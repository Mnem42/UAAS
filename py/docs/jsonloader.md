# JSON loader `(prefloader.py)`

This file manages all JSON loading (e.g. checklists,ip targets). This also does
file loading. It can print formatted entries for status, if the parameter
nescessary is set. Ignore things in function signatures enclosed in square
brackets.

#### `load_file(print_status[bool],name[string])`

This loads a file, and parses the JSON. `print_status` should be set to `True`
to print formatted messages. It throws errors, even if `print_status` is set
to `True`.

#### `load_ipaddrs(print_status[bool],name[string])`

This loads ip addresses, with a specific format. If `print_details` is set to
`True`, it prints formatted text. It does not throw anyy errors internally
(all errors thrown by it are from some function called within it).