const fs = require("fs");

function iterateCodepoints(pattern, filePath) {
    try {
        const regex = new RegExp(pattern, "u");
        const writeStream = fs.createWriteStream(filePath, { flags: "w" });
        for (let i = 0; i <= 0x10ffff; i++) {
            // if (0xd800 <= i && i <= 0xdfff) {
            //     continue;
            // }
            const char = String.fromCodePoint(i);
            if (regex.test(char)) {
                writeStream.write(`${i.toString(16).toUpperCase()}\n`);
            }
        }
        writeStream.end();
    } catch (err) {
        console.error("Error:", err);
    }
}

function main() {
    if (process.argv.length < 4) {
        console.log("Usage: node main.js <pattern> <file_path>");
        return;
    }
    const pattern = process.argv[2];
    const filePath = process.argv[3];
    iterateCodepoints(pattern, filePath);
}

main();
