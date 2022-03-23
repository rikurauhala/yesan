import unittest

from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_rahamaara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_maara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_maukkaiden_maara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisten_kateisosto_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisten_kateisosto_palauttaa_vaihtorahaa_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(260), 20)

    def test_edullisten_kateisosto_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisten_riittamaton_kateisosto_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisten_riittamaton_kateisosto_palauttaa_rahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(10), 10)

    def test_edullisten_riittamaton_kateisosto_ei_kasvata_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_kateisosto_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaiden_kateisosto_palauttaa_vaihtorahaa_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(420), 20)

    def test_maukkaiden_kateisosto_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaiden_riittamaton_kateisosto_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaiden_riittamaton_kateisosto_palauttaa_rahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(10), 10)

    def test_maukkaiden_riittamaton_kateisosto_ei_kasvata_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisten_korttiosto_veloittaa_summan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 260)

    def test_edullisten_korttiosto_palauttaa_true(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_edullisten_korttiosto_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisten_riittamaton_korttiosto_ei_muuta_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_edullisten_riittamaton_korttiosto_palauttaa_false(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_edullisten_riittamaton_korttiosto_ei_kasvata_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 2)
    
    def test_edullisten_korttiosto_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaiden_korttiosto_veloittaa_summan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_maukkaiden_korttiosto_palauttaa_true(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_maukkaiden_korttiosto_kasvattaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaiden_riittamaton_korttiosto_ei_muuta_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_maukkaiden_riittamaton_korttiosto_palauttaa_false(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_maukkaiden_riittamaton_korttiosto_ei_kasvata_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaiden_korttiosto_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahan_lataaminen_kortille_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_lataaminen_kortille_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_negatiivisen_summan_lataaminen_kortille_ei_vaikuta_kortin_saldoon(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo, 500)

    def test_negatiivisen_summan_lataaminen_kortille_ei_vaikuta_kassan_rahamaaraan(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
