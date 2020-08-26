import numpy as np

'''
def py_cpu_nms(dets, thresh):
    """Pure Python NMS baseline."""
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)  # 计算出所有图片的面积
    order = scores.argsort()[::-1]  # 图片评分按升序排序

    keep = []  # 用来存放最后保留的图片的相应index
    while order.size > 0:
        i = order[0]  # i 是还未处理的图片中的最大评分index
        keep.append(i)  # 保留改图片的值
        # 矩阵操作，下面计算的是图片i分别与其余图片相交的矩形的坐标
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        # 计算出各个相交矩形的面积
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        # 计算重叠比例
        ovr = inter / (areas[i] + areas[order[1:]] - inter)

        #只保留比例小于阙值的图片，然后继续处理
        inds = np.where(ovr <= thresh)[0]
        order = order[inds + 1]

    return keep
'''

dets = np.array([[1, 1, 2, 2, 5],
                 [1.5, 1.5, 4, 4, 6],
                 [4, 4, 5, 5, 6]])

def py_nus_cpu(bbox, thresh):
    x1 = bbox[:, 0]
    y1 = bbox[:, 1]
    x2 = bbox[:, 2]
    y2 = bbox[:, 3]
    scores = bbox[:, 4]
    areas = (x2-x1+1)*(y2-y1+1)
    order = scores.argsort()[::-1]
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0, xx2-xx1+1)
        h = np.maximum(0, yy2-yy1+1)
        inter = w*h
        iou = inter/(areas[i]+areas[order[1:]]-inter)
        ind = np.where(iou <= thresh)[0]
        order = order[ind+1]
    return keep

print(py_nus_cpu(dets, 0.2))