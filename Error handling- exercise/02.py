class NameNotFound(Exception):
    pass


class MustContainAtSymbol(Exception):
    pass


class TooManyAtSymbols(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomain(Exception):
    pass


ALLOWED_DOMAINS = ['.com', '.bg', '.org', '.net']


def validate_email(email):
    counter = 0
    if '@' not in email:
        counter += 1
        raise MustContainAtSymbol('Email must contain @')
    username, domain, *rest = email.split('@')
    if len(rest) > 0:
        counter += 1
        raise TooManyAtSymbols('Тhe whole email must contain one and only one "@" symbol')
    if len(username) <= 4:
        counter += 1
        raise NameTooShortError('Name must be more than 4 characters')

    if domain.split('.')[-1] not in ['com', 'bg', 'net', 'org']:
        counter += 1
        raise InvalidDomain(f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}")

    if counter == 0:
        print(f'Email is valid')


def main():
    while True:
        email = input()
        if email == 'End':
            break
        validate_email(email)


if __name__ == '__main__':
    main()
    print('success')
