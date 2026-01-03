import os


def copy_file(source, destination, chunk_size=4096):
        if not os.path.exists(source):
            print(f"에러: {source} 파일을 찾을 수 없습니다")
            return False

        file_size = os.path.getsize(source)
        copied_size = 0

        with open(source, 'rb') as f_in:
            with open(destination, 'wb') as f_out:
                while True:
                    chunk = f_in.read(chunk_size)
                    if not chunk:
                        break
                    f_out.write(chunk)
                    copied_size += len(chunk)

        dest_size = os.path.getsize(destination)
        print(f"복사 완료!")
        print(f"원본 파일 크기: {file_size} bytes")
        print(f"복사본 파일 크기: {dest_size} bytes")
        print(f"일치 여부: {'일치' if file_size == dest_size else '불일치'}")
        return True


with open('original.txt', 'w', encoding='utf-8') as f:
    f.write("테스트 파일입니다.\n" * 100)

copy_file('original.txt', 'copied.txt')