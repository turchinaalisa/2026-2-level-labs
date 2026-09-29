"""
Language detection starter.
"""
from main import (
    calculate_frequencies,
    check_profile,
    compare_profiles_by_top_n,
    create_language_profile,
    detect_language_by_top_n,
    get_top_n_words,
    remove_stop_words,
    tokenize,
)

# pylint: disable=unused-variable, duplicate-code, too-many-return-statements
from lab_1_classify_profile.main import (
    calculate_frequencies,
    collect_profiles,
    create_language_profile,
    detect_language_advanced,
    detect_language_by_mse,
    detect_language_by_top_n,
    get_top_n_words,
    print_report,
    remove_stop_words,
    save_profile,
    tokenize,
)


def main() -> None:
    """
    Launches an implementation.
    """
    with open("lab_1_classify_profile/assets/texts/de.txt", "r", encoding="utf-8") as file:
        de_text = file.read()
    with open("lab_1_classify_profile/assets/texts/unknown.txt", "r", encoding="utf-8") as file:
        unknown_text = file.read()
    with open("lab_1_classify_profile/assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    with open("lab_1_classify_profile/assets/texts/en.txt", "r", encoding="utf-8") as file:
        en_text = file.read()

    result = None

    tokenized_text = tokenize(de_text)
    if tokenized_text is None:
        return None

    text_without_stopwords = remove_stop_words(tokenized_text, stopwords)
    if text_without_stopwords is None:
        return None

    calculated_frequencies = calculate_frequencies(text_without_stopwords)

    if calculated_frequencies is None:
        return None

    unk_profile = create_language_profile("unknown", unknown_text, stopwords)
    de_profile = create_language_profile("de", de_text, stopwords)
    en_profile = create_language_profile("en", en_text, stopwords)

    if (unk_profile is None
        or de_profile is None
        or en_profile is None):
        return None

    print(get_top_n_words(calculated_frequencies, 7))
    print(detect_language_by_top_n(unk_profile, en_profile, de_profile, 15))
    result = detect_language_by_mse(unk_profile, en_profile, de_profile)

    save_profile(unk_profile, 'lab_1_classify_profile/assets/profiles')
    save_profile(de_profile, 'lab_1_classify_profile/assets/profiles')
    save_profile(en_profile, 'lab_1_classify_profile/assets/profiles')

    list_of_paths = ['lab_1_classify_profile/assets/profiles/la.json',
                     'lab_1_classify_profile/assets/profiles/de.json',
                     'lab_1_classify_profile/assets/profiles/en.json']
    collected_profiles = collect_profiles(list_of_paths)

    if collected_profiles is None:
        return None

    advanced_detection = detect_language_advanced(unk_profile, collected_profiles, 15)

    if advanced_detection is None:
        return None

    print_report(unk_profile, advanced_detection, 15)

    assert result, "Detection result is None"
    return None

    # Mark 4

    de_tokens = tokenize(de_text)
    de_tokens = remove_stop_words(de_tokens, stopwords)
    de_frequency = calculate_frequencies(de_tokens)
    de_get_top_n_words = get_top_n_words(de_frequency, 7)
    result = de_get_top_n_words

    print(result)

    # Mark 6

    en_language_profile = create_language_profile("English", en_text, stopwords)
    de_language_profile = create_language_profile("German", de_text, stopwords)
    unknown_language_profile = create_language_profile("Unknown", unknown_text, stopwords)

    compare_languages = detect_language_by_top_n(unknown_language_profile, en_language_profile, de_language_profile, 15)

    print(compare_languages)


    assert result, "Detection result is None"

if __name__ == "__main__":
    main()
