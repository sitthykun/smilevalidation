class A:
    bb = {
        'hello': 'world'
    }


class B(A):
    # super().bb.update(
    #     {'dara':'thyda'}
    # )
    A.bb.update(
        {'dara': 'thyda'}
    )


print(B.bb)