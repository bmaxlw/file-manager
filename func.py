import time
import datetime
import os


class FileManager:

    def track_files_in_dir(self, dir_path: str, log_path: str, refresh_time: int) -> None:
        while True:
            dir_objects: list = os.listdir(dir_path)
            objects = '\n'.join(dir_objects)
            with open(log_path, 'a') as log:
                log.write(f'\n{datetime.datetime.now()}\n{objects}\n')
                log.close()
            print(f'{datetime.datetime.now()} | Recording...')
            time.sleep(refresh_time)

    def move_files(self, src_dir: str, tgt_dir: str, extensions: tuple = ()) -> None:
        if len(extensions) == 0:
            for file in os.listdir(src_dir):
                os.rename(f'{src_dir}/{file}', f'{tgt_dir}/{file}')
        elif len(extensions) > 0:
            for ext in extensions:
                for file in os.listdir(src_dir):
                    if file.__contains__(ext):
                        os.rename(f'{src_dir}/{file}', f'{tgt_dir}/{file}')
                    else:
                        continue
