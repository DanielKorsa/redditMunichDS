
import pprint
import re

def clean_description(descr_list):
    """[Clean description text for printing a word cloud graph]
    Args:
        descr_list ([list]): [list of descriptions]
    Returns:
        [str]: [clean str]
    """
    plain_text = ' '.join(descr_list)
    pure_text = re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿ/]+', ' ', plain_text)
    words_list = pure_text.split(' ')
    clean_words_list = [word.lower() for word in words_list]
    clean_text = ' '.join(clean_words_list)

    return clean_text