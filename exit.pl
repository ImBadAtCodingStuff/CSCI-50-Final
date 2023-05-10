#!/usr/bin/perl
#	Primary Author: Nicole Niesen

print ("Would you like to exit the program? Y/N: ");
$choice = <STDIN>;
chomp($choice);
$ch = lc $choice;
$yes = "y";
$no = "n";
if ($ch eq $yes) {
	exit;
}
else {
	system("sh", "MainMenuSelect.sh")
}