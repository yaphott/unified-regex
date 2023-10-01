<?php

function iterateCodepoints($pattern, $filePath) {
    $file = fopen($filePath, 'w');
    if (!$file) {
        return "Could not create file: " . $filePath;
    }

    $regex = '/' . $pattern . '/u';
    if (@preg_match($regex, '') === false) {
        return "Invalid regular expression: " . $pattern;
    }

    for ($i = 0; $i <= 0x10ffff; $i++) {
        // if (0xd800 <= $i && $i <= 0xdfff) {
        //     continue;
        // }
        $char = mb_chr($i);
        if (!mb_check_encoding($char, 'UTF-8')) {
            continue;
        }
        if (preg_match($regex, $char)) {
            fwrite($file, sprintf("%04X\n", $i));
        }
    }

    fclose($file);
    return null;
}

if ($argc < 3) {
    echo "Usage: php " . $argv[0] . " <regular_expression> <output_file_path>\n";
    exit(1);
}

$pattern = $argv[1];
$filePath = $argv[2];

$error = iterateCodepoints($pattern, $filePath);
if ($error) {
    echo "Error: " . $error . "\n";
}

?>
