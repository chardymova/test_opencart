class ProductPageLoc:
    class Photos:
        main_photo = {'css': 'ul.thumbnails > li:nth-child(1)'}
        additional_photos = {'css': 'ul.thumbnails > li:not(:nth-child(1))'}

    class Text:
        product_name = {'css': 'div#product-product div[class="col-sm-4"] h1'}

    class Actions:
        add_to_wl = {'css': 'i.fa-heart'}
        compare = {'css': 'i.fa-exchange'}
        add_to_cart = {'css': 'button#button-cart'}
        like = {'css': 'a.addthis_button_facebook_like'}
        tweet = {'css': '#twitter-widget-0'}
        share = {'css': 'a.addthis_counter'}

    class RelatedProducts:
        clickable_photos = {'css': 'div.row .product-thumb .image'}
