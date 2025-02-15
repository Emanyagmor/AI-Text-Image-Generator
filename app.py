from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")
    mode = data.get("mode", "text")
    
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    if mode == "text":
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return jsonify({"response": response["choices"][0]["message"]["content"]})
    
    elif mode == "image":
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return jsonify({"image_url": response["data"][0]["url"]})
    
    else:
        return jsonify({"error": "Invalid mode. Use 'text' or 'image'"}), 400

if __name__ == "__main__":
    app.run(debug=True)
