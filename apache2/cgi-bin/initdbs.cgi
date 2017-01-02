#!/usr/bin/perl -w

### Script to build initial databases for BadStore.net v2.0 ###

### Specify required PERL modules ###
use CGI::Carp qw(fatalsToBrowser);
#use strict;
use DBI();

print "Content-type: text/html\n\n";

### If the databases exist - delete them ###
if (-e "/usr/local/apache/data/guestbookdb") {
	`rm /usr/local/apache/data/guestbookdb`;
	`touch /usr/local/apache/data/guestbookdb`;
	`chown 65534 /usr/local/apache/data/guestbookdb`;
} 
`/usr/local/mysql/bin/mysqladmin drop badstoredb -f`;

### Create new databases and tables ###
my $drh = DBI->install_driver("mysql");
my $rc = $drh->func("createdb", badstoredb, localhost, root, secret, 'admin');

# Connect to the database
my $dbh = DBI->connect("DBI:mysql:database=badstoredb;host=localhost", "root", "secret",{'RaiseError' => 1});

### Create orderdb table
$dbh->do("CREATE TABLE orderdb (sessid INTEGER, orderdate DATE, ordertime TIME, ordercost VARCHAR(10), orderitems INTEGER, itemlist VARCHAR(50), accountid VARCHAR(30), ipaddr VARCHAR(20), cartpaid VARCHAR(1), ccard VARCHAR(16), expdate VARCHAR(4))");
### Add orders to orderdb
$dbh->do("INSERT INTO orderdb VALUES (1078228766,CURDATE(),CURTIME(),'\$46.95',3,'1000,1003,1008','joe\@supplier.com','10.10.10.50','Y','4111111111111111','0705'),
(1078228767,CURDATE(),CURTIME(),'\$46.95',3,'1000,1003,1008','joe\@supplier.com','10.10.10.150','Y','5500000000000004','0905'),
(1078229834,SUBDATE(CURDATE(),1),SUBTIME(CURTIME(),1),'\$22.95',1,'1008','joe\@supplier.com','10.10.10.50','Y','340000000000009','1008'),
(1078232948,SUBDATE(CURDATE(),1),SUBTIME(CURTIME(),'2:5:2'),'\$144.93',3,'1011,1012,1014','mary\@spender.com','192.168.10.70','Y','30000000000004','0506'),
(1078232048,SUBDATE(CURDATE(),1),CURTIME(),'\$137.90',3,'1008,1009,1011','sue\@spender.com','10.10.10.350','Y','601100000004','1006'),
(1078228766,CURDATE(),CURTIME(),'\$46.95',3,'1000,1003,1008','joe\@supplier.com','10.10.10.50','Y','4111111111111111','0705'),
(1078228767,SUBDATE(CURDATE(),2),CURTIME(),'\$46.95',3,'1000,1003,1008','joe\@supplier.com','10.10.10.150','Y','5500000000000004','0905'),
(1078229834,SUBDATE(CURDATE(),2),SUBTIME(CURTIME(),'8:9:4'),'\$22.95',1,'1008','joe\@supplier.com','10.10.10.50','Y','340000000000009','1008'),
(1078232048,SUBDATE(CURDATE(),2),SUBTIME(CURTIME(),'2:34:8'),'\$137.90',3,'1008,1009,1011','mary\@spender.com','192.168.10.70','Y','30000000000004','0506'),
(1078232048,SUBDATE(CURDATE(),2),CURTIME(),'\$137.90',3,'1008,1009,1011','sue\@spender.com','10.10.10.350','Y','6011000000000004','1006'),
(1078228766,SUBDATE(CURDATE(),3),CURTIME(),'\$46.95',3,'1000,1003,1008','joe\@supplier.com','10.10.10.50','Y','4111111111111111','0705'),
(1078228767,SUBDATE(CURDATE(),3),CURTIME(),'\$46.95',3,'1000,1003,1008','joe\@supplier.com','10.10.10.150','Y','5500000000000004','0905'),
(1078229834,SUBDATE(CURDATE(),3),CURTIME(),'\$22.95',1,'1008','joe\@supplier.com','10.10.10.50','Y','340000000000009','1008'),
(1078232048,SUBDATE(CURDATE(),3),CURTIME(),'\$137.90',3,'1008,1009,1011','mary\@spender.com','192.168.10.70','Y','30000000000004','0506'),
(1078232048,SUBDATE(CURDATE(),4),SUBTIME(CURTIME(),'3:6:2'),'\$137.90',3,'1008,1009,1011','sue\@spender.com','10.10.10.350','Y','6011000000000004','1006'),
(1078228766,SUBDATE(CURDATE(),6),SUBTIME(CURTIME(),'7:2:8'),'\$46.95',3,'1000,1003,1008','joe\@supplier.com','10.10.10.50','Y','4111111111111111','0705'),
(1078228767,SUBDATE(CURDATE(),7),CURTIME(),'\$46.95',3,'1000,1003,1008','joe\@supplier.com','10.10.10.150','Y','5500000000000004','0905'),
(1078229834,SUBDATE(CURDATE(),13),SUBTIME(CURTIME(),'2:4:9'),'\$22.95',1,'1008','joe\@supplier.com','10.10.10.50','Y','340000000000009','1008'),
(1078232048,SUBDATE(CURDATE(),19),CURTIME(),'\$137.90',3,'1008,1009,1011','mary\@spender.com','192.168.10.70','Y','30000000000004','0506'),
(1078232388,SUBDATE(CURDATE(),19),CURTIME(),'\$1137.90',3,'1008,1009,1011','sue\@spender.com','10.10.10.350','Y','6011000000000004','1006'),
(1078233380,SUBDATE(CURDATE(),35),CURTIME(),'\$360.00',1,'1002','fred\@newuser.com','172.22.15.47','Y','201400000000009','0705')");

### Create userdb table
$dbh->do("CREATE TABLE userdb (email VARCHAR(40), passwd VARCHAR(32), pwdhint VARCHAR(8), fullname VARCHAR(50), role VARCHAR(1))");
### Add users to userdb
$dbh->do("INSERT INTO userdb VALUES ('AAA_Test_User','098F6BCD4621D373CADE4E832627B4F6','black','Test User','U'),
('admin','5EBE2294ECD0E0F08EAB7690D2A6EE69','black','Master System Administrator','A'),
('joe\@supplier.com','62072d95acb588c7ee9d6fa0c6c85155','green','Joe Supplier','S'),
('big\@spender.com','9726255eec083aa56dc0449a21b33190','blue','Big Spender','U'),
('ray\@supplier.com','99b0e8da24e29e4ccb5d7d76e677c2ac','red','Ray Supplier','S'),
('robert\@spender.net','e40b34e3380d6d2b238762f0330fbd84','orange','Robert Spender','U'),
('bill\@gander.org','5f4dcc3b5aa765d61d8327deb882cf99','purple','Bill Gander','U'),
('steve\@badstore.net','8cb554127837a4002338c10a299289fb','red','Steve Owner','U'),
('fred\@whole.biz','356c9ee60e9da05301adc3bd96f6b383','yellow','Fred Wholesaler','U'),
('debbie\@supplier.com','2fbd38e6c6c4a64ef43fac3f0be7860e','green','Debby Supplier','S'),
('mary\@spender.com','7f43c1e438dc11a93d19616549d4b701','blue','Mary Spender','U'),
('sue\@spender.com','ea0520bf4d3bd7b9d6ac40c3d63dd500','orange','Sue Spender','U'),
('curt\@customer.com','0DF3DBF0EF9B6F1D49E88194D26AE243','green','Curt Wilson','U'),
('paul\@supplier.com','EB7D34C06CD6B561557D7EF389CDDA3C','red','Paul Rice','S'),
('kevin\@spender.com',NULL,NULL,'Kevin Richards','U'),
('ryan\@badstore.net','40C0BBDC4AEEAA39166825F8B477EDB4','purple','Ryan Shorter','A'),
('stefan\@supplier.com','8E0FAA8363D8EE4D377574AEE8DD992E','yellow','Stefan Drege','S'),
('landon\@whole.biz','29A4F8BFA56D3F970952AFC893355ABC','purple','Landon Scott','U'),
('sam\@customer.net','5EBE2294ECD0E0F08EAB7690D2A6EE69','red','Sam Rahman','U'),
('david\@customer.org','356779A9A1696714480F57FA3FB66D4C','blue','David Myers','U'),
('john\@customer.org','EEE86E9B0FE29B2D63C714B51CE54980','green','John Stiber','U'),
('heinrich\@supplier.de','5f4dcc3b5aa765d61d8327deb882cf99','red','Heinrich H√ºber','S'),
#('ichiro\@customer.jp','AEA6DE9CBAEE9D2704DCF81F4A194991','blue','Â±±Âè£„ÄÄ‰∏ÄÈÉ,'U'),
('tommy\@customer.net','7f43c1e438dc11a93d19616549d4b701','orange','Tom O''Kelley','U')");

### Create itemdb table
$dbh->do("CREATE TABLE itemdb (itemnum INTEGER, sdesc VARCHAR(20), ldesc VARCHAR(40), qty INTEGER, cost FLOAT(8,2), price FLOAT(8,2), isnew VARCHAR(1))");
#Add items to itemdb
$dbh->do("INSERT INTO itemdb VALUES (1000,'Snake Oil','Useless but expensive',5,4.35,11.50,'Y'),
(1001,'Crystal Ball','The finest Austrian crystal for complete clarity',2,13.95,49.95,'N'),
(1002,'Magic Hat','The classic magicians hat',7,18.45,60.00,'N'),
(1003,'Magic Rabbit','Cute white bunny',27,3.50,12.50,'Y'),
(1004,'Security Appliance','Everybody needs one',3,400,3999,'N'),
(1005,'Perfect Code','The rarest magic of all',1,5,5000.00,'Y'),
(1006,'Security Blanket','Keeps you warm and toasty',4,9.5,16.00,'N'),
(1007,'Bag ''o Fud','For those who believe anything',9,.50,200,'N'),
(1008,'ROI Calculator','Accurate Return on Investment',99,2.30,22.95,'Y'),
(1009,'Planning Template','Business Planning Tool',2,6.7,24.95,'Y'),
(1010,'Security 911','Technical Support Agreement',1,99,9999,'N'),
(1011,'Money','There''s never enough',1,3,90.00,'Y'),
(1012,'Endless Cup','Perfect for late nights',74,4.56,23.98,'Y'),
(1013,'Invisibility Cloak','For when you just want to hide',1,0,8995,'N'),
(1014,'Disappearing Ink','Makes perfect signatures',43,8.96,30.95,'Y'),
(9999,'Test','Test Item',0,0,0,'N')");

### Create acctdb table
$dbh->do("CREATE TABLE acctdb (invnum VARCHAR(20), amount FLOAT(8,2), status VARCHAR(10), paidon DATE, bankinfo VARCHAR(20), rma CHAR(1))");
#Add items to acctdb
$dbh->do("INSERT INTO acctdb VALUES ('MS-45921',4976.48,'Paid',CURDATE(),'33011:38349873766',0),
('MS-45876',983.93,'Submitted',CURDATE(),'33011:38349873766',1),
('MS-45873',34897.21,'Received',SUBDATE(CURDATE(),1),'78011:38334587297',0)");

# Disconnect from the database.
$dbh->disconnect();

### Create Guestbookdb file
# if exists
open(FILE, ">>/usr/local/apache/data/guestbookdb") or die("Unable to open Guestbook data file: $!\n");
print FILE ("Wednesday, February 18, 2004 at 07:42:34~Joe Shopper~joe\@microsoft.com~This is a great site!  I'm going to shop here every day.\n");
print FILE ("Wednesday, February 18, 2004 at 11:41:07~John Q. Public~jqp\@whitehouse.gov~Let me know when the summer items are in.\n");
print FILE ("Friday, February 20, 2004 at 14:05:22~Big Spender~billg\@microsoft.com~Where's the big ticket items?\n");
print FILE ("Sunday, February 22, 2004 at 06:16:05~Evil Hacker~s8n\@haxor.com~You have no security!  I can own your site in less than 2 minutes.  Pay me \$100,000 US currency by the end of day Friday, or I will hack you offline and sell the credit card numbers I found on your site.  Send the money direct to my PayPal account.\n");
close(FILE);

print "<HTML><HEAD><H1>BadStore.net - Database Reset</H1></HEAD><BODY><p><hr><p>Databases have been reset...</BODY></HTML>\n";
