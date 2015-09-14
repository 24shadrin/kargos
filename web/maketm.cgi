#!/usr/bin/perl

    print "Content-Type: text/html\n\n";
    print "<html>";
    print "<body>";
    print "<meta charset='utf-8'/>";
$url="http://192.168.0.200/web/timelapse/";
$filo="/var/www/web/timelapse/today.avi";
$time=localtime;
$lock="/var/www/web/lock/lock";

#$tm=system "/var/www/web/tm";
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
print $bufer;

if(-e "$lock"){
print "<p style=font-family:times;font-size:400%;color:red>";
print "Процесс склейки уже запущен. Попробуйте через 5 минут.";
}
else
{
$tm=system "/var/www/web/tm";


if(-e "$filo") {
print "<img src=images/beward.jpg>";
print "<p style=font-family:times;font-size:400%;color:blue>";
print "Склейка завершена. ";

@mas=split(" ", $time);
print (join(" ", @mas[2],@mas[1],@mas[3]));
print "\n";

print "<br>";
print "Кликните на картинку!";
print "</p>";

@flist = glob "fortm/*.jpg";
$i=$#flist;
$j=@flist[$i];


print "<p><a href=timelapse/today.avi><img src=$j width=640 height=480 alt=click></a></p>";
}
else
{
print "<p style=font-family:times;font-size:400%;color:red>";
print "Что-то пошло не так. Попробуйте через 5 минут";
print "</p>";
}
}
print "\n";
