from pywebio.output import *
def navbar(link1, name1, link2, name2, link3, name3):
    navbar_html = f"""
    <ul class="nav justify-content-center fixed-top border border-black nav-fill fs-6">
        <li class="nav-item border border-black">
            <a class="nav-link fs-6" href="{link1}">{name1}</a>
        </li>
        <li class="nav-item border border-black">
            <a class="nav-link fs-6" href="{link2}">{name2}</a>
        </li>
        <li class="nav-item border border-black">
            <a class="nav-link fs-6" href="{link3}">{name3}</a>
        </li>
    </ul>
    """

    put_html(navbar_html)