#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Form Example</title>'
echo '</head>'
echo '<body   bgcolor="#007bff" text="#000000" > '


echo '<div align="center"> '
echo '<br><br><br>'
echo '<h1 style="font-family:Impact; color:f7b815; font-size:40px;" >Jack Experts </h1>'
echo '<p  style="font-family:Roboto; color:fffff; font-size:20px;" 
style="color:white;">Soma</p>'
echo "<form  method=GET action=\"result.cgi\">" \
      '<table nowrap  >' \
      '<tr><td>Valor 1  </TD><TD><input style="border-radius: 10px;" type="text" name="val1" size=8></td></tr>' \
      '<tr><td>Valor 2  </td><td><input style="border-radius: 10px;"  type="text" name="val2" size=8 value=""></td>' \
      '</tr></table> '

#
echo ' <br><input style="border-radius: 10px; background-color:#53ff1a;"  type="submit" value="Calculate">' \
      '<input style="border-radius: 10px; width:90; background-color:red;"  type="reset" value="Reset"></form></div>'


echo '</body>'
echo '</html>'
