<p align="center">
  <img src="https://raw.githubusercontent.com/archanakalburgi/archanakalburgi/main/assets/nyc-skyline.jpeg" alt="Lower Manhattan skyline at sunset" width="100%">
</p>

# Hi there ! 👋

Hello 👋, I'm Archana Kalburgi, and currently from the New York – New Jersey area, USA.

I am professionally a data engineer / software engineer. You can find me on
<a href="https://www.linkedin.com/in/archana-kalburgi/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" height="20"></a>
or
<a href="https://x.com/archanakalburgi"><img src="https://img.shields.io/badge/-1a1a1a?style=flat-square&logo=x&logoColor=white" alt="X" height="20"></a>.

Outside of work, I enjoy building small tools of my own — mostly around search, retrieval and data. The repositories here are those side projects.

## ✍️ Blog & Writing

Apart from coding, I also maintain a blog — you can find my articles at [archanakalburgi.github.io](https://archanakalburgi.github.io), where I write up what I build and what I measure.

A sample of my recent articles:

<!-- POSTS:START -->
- [Evaluating metadata classification for a retrieval pipeline](https://archanakalburgi.github.io/2026/10/10/evaluating-metadata-classification.html)
- [Evaluating document chunking for retrieval pipeline](https://archanakalburgi.github.io/2026/06/26/evaluating-document-chunking.html)
- [Semantic File Search with LangChain and Chroma](https://archanakalburgi.github.io/2025/05/01/semantic-file-search.html)
<!-- POSTS:END -->

<sub>↻ this list updates itself from the blog feed — see [`scripts/update_writing.py`](scripts/update_writing.py)</sub>

## 🔎 FindFiles

> Point it at a folder of PDFs and ask what you have — and what you're missing.

Your documents are searchable by filename, not by meaning, and a download called `3yik1cp8js65.pdf` gives you nothing to type. Worse, the real question usually isn't *find this file*. It's *for this task, which of the required documents do I already have, and which am I missing?* Full-text search can tell you what's present; it can't tell you what's absent.

FindFiles indexes a folder of PDFs (OCR fallback for scans), then answers both. Everything runs on-device — local embeddings, local classification through Ollama — so tax forms and medical records never leave the machine.

```
What would you like to do?

  1  Search for files    semantic similarity search
  2  Complete a task     checklist + gap detection
  3  Add a file          index a newly saved file
```

`python` · `chroma` · `sentence-transformers` · `llama3.2 / ollama` · `tesseract`

**[→ github.com/archanakalburgi/findfiles](https://github.com/archanakalburgi/findfiles)**

## 🖼️ Image Search with CLIP

> Describe a picture in plain language, get the picture back.

Semantic matching between text and images — embed a folder of images once, then retrieve them by description instead of by filename. Wrapped in a small Flask app.

`python` · `clip` · `flask`

**[→ github.com/archanakalburgi/Image_Search_OpenAI_Clip](https://github.com/archanakalburgi/Image_Search_OpenAI_Clip)**

## 📈 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=archanakalburgi&layout=compact&langs_count=8&hide_border=true&disable_animations=true&bg_color=0b1020&title_color=5eead4&text_color=97a6cc&icon_color=5eead4" alt="Most used languages" height="160">
  <img src="https://streak-stats.demolab.com/?user=archanakalburgi&hide_border=true&disable_animations=true&background=0b1020&stroke=1b2448&ring=5eead4&fire=5eead4&currStreakNum=eef2ff&sideNums=eef2ff&currStreakLabel=5eead4&sideLabels=97a6cc&dates=97a6cc" alt="Contribution streak" height="160">
</p>

## 🧰 More

<details>
<summary><b>The rest of the stack</b></summary>

<br>

- **Pipelines** — Apache Beam / Dataflow, Airflow, PySpark, dbt
- **Stores** — BigQuery, Chroma
- **Queues** — Amazon SQS
- **ML** — sentence-transformers, scikit-learn, Ollama / local LLMs

</details>

<details>
<summary><b>Earlier work</b></summary>

<br>

- [real_time_data_streaming](https://github.com/archanakalburgi/real_time_data_streaming) — data from collection to operationalization, in real time
- [amazon_sqs_processing](https://github.com/archanakalburgi/amazon_sqs_processing) — read, transform and load messages off a queue
- [CLI_Ticket_Viewer](https://github.com/archanakalburgi/CLI_Ticket_Viewer) — Zendesk tickets in the terminal
- [Machine-learning-and-deep-learning-projects](https://github.com/archanakalburgi/Machine-learning-and-deep-learning-projects) — coursework-era notebooks

</details>
