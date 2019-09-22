from howdoi import howdoi


def solve_query(query):
    search_query = query
    parser = howdoi.get_parser()
    args = vars(parser.parse_args(query.split(' ')))
    output = howdoi.howdoi(args)
    return output

