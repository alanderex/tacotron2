import random
from pathlib import Path

text_f_location = Path('../../../audioservices/project/')
text_files = sorted(text_f_location.glob('audio_text_filelist_*.txt'))

all_text = []
for tf in text_files:
    all_text.append(tf.read_text())

all_text = '\n'.join(all_text).replace('\n\n', '\n')

if '/segments/' not in all_text:
    # fix missing dir for all paths
    new_data = []
    for x in all_text.split('\n'):
        try:
            file, text = x.split('|')
            *paths, name = file.split('/')
            new_file = '/'.join(paths + ['segments', name])
            new_data.append(f"{new_file}|{text}")
        except ValueError:
            pass

    all_text = '\n'.join(new_data)

test_data = random.sample(all_text.split('\n'), 1000)

Path('filelists/audio_text_filelist_train.txt').write_text(all_text)
Path('filelists/audio_text_filelist_test.txt').write_text('\n'.join(test_data))
