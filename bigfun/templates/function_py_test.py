CACHE = {}
CURRENT_LOCATION = 'europe-west1'


def run():
    {% for name, value in arguments %}
    {{ name }} = {{ value | indent(4) }}
    {% endfor %}

    {{ code | indent(4) }}

result = run()
print(result)