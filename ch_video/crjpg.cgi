#!/usr/bin/perl

    print "Content-Type: text/html\n\n";
    print "<html>";

    print "<body>";
    print "\n";

@dat=($day, $month, $year) = (localtime)[3,4,5];

$t1=@dat[0];
$t2=@dat[1]+1;
$t3=@dat[2]+1900;

$truedat=join('-',$t3,$t2,$t1);

$url="index.html";

system "/web/subfolder";

$path="jpg";

print "<p><a href=$url> <--back</a></p>";

open(filo, "list") || die "file daz not eksist";
while ($line = <filo>)
{
print "<img src=$path/$line width=20%>";
}
close(filo);

print "\n";

print "<br>";
"\n";

print "<p><a href=$url> <--back</a></p>";

    print "</body>";
    print "</html>";
print "\n";