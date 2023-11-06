from datetime import datetime

def p_date(datetime_str):
    time = datetime.strptime(str(datetime_str), '%Y-%m-%d %H:%M:%S.%f')
    return time.second + 60*time.minute + 3600*time.hour+86400*time.day


# if __name__ == "__main__":
#     p_date('2023-11-06 19:56:12.355464')
