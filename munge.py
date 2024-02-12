input_filepath = "./data/GLB.Ts+dSST.txt"
final_output_filepath = "./data/clean_data.csv"
yearflag = False
yearflagfound = False
with open(input_filepath, 'r') as infile, open(final_output_filepath, 'w') as outfile:
    for line in infile:
        if line.strip() == "" or "*" in line:
            continue
        if "Year" in line:
            if not yearflag:
                yearflag = True
            if not yearflagfound:
                columns = line.strip().split()
                modified_line = ' '.join(columns[:-1])
                outfile.write(modified_line + '\n')
                yearflagfound = True
            continue
        if yearflag:
            if "Divide" in line:
                break  
            columns = line.strip().split()
            modified_columns = columns[:-1]
            processed_values = [modified_columns[0]]
            for value in modified_columns[1:]:
                try:
                    processed_value = "{:.1f}".format(float(value) / 100 * 1.8)
                except ValueError:
                    processed_value = value
                processed_values.append(processed_value)
            outfile.write(' '.join(processed_values) + '\n')
