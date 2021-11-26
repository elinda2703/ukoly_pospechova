import csv
with open(r"vstup.csv", encoding="utf-8") as csvinfile, open(r"vystup_7denni.csv", "w", encoding="utf-8", newline="") as csvoutfile_den, open(r"vystup_rok.csv", "w", encoding="utf-8", newline="") as csvoutfile_rok:
    reader = csv.reader(csvinfile, delimiter=",")
    writer_den = csv.writer(csvoutfile_den)
    writer_rok = csv.writer(csvoutfile_rok)
    first_date_week = None
    first_date_year = None
    days_in_week = 0
    days_in_year = 0
    prefix = None
    prutok_sum_week = 0
    prutok_sum_year = 0

    for row in reader:
        if prefix is None:
            prefix = row[0:2]

        if first_date_week is None:
            first_date_week = row[2:5]

        if first_date_year is None:
            first_date_year = row[2:5]

        if days_in_week == 7:

            writer_den.writerow(prefix + first_date_week +
                                [round(prutok_sum_week/days_in_week, 4)])
            prutok_sum_week = 0
            first_date_week = row[2:5]
            days_in_week = 0

        if first_date_year[0] != row[2]:
            writer_rok.writerow(prefix + first_date_year +
                                [round(prutok_sum_year/days_in_year, 4)])
            prutok_sum_year = 0
            first_date_year = row[2:5]
            days_in_year = 0

        days_in_year += 1
        days_in_week += 1

        prutok_sum_week += float(row[5])
        prutok_sum_year += float(row[5])

    writer_den.writerow(prefix + first_date_week +
                        [round(prutok_sum_year/days_in_week, 4)])
    writer_rok.writerow(prefix + first_date_year +
                        [round(prutok_sum_year/days_in_year, 4)])
