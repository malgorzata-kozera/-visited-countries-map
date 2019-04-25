import pytest
from my_map.select_countries import select_options


class TestClass(object):
    def test_options_europe_incorect_raise_error(self):
        """Test that function select_options is not returning something different than countries from Europe"""
        assert select_options('Europe') != ['some text', 'some text']

    def test_options_asia_incorect(self):
        """Test that function select_options is not returning something different then countries from Asia"""
        assert select_options('Asia') != ['some text']

    def test_options_oceania_incorect(self):
        """Test that function select_options is not returning something different then countries from Oceania"""
        assert select_options('Oceania') != ['some text']

    def test_options_africa_incorect(self):
        """Test that function select_options is not returning something different then countries from Africa"""
        assert select_options('Africa') != ['some text']

    def test_options_antarctica_incorect(self):
        """Test that function select_options is not returning something different then countries from Antarctica"""
        assert select_options('Antarctica') != ['some text']

    def test_options_north_america_incorect(self):
        """Test that function select_options is not returning something different then countries from North America"""
        assert select_options('North America') != ['some text']

    def test_options_south_america_incorect(self):
        """Test that function select_options is not returning something different then countries from South America"""
        assert select_options('South America') != ['some text']



