import re


def code_postal_valide(code_postal: str):
    return re.fullmatch(r"^[A-Z]\d[A-Z] ?\d[A-Z]\d$", code_postal) is not None


def num_téléphone_valide(num_téléphone: str):
    return re.fullmatch(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$", num_téléphone) is not None


def email_valide(email: str):
    return re.fullmatch(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.["
                        r"a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email)


def format_date_valide(date: str):
    return re.fullmatch(r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$", date)


assert code_postal_valide("J3L 0C6")
assert num_téléphone_valide("450 447-7059")
assert email_valide("jonathan.duplantis@hotmail.com")
