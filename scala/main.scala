import java.io.{BufferedWriter, FileWriter}
import scala.util.matching.Regex
import util.control.Breaks._

object Main extends App {
  if (args.length < 2) {
    println("Usage: sbt \"run <pattern> <file_path>\"")
  } else {
    val pattern = args(0)
    val filePath = args(1)

    val regex = new Regex(pattern)
    val writer = new BufferedWriter(new FileWriter(filePath))

    for (i <- 0 to 0x10ffff) {
      breakable {
        // if (0xd800 <= i && i <= 0xdfff) break
        val char = new String(Character.toChars(i))
        if (regex.findFirstIn(char).isDefined) {
          writer.write(f"$i%04X\n")
        }
      }
    }

    writer.close()
  }
}
