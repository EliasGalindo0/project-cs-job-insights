from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for job in result:
        assert 'title' and 'salary' and 'type' in job
        assert 'titulo' and 'salario' and 'tipo' not in job
