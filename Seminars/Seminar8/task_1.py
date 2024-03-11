# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
from pathlib import Path

_PATH_SOURCE = Path.cwd() / 'task_1' / 'source'
_PATH_RESULT = Path.cwd() / 'task_1' / 'result.json'


def func(input_data: Path = _PATH_SOURCE, output: Path = _PATH_RESULT):
    with open(input_data, 'r', encoding='utf-8') as source, \
            open(output, 'w', encoding='utf-8') as result:
        data = {}
        while line := source.readline():
            data[line.split('|')[0].capitalize()] = float(line.split('|')[1].strip())
        json.dump(data, result, separators=(',\n', ':'))


if __name__ == '__main__':
    func()
