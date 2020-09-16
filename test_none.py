n = None
s = ''
bf = False
b = b''
r = r''
d = {}
l = []
st = ()
bt = True

if n:
    print(f'n={n} is not None')

if s:
    print(f's={s} is not None')

if bf:
    print(f'bf={bf} is not None')

if bt:
    print(f'bt={bt} is not None and True')

if b:
    print(f'b={b} is not None')

if r:
    print(f'r={r} is not None')

if d:
    print(f'd={d} is not None')

if l:
    print(f'l={l} is not None')

if st:
    print(f'set={st} is not None')
else:
    print(f'{type(st)}')

if bool('fdafd'):
    print(f'if show this message, it meant, test string with bool("fdafd") is True')

if 'fdavd':
    print(f'if show this message, it meant, test string with "fdavd" is True')

if 121:
    print(f'if show this message, it meant, test numeric with 121 is True')

print('test')