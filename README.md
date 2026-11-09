# Robust Speaker Diarization under Noisy and Overlapping Speech

## Overview

Speaker diarization is the task of identifying **who spoke when** in an audio recording. While modern diarization systems perform reasonably well under controlled recording conditions, their performance can degrade when dealing with background noise, overlapping speech, distant speakers, and variations in recording quality.

This project aims to investigate the robustness of speaker diarization systems under such challenging audio conditions.

The central objective is to understand where existing diarization pipelines fail, analyse the factors contributing to these failures, and explore methods that could improve their reliability.

Rather than immediately building a model from scratch, the project begins with reproducing and evaluating an existing pretrained diarization system. Its limitations will then guide further experimentation.

## Research Objectives

- Establish a reproducible speaker diarization baseline.
- Investigate the effects of noise, overlapping speech, and recording conditions on diarization performance.
- Analyse common error patterns, including missed speech, false alarms, and speaker confusion.
- Explore approaches to improve diarization robustness.
- Evaluate proposed changes through controlled experiments and quantitative metrics.

## Initial Approach

The initial phase will use the pretrained [pyannote.audio](https://github.com/pyannote/pyannote-audio) speaker diarization pipeline as a baseline.

The investigation will broadly follow this process:

1. **Baseline reproduction:** Run an existing pretrained diarization pipeline and establish a consistent evaluation setup.
2. **Performance analysis:** Evaluate predictions against reference speaker annotations.
3. **Failure analysis:** Identify recurring errors across different audio conditions.
4. **Experimentation:** Formulate research hypotheses and test potential improvements.
5. **Evaluation:** Compare experimental results against the baseline using consistent metrics.

## Evaluation

The primary evaluation metric will be **Diarization Error Rate (DER)**, which accounts for missed speech, false alarm speech, and speaker confusion.

Additional metrics and runtime measurements may be considered depending on the experiments.

Evaluation will use annotated datasets such as the [AMI Meeting Corpus](https://groups.inf.ed.ac.uk/ami/corpus/) and [VoxConverse](https://github.com/joonson/voxconverse), subject to their access conditions and suitability for the experiments.