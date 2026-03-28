# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:18:40 2024

@author: 9387758
"""

from summarizer import Summarizer
model = Summarizer()
text = "The history of Graphics Processing Units (GPUs) dates back to the early 1980s when companies like IBM and Texas Instruments developed specialized graphics accelerators for rendering images and improving overall graphical performance. However, it was not until the late 1990s and early 2000s that GPUs gained prominence with the advent of 3D gaming and multimedia applications. NVIDIA's GeForce 256, released in 1999, is often considered the first GPU, as it integrated both 2D and 3D acceleration on a single chip. ATI (later acquired by AMD) also played a significant role in the development of GPUs during this period. The parallel architecture of GPUs, with thousands of cores, allows them to handle multiple computations simultaneously, making them well-suited for tasks that require massive parallelism. Today, GPUs have evolved far beyond their original graphics-centric purpose, now widely used for parallel processing tasks in various fields, such as scientific simulations, artificial intelligence, and machine learning.  Industries like finance, healthcare, and automotive engineering leverage GPUs for complex data analysis, medical imaging, and autonomous vehicle development, showcasing their versatility beyond traditional graphical applications. With advancements in technology, modern GPUs continue to push the boundaries of computational power, enabling breakthroughs in diverse fields through parallel computing. GPUs also remain integral to the gaming industry, providing immersive and realistic graphics for video games where high-performance GPUs enhance visual experiences and support demanding game graphics. As technology progresses, GPUs are expected to play an even more critical role in shaping the future of computing."
# Specifying the number of sentences in the summary
summary = model(text, num_sentences=4) 
print(summary)