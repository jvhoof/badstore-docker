#!/usr/bin/perl -w

#########################################
# bsheader.cgi v1.2
# Cart header program for BadStore.net
#########################################

use CGI qw(:standard);
use MIME::Base64;

### Read CartID Cookie ###
$ctemp=cookie('CartID');
@c_cookievalue=split(":", ("$ctemp"));
$id=shift(@c_cookievalue);
$items=shift(@c_cookievalue);
$cost=shift(@c_cookievalue);
$price='$' . sprintf("%.2f", $cost);

### Read SSOid Cookie ###
$stemp=cookie('SSOid');
$stemp=decode_base64($stemp);
@s_cookievalue=split(":", ("$stemp"));
$email=shift(@s_cookievalue);
$passwd=shift(@s_cookievalue);
$fullname=shift(@s_cookievalue);

if ($fullname eq '') {
	$fullname="{Unregistered User}";
}

if ($items eq '') {
	$items="0";
}

print "Content-type: text/html\n\n";

print qq|
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
  <meta http-equiv="Content-type" content="text/html;charset=utf-8" />
  <link rel="stylesheet" type="text/css" href="/css/global.css" media="all" />
  <style type="text/css">html,body {background-color:transparent !important; background-color:inherit}</style>
</head>
<body>
 Welcome <B> $fullname </B> - Cart contains $items items at $price
</body>
</html>|;	  
