from behave import given, then


@given('query "{query}"')  # noqa
def step_impl(context, query):
    cur = context.conn.cursor()
    cur.execute(query)
    cur.execute('commit;')


@then('query "{query}" equals')  # noqa
def step_impl(context, query):
    cur = context.conn.cursor()
    cur.execute(query)
    r = cur.fetchall()
    formatted = ';'.join(map(lambda x: '|'.join(map(str, x)), r))
    res = []
    for row in context.table:
        res.append(row['seq'] + '|' + row['op'])
    result = ';'.join(res)
    assert formatted == result, 'Unexpected result: ' + formatted
