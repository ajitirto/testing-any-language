#!/bin/bash

# simple test python 
echo "########PYHTON###########"
python3 python/test_add.py
echo "########PYHTON###########"



echo "########PHP###########"
 ~/development-app/testing-any-language/php/vendor/bin/phpunit ~/development-app/testing-any-language/php/MathTest.php
echo "########PHP###########"


echo "########GO###########"
cd go;
go test;
cd ..
echo "########GO###########"