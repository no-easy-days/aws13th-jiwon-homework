def text_statistics(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        max_line_length = max(len(line) for line in lines) if lines else 0

        print(f"전체 줄 수: {line_count}")
        print(f"전체 단어 수: {word_count}")
        print(f"전체 문자 수: {char_count}")
        print(f"가장 긴 줄의 길이: {max_line_length}")


text_statistics('text.txt')