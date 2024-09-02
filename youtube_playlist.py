import os
import google.auth
from googleapiclient.discovery import build
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
API_KEY = os.getenv('YOUTUBE_API_KEY')
PLAYLIST_ID = 'PLMFPOLE2cW1yu-FfYiGElIrDqQfKmZGLM'

def get_video_titles(youtube, playlist_id):
    video_titles = []
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50
    )

    while request:
        response = request.execute()
        for item in response['items']:
            title = item['snippet']['title']
            video_titles.append(title)
        
        request = youtube.playlistItems().list_next(request, response)
    
    return video_titles

def generate_completion_with_gemini(prompt):
    try:
        response = genai.generate_text(
            model="models/text-bison-001",
            prompt=prompt,
            temperature=0.7,
            max_output_tokens=500
        )
        return response.result
    except Exception as e:
        print(f"Erro ao gerar a conclusão para o prompt '{prompt}': {e}")
        return f"Erro ao gerar a conclusão para o prompt: {prompt}"

def generate_report_with_completions(titles):
    reports = []
    for title in titles:
        prompt = (f"Key concepts, As a DevOps manager, project manager, and repository manager, "
                  f"analyze the following video title and provide insights from each of these perspectives: '{title}'")
        
        completion = generate_completion_with_gemini(prompt)
        reports.append(completion)
    
    return reports

def save_reports_to_txt(reports):
    with open("devops_project_repo_reports.txt", "w", encoding="utf-8") as f:
        for i, report in enumerate(reports):
            f.write(f"Report {i+1}:\n")
            f.write(report)
            f.write("\n\n")

def main():
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    titles = get_video_titles(youtube, PLAYLIST_ID)
    
    if titles:
        reports = generate_report_with_completions(titles)
        save_reports_to_txt(reports)
        print(f"Reports successfully generated for {len(titles)} videos.")
    else:
        print("No titles found.")

if __name__ == '__main__':
    main()
