import validators
import pytube

youTube_page = "https://www.youtube.com/pqtjup(io"
valid = validators.url(pytube.Search(youTube_page))
print(valid)