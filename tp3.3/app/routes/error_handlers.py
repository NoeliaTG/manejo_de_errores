from flask import Blueprint
from ..models.exceptions import FilmNotFound



errors = Blueprint("errors", __name__)
@errors.app_errorhandler(FilmNotFound)
def handle_bad_request(error):
    return error.get_response()