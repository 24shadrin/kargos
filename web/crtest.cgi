#!/usr/bin/perl

#require "sfile";

    print "Content-Type: text/html\n\n";
    print "<html>";

    print "<body>";
    print "\n";

@dat=($day, $month, $year) = (localtime)[3,4,5];

$t1=@dat[0];
$t2=@dat[1]+1;
$t3=@dat[2]+1900;

$t0=0;

if ( $t1 < 10 )
{
$tt=$t0.$t1;
}

else
{
$tt=$t1;
}


###$truedat=$sfile::fullpath;

###$p="/home/pi/beward/$truedat/beward/1";

$url="index.html";

###system "cd /var/www/web/jpg && rm /var/www/web/jpg/*";

$path="jpg";

###system "cd $p && ls  $p |grep jpg |tail -n 20 |xargs cp  --target-directory=/var/www/web/jpg";

###system "ls  /var/www/web/jpg > /var/www/web/list";

print "<p><a href=$url> back</a></p>";
print "<br>";
$param="wedth=20%";
open(filo, "list") || die "file daz not eksist";
while ($line = <filo>)
{
#print "<img src=$path/$line width=20% align=right>";
print "<img src=$path/$line>";

#print $line;
}
close(filo);

print "\n";

print "<br>";
"\n";

print "<p><a href=$url> back</a></p>";

    print "</body>";
    print "</html>";
print "\n";
