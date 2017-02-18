

class icc_fosgenTests:

    def setUp(self):
        pass

    def test_something(self):
        self.assertEqual(1 + 1, 2)

    def tearDown(self):
        pass


class TestsSimples:

    #    def test_str_eq(self):
    #        assert 'ОПК–2' == "ОПК-2"

    def test_extractor_competentions(self):
        from icc.fosgen.constants import extract_comps, COMPETENTIONS
        d = extract_comps(COMPETENTIONS)
        print(d)
        assert len(d) >= 3
        assert d["ОК-7"]
        assert d["ОПК-2"]
        assert d["ОПК-5"]

    def test_extractor_labs(self):
        from icc.fosgen.constants import extract_work_names, LABS
        d = extract_work_names(LABS)
        print(d)
        assert len(d) >= 5
        assert d[1]


class ExampleOfAIWorkProgram:
    pass
