import logon_data


def extract_combination(mail, pwd):
    try:
        idx = logon_data.mail_data.index(mail)
        if pwd == logon_data.pwd_data[idx]:
            return True
    except:
        return False

    return False

