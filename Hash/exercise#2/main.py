"""
Problem: A telephone directory

Description:
        I'd like to check if one of the phone numbers in the telephone directory is a prefix of another number.
        If the phone numbers are as follows, the rescue team's phone number is the prefix
        of Young-seok's phone number.

        * rescue team : 119
        * Jun-young : 97 674 223
        * Young-seok : 11 9552 4421

        When 'phone_book' which is an array(list) containing phone numbers is given
        as a parameter of the solution method, write the solution method to return false if there is a phone number
        which is a prefix of another number or return true if not.

Restrictions:
        1. Length of phone_book array is more than 1 and less than 1,000,000
        2. Length of each phone number is more than 1 and less than 20
        3. The same phone numbers cannot exist in the telephone directory

        * 입출력 예시는 프로그래머스에 기재되어있으며 테스트 케이스 또한 프로그래머스 참고
        https://programmers.co.kr/learn/courses/30/lessons/42577
"""


def solution(phone_book):
    hash_table = {}

    for phone_number in phone_book:
        hash_table[phone_number] = 1 # set hash table

    for phone_number in phone_book:
        prefix = ""
        for p in phone_number[:-1]:
            prefix += p # set prefix
            if prefix in hash_table: # prefix presence check
                return False # if True, return False
    return True

pb = ["119", "97674223", "1195524421"]
pb2 = ["123","456","789"]
pb3 = ["12","123","1235","567","88"]

if (solution(pb), solution(pb2), solution(pb3)) == (True, False, True):
    print("Correct")
else:
    print("Wrong")