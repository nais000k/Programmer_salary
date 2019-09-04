import requests
from terminaltables import AsciiTable, DoubleTable, SingleTable
from secondary_functions import print_statistics_table_view, predict_salary 
from terminaltables import AsciiTable

URL = "https://api.hh.ru/vacancies/"
HEADERS = {"User-Agent": "User-Agent"}
SEARCH_AREA = 1
SEARCH_PERIOD = 30


def get_quantity_of_vacancies(vacancy):
    params = {
        "text": "Разработчик {}".format(vacancy),
        "area": SEARCH_AREA,
        "period": SEARCH_PERIOD}
    response = requests.get(URL, params=params, headers=HEADERS)
    response.raise_for_status()
    response = response.json()
    quantity_of_vacancy = response["found"]
    return quantity_of_vacancy


def get_salaries_of_developers(vacancy):
    global_vacancy_data = get_global_vacancy_data(vacancy)
    salaries_in_rub = []
    salaries = []
    for page in global_vacancy_data:
        for item in page:
            item = item["salary"]
            salaries.append(item)
    for salary in salaries:
        if salary["currency"] != "RUR":
            salary = {"from": None, "to": None}
        else:
            salary = salary
        salaries_in_rub.append(salary)
    return salaries_in_rub


def get_vacancy_processed(predicted_salaries):
    vacancy_processed = 0
    for salary in predicted_salaries:
        if salary != 0:
            vacancy_processed += 1
    return vacancy_processed


def get_average_salary_for_one_vacancy(predicted_salaries):
    average_salary_for_one_vacancy = sum(
        predicted_salaries) / get_vacancy_processed(predicted_salaries)
    return int(average_salary_for_one_vacancy)


def get_global_vacancy_data(vacancy):
    global_vacancy_data = list()
    page = 0
    pages_number = 1
    while page < pages_number:
        params = {
            "text": "{}".format(vacancy),
            "area": SEARCH_AREA,
            "period": SEARCH_PERIOD,
            "only_with_salary": "True",
            "page": page}
        page_data = requests.get(URL, params=params, headers=HEADERS)
        page_data.raise_for_status()
        page_data = page_data.json()
        pages_number = page_data['pages']
        print("{} Добавлено из {}".format(page, page_data["pages"]))
        page += 1
        global_vacancy_data.append(page_data["items"])
    return global_vacancy_data


def get_statistics_for_languages():
    top_10_programming_languages = [
        "Javascript",
        "Java",
        "Python",
        "Ruby",
        "PHP",
        "C++",
        "C#",
        "C",
        "Go",
        "Scala"]
    statistics_for_all_languages = dict()
    for language in top_10_programming_languages:
        salaries = get_salaries_of_developers(language)
        predicted_salaries = [predict_salary(salary["from"], salary["to"]) for salary in salaries]
        statistics_for_all_languages[language] = {
                "vacancy_found": get_quantity_of_vacancies(language),
                "vacancy_processed": get_vacancy_processed(predicted_salaries),
                "average_salary": get_average_salary_for_one_vacancy(predicted_salaries)
            }
    return statistics_for_all_languages


if __name__ == "__main__":
    try:
        stat_for_langguages = get_statistics_for_languages()
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))
    except requests.exceptions.ConnectionError as error:
        exit("Can't get data from server:\n{0}".format(error))
    print_statistics_table_view(stat_for_langguages)
   