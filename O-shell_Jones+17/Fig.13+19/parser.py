def parse_file(file_name):
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    fields = {}
    try:
        with open(file_name, 'r') as fin:
            for line in fin:
                split_line = line.split('=')
                if len(split_line) >= 2:
                    lhs = split_line[0].strip()
                    rhs = split_line[1].strip()
                    
                    split_rhs = rhs.split()
                    rhs_value = split_rhs[0]
                    if isfloat(rhs_value):
                        rhs_value = float(rhs_value)
                    
                    fields[lhs] = rhs_value
                    
            fin.close()
    except IOError:
        print "Error: Cannot read '{:s}'!".format(file_name)
        
    return fields
