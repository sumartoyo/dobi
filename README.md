access a dict like an object

## Installation

```
pip install dobi
```

## Usage

create a dobi like you create a dict

```
>>> from dobi import dobi
>>> person = dobi(name='john', age=42)
>>> cat = dobi({'name': 'mr fluffy', age=5})
```

access it like a dict or an object

```
>>> person['name']
'john'
>>> person.name
'john'
>>> person.name = 'sam'
>>> person.name
'sam'
>>> person.country = 'china'
>>> person.country
'china'
>>> del person.country
>>> person
{'name': 'sam', 'age': 42}
```

object-style access to unkown key returns `None` whereas in dict-style raises **KeyError**

it can do whatever a dict can do

```
>>> len(person)
2
>>> 'name' in person
True
>>> 'unknown_key' in person
False
>>> for key in person: print(key, person[key]) 
name sam
age 42
>>> import json
>>> json.dumps(person)
'{"name": "sam", "age": 42}'
```

use `.todict()` to convert back to dict

```
>>> type(person.todict())
<class 'dict'>
```

check is something a dobi

```
>>> dobi.isdobi(person)
True
>>> dobi.isdobi(person.todict())
False
```

## License

MIT
