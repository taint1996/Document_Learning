module Ex25

    # this function will break up words
    def Ex25.break_words(stuff)
        words = stuff.split(' ')
        return words
    end

    # sort the words
    def Ex25.sort_words(words)
        return words.sort
    end

    # get the first word in array
    def Ex25.print_first_word(word)
        return word.shift
    end

    # get the last word in array
    def Ex25.print_last_word(word)
        return word.pop
    end

    # Takes in a full sentence and returns the sorted words.
    def Ex25.sort_sentences(sentence) 
        words = Ex25.break_words(sentence)
        return Ex25.sort_words(words)
    end

    # Prints the first and last words of the sentence.
    def Ex25.print_first_and_last(sentence)
        words = Ex25.break_words(sentence)
        first = Ex25.print_first_word(words)
        last = Ex25.print_last_word(words)
    end 

    # Sorts the words then prints the first and last one.
    def Ex25.print_first_and_last_sorted(sentence)
        words = Ex25.sort_sentences(sentence)
        Ex25.print_first_word(words)
        Ex25.print_last_word(words)
    end
end