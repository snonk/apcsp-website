#!/bin/bash

echo -e "Content-type: text/html\n\n"
echo "<h1>Status of Raspberry Pis: </h1>"
echo "<pre>$(./rpistatus)</pre>"
