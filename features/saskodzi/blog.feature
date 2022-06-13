# language: pl

@saskodzi
Właściwość: Blog Posty

    @web @automated @blog-posts @debug
    Szablon scenariusza: Listowanie postów na blogu - "<domena>"
        Zakładając że blog zostanie odwiedzony używając domeny <domena>
        Jeśli odwiedzający kliknie przycisk "Blog"
        Wtedy powinien zostać przekierowany do strony z blogiem
        Oraz powinien zostać wyświetlony nagłówek "Posty"
        Oraz posty powinny zostać wylistowane

        Przykłady:
          | domena                   |
          | https://saskodzi.pl      |
          | https://blog.saskodzi.pl |


    @web @automated @blog-posts
    Szablon scenariusza: Przejście do posta - "<post>"
        Zakładając że blog zostanie odwiedzony używając domeny <domena>
        Jeśli zostanie wybrany nagłówek posta <naglowek_posta>
        Wtedy powinien zostać wyświetlony ekran z postem <naglowek_posta>

        Przykłady:
          | domena                        | naglowek_posta        |
          | https://saskodzi.pl/blog      | Python dictionary FUN |
          | https://saskodzi.pl/blog      | Python string FUN     |
          | https://blog.saskodzi.pl/blog | Python dictionary FUN |
          | https://blog.saskodzi.pl/blog | Python string FUN     |
