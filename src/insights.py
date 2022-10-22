from src import jobs


def get_unique_job_types(path):
    content = jobs.read(path)
    job_types = []

    for row in content:
        if row['job_type'] not in job_types:
            job_types.append(row['job_type'])

    return job_types


def filter_by_job_type(jobs, job_type):
    result = []

    for row in jobs:
        if row['job_type'] == job_type:
            result.append(row)

    return result


def get_unique_industries(path):
    content = jobs.read(path)
    industry = []

    for row in content:
        if row['industry'] not in industry and row['industry'] != '':
            industry.append(row['industry'])

    return industry


def filter_by_industry(jobs, industry):
    result = []

    for row in jobs:
        if row['industry'] == industry:
            result.append(row)

    return result


def get_max_salary(path):
    content = jobs.read(path)
    salary = []

    for item in content:
        if item['max_salary'].isnumeric():
            salary.append(int(item['max_salary']))

    return max(salary)


def get_min_salary(path):
    content = jobs.read(path)
    salary = []

    for item in content:
        if item['min_salary'].isnumeric():
            salary.append(int(item['min_salary']))

    return min(salary)


def matches_salary_range(job, salary):
    if ('min_salary' not in job or 'max_salary' not in job):
        raise ValueError("doesn't exists")
    elif (type(job['min_salary']) != int or type(job['max_salary']) != int):
        raise ValueError("aren't valid integers")
    elif(job['min_salary'] > job['max_salary']):
        raise ValueError("Salary min is greather than Max Salary")
    elif(type(salary) != int):
        raise ValueError("Salary isn't a valid integer")
    else:
        return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
