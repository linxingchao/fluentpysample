

def get_creatoes(record:dict) -> list:
    match record:
        case {'type':'book','api':2,'authors':[*names]}:
            return names
        case {'type':'book','api':2,'authors':name}:
            return [name]
        case {'type':'book'}:
            raise ValueError(f"invalid 'book' record:{record!r}")
        case _:
            raise ValueError(f'invalid record:{record!r}')