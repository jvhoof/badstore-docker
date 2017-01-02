/* Cardvrfy.js - Part of BadStore.net */

function DoCardvrfy(x)
{

var card=(x["ccard"].value);
var cexp=(x["expdate"].value);
var validcard= /([0-9]{13,16})/;
var validexpr= /([0-9]{4})/;
var mastercard= /(5[0-9]{15})/;
var visacard= /(4[0-9]{15})/;
var amexcard= /(3[0-9]{14})/;
var discovercard= /(6011[0-9]{12})/;

// Check for input
if ((card == '') || (cexp == ''))  {
	alert("You haven't entered enough information!");
 	return false; 
}

// Ensure only numbers

if (!validcard.exec(card)) {
	alert("Only valid numbers are allowed - and no spaces or dashes!");
	return false; 
}

// Check for a MasterCard
if (mastercard.test(card)) {
	alert("Thank you for using MasterCard!");
	return true;
}

// Check for Visa
if (visacard.exec(card)) {
	alert("Thank you for using Visa!");
	return true;
}

// Check for American Express
if (amexcard.exec(card)) {
	alert("Thank you for using American Express!");
	return true;
}

// Check for Discover
if (discovercard.exec(card)) {
	alert("Thank you for using Discover!");
	return true;
}

// Unknown credit card type
alert("You have entered an unaccepted card - please use a supported method of payment");
return false;
}

