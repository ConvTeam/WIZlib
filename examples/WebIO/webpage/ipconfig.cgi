<html>
<head>
<title></title>
<script language=javascript>
j=5;
function func(){
	document.getElementById('delay').innerText=' '+j+' ';
	j--;
	setTimeout('func()',1000);
	if(j<0)
		location.href='ipconfig.htm';
}
</script>
</head>

<body onload='func()'>
Please wait for a while, the configuration page will be loaded automatically in<span style='color:red;' id='delay'></span> seconds.
</body>
</html>

<!--
<? SetValue(IP) ?>
<? SetValue(GW) ?>
<? SetValue(SUB) ?>
<? SetValue(DNS) ?>
-->
