def get_tunes_by_book(df, book_number):
    """Get all tunes from a specific book"""
    df = df[df["book_number"] ==  book_number]
    return df


def get_tune(df, tune_type):
    """Get the tune types"""
    df_2 = df[df["type"].str.lower() == tune_type.lower()] # FOR THE FUTURE, case = False wouldnt work fix later
    return df_2


def search(df, search_terms):
    '''function to return the title of a song (used for tkinter)'''
    df_3 = df[df["title"].str.contains(search_terms, case = False)]
    return df_3
