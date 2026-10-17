# Archana Kalburgi

I build retrieval systems that run on your own machine — and I measure them instead of trusting them. Data engineering and ML systems by trade; local-first document intelligence the rest of the time.

**Now · October 2026**

- 🔨 Building **FindFiles** — ask a folder of PDFs what you have and what you're still missing
- 📏 Evaluating that pipeline one stage at a time: chunking, then metadata classification, retrieval ranking next
- ✍️ Writing up each evaluation, numbers and all, at [archanakalburgi.github.io](https://archanakalburgi.github.io)

---

### 🔎 [FindFiles](https://github.com/archanakalburgi/findfiles)

Your documents are searchable by filename, not by meaning — and a download called `3yik1cp8js65.pdf` gives you nothing to type. Worse, the real question usually isn't *find this file*. It's *for this task, which of the required documents do I already have, and which am I missing?* Full-text search can tell you what's present; it can't tell you what's absent.

FindFiles indexes a folder of PDFs (OCR fallback for scans), then answers both questions. Everything runs on-device — local embeddings, local classification through Ollama — so tax forms and medical records never leave the machine.

```
What would you like to do?

  1  Search for files    semantic similarity search
  2  Complete a task     checklist + gap detection
  3  Add a file          index a newly saved file
```

`python` · `chroma` · `sentence-transformers` · `llama3.2 / ollama` · `tesseract`

### 🖼️ [Image Search with CLIP](https://github.com/archanakalburgi/Image_Search_OpenAI_Clip)

Describe a picture in plain language, get the picture back. Semantic matching between text and images, wrapped in a small Flask app.

`python` · `clip` · `flask`

---

### Writing

Evaluations rather than tutorials — each one measured against a labeled set of 53 real government forms, on-device.

<!-- POSTS:START -->
- **[Evaluating metadata classification for a retrieval pipeline](https://archanakalburgi.github.io/2026/10/10/evaluating-metadata-classification.html)** — Retrieval was tuned, so I measured the next stage: how reliably a local model labels each document. Across input windows, more than half the document types stayed wrong, and the chunking… <br><sub>10 Oct 2026</sub>
- **[Evaluating document chunking for retrieval pipeline](https://archanakalburgi.github.io/2026/06/26/evaluating-document-chunking.html)** — How I evaluated the chunking layer of FindFiles by sweeping chunk size, overlap, and splitting strategy against a labeled set of 53 real government forms, on-device. <br><sub>26 Jun 2026</sub>
- **[Semantic File Search with LangChain and Chroma](https://archanakalburgi.github.io/2025/05/01/semantic-file-search.html)** — A walkthrough of a semantic file search assistant that indexes local documents and enables intelligent retrieval using vector embeddings. <br><sub>1 May 2025</sub>
<!-- POSTS:END -->

---

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

---

Reach me on [LinkedIn](https://www.linkedin.com/in/archana-kalburgi/) · read more at [archanakalburgi.github.io](https://archanakalburgi.github.io)
