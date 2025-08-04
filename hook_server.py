from flask import Flask, request, jsonify
from requests_toolbelt.multipart import decoder
import os
from PIL import Image
import pytesseract
import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3:8b"

app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def hook():
    # Ambil raw data dan header
    content_type = request.headers.get('Content-Type', '')
    data = request.get_data()
    print("\n=== REQUEST RECEIVED ===")
    print("Headers:", dict(request.headers))
    print("Content-Type:", content_type)
    print("request.data (truncated):", data[:300])

    # Handle multipart (file)
    if "multipart" in content_type or data.startswith(b"--"):
        if "multipart" in content_type:
            multipart_data = decoder.MultipartDecoder(data, content_type)
        else:
            boundary = data.split(b"\r\n")[0][2:].decode()
            multipart_data = decoder.MultipartDecoder(data, "multipart/form-data; boundary=" + boundary)

        os.makedirs("uploads", exist_ok=True)
        ocr_text = ""
        for part in multipart_data.parts:
            cd = part.headers.get(b'Content-Disposition', b'').decode()
            if 'filename=' in cd:
                filename = cd.split('filename=')[1].replace('"','').strip()
                filepath = os.path.join("uploads", filename)
                with open(filepath, "wb") as f:
                    f.write(part.content)
                print(f"File saved: {filepath}")
                # OCR langsung
                try:
                    text = pytesseract.image_to_string(Image.open(filepath))
                    ocr_text = text.strip()
                    print("HASIL OCR:", ocr_text[:300])
                except Exception as e:
                    print("OCR ERROR:", e)
        # Kirim ke Ollama jika ocr_text ada
        hasil_llm = "Tidak ada hasil OCR."
        if ocr_text:
            prompt = f"Ambil data tabel dari text ini:\n{ocr_text}\nJawab pakai format tabel untuk Excel."
            payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
            try:
                resp = requests.post(OLLAMA_API_URL, json=payload, timeout=120)
                hasil_llm = resp.json().get("response", "Tidak ada respon dari LLM.")
                print("HASIL OLLAMA:", hasil_llm[:300])
            except Exception as e:
                hasil_llm = f"ERROR OLLAMA: {e}"
        return jsonify({"ok": True, "hasil_llm": hasil_llm}), 200

    # Fallback jika request bukan multipart
    return jsonify({"ok": False, "msg": "Request not multipart"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
