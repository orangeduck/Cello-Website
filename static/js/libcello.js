/**
 * libcello patterns
 *
 * @author Daniel Holden
 * @version 1.0.0
 */
Rainbow.extend('libcello', [
    {
        'name': 'keyword.operator',
        'pattern': /\$|\+|\!|\-|&(gt|lt|amp);|\||\*|\=|%|#/g
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
      'name':'keyword',
      'pattern': /\b(fun|var|is|isnt|not|and|or|else|foreach|with|try|catch|throw|if|if_eq|if_neq|if_gt|if_lt|if_ge |if_le|typedef|for|while|switch|case|break|do|return|sizeof|as|void|unsigned|const|char|short|int|long|bool|float|double|size_t|true|false|va_list\*|void\*|char\*|char\*\*|var\*|FILE\*|va_list|bool|struct|union|static|extern|volatile|in|enum|int64_t|int32_t|int16_t|int8_t|uint64_t|uint32_t|uint16_t|uint8_t|define|include|FILE|NULL)(?=\(|\b)/g
    },
    {
      'name':'entity.class',
      'pattern': /\b(Int|Float|Type|String|List|Array|Some|None|Undefined|Table|File|Process|Map|Tree|Function|Dictionary|Char|Ref|Box|TypeError|ValueError|ClassError|IndexOutOfBoundsError|KeyError|OutOfMemoryError|IOError|FormatError|ProgramAbortedError|DivisionByZeroError|IllegalInstructionError|ProgramInterruptedError|SegmentationError|ProgramTerminationError|Thread|Mutex|Image|Point|Color|GC|Slice|Tuple)(?=\(|\b)/g
    },
    {
      'name':'entity.function',
      'pattern':/\b(cast|new|new_root|new_raw|new_with|new_root_with|new_raw_with|del|del_root|del_raw|alloc|alloc_raw|alloc_root|alloc_stack|dealloc|dealloc_raw|dealloc_root|construct|construct_with|destruct|assign|copy|eq|neq|gt|lt|ge|le|cmp|ref|deref|reserve|len|clear|mem|rem|empty|sort|sort_with|maximum|minimum|reverse|iter_init|iter_next|iter_last|iter_prev|mark|hash|hash_data|push|push_at|pop|pop_at|set|get|c_char|c_str|c_int|c_float|begin|end|sopen|sclose|sseek|stell|sflush|seof|sread|swrite|method|type_method|implements|instance|type_of|type_implements|type_instance|madd|msub|mmul|mdiv|mneg|mabs|map|call_with|call|format_to|format_from|format_to_va|format_from_va|show|show_to|print|println|print_to|print_with|println_with|print_to_with|look|look_from|scan|scanln|scan_from|scan_with|scanln_with|scan_from_with|current|join|terminate|lock|unlock|lock_try|append|concat|bool_var|tuple|mark|size|help|help_to|start|stop|running|subtype|key_subtype|val_subtype|name|brief|description)(?=\(|\b)/g
    },
    {
      'name':'support.class',
      'pattern':/\b(Alloc|New|Assign|Copy|Cmp|Hash|C_Int|C_Float|C_Str|Reverse|Iter|Push|Stream|Call|Sort|Concat|Show|Format|Lock|Get|Cast|Clear|Current|Doc|Help|Join|Len|Mark|Pointer|Reserve|Size|Start|Subtype)(?=\(|\b)/g
    }
], true);
