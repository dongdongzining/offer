def iou(x1,y1,w1,h1,x2,y2,w2,h2):
    up = min(y1 + h1 / 2, y2 + h2 / 2)
    down = max(y1 - h1 / 2, y2 - h2 / 2)
    left = max(x1 - w1 / 2, x2 - w2 / 2)
    right = min(x1 + w1 / 2, x2 + w2 / 2)

    if up > down and right > left:
        intersetion = (up - down) * (right - left)
        union = w1 * h1 + w2 * h2 - intersetion
        return intersetion / union
    else:
        return 0