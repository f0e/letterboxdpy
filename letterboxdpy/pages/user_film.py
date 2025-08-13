from letterboxdpy.core.scraper import parse_url
from letterboxdpy.constants.project import DOMAIN, GENRES


class UserFilm:
    def __init__(self, username: str) -> None:
        self.username = username
        self.url = f"{DOMAIN}/{self.username}/film"

    def get_film(self, film_slug: str) -> dict:
        return extract_user_film(self.url, film_slug)


def extract_user_film(url: str, film_slug: str) -> dict:
    try:
        dom = parse_url(f"{url}/{film_slug}/")
    except:
        return None

    film_info = {}

    # Extract film name
    film_name_tag = dom.find("h2", class_="name -primary prettify")
    if film_name_tag and film_name_tag.a:
        film_info["name"] = film_name_tag.a.text.strip()

    # Extract release year
    release_year_tag = dom.find("span", class_="releasedate")
    if release_year_tag and release_year_tag.a:
        film_info["release_year"] = int(release_year_tag.a.text.strip())

    # Extract rating
    rating_tag = dom.find("span", class_="rating")
    if rating_tag:
        # Rating is in the last part of the class name, e.g., 'rated-large-10' -> 10
        rating_classes = rating_tag.get("class", [])
        for cls in rating_classes:
            if "rated-large-" in cls:
                try:
                    film_info["rating"] = (
                        int(cls.split("-")[-1]) / 2
                    )  # Ratings are out of 10, convert to 5-star
                    break
                except ValueError:
                    film_info["rating"] = None  # Fallback if parsing fails
    else:
        film_info["rating"] = None

    # Extract liked status
    liked_tag = dom.find("span", class_="icon-liked")
    film_info["liked"] = bool(liked_tag)

    # Extract view date
    view_date_meta_tag = dom.find("meta", content=True)
    if (
        view_date_meta_tag
        and view_date_meta_tag.get("content")
        and "20" in view_date_meta_tag.get("content")
    ):
        film_info["view_date"] = view_date_meta_tag["content"]
    else:
        # Fallback to parsing from p.view-date if meta tag isn't as expected or missing
        view_date_links = dom.select("p.view-date a")
        if len(view_date_links) >= 3:
            day = view_date_links[0].text.strip()
            month = view_date_links[1].text.strip()
            year = view_date_links[2].text.strip()
            # This will create a string like "03 Sep 2024". You might want to parse it into a date object.
            film_info["view_date"] = f"{day} {month} {year}"
        else:
            film_info["view_date"] = None

    return film_info
