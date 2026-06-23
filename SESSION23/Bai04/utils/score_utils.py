# module tính toán thực hiện quan tới điểm số

# hàm tính toán điểm trung bình
def calculate_average(scores: list) -> float | str:
    if not scores:
        return 0.0, "None"

    # Tính tổng trực tiếp bằng hàm sum(scores) gọn sạch code
    total_score = sum(scores)
    avg_score = total_score / len(scores)

    # tính rank
    if avg_score >= 8:
        rank = "Giỏi"
    elif avg_score >= 6.5:
        rank = "Khá"
    elif avg_score >= 5.0:
        rank = "Trung binh"
    else:
        rank = "Yeu"

    return avg_score, rank
