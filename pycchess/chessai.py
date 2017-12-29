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
        'engine_executable': './eleeye/eleeye',
        'support_fen_moves': True,
        'support_fen_startpos': True
    }
}
ai_engines['bitstronger'] = {
    'options': {
        'engine_executable': './BitStronger/BitStronger',
        'support_fen_moves': True,
        'support_fen_startpos': True
    }
}
ai_engines['mars'] = {
      'options': {
      'engine_executable': './mars',
      'support_fen_moves': False,
      'support_fen_startpos': False
                                      }
}

def get_ai_engine_options(name):
    if name in ai_engines:
        return ai_engines[name]['options']
    return {}
