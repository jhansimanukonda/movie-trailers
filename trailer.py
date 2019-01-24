import media
import fresh_tomatoes

frozen=media.Animatedmovies("frozen",
                    "animated movie",
                    "http://p6.storage.canalblog.com/67/10/1051847/91176699_o.jpg",
                    "https://youtu.be/FLzfXQSPBOg")
tangled=media.Animatedmovies("tangled",
                        "animated movie",
                        "http://i.ebayimg.com/00/s/NDk5WDM1OA==/z/0UgAAOxyVLNS-sa5/$_3.JPG?set_id=2",
                        "https://youtu.be/2f516ZLyC6U")
cinderella=media.Animatedmovies("cinderella",
                    "animated movie",
                    "https://i.pinimg.com/originals/aa/80/fc/aa80fc86e6f49ef560c141f364d23534.jpg",
                    "https://youtu.be/cL-RjWKtZrM")
movies=[frozen,tangled,cinderella]
fresh_tomatoes.open_movies_page(movies)
