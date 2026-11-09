def buat_soal():
    return {"pertanyaan": "Apa ibukota Indonesia?", "jawaban": "jakarta"}

def hitung_skor(jawaban_user, jawaban_benar):
    if jawaban_user.lower() == jawaban_benar.lower():
        return 100
    return 0

