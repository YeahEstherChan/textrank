
from nltk.tokenize import sent_tokenize
import nltk.data
from sentence_splitter import split_into_sentences
import os
import os.path

SAMPLES_DIRECTORY = "samples"
DEBUG = False


def compare_sentences(output_list_1, output_list_2):
    total_sentences = len(output_list_1)
    sentences_hit = 0

    for line in output_list_1:
        if line in output_list_2:
            sentences_hit += 1
        else:
            if DEBUG:
                print "Line not found on source #2:", line

    return float(sentences_hit) / float(total_sentences)


def compare(sample_text_file_name):
    """
    Given the filename of a sample text, extracts its sentences using two
    different methods.
    Returns the proportion between the mathes of both methods and the number of
    sentences of the first.
    """
    sample_text = nltk.data.load(sample_text_file_name)
    output_1 = sent_tokenize(sample_text)
    output_1 = [sentence.encode('utf8') for sentence in output_1]

    with open(sample_text_file_name) as text_fp:
        sample_text = text_fp.read()

    output_2 = split_into_sentences(sample_text)

    return compare_sentences(output_1, output_2)


def run_tests():
    """ Tests the sentence_splitter function by comparing a sample result
    with the output of the sentence_tokenize function in NLTK.
    """
    for filename in os.listdir(SAMPLES_DIRECTORY):
        filepath = os.path.join(SAMPLES_DIRECTORY, filename)
        accuracy = compare(filepath)
        print "Accuracy for sample text '{filename}': {acc}".format(filename=filename, acc=accuracy)


run_tests()