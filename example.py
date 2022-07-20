from eip712 import eip712_encode, eip712_signature

# An example of a valid Ethereum private key.
PRIVATE_KEY = '0x8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f'

# An example of a valid Ethereum address.
ADDRESS = '0x8e12f01dae5fe7f1122dc42f2cb084f2f9e8aa03'


def get_eip712_payload():
    types = {'EIP712Domain': [{'name': 'name', 'type': 'string'},
                              {'name': 'version', 'type': 'string'},
                              {'name': 'chainId', 'type': 'uint256'},
                              {'name': 'verifyingContract', 'type': 'address'}],
             'Mailbox': [{'name': 'owner', 'type': 'address'},
                         {'name': 'messages', 'type': 'Message[]'}],
             'Message': [{'name': 'sender', 'type': 'address'},
                         {'name': 'subject', 'type': 'string'},
                         {'name': 'isSpam', 'type': 'bool'},
                         {'name': 'body', 'type': 'string'}]}

    msgs = [{'sender': ADDRESS,
             'subject': 'Hello World',
             'body': 'The sparrow flies at midnight.',
             'isSpam': False},
            {'sender': ADDRESS,
             'subject': 'You may have already Won! :dumb-emoji:',
             'body': 'Click here for sweepstakes!',
             'isSpam': True}]

    mailbox = {'owner': ADDRESS,
               'messages': msgs}

    payload = {'types': types,
               'primaryType': 'Mailbox',
               'domain': {'name': 'MyDApp',
                          'version': '3.0',
                          'chainId': 41,
                          'verifyingContract': ADDRESS},
               'message': mailbox}

    encoded_parts = eip712_encode(payload)
    return b''.join(encoded_parts)


if __name__ == '__main__':
    payload = get_eip712_payload()
    sig = eip712_signature(payload, PRIVATE_KEY)

    print("Payload:", payload)
    print("Signature:", sig)
