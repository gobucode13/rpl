def buat_soal():
    return {"pertanyaan": "apa ibukota indonesia", "jawaban": "Jakarta"}

def hitung_skor(jawaban user, jawaban_benar):
    if jawaban_user.lower() == jawaban_benar.lower():
        return 100
    return 0

    