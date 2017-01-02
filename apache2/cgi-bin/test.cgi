#!/usr/bin/perl -w

# Test Script to verify execution of CGI scripts
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard :html3);
use Digest::MD5 qw(md5_hex);
use MIME::Base64;

print "Content-Type: text/html\n\n";

$time=time;
print "<html><head>\n";
print "<title>CGI Script Test.CGI Execution Successful</title></head>\n";
print "Session ID Test:  ",$time,p,
"Base64 Encoding:  ",encode_base64("secret"),p,
"MD5 Hash:  ",md5_hex("secret"),p,p,
"<body><p>This concludes our test....</body></html>\n";
