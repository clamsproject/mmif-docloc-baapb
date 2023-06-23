import unittest
from mmif_docloc_baapb import resolve

class TestDocloc(unittest.TestCase):
    #using the search directory wgbh in llc_data/clams in the julia-child server
    def test_resolve(self):
        result = resolve("baapb://cpb-aacip-75-84zgn33s.video")
        self.assertEqual(result, "wgbh/NJN_Network/cpb-aacip-75-84zgn33s.mp4")

if __name__ == '__main__':
    unittest.main()