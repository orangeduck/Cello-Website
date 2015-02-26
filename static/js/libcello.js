/**
 * libcello patterns
 *
 * @author Daniel Holden
 * @version 1.0.0
 */
Rainbow.extend('libcello', [
    {
        'name': 'keyword.operator',
        'pattern': /\$|\+|\!|\-|&(gt|lt|amp);|\||\*|\=/g
    },    
    {
      'matches': {
            1: {
                'name': 'keyword.operator',
                'pattern': /\=/g
            },
            2: {
                'name': 'string',
                'matches': {
                    'name': 'constant.character.escape',
                    'pattern': /\\('|"){1}/g
                }
            }
        },
        'pattern': /(\(|\s|\[|\=|:)(('|")([^\\\1]|\\.)*?(\3))/gm    
    },
    {
        'name': 'comment',
        'pattern': /\/\*[\s\S]*?\*\/|(\/\/)[\s\S]*?$/gm
    },
    {
        'name': 'constant.numeric',
        'pattern': /\b(\d+(\.\d+)?(e(\+|\-)?\d+)?(f|d)?|0x[\da-f]+)\b/gi
    },
    {
        'name': 'meta.preprocessor',
        'matches': {
            1: [
                {
                    'matches': {
                        1: 'keyword.define',
                        2: 'entity.name'
                    },
                    'pattern': /(\w+)\s(\w+)\b/g
                },
                {
                    'name': 'keyword.define',
                    'pattern': /endif/g
                },
                {
                    'name': 'constant.numeric',
                    'pattern': /\d+/g
                },
                {
                    'matches': {
                        1: 'keyword.include',
                        2: 'string'
                    },
                    'pattern': /(include)\s(.*?)$/g
                }
            ]
        },
        'pattern': /\#([\S\s]*?)$/gm
    },
    {
      'name':'keyword',
      'pattern': /\b(fun|var|is|not|and|or|else|foreach|with|try|catch|throw|if|if_eq|if_neq|if_gt|if_lt|if_ge |if_le|typedef|for|while|switch|case|break|do|return|sizeof|as|void|unsigned|const|char|short|int|long|bool|float|double|size_t|true|false|va_list\*|void\*|char\*|char\*\*|var\*|FILE\*|va_list|bool|struct|union|static|extern|volatile|in|enum)(?=\(|\b)/g
    },
    {
      'name':'entity.class',
      'pattern': /\b(Int|Real|Bool|Type|True|False|String|List|Array|Some|None|Undefined|Table|File|Map|Tree|Function|Dictionary|Char|NULL|Reference|Pool|Singleton|TypeError|ValueError|ClassError|IndexOutOfBoundsError|KeyError|OutOfMemoryError|IOError|FormatError|ProgramAbortedError|DivisionByZeroError|IllegalInstructionError|ProgramInterruptedError|SegmentationError|ProgramTerminationError|Vec2|Thread|Mutex)(?=\(|\b)/g
    },
    {
      'name':'entity.function',
      'pattern':/\b(cast|new|del|alloc|dealloc|construct|destruct|assign|copy|eq|neq|gt|lt|ge|le|len|clear|mem|rem|empty|sort|maximum|minimum|reverse|iter_init|iter_next|hash|push|push_at|pop|pop_at|set|get|c_char|c_str|c_int|c_float|begin|end|sopen|sclose|sseek|stell|sflush|seof|sread|swrite|method|implements|instance|type_of|madd|msub|mmul|mdiv|mneg|mabs|map|call_with|call|format_to|format_from|format_to_va|format_from_va|show|show_to|print|println|print_to|print_with|println_with|print_to_with|look|look_from|scan|scanln|scan_from|scan_with|scanln_with|scan_from_with|current|join|terminate|lock|unlock|lock_try|append|concat|bool_var|tuple)(?=\(|\b)/g
    },
    {
      'name':'support.class',
      'pattern':/\b(New|Assign|Copy|Eq|Ord|Hash|Serialize|AsLong|AsDouble|AsStr|AsChar|Num|Collection|Reverse|Iter|Push|At|Dict|With|Stream|Call|Retain|Sort|Append|Show|Format|Vector|Process|Lock)(?=\(|\b)/g
    }
], true);
