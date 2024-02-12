import csv

input_filepath = "./data/clean_data.csv"
final_output_filepath = "./data/averageanomaliesbydecade.csv"
dnindex = 14
decadedistionary = {}
with open(input_filepath, 'r') as file:
    first_line = True
    for line in file:
        if first_line:
            first_line = False
            continue
        
        parts = line.strip().split()
        if len(parts) > dnindex:
            year = int(parts[0])
            if year < 1890:
                decade = 1880
            else:
                decade = (year // 10) * 10
            
            dn_value = float(parts[dnindex])
            if decade not in decadedistionary:
                decadedistionary[decade] = {'sum': 0, 'count': 0}
            decadedistionary[decade]['sum'] += dn_value
            decadedistionary[decade]['count'] += 1
with open(final_output_filepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Decade', 'Average D-N Anomaly (°F)'])

    for decade, data in sorted(decadedistionary.items()):
        avg_anomaly = data['sum'] / data['count']
        writer.writerow([f"{decade}s" if decade != 1880 else "1881-1889", f"{avg_anomaly:.2f}"])