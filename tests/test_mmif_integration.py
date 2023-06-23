import unittest
from mmif.serialize import Document
from mmif import Mmif

class TestDocloc(unittest.TestCase):
    #using the search directory wgbh in llc_data/clams in the julia-child server
    def test_mmif_integration(self):
        new_doc = Document()
        new_doc.id = "d1"
        docloc = 'baapb://cpb-aacip-75-84zgn33s.video'
        new_doc.location = docloc
        self.assertEqual(new_doc.location_path(), "wgbh/NJN_Network/cpb-aacip-75-84zgn33s.mp4")

if __name__ == '__main__':
    unittest.main()

