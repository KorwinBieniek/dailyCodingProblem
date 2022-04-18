# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

def decode_message(digits, n):
    count = [0] * (n + 1)

    count[0] = 1
    count[1] = 1

    for i in range(2, n + 1):

        count[i] = 0

        if (digits[i - 1] > '0'):
            count[i] = count[i - 1]

        if (digits[i - 2] == '1' or
                (digits[i - 2] == '2' and
                 digits[i - 1] < '7')):
            count[i] += count[i - 2]

    return count[n]


message = '111'
print(decode_message(message, len(message)))
