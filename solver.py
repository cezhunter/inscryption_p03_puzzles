def func_alpha(k, n):
    
    """
        given a k and an n (how many playable cards, and the length of the chain)
        return all possible combinations of positions of cards with no repeating.
    """
    
    def any_repeat(l):
        for i in l:
            if l.count(i) > 1:
                return True
        return False

    def inner(l, d):
        i = 0
        r = []
        while i < n:
            l[d] = i
            if d == len(l) - 1:
                if not any_repeat(l):
                    r.append(tuple(l))
            else:
                r += inner(l[:], d+1)
            i += 1
        return r
    r = inner(k*[0], 0)
    return r



def func_beta(lis, option, vals):
    mapping = {c: v for c, v in zip(option, vals)}
    s = t = 0
    for i in sorted(option) + [len(lis)]:
        vals = [mapping.get(s-1), mapping.get(i)]
        if None in vals:
            additional = 0
        else:
            additional = sum(vals)
        t += sum([item + additional for item in lis[s:i]])
        s = i + 1
    return t


def func_pi(option, seq, k):
    r = seq[:]
    for i, o in enumerate(option):
        r[o] = f'[{k[i]}]'
    return tuple(r)
        

def func_gamma(seq, k, target):
    options = func_alpha(len(k), len(seq))
    solutions = []
    for option in options:
        r = func_beta(lis, option, k)
        if r == target:
            solutions.append(func_pi(option, seq, k))
    return set(solutions)