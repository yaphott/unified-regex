import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.CharacterCodingException;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Main {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java Main <pattern> <file_path>");
            return;
        }

        String pattern = args[0];
        String filePath = args[1];
        try {
            iterateCodepoints(pattern, filePath);
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static void iterateCodepoints(String pattern, String filePath) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            Pattern regex = Pattern.compile(pattern);
            CharsetDecoder decoder = Charset.forName("UTF-8").newDecoder();

            for (int i = 0; i <= 0x10ffff; i++) {
                // if (0xd800 <= i && i <= 0xdfff) {
                //     continue;
                // }
                char[] chars = Character.toChars(i);
                String charStr = new String(chars);

                try {
                    decoder.reset();
                    decoder.decode(java.nio.ByteBuffer.wrap(charStr.getBytes("UTF-8")));
                } catch (CharacterCodingException e) {
                    continue;
                }

                Matcher matcher = regex.matcher(charStr);
                if (matcher.matches()) {
                    writer.write(String.format("%04X%n", i));
                }
            }
        }
    }
}
