<p align="center">
  <img src="https://raw.githubusercontent.com/archanakalburgi/archanakalburgi/main/assets/nyc-skyline-sunset.jpeg" alt="Lower Manhattan skyline at sunset" width="100%">
</p>

# Hi there ! 👋

Hello 👋, I'm Archana Kalburgi, and currently from the New York – New Jersey area, USA.

I am professionally a data engineer / software engineer. You can find me on
<a href="https://www.linkedin.com/in/archana-kalburgi/"><img src="https://img.shields.io/badge/LinkedIn-9caf88?style=flat-square&logo=linkedin&logoColor=2e3a29" alt="LinkedIn" height="20"></a>
or
<a href="https://x.com/archanakalburgi"><img src="https://img.shields.io/badge/-9caf88?style=flat-square&logo=x&logoColor=2e3a29" alt="X" height="20"></a>.

Beyond my day job, I work on ideas of my own. These repositories bring them to life.

## ✍️ Blog & Writing

Apart from coding, I also maintain a blog — you can find my articles at [archanakalburgi.github.io](https://archanakalburgi.github.io), where I write up what I build and what I measure.

A sample of my recent articles:

<!-- POSTS:START -->
- [Evaluating metadata classification for a retrieval pipeline](https://archanakalburgi.github.io/2026/10/10/evaluating-metadata-classification.html)
- [Evaluating document chunking for retrieval pipeline](https://archanakalburgi.github.io/2026/06/26/evaluating-document-chunking.html)
- [Semantic File Search with LangChain and Chroma](https://archanakalburgi.github.io/2025/05/01/semantic-file-search.html)
<!-- POSTS:END -->

<!-- The list above is regenerated daily from the blog's Atom feed by scripts/update_writing.py. Edit that script, not the list. -->

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
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=archanakalburgi&layout=compact&langs_count=8&hide_border=true&disable_animations=true&bg_color=dfe7d8&title_color=46573f&text_color=5c6b55&icon_color=6d8364" alt="Most used languages" width="38%">
  <img src="https://streak-stats.demolab.com/?user=archanakalburgi&hide_border=true&disable_animations=true&background=dfe7d8&stroke=bcc9b2&ring=6d8364&fire=6d8364&currStreakNum=3f4f3a&sideNums=3f4f3a&currStreakLabel=46573f&sideLabels=5c6b55&dates=5c6b55" alt="Contribution streak" width="60%">
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
