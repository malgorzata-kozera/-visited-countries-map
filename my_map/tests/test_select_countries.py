import pytest
from my_map.select_countries import select_options

class TestClass(object):
    def test_options_europe_uncorect(self):
        """Test that function select_options is not returning something different then countries from Europe"""
        assert select_options('Europe') != ['some text','some text']

    def test_options_asia_uncorect(self):
        """Test that function select_options is not returning something different then countries from Asia"""
        assert select_options('Asia') != ['some text']

    def test_options_oceania_uncorect(self):
        """Test that function select_options is not returning something different then countries from Oceania"""
        assert select_options('Oceania') != ['some text']

    def test_options_africa_uncorect(self):
        """Test that function select_options is not returning something different then countries from Africa"""
        assert select_options('Africa') != ['some text']

    def test_options_antarctica_uncorect(self):
        """Test that function select_options is not returning something different then countries from Antarctica"""
        assert select_options('Antarctica') != ['some text']

    def test_options_north_america_uncorect(self):
        """Test that function select_options is not returning something different then countries from North America"""
        assert select_options('North America') != ['some text']

    def test_options_south_america_uncorect(self):
        """Test that function select_options is not returning something different then countries from South America"""
       assert select_options('South America') != ['some text']

    def test_europe_corect(self):
        assert select_options('Europe') == [('Albania', 'Albania'), ('Andorra', 'Andorra'),
                                             ('Austria', 'Austria'), ('Belarus', 'Belarus'),
                                             ('Belgium', 'Belgium'), ('Bosnia and Herzegovina',
                                                                      'Bosnia and Herzegovina'),
                                             ('Bulgaria', 'Bulgaria'), ('Croatia', 'Croatia'),
                                             ('Czech Republic', 'Czech Republic'), ('Denmark',
                                                                                    'Denmark'),
                                             ('Estonia', 'Estonia'), ('Faroe Islands',
                                                                      'Faroe Islands'),
                                             ('Finland', 'Finland'), ('France', 'France'),
                                             ('Germany', 'Germany'), ('Gibraltar', 'Gibraltar'),
                                             ('Greece', 'Greece'), ('Holy See (Vatican City)',
                                                                    'Holy See (Vatican City)'),
                                             ('Hungary', 'Hungary'), ('Iceland', 'Iceland'),
                                             ('Ireland', 'Ireland'), ('Italy', 'Italy'),
                                             ('Latvia', 'Latvia'), ('Liechtenstein',
                                                                    'Liechtenstein'),
                                             ('Lithuania', 'Lithuania'), ('Luxembourg',
                                                                          'Luxembourg'),
                                             ('Macedonia', 'Macedonia'), ('Malta', 'Malta'),
                                             ('Moldova', 'Moldova'), ('Monaco', 'Monaco'),
                                             ('Netherlands', 'Netherlands'), ('Norway', 'Norway'),
                                             ('Poland', 'Poland'), ('Portugal', 'Portugal'),
                                             ('Romania', 'Romania'), ('Russia', 'Russia'),
                                             ('San Marino', 'San Marino'), ('Slovakia', 'Slovakia'),
                                             ('Slovenia', 'Slovenia'), ('Spain', 'Spain'),
                                             ('Svalbard', 'Svalbard'), ('Sweden', 'Sweden'),
                                             ('Switzerland', 'Switzerland'), ('Ukraine', 'Ukraine'),
                                             ('United Kingdom', 'United Kingdom'),
                                             ('Isle of Man', 'Isle of Man'), ('Montenegro', 'Montenegro'),
                                             ('Aland Islands', 'Aland Islands'),
                                             ('Serbia', 'Serbia')]
        #
        # def test_asia_corect(self):
        #     continent = 'Europe'
        #     assert select_options(continent) ==
        #
        # def test_africa_corect(self):
        #     assert select_options('Africa') ==
        #
        # def test_ocenia_corect(self):
        #     assert select_options('Oceania') ==
        #
        # def test_antarctica_corect(self):
        #     assert select_options('Antarctica') ==
        #
        # def test_north_america_corect(self):
        #     assert select_options('North America') ==
        #
        # def test_south_america_corect(self):
        #     assert select_options('South America') ==
        #
        #








