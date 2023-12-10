import logging
from django.shortcuts import render
from django.http import HttpResponse
from functools import wraps


logger = logging.getLogger(__name__)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'{func.__name__} launched')
        return func(*args, **kwargs)
    return wrapper


@log
def index(request):
    html = """
    <h1>Home</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit voluptate tenetur repellat odio. Neque, esse perferendis! Reprehenderit explicabo minus iusto.</p>"""
    return HttpResponse(html)


@log
def about(request):
    html = """
    <h1>About us</h1>
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quaerat magni iure veniam earum cupiditate provident asperiores omnis laborum facere, sint quisquam, culpa odio quasi beatae ex dignissimos velit rerum possimus consequatur. Aperiam dolore hic at quia modi recusandae molestiae tenetur ut provident obcaecati sunt cupiditate cum velit, consequuntur veniam nemo magnam! Facilis odio eum vitae nobis rem, delectus consequatur tempora laudantium ut nemo exercitationem nisi nihil atque. Sapiente eveniet esse incidunt possimus, saepe assumenda fugiat exercitationem quidem quis explicabo tempore placeat provident, eum quos quisquam beatae perspiciatis eos. Sed pariatur sequi eum quis debitis voluptates. Id, mollitia hic. Omnis, illum.</p>"""
    return HttpResponse(html)
