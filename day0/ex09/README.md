# Usage

- `python setup.py sdist bdist_wheel`
- `pip install ./dist/ft_package-0.0.1-py3-none-any.whl`
- `pip show -v ft_package`

```py
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```