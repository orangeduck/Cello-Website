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
      'pattern': /\b(var|var_list|val|is|not|and|or|elif|else|foreach|with|try|catch|throw|if|if_eq|if_neq|if_gt|if_lt|if_ge |if_le|typedef|for|while|switch|case|break|do|return|sizeof|as|void|unsigned|const|char|short|int|long |bool|float|double|size_t|true|false|va_list\*|void\*|char\*|char\*\*|var\*|FILE\*|va_list|bool|struct |union|static|extern|volatile|module|class|data|instance|type_data|type_begin|type_entry|type_end|lambda|lambda_id|lambda_const|lambda_compose|lambda_flip|lambda_partial|lambda_partial_l |lambda_partial_r|lambda_void|lambda_uncurry|lambda_void_uncurry|lambda_pipe|lambda_method_pipe|local|global|in|enum)(?=\(|\b)/g
    },
    {
      'name':'entity.class',
      'pattern': /\b(Int|Real|Bool|Type|True|False|String|List|Array|Some|None|Undefined|Table|File|Map|Tree|Function|Dictionary|Char|NULL|Reference|Pool|Singleton|TypeError|ValueError|ClassError|IndexOutOfBoundsError|KeyError|OutOfMemoryError|IOError|FormatError|ProgramAbortedError|DivisionByZeroError|IllegalInstructionError|ProgramInterruptedError|SegmentationError|ProgramTerminationError|Vec2|Thread|Mutex)(?=\(|\b)/g
    },
    {
      'name':'entity.function',
      'pattern':/\b(lit|cast|new|delete|allocate|deallocate|construct|destruct|assign|copy|eq|neq|gt|lt|ge|le|len|clear|contains|discard|is_empty|sort|maximum|minimum|reverse|iter_start|iter_end|iter_next|hash|push|push_at|push_back|push_front|pop|pop_at|pop_back|pop_front|at|set|get|put|as_char|as_str|as_long|as_double|enter_with|exit_with|stream_open|stream_close|stream_seek|stream_tell|stream_flush|stream_eof|stream_read|stream_write|serial_read|serial_write|type_class|type_class_method|type_implements|type_of|add|sub|mul|divide|negate|absolute|map|new_map|new_filter|new_foldl|new_foldr|new_sum|new_product|call_with|call|call_with_ptr|release|retain|assert|format_to|format_from|format_to_va|format_from_va|show|show_to|print|println|print_to|print_vl|println_vl|print_to_vl|look|look_from|scan|scanln|scan_from|scan_vl|scanln_vl|scan_from_vl|current|join|terminate|lock|unlock|lock_try|append|var_list_parse|var_list_new|var_list_get|var_list_end|bool_var)(?=\(|\b)/g
    },
    {
      'name':'support.class',
      'pattern':/\b(New|Assign|Copy|Eq|Ord|Hash|Serialize|AsLong|AsDouble|AsStr|AsChar|Num|Collection|Reverse|Iter|Push|At|Dict|With|Stream|Call|Retain|Sort|Append|Show|Format|Vector|Process|Lock)(?=\(|\b)/g
    }
], true);
