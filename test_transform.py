import pytest
from utils.transform import transform_data

def test_transform_data():
    sample_raw = [
        {
            'title': 'Produk A', 
            'price': '10 USD', 
            'description': 'Deskripsi produk A', 
            'rating': '4.5 / 5', 
            'colors': '3 Colors',
            'size': 'Size: M',
            'gender': 'Gender: Male'
        },
        {
            'title': 'Produk B', 
            'price': '20 USD', 
            'description': 'Deskripsi produk B', 
            'rating': '5 / 5', 
            'colors': '2 Colors',
            'size': 'Size: L',
            'gender': 'Gender: Female'
        },
    ]

    transformed = transform_data(sample_raw)

    assert 'colors' in transformed.columns
    assert transformed.shape[0] == 2
    assert transformed['price'].dtype == float
    assert transformed['rating'].dtype == float
    assert all(isinstance(x, int) for x in transformed['colors'])
    assert all(isinstance(x, str) for x in transformed['size'])
    assert all(isinstance(x, str) for x in transformed['gender'])
    assert transformed.loc[0, 'price'] == 10 * 16000
    assert transformed.loc[1, 'colors'] == 2
    assert transformed.loc[0, 'size'] == 'M'
    assert transformed.loc[1, 'gender'] == 'Female'