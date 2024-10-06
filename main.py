import os


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data


def task_one():
    def fill_cook_book(data):
        book = {}
        dish = None
        count_ingredients = 0
        list_ingredients = []

        for line in data:
            line = line.strip()
            if line.isnumeric():
                count_ingredients = int(line)
            elif line.find('|') != -1 and count_ingredients > 0:
                arr = line.split('|')
                list_ingredients.append(
                    {
                        'ingredient_name': arr[0],
                        'quantity': int(arr[1]),
                        'measure': arr[2],
                    }
                )
                count_ingredients -= 1
                if count_ingredients == 0 and dish is not None:
                    book.setdefault(dish, list_ingredients)
                    list_ingredients = []
            else:
                dish = line
        return book

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for dish in dishes:
            for dish_from_book, list_ingredients in cook_book.items():
                if dish_from_book == dish:
                    for ingredient in list_ingredients:
                        ingredient_name = ingredient['ingredient_name'].strip()
                        measure = ingredient['measure'].strip()
                        quantity = ingredient['quantity']
                        if ingredient_name not in shop_list:
                            shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity * person_count}
                        else:
                            shop_list[ingredient_name]['quantity'] += quantity * person_count
        return shop_list

    data_file = read_file('recipes.txt')
    cook_book = fill_cook_book(data_file)
    shop_person_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

    print(cook_book)
    print(shop_person_list)


def task_two():

    def read_files_from_folder(file_names):
        files = {}
        for file_name in file_names:
            file_path = os.path.join('.\\sorted', file_name)
            data_file = read_file(file_path)
            files[file_name] = {'count_row': len(data_file), 'data': data_file}
        return files

    def write_result_file(files):
        with open('.\\sorted\\result.txt', 'w', encoding='utf-8') as file:
            for file_name, info in files.items():
                file.writelines(file_name+'\n'+str(info['count_row'])+'\n')
                for line in info['data']:
                    file.write(line)
                file.write('\n')

    list_file_names = ['1.txt', '2.txt', '3.txt']
    dict_files = read_files_from_folder(list_file_names)
    sorted_dict_files = {key: value for key, value in sorted(dict_files.items(), key=lambda item: item[1]['count_row'])}
    write_result_file(sorted_dict_files)


if __name__ == "__main__":
    task_one()
    task_two()
