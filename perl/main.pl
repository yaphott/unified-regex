use utf8;
use open qw(:std :utf8);
use Encode;

sub iterate_codepoints {
    my ($pattern, $file_path) = @_;
    open(my $fh, '>', $file_path) or die "Could not open file '$file_path' $!";

    for my $i (0x0 .. 0x10ffff) {
        # if (0xd800 <= $i && $i <= 0xdfff) {
        #     next;
        # }
        my $char = chr($i);
        if ($char =~ /$pattern/) {
            printf $fh "%04X\n", $i;
        }
    }
    close $fh;
}

if (@ARGV < 2) {
    print "Usage: perl main.pl <pattern> <file_path>\n";
    exit;
}

my ($pattern, $file_path) = @ARGV;
iterate_codepoints($pattern, $file_path);
