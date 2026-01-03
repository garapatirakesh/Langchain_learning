from litellm import video_generation, video_status, video_content
import os
import time

os.environ["OPENAI_API_KEY"] = "XXX"

# Generate video
response = video_generation(
    model="openai/sora-2",
    prompt="A cat playing with a ball of yarn in a sunny garden",
    seconds="8",
    size="720x1280"
)

print(f"Video ID: {response.id}")
print(f"Initial Status: {response.status}")

# Check status until video is ready
while True:
    status_response = video_status(
        video_id=response.id,
        custom_llm_provider="openai"
    )
    
    print(f"Current Status: {status_response.status}")
    
    if status_response.status == "completed":
        break
    elif status_response.status == "failed":
        print("Video generation failed")
        break
    
    time.sleep(10)  # Wait 10 seconds before checking again

# Download video content when ready
video_bytes = video_content(
    video_id=response.id,
    custom_llm_provider="openai"
)

# Save to file
with open("generated_video.mp4", "wb") as f:
    f.write(video_bytes)