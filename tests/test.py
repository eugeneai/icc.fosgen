

class icc_fosgenTests:

    def setUp(self):
        pass

    def test_something(self):
        self.assertEqual(1 + 1, 2)

    def tearDown(self):
        pass


class TestsSimples:

    def test_extractor(self):
        from icc.fosgen.constants import extract_comps, COMPETENTIONS
        d = extract_comps(COMPETENTIONS)
        print(d)
        assert len(d) >= 3


class ExampleOfAIWorkProgram:
    pass
