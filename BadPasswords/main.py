def is_password_rejected(seq, p_old, p_new):
    for s in seq:
        prefix = ""
        suffix = ""
        if p_old in s and p_new in s:
            for i in range(min(len(p_old), len(p_new))):
                if p_old[i] != p_new[i]:
                    break
                prefix += p_old[i]
            for i in range(1, min(len(p_old), len(p_new)) + 1):
                if p_old[-i] != p_new[-i]:
                    break
                suffix = p_old[-i] + suffix
            if p_old[len(prefix):-len(suffix)] in s and p_new[len(prefix):-len(suffix)] in s:
                return True
    return False

n = int(input())
sequences = []
for _ in range(n):
    sequence = input().split()[1:]
    sequences.append("".join(sequence))

p = int(input())
for _ in range(p):
    p_old, p_new = input().split()
    rejected = is_password_rejected(sequences, p_old, p_new)
    if rejected:
        print("REJECT")
    else:
        print("OK")
