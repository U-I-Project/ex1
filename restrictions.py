import ast

def check_import(tree, allowed_import):
    for stmt in ast.walk(tree):
        if isinstance(stmt, ast.Import):
            for alias in stmt.names:
                assert alias.name in allowed_import, 'import module {0} is not allowed'.format(alias.name)
        if isinstance(stmt, ast.ImportFrom):
            assert stmt.module in allowed_import, 'import module {0} is not allowed'.format(stmt.module)

def check_anti_stmt(tree, disallowed_stmt):
    for stmt in ast.walk(tree):
        assert type(stmt) not in disallowed_stmt, 'statement {0} is not allowed'.format(type(stmt))

def main():
    import_set = ('sys', 'math')
    stmt_antiset = (ast.For, ast.While, ast.AsyncFor)

    with open("leapmonth.py") as f:
        tree = ast.parse(f.read())
    check_import(tree, import_set)
    check_anti_stmt(tree, stmt_antiset)

if __name__ == '__main__':
    main()
