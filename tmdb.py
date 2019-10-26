import requests
import json
from colorama import init, Fore, Style
init()


class TMDB:
    def __init__(self, api_key):
        self.api_key = api_key
        self.main_uri = 'https://api.themoviedb.org/3/'

    def search_tv(self, query):
        # response = requests.get(self.main_uri + 'search/tv', params={
        #     "api_key": self.api_key,
        #     "query": query,
        # })
        # results = response.json()['results']
        results = [{'overview': "Bored and unhappy as the Lord of Hell, Lucifer Morningstar abandoned his throne and retired to Los Angeles, where he has teamed up with LAPD detective Chloe Decker to take down criminals.\xa0But the longer he's away from the underworld, the greater the threat that the worst of humanity could escape.", 'poster_path': '/1sBx2Ew4WFsa1YY32vlHt079O03.jpg', 'origin_country': ['US'], 'name': 'Lucifer', 'vote_count': 1105, 'original_language': 'en', 'original_name': 'Lucifer', 'backdrop_path': '/6kZCuvbirx6ibJfaWqwV2p90yPI.jpg', 'id': 63174, 'popularity': 102.479, 'first_air_date': '2016-01-25', 'vote_average': 7.4, 'genre_ids': [80, 10765]}, {'overview': '', 'poster_path': '/cc4KO3xjvzAxRQ1Q5QZC9wkcwTk.jpg', 'origin_country': ['JP'], 'name': 'Comet Lucifer', 'vote_count': 3, 'original_language': 'ja', 'original_name': 'コメット・ルシファー', 'backdrop_path': '/9SzNNYYHBeujYYreNeNojTaVtvm.jpg', 'id': 68256, 'popularity': 3.062, 'first_air_date': '2015-10-04', 'vote_average': 7.3, 'genre_ids': [16, 10759, 10765]},
                   {'overview': 'A string of murders brings together a conflicted detective, a psychic librarian, and a mysterious prosecutor with dubious motives in this action thriller starring Uhm Tae Woong, Joo Ji Hoon, and Shin Min Ah. Detective Kang Oh Soo is assigned to two seemingly unrelated murder cases, where the only clues left behind are tarot cards. He is lead to Seo Hae In, a quiet librarian who has the ability to make a psychic connection to an object to discover its history. She reveals to him that the victims were connected to the death of a high school boy years ago. The one common link between the suspects is their defense attorney, Oh Seung Ha, a young lawyer with questionable motives. Find out how everything is more connected than you think in this suspenseful thriller.\n\nThe series is the second installment of the revenge trilogy by director Park Chan-hong and writer Kim Ji-woo, after Resurrection in 2005 and followed by Shark in 2013.', 'poster_path': '/9FEbd7soyed3AZYMpfeJXPSQxIX.jpg', 'origin_country': ['KR'], 'name': 'The Lucifer', 'vote_count': 4, 'original_language': 'ko', 'original_name': '마왕', 'first_air_date': '2007-03-21', 'id': 46560, 'backdrop_path': '/by7QAcfHvnE8Ks7JUOSk7Q2bQjb.jpg', 'popularity': 1.36, 'vote_average': 6.5, 'genre_ids': [18, 9648, 10749]}]

        print(Fore.GREEN + '>Found {} results.\n'.format(len(results)))
        if len(results) > 1:
            print(
                Fore.YELLOW + 'More than one result, enter the number of the correct result:\n')
            for i in range(0, len(results)):
                print(Fore.RESET + '{}.\tName: {}\n\tPopularity: {}\n\tOverview: {}\n\n'.format(
                    i,
                    results[i]['name'],
                    results[i]['popularity'],
                    results[i]['overview']
                ))
            result_index = input(Fore.YELLOW + 'Enter your selection: ')
            return results[int(result_index)]['id']
        return results[0]['id'] or False
