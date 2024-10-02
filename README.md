## Toward Symptom Assessment Guided Symptom Investigation and Disease Diagnosis

The repository contains code and dataset for research article titled 'Toward Symptom Assessment Guided Symptom Investigation and Disease Diagnosis' published at IEEE Transactions on Artificial Intelligence. 

### Abstract
Automatic disease diagnosis has gained immense popularity and demand over the past few years, and it is emerging as an effective diagnostic assistant to doctors. Diagnosis assistants assist clinicians in conducting a thorough symptom investigation and identifying possible diseases. Doctors correctly diagnose patients by observing only a few symptoms in most cases, even though the diagnosed disease has numerous symptoms. Also, some common symptoms, such as fever and headache, usually emerge due to other symptoms, which do not play a major role in identifying suffering diseases. In this work, we investigate the role of symptom importance in disease diagnosis through several feature engineering techniques and propose a novel symptom assessment guided symptom investigation and disease diagnosis (SA-SIDD) assistant using hierarchical reinforcement learning (HRL). The proposed SA-SIDD assistant first collects an adequate set of symptoms/sign information through conversing with users and then diagnoses a disease based on the extracted symptoms. We incorporated a symptom assessment module with the diagnosis framework that evaluates the relevance of current inspected symptom at each turn and reinforces the assistant to investigate distinctive and context-aligned symptoms using an assessment critic. The proposed methodology outperforms the state-of-the-art method, HRL, on two publicly available datasets, which firmly establishes the crucial role of symptom importance in disease diagnosis and the need for the proposed symptom assessment incorporated disease diagnosis framework. Furthermore, we have also conducted a human evaluation, revealing that the diagnosis method greatly enhances end-user satisfaction because of context-aligned relevant and minimal symptom investigation.

![Working](https://github.com/NLP-RL/SA-SIDD/blob/main/SA-SIDD.jpg)

### Full Paper: https://ieeexplore.ieee.org/document/10017134


### Citation Information 
If you find this code useful in your research, please consider citing:
~~~~

@article{tiwari2023toward,
  title={Toward Symptom Assessment Guided Symptom Investigation and Disease Diagnosis},
  author={Tiwari, Abhisek and Raj, Rishav and Saha, Sriparna and Bhattacharyya, Pushpak and Tiwari, Sarbajeet and Dhar, Minakshi},
  journal={IEEE Transactions on Artificial Intelligence},
  volume={4},
  number={6},
  pages={1752--1766},
  year={2023},
  publisher={IEEE}
}
Please contact us @ abhisektiwari2014@gmail.com for any questions, suggestions, or remarks.
