# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date=None, description=None, change=None):
        self.date = date
        self.description = description
        self.change = change


def create_entry(date, description, change):
    return LedgerEntry(
        date=datetime.strptime(date, '%Y-%m-%d'),
        description=description,
        change=change
    )


def format_currency(change, currency_symbol, locale):
    def format_major_units(abs_change, locale):
        major_units = abs_change // 100
        major_parts = []
        while major_units > 0:
            major_parts.insert(0, f"{major_units % 1000}")
            major_units //= 1000
        separator = '.' if locale == 'nl_NL' else ','
        return separator.join(major_parts) if major_parts else '0'

    def format_minor_units(abs_change):
        return f"{abs_change % 100:02}"

    is_negative = change < 0
    abs_change = abs(change)
    major_str = format_major_units(abs_change, locale)
    minor_str = format_minor_units(abs_change)

    if locale == 'nl_NL':
        formatted = f"{currency_symbol} {'-' if is_negative else ''}{major_str},{minor_str}"
        while len(formatted) < 12:
            formatted = ' ' + formatted
        formatted = formatted.ljust(13)
        return formatted

    formatted = f"{currency_symbol}{major_str}.{minor_str}"
    if is_negative:
        formatted = f"({formatted})"
    else:
        formatted += ' '
    return formatted.rjust(13)


def format_date(date, locale):
    if locale == 'en_US':
        return date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return date.strftime('%d-%m-%Y')


def format_description(description):
    return description[:22] + '...' if len(description) > 25 else description.ljust(25)


def generate_header(locale):
    if locale == 'en_US':
        return "Date       | Description               | Change       "
    elif locale == 'nl_NL':
        return "Datum      | Omschrijving              | Verandering  "


def format_entries(currency, locale, entries):
    currency_symbol = '$' if currency == 'USD' else '€'
    header = generate_header(locale)
    rows = [header]

    while entries:
        entry = min(entries, key=lambda e: (e.date, e.change, e.description))
        entries.remove(entry)

        date_str = format_date(entry.date, locale)
        description_str = format_description(entry.description)
        change_str = format_currency(entry.change, currency_symbol, locale)

        rows.append(f"{date_str} | {description_str} | {change_str}")

    return '\n'.join(rows)

