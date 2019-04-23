
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three exclamation marks"""
    echo_words = ""
    shout_words = ""
    try: 
        echo_words = word1 * echo

        shout_words = echo_words + "!!!"
    except:
        print("word must be a string and echo must be an integer")

    return shout_words


