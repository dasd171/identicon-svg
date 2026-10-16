import hashlib, sys
def identicon(text, size=5, px=40):
    h = hashlib.md5(text.encode()).hexdigest(); color = "#" + h[:6]
    bits = [int(c, 16) % 2 == 0 for c in h[6:]]; cells = []
    for y in range(size):
        for x in range((size + 1) // 2):
            if bits[y * 3 + x]:
                for xx in {x, size - 1 - x}: cells.append(f'<rect x="{xx*px}" y="{y*px}" width="{px}" height="{px}"/>')
    s = size * px
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}"><rect width="100%" height="100%" fill="#f0f0f0"/><g fill="{color}">{"".join(cells)}</g></svg>'
if __name__ == "__main__":
    name = " ".join(sys.argv[1:]) or "hello"
    open(f"{name}.svg", "w").write(identicon(name)); print(f"已生成 {name}.svg")
