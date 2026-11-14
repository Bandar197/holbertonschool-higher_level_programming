#!/usr/bin/python3
"""Generate invitation files by filling in attendee placeholders."""


FIELDS = ('name', 'event_title', 'event_date', 'event_location')


def generate_invitations(template, attendees):
    """Write one personalized invitation per attendee, starting at output_1.txt.

    Invalid or empty inputs are reported without producing output files.
    Missing or null attendee values are represented by ``N/A``.
    """
    if not isinstance(template, str):
        print('Error: Invalid template type. Expected string, got {}.'
              .format(type(template).__name__))
        return

    if not isinstance(attendees, list):
        print('Error: Invalid attendees type. Expected list of dictionaries, '
              'got {}.'.format(type(attendees).__name__))
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print('Error: Invalid attendees type. Expected list of dictionaries.')
        return

    if not template:
        print('Template is empty, no output files generated.')
        return

    if not attendees:
        print('No data provided, no output files generated.')
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        for field in FIELDS:
            value = attendee.get(field)
            replacement = str(value) if value not in (None, '') else 'N/A'
            invitation = invitation.replace('{' + field + '}', replacement)

        try:
            with open('output_{}.txt'.format(index), 'w',
                      encoding='utf-8') as output:
                output.write(invitation)
        except OSError as error:
            print('Error writing output_{}.txt: {}'.format(index, error))
