# To be changed

def compute_ik(dx, dy):
    base_rotation = dx * 0.1
    shoulder_angle = dy * 0.1
    elbow_angle = (dx + dy) * 0.05
    wrist_angle = 0
    return [base_rotation, shoulder_angle, elbow_angle, wrist_angle]
