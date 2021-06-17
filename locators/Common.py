class SearchLoc:
    input_group = {'css': '#search'}
    input_field = {'css': input_group['css'] + ' input[type = text]'}
    search_button = {'css': input_group['css'] + ' button[type = button]'}


class CartLoc:
    cart_button = {'css': 'div#cart'}
    cart_view = {'css': 'i.fa-shopping-cart'}
