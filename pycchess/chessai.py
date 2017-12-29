ai_engines = {}
ai_engines['harmless'] = {
    'options': {
        'engine_executable': './harmless',
        'support_fen_moves': False,
        'support_fen_startpos': False
    }
}
ai_engines['eleeye'] = {
    'options': {
        'engine_executable': './eleeye',
        'support_fen_moves': True,
        'support_fen_startpos': True
    }
}

def get_ai_engine_options(name):
    if name in ai_engines:
        return ai_engines[name]['options']
    return {}
