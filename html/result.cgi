#!/bin/bash

echo "Content-type: text/html"
echo ""


var1=`echo "$QUERY_STRING" | awk '{split($0,array,"&")} END{print array[1]}' | awk '{split($0,array,"=")} END{print array[2]}'`
var2=`echo "$QUERY_STRING" | awk '{split($0,array,"&")} END{print array[2]}' | awk '{split($0,array,"=")} END{print array[2]}'`

echo '<small><em>'
echo "Time " $(date +%H:%M:%S)
echo '<br>'
echo "CPU:$(top -b -n 1 | grep "Cpu(s)" | awk '{print $2 + $4}')"
echo '<br>'
echo "Mem:$(free -m | awk 'NR==2{printf "%.2f%%\t\t", $3*100/$2 }')"
echo '<br>'
echo "Disk used:$(df -h | awk '$NF=="/"{printf "%s", $5}')"
echo '<br>'
echo "sensors temp:$(sensors | grep "Core 0" | awk '{print $3}')"
echo '</em></small>'

/bin/cat << EOM
<HTML>
<head >

</head>
<body bgcolor="#ffffff" text="#000000">

<HR SIZE=5>

<h1 align="center" >Resultado : $((var1+var2))  </h1>
<HR SIZE=5>

<div style="line-heigth:100px;"
 border="5" align="center">
 <img    src="https://jackexperts.com/assets/img/jac/preto.png"  width="190" height="120"  />

</div>

<meta http-equiv="refresh" content="3" url="result.cgi">
