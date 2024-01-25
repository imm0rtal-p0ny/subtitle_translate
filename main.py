from googletrans import Translator


def run(path, name, lang='uk'):
    data = build(path)
    translate(data, lang)
    if save(data, name):
        print('Done')


def build(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = (f.read())
        data = data.split('\n\n')
        result = []
        for i in data:
            result.append(i.split('\n'))

    return result


def translate(data, language):
    for j in data:
        translator = Translator()
        for i in j[2:]:
            result = translator.translate(i, dest=language)
            j.append(result.text)

        return data


def save(data, name):
    result = ''
    for column in data:
        result += '\n'.join(column)
        result += '\n\n'
    with open(name + '.srt', 'w', encoding='utf-8') as f:
        f.write(result)

    return True

