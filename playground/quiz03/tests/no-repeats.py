test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats (list 5 4 5 4 2 2))
          867aed82218d6289678b6b3115e43cad
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (no-repeats '(1 2 3 4))
          e0e48db6907ba70b8522caf1202d820e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (no-repeats '(1 1 3 3 5 5))
          54b490738b6837f76a54c8813896eec0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (no-repeats '(3 2 1 2 3))
          c7469bc68c0286430a1e3ae9d426bd00
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (no-repeats '(4 2 4 5))
          367182e94d618bfe1fd6b3ba7bac07f7
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz03)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}