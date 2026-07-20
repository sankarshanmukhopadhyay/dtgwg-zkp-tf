---
layout: default
title: "Observable event analysis"
parent: "Privacy Engineering"
grand_parent: "Implementation Guide"
nav_order: 3
has_toc: true
---
# Observable event analysis

The presentation event remains observable even when the proof transcript is zero knowledge. Deployments analyse who can observe that a proof was requested, generated, mediated, retried, rejected or stepped up.

The analysis records event type, observer, timestamp granularity, network and device metadata, retention, correlation scope, legitimate operational purpose, mitigation and residual harm. It includes the behavioural signal created by repeated human-presence challenges or intent-drift step-ups.
