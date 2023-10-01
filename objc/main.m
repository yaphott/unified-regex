#import <Foundation/Foundation.h>

void iterateCodepoints(NSString *pattern, NSString *filePath) {
    NSError *error = NULL;
    NSMutableArray* array = [[NSMutableArray alloc] init];
    NSRegularExpression *expr = [NSRegularExpression regularExpressionWithPattern: pattern options:0 error:&error];
    NSOutputStream *stream = [[NSOutputStream alloc] initToFileAtPath:filePath append:NO];

    for (int i = 0; i <= 0x10ffff; ++i) {
        // if (i >= 0xd800 && i <= 0xdfff) continue;

        NSData *charData = [[NSData alloc] initWithBytes:&i length:sizeof(int)];
        NSString *ts = [[NSString alloc] initWithData:charData encoding:NSUTF32LittleEndianStringEncoding];
        if ([expr numberOfMatchesInString:ts options:0 range:NSMakeRange(0, [ts length])] > 0) {
            [array addObject: [NSString stringWithFormat:@"%X", i]];
        }
    }

    [stream open];
    for (NSString *s in array) {
        NSData *data = [s dataUsingEncoding:NSUTF8StringEncoding];
        [stream write:[data bytes] maxLength:[data length]];
        [stream write:(const uint8_t *)"\n" maxLength:1];
    }
    [stream close];
}


int main(int argc, const char *argv[]) {
    @autoreleasepool {
        if (argc < 3) {
            NSLog(@"Usage: ./main <pattern> <file_path>");
        } else {
            NSString *pattern = [NSString stringWithUTF8String:argv[1]];
            NSString *filePath = [NSString stringWithUTF8String:argv[2]];
            iterateCodepoints(pattern, filePath);
        }
    }
    return 0;
}
