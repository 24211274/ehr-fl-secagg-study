# Evidence Companion — current result traceability supplement

Revision 1.14 supplies newly reconstructed per-seed worst-client and scenario-error records. The derivation uses preserved scores, source labels and frozen validation calibration records; it does not recover the historical missing files or repeat training. All 24 formatted Table 4.8 fields and all six Table 4.10 FPR fields matched. Independent calculations checked all 60 worst-client records and all 44,220 scenario records. Scientific table values and figures are unchanged.

- [Result_Traceability_Evidence.zip](Result_Traceability_Evidence.zip) — SHA-256 `32e36e7c098628904fcb25ea48f092913eebd7948715e092937e88bc09124db5`. Includes portable derivation code, preserved inputs, full numerical records, original-member hashes, execution receipt and independent checks.
- [worst_client_by_seed_reconstructed.csv](worst_client_by_seed_reconstructed.csv)
- [scenario_error_by_seed_reconstructed.csv](scenario_error_by_seed_reconstructed.csv)
- [Data provenance and ethics requirements](Data_Provenance_and_Ethics_Requirements_AR.md)

The data-generation provenance, source-label validity, use/redistribution rights and institutional ethics status remain unverified to the extent described in the thesis. Numerical reconciliation does not resolve these matters. The prior annotated revision is retained in Evidence_Companion_Files.zip.

The historical record below is preserved verbatim. Earlier statements that trace files were not located describe the audit state before this reconstruction and are not claims about the current supplementary outputs.

---

# Evidence Companion

This companion preserves historical execution records and original passages relocated or condensed in revision 1.13. It is not a new experiment or a claim of independent certification. Current scientific findings are in the thesis; these archived passages retain their original dates, labels and version boundaries.

## Original evidence packages

- [ME06_Evidence.zip](ME06_Evidence.zip) — SHA-256 `ed395d9fad8dd017b6ef726bfd76091ba8a63101e6d0b97183ab229d0427313c`
- [Security_Validation_Evidence.zip](Security_Validation_Evidence.zip) — SHA-256 `91758a2f62315c25baf5f358b3ea0aa9fdee4120c93fb7c455778adbb27daf2f`
- [SV05_Repair_Evidence.zip](SV05_Repair_Evidence.zip) — SHA-256 `df0f9e7ad730f0be80a8454d4d4c0eb24eb50edbc7822e57a9fa9dbaecf8161d`
- [Literature_Refresh_ME04_ME05_20261011.zip](Literature_Refresh_ME04_ME05_20261011.zip) — SHA-256 `3f5d4365e084d99c69d8fa0ff94d8a40b3b496cf26ee2c27eebce438b84cf1a8`

## Provenance of this editorial record

Source revision: v1.12 clean reading copy. SHA-256 `6d6e89844a5e8bd989fe01cd036af7818aa54837725651ea067eee232c65c65f`. The prior annotated copy and comments are preserved in Evidence_Companion_Files.zip. Paragraph and table IDs below refer to that source revision, not current page numbers.

## Exact original passages and retention map

### P612 — MOVE_TO_COMPANION

**Source section:** REFERENCES

**Reason:** نقل فقرة Capparelli السياقية إلى السجل المرافق يجعل هذا المرجع غير مستشهد به في الدراسة؛ تحفظ بياناته مع الفقرة المنقولة.

**Retained information:** ['Evidence Companion / P290 and P612']

**Original wording (historical):**

Capparelli, F., de Ligio, M. R., & Finocchiaro, G. (2026). Adaptive access governance in healthcare. Studies in Health Technology and Informatics. https://doi.org/10.3233/SHTI260582

### P32 — REWRITE

**Source section:** Front matter

**Reason:** تقصير الملخص حول السؤال والتصميم والنتائج والحدود، وإزالة لغة إدارة التدقيق ورمز SV-05 مع إبقاء الفشل والإصلاح المنفصل وحدّ البيانات الوصفية.

**Retained information:** ['P32', 'P362', 'P366', 'Results §4.10–4.11', 'Evidence_Companion / Replay and security chronology']

**Original wording (historical):**

Federated learning (FL) applied to electronic health record (EHR) access logs can support anomaly detection without requiring the centralisation of raw log data. However, sharing individual client model updates with a central server raises privacy concerns. This study evaluates the role of secure aggregation in limiting direct server inspection of individual client updates, alongside observed differences in detection performance and training-workflow cost. A Flower-based architecture was implemented in which simulated clients trained a compact long short-term memory (LSTM) autoencoder locally. Three configurations were compared: pooled centralised training, standard Federated Averaging (FedAvg), and a locally modified Secure Aggregation Plus (SecAgg+) path. A fixed synthetic benchmark was evaluated under Reference and controlled Non-IID client-sampling conditions across five seeds, using routine-validation calibration and two separate test sets from the same synthetic source. On the primary test, the mean paired average-precision (AP) difference between SecAgg+ and FedAvg was +0.0047 under Reference sampling and +0.0001 under Non-IID sampling; equivalence was not established. The SecAgg+ workflow increased mean fit-path time by 132.8% and 128.6%, respectively, and application-message content by approximately 49.9%, while federation did not consistently outperform pooled training. On the secondary test, SecAgg+ false-positive rates reached 98.58% and 96.40%, indicating poor handling of unusual legitimate activity. These findings show that SecAgg+ can limit direct inspection of individual updates, but with substantial training-workflow overhead and no clear utility gain in this benchmark. A same-host replay in a fresh environment reproduced the compared predictive results exactly, with a disclosed scaler-metadata compatibility exception. The bounded security audit found one rejection failure and a metadata boundary. A subsequent patch and targeted retest resolved SV-05; the metadata boundary remains. Protection claims assume trusted hosts and honest participants, and deployment conclusions remain constrained by the simulated data source.

**Revised wording before appendix renumbering:**

Federated learning (FL) applied to electronic health record (EHR) access logs can support anomaly detection without centralising raw log data, but individual client model updates raise privacy concerns. This study evaluates secure aggregation for limiting direct server inspection of these updates and measures the associated differences in detection performance and training-workflow cost. A Flower-based architecture used simulated clients to train a compact long short-term memory (LSTM) autoencoder. Three configurations were compared: pooled centralised training, standard Federated Averaging (FedAvg), and a locally modified Secure Aggregation Plus (SecAgg+) path. A fixed synthetic benchmark was evaluated under Reference and controlled Non-IID sampling across five seeds, using routine-validation calibration and two test sets from the same synthetic source. On the primary test, the mean paired average-precision (AP) difference between SecAgg+ and FedAvg was +0.0047 under Reference sampling and +0.0001 under Non-IID sampling; equivalence was not established. SecAgg+ increased mean fit-path time by 132.8% and 128.6%, respectively, and application-message content by approximately 49.9%, while federation did not consistently outperform pooled training. On the secondary test, SecAgg+ false-positive rates reached 98.58% and 96.40%, indicating poor handling of unusual legitimate activity. The findings show that SecAgg+ can limit direct inspection of individual updates under trusted-host and honest-participant assumptions, with substantial workflow overhead and no clear utility gain in this benchmark. A fresh-environment replay on the same host reproduced the compared predictive results exactly, subject to a disclosed scaler-metadata compatibility exception. Later bounded implementation checks identified a rejection failure that was resolved by a separately versioned patch and targeted retest; a diagnostic-metadata boundary remained. These findings remain constrained by the simulated data source.

### P228 — DELETE_REDUNDANT

**Source section:** 1.2 Problem statement

**Reason:** تكرار حدود القياس والتصميم داخل مشكلة البحث؛ تحدد الفقرة السابقة المقارنة بالفعل، وتُشرح الإجراءات والحدود في المنهجية.

**Retained information:** ['P242: fixed simulated benchmark', 'P355 وP359: message/aggregation checks', 'P361: privacy leakage not quantified', 'P387: no prespecified acceptable cost']

**Original wording (historical):**

The study examines this trade-off on a fixed synthetic benchmark. Implementation checks examine the messages exchanged during aggregation and whether the aggregate matches the expected numerical result within the specified tolerance. These checks do not quantify privacy leakage. No maximum acceptable execution or communication cost was specified before the experiments. I therefore report the measured overhead without declaring it acceptable for deployment.

### P233 — DELETE_REDUNDANT

**Source section:** 1.3 Research questions

**Reason:** تكرر تعريف RQ1 الواضح بالفعل في السؤال نفسه من دون إضافة معيار أو إجراء.

**Retained information:** ['P231: RQ1', 'P377–P378: operational definitions and metrics']

**Original wording (historical):**

For RQ1, detection effectiveness concerns distinguishing sessions labelled as threats from legitimate sessions, including unusual legitimate activity.

### P244 — REWRITE

**Source section:** 1.5 Research scope

**Reason:** حصر فقرة النطاق في حدود الدراسة الفعلية؛ نقل أصل تعديل مولّد الأقنعة وعدم تطوير بروتوكول جديد إلى موضع التنفيذ الذي يفسرهما.

**Retained information:** ['P244', 'P358']

**Original wording (historical):**

SecAgg+ was applied to individual client model updates during aggregation, under the assumptions in Section 3.8. Shared data preparation, researcher-side evaluation and local file storage were not protected by this mechanism. TLS and local-only training were not evaluated. The study did not compare alternative model families or aggregation strategies, or evaluate personalisation, differential privacy or poisoning attacks. No new FL framework or cryptographic protocol was developed. The local modification to the SecAgg+ mask generator was adapted from an existing contribution, as documented in Section 3.8.

**Revised wording before appendix renumbering:**

SecAgg+ covered individual client model updates during aggregation under the assumptions in Section 3.8; shared preprocessing, researcher-side evaluation and local storage remained outside that boundary. TLS, local-only training, alternative model families or aggregation strategies, personalisation, differential privacy and poisoning attacks were not evaluated.

### P246 — REWRITE

**Source section:** 1.6 Contribution and significance

**Reason:** عرض المساهمة كمعرفة تجريبية واضحة بدل افتتاحها بالنفي وتكرار وصف تنفيذ المشروع.

**Retained information:** ['P246']

**Original wording (historical):**

The contribution is an implementation and evaluation of federated EHR access-anomaly detection with SecAgg+, rather than a new detection algorithm. Standard FedAvg and the SecAgg+ configuration are compared using the same model architecture, training schedules and evaluation procedure. This comparison measures the detection and execution-cost differences associated with adding protected aggregation. A pooled centralised reference also allows federated and centralised detection performance to be compared.

**Revised wording before appendix renumbering:**

The study provides a controlled comparison of federated EHR access-anomaly detection with and without SecAgg+, using the same LSTM-autoencoder architecture, training schedules and evaluation procedure. It measures the detection and execution-cost differences associated with protected aggregation and compares federated detection with a pooled centralised reference. The contribution is empirical evaluation of this implementation rather than a new detection algorithm.

### P247 — REWRITE

**Source section:** 1.6 Contribution and significance

**Reason:** إبقاء النتيجة السلبية والعبء المقاس، وحذف الدفاع المتكرر عن عدم افتراض الفائدة التشغيلية؛ نطاق الحماية معرف مباشرة في P244 وP354.

**Retained information:** ['P247', 'P244', 'P354']

**Original wording (historical):**

The results show small observed differences in average precision between the two federated configurations, while the SecAgg+ configuration had higher measured execution time and a larger volume of application-message content. All three configurations struggled to distinguish threats from unusual legitimate activity. The study therefore assesses the cost of adding update protection without assuming that the detector is operationally useful. Its findings remain limited to the tested setting and security assumptions.

**Revised wording before appendix renumbering:**

The two federated configurations showed small observed differences in average precision, while SecAgg+ required more execution time and application-message content. All three configurations struggled to distinguish threats from unusual legitimate activity. These findings identify the measured cost of update protection and a detection limitation in the tested setting.

### P254 — REWRITE

**Source section:** 2.1 EHR access security and audit logs

**Reason:** جعل الفقرة مقارنة بين آليات الوسم والتقييم، وترك الأعداد التفصيلية الموجودة فعلاً في جدول الأدلة بدلاً من سردها مرتين.

**Retained information:** ['P254', 'Table 2.3 / T3 rows 1–2']

**Original wording (historical):**

Boxwala et al. (2011) used 1,291 accesses labelled suspicious or appropriate by privacy officers to train logistic regression and support vector machine models. These training labels did not represent confirmed incident outcomes. Their external evaluation comprised 58 independently investigated inappropriate accesses and assessed sensitivity, but could not independently estimate false-positive rates because all cases were positive. Kim et al. (2011) combined anomaly and signature filtering to select examples for logistic regression training. Thirty mixed samples combined intervention positives with negatives borrowed from the control sample; their independent test comprised 78 inappropriate accesses and was also positive-only. Table 2.3 reports the results and these evidence limits.

**Revised wording before appendix renumbering:**

Boxwala et al. (2011) trained logistic regression and support vector machine models on accesses labelled suspicious or appropriate by privacy officers, rather than confirmed incident outcomes. Kim et al. (2011) combined anomaly and signature filtering to select logistic-regression training examples, using intervention positives with negatives borrowed from the control sample. Their external tests contained only inappropriate accesses, independently investigated for Boxwala et al. and independently identified for Kim et al. These positive-only tests allowed sensitivity assessment but no independent false-positive-rate estimate. Table 2.3 gives the sample sizes, results and evaluation limits.

### P255 — REWRITE

**Source section:** 2.1 EHR access security and audit logs

**Reason:** إبقاء قيد استقلال الأدلة مع تقديم سبب القيد أولاً ودمج الجمل التي تكرر عدد المنشورات والتعميم.

**Retained information:** ['P255']

**Original wording (historical):**

These papers are not independent replications across unrelated hospital populations. Kim et al. (2011) describe their filtering study as MAP2, extending the MAP1 work reported by Boxwala et al. (2011). Menon et al. (2014) identify the Hospital dataset as data collected for Kim et al.’s earlier study. Their different models and evaluations contribute methodological evidence, but the shared institutional data lineage limits how much the number of publications alone supports generalisation.

**Revised wording before appendix renumbering:**

These studies share an institutional data lineage. Kim et al. (2011) describe MAP2 as an extension of the MAP1 work reported by Boxwala et al. (2011), and Menon et al. (2014) identify their Hospital dataset as data collected for Kim et al.’s earlier study. Their different methods contribute evidence, but the publications do not constitute independent replications across unrelated hospital populations.

### P259 — REWRITE

**Source section:** 2.2 AI-based detection of inappropriate EHR access

**Reason:** حصر النص في الاستنتاج المقارن الذي يهم البحث: ارتفاع accuracy لا يكفي مع PPV منخفض؛ إبقاء بقية قيم الدراسة في جدول 2.3.

**Retained information:** ['P259', 'T3R8C2P0']

**Original wording (historical):**

Hurst et al. (2022) applied supervised classifiers to features aggregated from records at a UK hospital. Density-based detection and checks against corresponding records informed the initial labels. The available description does not establish that every labelled case was independently investigated. The study used a 70:30 split, as summarised in Table 2.3. Its supervised approach differs from the present model, which learns to reconstruct routine sessions. With anomalies treated as the positive class, Table 10 reports test accuracy of 0.9896 and positive predictive value (PPV) of 0.4486, and validation accuracy of 0.9908 and PPV of 0.5182. PPV is the proportion of predicted-positive cases labelled positive. These values show why accuracy alone is insufficient to characterise positive predictions; differences in data, labels and units prevent direct comparison with this study’s precision or AP.

**Revised wording before appendix renumbering:**

Hurst et al. (2022) applied supervised classifiers to features aggregated from UK hospital records, with density-based screening and record checks informing the labels. Independent investigation of every labelled case was not established. With anomalies treated as positive, their Table 10 reports test accuracy of 0.9896 and positive predictive value (PPV) of 0.4486. PPV is the proportion of predicted-positive cases labelled positive; its low value despite high accuracy shows why accuracy alone is insufficient. Table 2.3 retains the split and validation results. Differences in data, labels and units prevent direct comparison with the present routine-session reconstruction model’s precision or AP.

### P260 — REWRITE

**Source section:** 2.2 AI-based detection of inappropriate EHR access

**Reason:** إبقاء أثر اشتراك مصدر البيانات على الاستدلال، ونقل معرّف المستودع الخام إلى خريطة توثيق المصادر.

**Retained information:** ['P260', 'Evidence_Companion / Literature source identities']

**Original wording (historical):**

Hurst et al. (2022) and Tabassum et al. (2024) cite the same UK hospital dataset identifier (10.17026/dans-znf-sh4q). Their labelling and modelling procedures differ, so their results should be considered as analyses with a shared data source rather than independent validation at two hospitals. Density-informed labels and outlier-generated pseudo-labels also answer different questions from independently adjudicated misuse.

**Revised wording before appendix renumbering:**

Hurst et al. (2022) and Tabassum et al. (2024) analyse the same UK hospital data source using different labelling and modelling procedures. Their results therefore represent analyses of shared data rather than independent validation at two hospitals. Density-informed labels and outlier-generated pseudo-labels also differ from independently adjudicated misuse.

### P261 — REWRITE

**Source section:** 2.2 AI-based detection of inappropriate EHR access

**Reason:** صياغة نقد المصدر مباشرة وحذف جملة عامة عن ضرورة مقارنة طريقة الوسم، مع الإبقاء على عدم الاتساق العددي وعدم اختيار رقم تعسفاً.

**Retained information:** ['P261', 'T3R9C2P0']

**Original wording (historical):**

Tabassum et al. (2024) used Isolation Forest and Local Outlier Factor to generate labels from hospital electronic patient record (EPR) data before training classifiers. Performance against these labels may reflect agreement with the labelling algorithms rather than detection of independently confirmed threats. Comparisons across studies must therefore account for how labels were obtained. SVM accuracy was 99.21% with IF-derived labels and 98.21% with LOF-derived labels. The article assigns IF-SVM sensitivity inconsistently: 99.75% in the abstract and baseline comparison, versus 98.23% in the results discussion, so this review does not select one value.

**Revised wording before appendix renumbering:**

Tabassum et al. (2024) generated labels with Isolation Forest and Local Outlier Factor before training classifiers on hospital electronic patient record (EPR) data. Performance against these pseudo-labels may reflect agreement with the labelling algorithms rather than detection of independently confirmed threats. SVM accuracy was 99.21% with IF-derived labels and 98.21% with LOF-derived labels. The source reports inconsistent IF-SVM sensitivities: 99.75% in the abstract and baseline comparison, versus 98.23% in the results discussion. Table 2.3 retains both values rather than selecting one.

### P262 — REWRITE

**Source section:** 2.2 AI-based detection of inappropriate EHR access

**Reason:** جمع نقد Senturk في موضع مناقشة النموذج بدلاً من تكراره لاحقاً داخل فقرة تجمع ثلاثة مصادر؛ ترك تبرير اختيار النموذج للفقرة التالية.

**Retained information:** ['P262', 'P263', 'P288 original → Evidence_Companion / Senturk source comparison']

**Original wording (historical):**

Recurrent autoencoders model ordered event sequences and can be trained on routine behaviour without requiring examples of every threat. Martínez Llamas et al. (2025) combined an LSTM autoencoder with Flower and FedAvg for EHR access-anomaly detection. Senturk et al. (2025) compared vector and LSTM autoencoders trained on normal synthetic EHR activity, with validation-derived reconstruction thresholds and Integrated Gradients explanations. In their 200-observation evaluation, the vector model had higher anomaly recall and F1, while the LSTM produced fewer false positives; the raw-log-to-evaluation mapping and temporal or entity separation were insufficiently specified. These studies support considering a sequence-based model, but do not establish that a compact LSTM autoencoder is the best choice for this dataset.

**Revised wording before appendix renumbering:**

Recurrent autoencoders model ordered event sequences and can be trained on routine behaviour without examples of every threat. Martínez Llamas et al. (2025) combined an LSTM autoencoder with Flower and FedAvg for EHR access-anomaly detection. Senturk et al. (2025) compared vector and LSTM autoencoders trained on normal synthetic activity, using validation-derived reconstruction thresholds and Integrated Gradients. In their 200-observation evaluation, the vector model had higher anomaly recall and F1, while the LSTM produced fewer false positives. The raw-log-to-evaluation mapping and temporal or entity separation were insufficiently specified; test-to-behaviour-modelling feedback in Fig. 1 and inconsistencies between explanation text and figures also limit claims of independent validation and explanation faithfulness. The experiment was centralised and did not evaluate federated learning or secure aggregation.

### P263 — REWRITE

**Source section:** 2.2 AI-based detection of inappropriate EHR access

**Reason:** إزالة تكرار جملتين تؤديان وظيفة «يدعم مبدأ إعادة البناء»، مع إبقاء اختلاف الإجراءات وحدّ تفسير الانحراف وعدم اختبار تفوق النموذج.

**Retained information:** ['P263']

**Original wording (historical):**

Earlier methodological work supports the reconstruction approach. Malhotra et al. (2016) trained an LSTM encoder–decoder to reconstruct normal multivariate time series and detected deviations through reconstruction error. This supports the reconstruction principle, rather than the suitability of a particular EHR architecture. Their scoring and threshold procedures differed from the present implementation, and their predictor comparison favoured different models under predictable and unpredictable conditions. Reconstruction deviation does not itself establish unauthorised intent. A compact LSTM autoencoder is therefore a controlled model choice for the present architecture comparison; superiority over simpler or alternative detectors remains untested.

**Revised wording before appendix renumbering:**

Malhotra et al. (2016) trained an LSTM encoder–decoder to reconstruct normal multivariate time series and detected deviations through reconstruction error. Their scoring and threshold procedures differed from the present implementation, and their predictor comparison favoured different models under predictable and unpredictable conditions. This provides methodological support for reconstruction-based anomaly scoring, while reconstruction deviation alone does not establish unauthorised intent. The compact LSTM autoencoder is a controlled model choice for comparing training and aggregation; superiority over simpler or alternative detectors remains untested.

### P265 — REWRITE

**Source section:** 2.3 Federated learning for distributed anomaly detection

**Reason:** حفظ قيد binary classification الوارد في الأصل حتى لا ينفصل الرقم المنقول عن نوع المهمة المقاسة.

**Retained information:** ['P265', 'P221–P222', 'P273']

**Original wording (historical):**

FedAvg combines locally trained model parameters, usually weighted by the number of training examples at each client (McMahan et al., 2017). Clients train on their own data rather than sending raw sessions to the server for training. This does not by itself guarantee better detection or the confidentiality of model updates. Lazzarini et al. (2023) provide relevant federated intrusion-detection methodology outside the EHR setting. In their binary-classification results, centralised accuracy/F1 were 0.9840/0.9772 versus 0.9759/0.9661 for aggregated FL on ToN_IoT, and 0.9840/0.9610 versus 0.9820/0.9554 on CICIDS2017 (Tables 5 and 7). These network-data comparisons preserved class proportions across simulated clients; they do not establish EHR detection performance or generalisation across heterogeneous institutions.

**Revised wording before appendix renumbering:**

FedAvg combines locally trained parameters, usually weighted by the number of training examples at each client (McMahan et al., 2017). Lazzarini et al. (2023) report binary-classification results for network-intrusion detection: centralised accuracy/F1 were 0.9840/0.9772 versus 0.9759/0.9661 for aggregated FL on ToN_IoT, and 0.9840/0.9610 versus 0.9820/0.9554 on CICIDS2017 (Tables 5 and 7). These experiments preserved class proportions across simulated clients. They provide federated methodology outside EHR monitoring, rather than evidence of EHR performance or generalisation across heterogeneous institutions.

### P266 — REWRITE

**Source section:** 2.3 Federated learning for distributed anomaly detection

**Reason:** الإبقاء على الدليل المختلف بين مجموعتي البيانات وعدم افتراض فائدة FedProx، ونقل تفاصيل شرط دراستنا إلى منهجية بنائه بدلاً من تكرارها هنا.

**Retained information:** ['P266', 'P333', 'P331']

**Original wording (historical):**

Heterogeneity can also interact with local optimisation. McMahan et al. (2017) showed that excessive local epochs could cause plateauing or divergence in their Shakespeare experiment, although their MNIST result behaved differently. Li et al. (2020) proposed FedProx, adding a proximal term to limit deviation from the current global model, and evaluated statistical and systems heterogeneity. These findings motivate reporting local training and client distributions together; they do not show that FedProx would improve this EHR task. The present department-based resampling within fixed simulated clients changes the pooled department mix and repeated-session exposure as well as between-client heterogeneity (§3.4). It does not establish robustness across independently administered hospitals.

**Revised wording before appendix renumbering:**

Heterogeneity can interact with local optimisation. McMahan et al. (2017) found plateauing or divergence with excessive local epochs in their Shakespeare experiment, although their MNIST result behaved differently. Li et al. (2020) proposed FedProx, adding a proximal term to limit deviation from the current global model, and evaluated statistical and systems heterogeneity. These findings motivate explicit reporting of local training and client distributions. Section 3.4 distinguishes the present resampling condition from an isolated manipulation of between-client heterogeneity.

### P267 — DELETE_REDUNDANT

**Source section:** 2.3 Federated learning for distributed anomaly detection

**Reason:** تبرير المقارنة المركزية وتفصيل worst-client مقرهما المنهجية، وهما مكرران في P227/P344 وP377؛ تُضاف وظيفة إظهار ضعف أحد المشاركين إلى P377.

**Retained information:** ['P227', 'P344', 'P377 revised']

**Original wording (historical):**

A pooled centralised reference allows the detection performance of the same model architecture to be compared with that of federated training. It is used for comparison, not as a proposed deployment or a guaranteed best result. Client-level results, including those of the client with the lowest average precision, complement the global result because an overall result can hide poor performance for one participant.

### P269 — REWRITE

**Source section:** 2.3 Federated learning for distributed anomaly detection

**Reason:** دمج الشرح المتكرر حول المقارنة مع الاحتفاظ بكل نتيجة رقمية وحدود صلاحيتها.

**Retained information:** ['P269']

**Original wording (historical):**

The model processed non-overlapping windows of 100 events. For the centralised model, the reported reconstruction error was approximately 0.42, with 179 sequences and 4,220 requests flagged; the three-client model’s mean error at round 8 was 0.426. The threshold μ + 3σ was described as arbitrary, while federated thresholds were client-specific and derived from training reconstruction errors. Without anomaly labels, these outputs cannot establish verified precision, recall or false-positive rates. The reported experiment did not include a matched comparison of FedAvg with and without SecAgg+ in terms of detection performance and system cost. The present study makes that comparison using labelled synthetic sessions rather than real hospital logs. Differences in the data, labels and units of analysis prevent a direct claim of numerical superiority between the studies.

**Revised wording before appendix renumbering:**

The model processed non-overlapping windows of 100 events. Centralised reconstruction error was approximately 0.42, with 179 sequences and 4,220 requests flagged; the three-client model’s mean error at round 8 was 0.426. The threshold μ + 3σ was described as arbitrary, while federated thresholds were client-specific and training-derived. Without anomaly labels, these flags cannot establish precision, recall or false-positive rates. The reported experiment did not include a matched FedAvg–SecAgg+ comparison of detection performance and system cost. The present study evaluates that comparison on labelled synthetic sessions; the different data, labels and units preclude a direct numerical-superiority claim.

### P271 — REWRITE

**Source section:** 2.4 Secure aggregation of federated model updates

**Reason:** حصر المراجعة في ما فحصه المصدر فعلاً، وترك عدم قياس تسرب الخصوصية من نموذج EHR الحالي في حدود التقييم الأمني بدلاً من دفاع متكرر في مراجعة الأدبيات.

**Retained information:** ['P271', 'P354', 'P361']

**Original wording (historical):**

Individual client updates may reveal information about local training data, depending on the model and training conditions (Hatamizadeh et al., 2023). In medical image classification, those experiments examined conditions such as batch normalisation, batch size and local training iterations. The authors also found lower reconstruction risk when updates combined larger batches and more local training iterations, and cautioned that simplified settings could exaggerate practical risk. These findings support making the threat assumptions explicit when protecting updates, but they do not establish that patient records can be reconstructed from the updates in the present experiment or quantify how much information those updates might reveal.

**Revised wording before appendix renumbering:**

Individual client updates may reveal local training information depending on the model and training conditions (Hatamizadeh et al., 2023). In medical image classification, those experiments examined batch normalisation, batch size and local training iterations. Reconstruction risk was lower when updates combined larger batches and more local iterations, and the authors cautioned that simplified settings could exaggerate practical risk. These conditions motivate an explicit threat model when protecting updates.

### P272 — REWRITE

**Source section:** 2.4 Secure aggregation of federated model updates

**Reason:** إزالة لغة تسليم المصدر «supplied» وربط الأدبيات باختيار إطار موحد؛ حُفظت افتراضات البرهان ونوع الـbenchmarks وحدّ التنفيذ المستقبلي.

**Retained information:** ['P272']

**Original wording (historical):**

Bonawitz et al. (2017) presented a practical Secure Aggregation protocol. Bell et al. (2020) reduced per-client overhead by replacing complete communication graphs with sparse graphs. Their proofs assume client corruptions fixed before execution and specified dropout bounds; the semi-malicious analysis requires honest public-key collection and commitment, or an external public-key infrastructure. The supplied full IACR version includes numerical parameter analyses and cryptographic component benchmarks; a system implementation remained future work. Li et al. (2022) described Salvia, a SecAgg(+) implementation for Flower, under a semi-honest threat model with encrypted, authenticated client–server links. The Flower 1.22.0 documentation also describes support for SecAgg+ (Flower Labs, n.d.). This allows standard FedAvg and the SecAgg+ configuration to use the same framework, rather than introducing differences between frameworks into the comparison.

**Revised wording before appendix renumbering:**

Bonawitz et al. (2017) presented a practical Secure Aggregation protocol. Bell et al. (2020) reduced per-client overhead by replacing complete communication graphs with sparse graphs. Their proofs assume client corruptions fixed before execution and specified dropout bounds; the semi-malicious analysis requires honest public-key collection and commitment, or an external public-key infrastructure. The full IACR version reports numerical parameter analyses and cryptographic component benchmarks, with system implementation left to future work. Li et al. (2022) described Salvia, a SecAgg(+) implementation for Flower under a semi-honest threat model with encrypted, authenticated client–server links. Flower 1.22.0 also supports SecAgg+ (Flower Labs, n.d.), allowing standard FedAvg and protected aggregation to be compared within the same framework.

### P273 — REWRITE

**Source section:** 2.4 Secure aggregation of federated model updates

**Reason:** إبقاء تعريف حدود التقنية في الأدبيات؛ حذف وصف اختبارات المشروع المكرر والموجود في P355/P359/P361.

**Retained information:** ['P273', 'P355', 'P359', 'P361']

**Original wording (historical):**

Secure Aggregation allows the server to compute an aggregate without directly inspecting each client’s update, provided the protocol’s assumptions hold. It does not replace transport protection such as TLS, nor does it by itself provide differential privacy, endpoint security or resistance to model poisoning. The present study checks the numerical aggregation result and whether exchanged messages contain unmasked individual updates. These checks do not establish resistance to attacks that try to infer information from the aggregate or final model.

**Revised wording before appendix renumbering:**

Secure Aggregation allows the server to compute an aggregate without directly inspecting each client’s update when the protocol’s assumptions hold. It does not replace transport protection such as TLS or by itself provide differential privacy, endpoint security or resistance to model poisoning.

### P274 — REWRITE

**Source section:** 2.4 Secure aggregation of federated model updates

**Reason:** شرح آلية الخطر ونطاق المصدر مباشرة، وحذف تكرار أن الدراسة الحالية لم تقيس membership inference؛ يبقى عدم قياس التسرب في المنهجية.

**Retained information:** ['P274', 'P361']

**Original wording (historical):**

Residual disclosure from the aggregate is a separate question. Ngo et al. (2024), in an arXiv preprint, analyse a passive server that observes aggregate updates and distinguishes between candidate client inputs under stated distributional knowledge. Their analysis and experiments show why secure aggregation alone should not be equated with a complete privacy guarantee. This is a different threat from direct inspection of an individual update and does not quantify membership-inference risk for the present EHR model.

**Revised wording before appendix renumbering:**

Ngo et al. (2024), in an arXiv preprint, analyse residual disclosure from aggregate updates. Their passive server distinguishes between candidate client inputs under stated distributional knowledge. This threat differs from direct inspection of an individual update and shows why secure aggregation alone should not be equated with a complete privacy guarantee.

### P277 — REWRITE

**Source section:** 2.5 Datasets and experimental validity

**Reason:** إزالة الافتتاح الإنشائي وتكرار تسمية benchmark مع إبقاء أبعاد صلاحية البيانات وما يلزم للتحقق منها.

**Retained information:** ['P277']

**Original wording (historical):**

Synthetic-data validity requires more than a plausible schema. Achterberg et al. (2024) distinguish fidelity to real data, usefulness for downstream tasks and privacy in evaluating synthetic longitudinal EHRs. Their study concerns patient trajectories, so its evaluation principles transfer more directly than its numerical results to staff access logs. For the present benchmark, labelled-session discrimination demonstrates performance on the supplied scenarios. It does not establish fidelity to operational workflows, independently validated authorisation decisions or transportability to real hospitals; those claims would require appropriate real-log comparisons and expert review.

**Revised wording before appendix renumbering:**

Achterberg et al. (2024) distinguish fidelity to real data, usefulness for downstream tasks and privacy when evaluating synthetic longitudinal EHRs. Their work concerns patient trajectories, so its evaluation principles transfer more directly than its numerical results to staff access logs. Performance on supplied synthetic scenarios does not establish clinical workflow fidelity, independently validated authorisation decisions or transportability to real hospitals; those questions require appropriate real-log comparisons and expert review.

### P280 — REWRITE

**Source section:** 2.6 Evaluation of detection and system overhead

**Reason:** تحويل الفقرة من إعادة شرح إجراءات قياس المشروع إلى مبرر اختيار أبعاد المقارنة؛ تفصيل الحدود يبقى في قسم المقاييس.

**Retained information:** ['P280', 'P346', 'P382', 'P383', 'P387']

**Original wording (historical):**

Cost comparisons depend on what is measured. In this study, elapsed training and aggregation time includes coordination between clients and the server. Application-message content is distinct from total network traffic, and timing inference on preprocessed inputs excludes data preparation and alert delivery. The comparison between standard FedAvg and the SecAgg+ configuration therefore concerns the implemented workflows, not cryptographic operations alone. Whether the additional cost is acceptable depends on the requirements of the intended deployment.

**Revised wording before appendix renumbering:**

System-cost comparisons require matched measurement boundaries. This study distinguishes training-and-aggregation workflow time, application-message content and prepared-input inference (Section 3.10), rather than treating them as interchangeable estimates of cryptographic overhead or deployment latency.

### P285 — REWRITE

**Source section:** 2.7 Comparison of selected studies

**Reason:** إزالة افتتاح تاريخ تحديث البحث، وتقديم المقارنة العلمية مباشرة؛ بقيت المقادير وطرق المقارنة والحدود.

**Retained information:** ['P285', 'P282', 'Evidence_Companion / Literature search chronology']

**Original wording (historical):**

The targeted literature update on 10 October 2026 identified other direct-domain designs whose absolute scores are not directly comparable with this study’s results. Matos et al. (2026) used 50,000 normal and 500 anomalous synthetic access events, an 80:20 stratified split and a meta-classifier combining autoencoder scores, LightGBM, rules and context. Their Table 2 reports LSTM recall of 0.2610 versus 0.8180 for the meta-classifier, illustrating that sequence modelling alone need not give the strongest detector in a particular benchmark. The supervised component, event labels and metrics differ from routine-only session reconstruction here. Its inference-latency and carbon estimates also measure different endpoints from the present training-workflow time and application-message content. Their §6.2 identifies real-log validation and federated learning/secure multiparty computation as future work.

**Revised wording before appendix renumbering:**

Matos et al. (2026) evaluated an alternative EHR detector on 50,000 normal and 500 anomalous synthetic access events, using an 80:20 stratified split and a meta-classifier combining autoencoder scores, LightGBM, rules and context. Their Table 2 reports LSTM recall of 0.2610 versus 0.8180 for the meta-classifier, showing that sequence modelling alone need not provide the strongest detector in that benchmark. Its supervised component, event-level labels and metrics differ from routine-only session reconstruction here. Inference-latency and carbon estimates also measure different endpoints from training-workflow time and application-message content. Real-log validation and federated learning/secure multiparty computation remained future work (§6.2).

### P286 — REWRITE

**Source section:** 2.7 Comparison of selected studies

**Reason:** جمع مشكلة المقامات والتقسيم في تسلسل واضح، وإزالة نفي تأكيد صحة بيانات مشروعنا من مصدر لا يدعي ذلك أصلاً.

**Retained information:** ['P286', 'P277', 'P310']

**Original wording (historical):**

Iqbal et al. (2026) evaluated VAE-based detection using synthetic access events and augmentation, reporting precision, recall, F1 and ROC-based results. These event-level results are not a matched comparison with the present session-level AP. Their methods describe an initial 2,000-event dataset, augmentation to 10,500 events and a 70:15:15 split, whereas their results also describe a 2,000-event test; the relationship between these denominators and the separation of related augmented examples require clarification. The source acknowledges that real clinical validation remains necessary. Its results provide an alternative model design, rather than independent evidence that the present benchmark is clinically representative.

**Revised wording before appendix renumbering:**

Iqbal et al. (2026) evaluated VAE-based detection using augmented synthetic access events and reported precision, recall, F1 and ROC-based results. The methods describe an initial 2,000-event dataset, augmentation to 10,500 events and a 70:15:15 split, whereas the results describe a 2,000-event test. The relationship between these denominators and the separation of related augmented examples remain unclear. The source acknowledges the need for real clinical validation. Its event-level evaluation offers an alternative model design but is not a matched comparison with the present session-level AP.

### P288 — REWRITE

**Source section:** 2.7 Comparison of selected studies

**Reason:** فصل الفقرة المركبة: إبقاء Sutradhar في فقرة واحدة، ودمج Tanvir في مقارنة الأعمال الاتحادية P291 وSenturk في P262؛ نقل محددات صفحات المصدر إلى سجل الأدلة.

**Retained information:** ['P288', 'P262', 'P291', 'Evidence_Companion / Sutradhar source locators']

**Original wording (historical):**

Healthcare federated-security work also narrows the novelty claim. Tanvir et al. (2026) combine IoT traffic and EMR payloads in a multimodal federated pipeline and report accuracy, F1 and system-cost endpoints. This differs from staff access-session anomaly detection. Their Table 8 removes differential privacy and secure aggregation together, so it cannot isolate the effect of secure aggregation alone. Sutradhar et al. (2026) propose a Hyperledger Fabric framework combining context-aware and attribute-based access control, audit logging, monitoring tools and Isolation Forest (pp. 2, 7, 10–12). They describe a three-month testbed simulating healthcare conditions, but do not specify the log dataset, sample size, label construction or training/test split (pp. 12, 16). Their reported detection and false-positive endpoints are not consistently defined across the results tables (pp. 15, 17–18), limiting numerical interpretation. Federated learning is proposed as future work, and the reported methods and experiments contain no federated model-update or secure-aggregation evaluation (pp. 18–19). The study informs access-governance design without evaluating the effect of adding SecAgg+ to FedAvg. Senturk et al. (2025) compare normal-only autoencoders with Integrated Gradients on centralised synthetic data, without a federated or secure-aggregation experiment. Its test-to-behaviour-modelling feedback in Fig. 1 and inconsistencies between the explanation text and figures limit claims of independent validation and explanation faithfulness.

**Revised wording before appendix renumbering:**

Sutradhar et al. (2026) propose a Hyperledger Fabric framework combining context-aware and attribute-based access control, audit logging, monitoring tools and Isolation Forest. Their three-month testbed simulated healthcare conditions, but the report does not specify the log dataset, sample size, label construction or training/test split. Detection and false-positive endpoints are inconsistently defined across its results tables, limiting numerical interpretation. Federated learning remains future work; the reported methods and experiments contain no federated model-update or secure-aggregation evaluation. The study therefore informs access governance rather than the effect of adding SecAgg+ to FedAvg.

### P289 — REWRITE

**Source section:** 2.7 Comparison of selected studies

**Reason:** إزالة عبارة عملية الفحص «inspected text» والإبقاء على الغموض المنهجي ذي الصلة بالمقارنة.

**Retained information:** ['P289']

**Original wording (historical):**

Maghrabi et al. (2026) describe a federated anomaly-detection system for health information systems using FedAvg and TLS. Their security description places SMPC in both the current design and future work, while the inspected text does not identify a named experimental dataset, sample size or matched plain-versus-secure aggregation arms. The study is therefore relevant prior federated healthcare-security work, but its reported results do not establish an equivalent controlled comparison on staff-access sessions.

**Revised wording before appendix renumbering:**

Maghrabi et al. (2026) describe a federated anomaly-detection system for health information systems using FedAvg and TLS. The available text places SMPC in both the current design and future work and does not identify a named experimental dataset, sample size or matched plain-versus-secure aggregation arms. It is relevant prior federated healthcare-security work, but its reported results do not establish an equivalent controlled comparison on staff-access sessions.

### P290 — MOVE_TO_COMPANION

**Source section:** 2.7 Comparison of selected studies

**Reason:** فقرة مصدر منفرد تصف أهمية عامة ثم تنفي تجربة لا يقدمها؛ لا تضيف نتيجة أو تصميم مقارنة يحتاجه خط الحجة الرئيسي.

**Retained information:** ['Evidence_Companion / Literature candidate notes / Capparelli et al. (2026)']

**Original wording (historical):**

Capparelli et al. (2026) further show the importance of contextual access governance; their proposed integration and referenced validation do not provide a new FedAvg–SecAgg+ experiment.

### P291 — REWRITE

**Source section:** 2.7 Comparison of selected studies

**Reason:** اختصار جملة المقارنة مع حفظ جميع عوامل صلاحية المقارنة، دون تغيير أو حذف تلخيص أي دراسة.

**Retained information:** ['P291', 'P288 original → Evidence_Companion']

**Original wording (historical):**

Transferable studies also constrain the novelty claim. Munusamy and Jothi (2026) combine blockchain, federated learning and secure third-party computation in an EHR-security preprint. Kamatchi and Uma (2025) evaluate an IoT insider-detection design with grouped component ablations, and Abbasi et al. (2025) evaluate FedAvg on CERT user profiles using simulated privacy mechanisms. Tanvir et al. (2026) and Javed et al. (2025) address broader healthcare privacy, security and efficiency. These studies require comparison by the unit of detection, the implemented protection mechanism, the controlled experimental factors and the definition of system cost. Their reported accuracies are not directly comparable across these different tasks and datasets.

**Revised wording before appendix renumbering:**

Related studies combine different detection tasks and protection mechanisms. Munusamy and Jothi (2026) combine blockchain, federated learning and secure third-party computation in an EHR-security preprint. Kamatchi and Uma (2025) evaluate IoT insider detection with grouped component ablations, while Abbasi et al. (2025) evaluate FedAvg on CERT user profiles using simulated privacy mechanisms. Tanvir et al. (2026) combine IoT traffic and EMR payloads in a multimodal federated pipeline, reporting accuracy, F1 and system costs; their Table 8 removes differential privacy and secure aggregation together and cannot isolate secure aggregation alone. Javed et al. (2025) address broader healthcare privacy, security and efficiency. Comparison requires matched detection units, protection mechanisms, experimental controls and cost definitions; accuracy values across these tasks and datasets are not interchangeable.

### P292 — REWRITE

**Source section:** 2.7 Comparison of selected studies

**Reason:** اختصار التكرار في تقديم الدراسات القابلة للاستفادة منها؛ حفظ نوع التجربة والضبط وحدود عزل أثر المكون والإحالة إلى الجدول.

**Retained information:** ['P292']

**Original wording (historical):**

Shamim et al. (2026) compare two encrypted SDN intrusion-detection implementations under matched detector and cryptographic-parameter settings, while Qazi et al. (2026) report private federated ERP anomaly detection with component ablations and utility/cost evaluation. These are substantive transferable precedents. Their different tasks and interventions require qualification: the former changes the cryptographic stack, and the latter's headline communication reduction compares different round budgets; Qazi et al.’s Table 20 does not isolate secure aggregation alone.

**Revised wording before appendix renumbering:**

Shamim et al. (2026) compare two encrypted SDN intrusion-detection implementations with matched detector and cryptographic parameters. Qazi et al. (2026) evaluate private federated ERP anomaly detection with component ablations and utility/cost measures. These transferable precedents use different interventions: Shamim et al. vary the cryptographic stack; Qazi et al.’s headline communication reduction compares round budgets, and their Table 20 does not isolate secure aggregation alone.

### P299 — REWRITE

**Source section:** 2.8 Research gap

**Reason:** إزالة تاريخ «refresh» وتفاصيل واجهة API والبحث الويب من فقرة الفجوة؛ الحفاظ على عدم اكتمال النصوص وحدّ الجدة، مع إحالة سجل البحث خارج المتن.

**Retained information:** ['P299', 'P298: fixed synthetic benchmark', 'Evidence_Companion / Literature search register']

**Original wording (historical):**

The contribution is bounded empirical evidence from this controlled comparison, rather than a new federated-learning algorithm. The targeted literature refresh of 11 October 2026 identified direct and transferable prior work, including additional healthcare-security designs and unresolved full-article candidates. FeadSeq (Guan et al., 2025) and the regular-versus-secure network-monitoring study (Lytvyn & Nguyen, 2024) remain qualified comparators because their complete articles were not available for examination in this refresh. The search register distinguishes complete public-API retrieval for the executed queries from top-result web discovery. These findings support the stated empirical positioning but do not certify exhaustive coverage, global priority or generalisation beyond the evaluated synthetic benchmark.

**Revised wording before appendix renumbering:**

The contribution is empirical evidence from this controlled comparison rather than a new federated-learning algorithm. Full articles for potentially relevant comparators, including FeadSeq (Guan et al., 2025) and the regular-versus-secure network-monitoring study (Lytvyn & Nguyen, 2024), were unavailable, leaving their experimental comparability unresolved. The literature review therefore supports this positioning without establishing exhaustive coverage or global priority. Search queries, retrieval coverage and candidate decisions are documented in the Evidence Companion.

### P301 — REWRITE

**Source section:** CHAPTER 3: METHODOLOGY

**Reason:** جعل افتتاح المنهجية يشرح وظيفة الفصل؛ نقل مقارنة المقترح السابق بالدراسة المنجزة إلى سجل القرارات.

**Retained information:** ['P301', 'Evidence_Companion / Proposal-to-executed-design changes']

**Original wording (historical):**

This chapter describes the implementation and evaluation of three configurations: pooled centralised training (A), standard Flower FedAvg (B), and Flower FedAvg with SecAgg+ (C). The comparison assessed detection performance and the additional execution cost of SecAgg+. Appendix E documents differences between the P1 proposal and the completed study.

**Revised wording before appendix renumbering:**

This chapter describes the implementation and evaluation of pooled centralised training (A), standard Flower FedAvg (B) and Flower FedAvg with SecAgg+ (C). It specifies the data, model, training controls and measurements used to compare detection performance and the additional workflow cost of SecAgg+.

### P303 — REWRITE

**Source section:** 3.1 Research design

**Reason:** الإبقاء على حقيقة توضيح الأسئلة والهدف الرابع بعد المراجعة عند نقل تاريخ المقترح خارج المتن؛ منع تصوير الصياغة المعدلة كأنها مسجلة مسبقاً.

**Retained information:** ['P303', 'P789 original → Evidence_Companion / P1 question/objective wording', 'P695 proposed Appendix retention by Appendix reviewer']

**Original wording (historical):**

The design combined three training configurations with two sampling conditions and five random seeds, giving 30 trained models. Comparing A with B addressed RQ1; comparing B with C addressed RQ2. The configurations used the same model architecture, feature encoding, data partitions, loss function, learning rate, batch size, calibration procedure and test sets. The centralised epoch and federated round budgets are specified in Section 3.9.

**Revised wording before appendix renumbering:**

The design combined three training configurations with two sampling conditions and five random seeds, giving 30 trained models. Comparing A with B addressed RQ1; comparing B with C addressed RQ2. The configurations used the same model architecture, feature encoding, data partitions, loss function, learning rate, batch size, calibration procedure and test sets. The centralised epoch and federated round budgets are specified in Section 3.9. The wording of the research questions and fourth objective was operationally clarified after review to reflect the comparisons and outcomes actually measured; it is not presented as the wording recorded before execution. The original P1 wording is retained in the Evidence Companion.

### P304 — REWRITE

**Source section:** 3.1 Research design

**Reason:** إزالة تكرار آلية تجميع بيانات A الموجودة في P344، وإبقاء سيطرة الباحث وحدود الاستقلال الفعلية واضحة.

**Retained information:** ['P304', 'P344']

**Original wording (historical):**

All processes and files were managed on one research computer, which was treated as trusted. In B and C, each Flower client application (ClientApp) loaded its assigned sessions and exchanged model updates and aggregation messages with the server rather than raw event records. Configuration A combined the sessions selected by the client sampling schedules for centralised training. The researcher also had access to records and scores during data preparation and evaluation. The separation between clients therefore concerned the training workflow; it did not prevent the researcher from accessing their data or represent independent organisational control.

**Revised wording before appendix renumbering:**

All processes and files were managed on one trusted research computer. In B and C, each Flower client application (ClientApp) loaded its assigned sessions and exchanged model updates and aggregation messages with the server rather than raw event records. The researcher retained access to records and scores during preparation and evaluation. Client separation therefore applied to the training workflow and did not provide independent organisational control.

### P305 — REWRITE

**Source section:** 3.1 Research design

**Reason:** الإبقاء على إحالة الشكل؛ وصف الأقنعة والقياسات غير المحمية مكرر في P355/P361 وفي الشكل نفسه.

**Retained information:** ['P305', 'P355', 'P361', 'Figure 3.1']

**Original wording (historical):**

Figure 3.1 shows the roles of the clients and server on the shared research computer. In configuration C, SecAgg+ masked individual client parameter updates for aggregation. This protection did not cover reported evaluation metrics or the researcher-side calibration of anomaly scores and alert thresholds.

**Revised wording before appendix renumbering:**

Figure 3.1 shows the client and server roles and the boundary of model-update protection on the shared research computer.

### P310 — REWRITE

**Source section:** 3.2 Dataset description

**Reason:** تحديد موضع manifest المنقول إلى السجل المرافق؛ الملحق يلخص منشأ البيانات ولا يحتوي الفهرس الكامل.

**Retained information:** ['P310 revised', 'Evidence_Companion / Dataset provenance']

**Original wording (historical):**

The experiments used the preserved researcher-supplied synthetic EHR access-log benchmark comprising eleven linked CSV tables, identified by the supplied source-file manifest (Appendix D.2). Its derivation from Mudliar’s public Kaggle dataset was not established. Authorship, original executable-generator provenance and redistribution rights for the executed snapshot remain unverified.

**Revised wording before appendix renumbering:**

The experiments used a researcher-supplied synthetic EHR access-log benchmark comprising eleven linked CSV tables, with 181,805 audit events and 17,464 sessions (Table 3.1). The source-file manifest in the Evidence Companion identifies the supplied snapshot; Appendix D.2 summarises its provenance. Its original creator, executable generator, scenario-construction rules, derivation from Mudliar’s public Kaggle dataset and redistribution rights remain unverified. Subsequently supplied custodial configuration and seed records do not independently establish how the snapshot was originally generated. Affected-event lists are supplied annotations rather than independent confirmation of misuse.

### P311 — DELETE_REDUNDANT

**Source section:** 3.2 Dataset description

**Reason:** دُمجت جميع المعلومات العلمية الفريدة في P310 الجديد؛ إبقاء الفقرتين يعيد غياب إثبات الأصل مرتين متتاليتين.

**Retained information:** ['P310 revised (entire scientific content)', 'Table 3.1', 'Evidence_Companion / Dataset provenance']

**Original wording (historical):**

The dataset contained 181,805 audit events and 17,464 sessions, with supporting tables summarised in Table 3.1. The original creator, executable-generator provenance and scenario-construction rules were not established. A custodial configuration and recorded seeds were subsequently supplied (Appendix D.2); these records do not independently establish how the executed snapshot was originally generated. The lists of affected events were annotations supplied with the dataset, not independent confirmation of misuse. 

### P315 — REWRITE

**Source section:** 3.2 Dataset description

**Reason:** فصل إجراء الفحص وتوقيته عن نتيجته: ما فُحص يبقى في المنهجية، ونتائج عدم التداخل وتكرر الكيانات تذهب إلى قسم النتائج.

**Retained information:** ['P315', 'Results §4.2.2 / P411 proposed consolidation', 'Evidence_Companion / Dataset descriptive checks']

**Original wording (historical):**

A descriptive audit after final evaluation found no shared session IDs between partitions and confirmed that their recorded UTC time ranges were ordered and did not overlap. Actor and patient IDs appeared in more than one partition. The original partitioning algorithm was unavailable, so these checks describe the supplied partitions rather than reconstruct how they were created. Physical-device overlap could not be assessed because the event table lacked identifiers for individual devices.

**Revised wording before appendix renumbering:**

After final evaluation, descriptive checks compared session identifiers, recorded UTC ranges and actor/patient overlap across the supplied partitions. The original partitioning algorithm was unavailable, so the checks characterised the retained partition structure rather than reconstructing its creation. Physical-device overlap could not be assessed because the event table lacked individual-device identifiers. The descriptive findings are reported in Section 4.2.2.

### P317 — REWRITE

**Source section:** 3.2 Dataset description

**Reason:** ترك معايير الإدراج والمعالجة كاملة، وإزالة تكرار عدم استعادة قواعد التوليد والتقسيم المثبت في P310/P315.

**Retained information:** ['P317', 'P310', 'P315']

**Original wording (historical):**

Inclusion was defined at the complete-session level. All source-assigned routine training and validation sessions were retained; the fixed tests retained their supplied classes and partitions. Structural or linkage failures caused preparation to stop rather than selectively exclude records. Unknown or missing categorical targets were masked in the loss, without removing their sessions. These rules describe the executed processing; the original dataset-generation and partitioning rules were not recovered.

**Revised wording before appendix renumbering:**

Inclusion was defined at the complete-session level. All source-assigned routine training and validation sessions were retained, and the tests retained their supplied classes and partitions. Structural or linkage failures stopped preparation rather than selectively excluding records. Unknown or missing categorical targets were masked in the loss without removing their sessions.

### P333 — REWRITE

**Source section:** 3.4 Simulated client construction

**Reason:** إبقاء كيفية قياس skew وحدود التصميم في المنهجية، ونقل النتائج الرقمية الوصفية إلى النتائج حتى لا يُمزج الإجراء بالمحصلة.

**Retained information:** ['P333', 'Results / descriptive department-skew findings', 'Tables C.3–C.4']

**Original wording (historical):**

Before resampling, the designated departments accounted for 21.003%, 21.787% and 9.929% of training sessions in C1, C2 and C3, respectively. Mean pairwise Jensen–Shannon divergence (JSD) between client department distributions was 0.003765 bits for the original distributions and 0.330615 bits for the expected Non-IID distributions. In the recorded check covering rounds 1–5, JSD ranged from 0.330714 to 0.334338 bits across the five seeds (Tables C.3–C.4). JSD was calculated using base-2 logarithms. This check assessed department skew, not every round or every form of client heterogeneity. Reference was not assumed to be perfectly IID. Because sampling was with replacement, this condition changed both the pooled training department mix and exposure to individual sessions, with repeated sessions possible within a minibatch. It was therefore not an isolated manipulation of between-client heterogeneity.

**Revised wording before appendix renumbering:**

Department skew was characterised using mean pairwise Jensen–Shannon divergence (JSD) with base-2 logarithms for the original and expected Non-IID distributions and observed draws from rounds 1–5 across the five seeds (Tables C.3–C.4). This check covered selected rounds and department composition, rather than every form of client heterogeneity; Reference was not assumed to be perfectly IID. Sampling with replacement also changed the pooled department mix and exposure to individual sessions, with repeats possible within a minibatch. The condition was therefore not an isolated manipulation of between-client heterogeneity.

### P352 — REWRITE

**Source section:** 3.7 Flower federated-learning workflow

**Reason:** صياغة ميزانية التدريب وقاعدة الاختيار كإجراءات؛ اكتمال التشغيل نتيجة موثقة بالفعل في §4.2.

**Retained information:** ['P352', 'Results §4.2']

**Original wording (historical):**

Each configuration completed its full training budget: 30 centralised epochs for A or 30 federated rounds for B and C. Checkpoint selection used the mean reconstruction loss across all routine-validation sessions, with each session contributing equally. Among epochs or rounds 1–30, the selected checkpoint was the earliest whose validation loss differed from the minimum by no more than 1e-12. An evaluation of the initial model was recorded as iteration 0, which was not eligible for selection. The selected checkpoint was then evaluated again without further optimiser updates.

**Revised wording before appendix renumbering:**

The training budget was 30 centralised epochs for A or 30 federated rounds for B and C. Checkpoint selection used mean reconstruction loss across all routine-validation sessions, with each session weighted equally. Among epochs or rounds 1–30, the selected checkpoint was the earliest whose validation loss differed from the minimum by no more than 1e-12. The initial model was evaluated at iteration 0 and was ineligible for selection. The selected checkpoint was evaluated again without further optimiser updates.

### P358 — REWRITE

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** الإبقاء على ما تغير ولماذا ونسبته وإصدار التنفيذ وحدّ هوية العجلة التاريخية؛ نقل تسلسل العثور على diff وأسماء الأرشيفات إلى ملف الأدلة.

**Retained information:** ['P358', 'T8R1C1P0/T8R8C1P0', 'Evidence_Companion / Build provenance', 'Results §4.11']

**Original wording (historical):**

The original masking helper reduced seeds to 32 bits and used NumPy RandomState. A counter-based HMAC-SHA256 helper was adapted from a fixed contributor commit associated with pull request (PR) #7570 and incorporated into the local Flower build 1.22.0+mai.prg7570.1 (saurabhvmagdum, 2026). Both B and C were revalidated with this build. Appendix C.2 identifies the preserved source files, change manifest, attribution and licence records. The helper-change diff was subsequently located in the supplied PRG validation archive (Appendix D.4), but the historical installed wheel payload was not supplied. The subsequent candidate rebuild and runtime checks are documented separately in Appendix D.8 and Section 4.11. This was a local software modification, not an official Flower release or a new protocol.

**Revised wording before appendix renumbering:**

The local Flower build 1.22.0+mai.prg7570.1 replaced the original helper, which reduced seeds to 32 bits and used NumPy RandomState, with a counter-based HMAC-SHA256 helper adapted from the fixed contributor commit associated with PR #7570 (saurabhvmagdum, 2026). Both B and C were revalidated with this build. This was a contributor backport in a local software version, not an official Flower release or a new protocol. Source, attribution, licence and build records are indexed in the Evidence Companion. The historical installed wheel payload was unavailable; a subsequent candidate rebuild and its runtime checks are distinguished from the historical environment (Section 4.11).

### P359 — REWRITE

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** الإبقاء على إجراءات التحقق السابقة للتجارب وقيمها المرجعية؛ إزالة نفي تكافؤ الكشف وتسرب الخصوصية المكرر في مواضعهما.

**Retained information:** ['P359', 'P361', 'P387', 'Tables C.2/C.5']

**Original wording (historical):**

Before the accepted main experiments, tests with predefined public vectors checked aggregation with equal and unequal client weights, numerical rounding and refusal conditions. Tables C.2 and C.5 report the expected aggregates, measured errors and acceptance limits, including a test using the main-run client counts. Numerical agreement supports those tested calculations, not equivalent detection performance or a measured reduction in privacy leakage.

**Revised wording before appendix renumbering:**

Before the accepted main experiments, predefined public-vector tests checked equal and unequal client weights, numerical rounding and refusal conditions. Tables C.2 and C.5 report the expected aggregates, measured errors and acceptance limits, including a fixture using the main-run client counts.

### P360 — MOVE_TO_COMPANION

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** تفصيل تاريخي عن الفرق بين عدّ callback وفحص المصدر وإثبات التنفيذ البعيد؛ يحتفظ المتن بالتمييز المختصر في P362 وبحدود المضيف في P354.

**Retained information:** ['Evidence_Companion / Historical callback evidence and execution-authenticity limits', 'P362 revised: historical aggregate-call versus later callback observations', 'P354: trusted local host']

**Original wording (historical):**

In the historical records, tests with missing replies or mismatched identifiers recorded no calls to the aggregation function. This alone did not establish that the client data callback had not run; the claim that checks preceded it was based on source-code inspection. Hash and message-format checks verified consistency, not execution authenticity on a remote host. The subsequent suite records local toy-fit and accepted-aggregate callbacks separately, including local work before late-stage rejection (Section 4.11).

### P361 — REWRITE

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** جمع حدود الحماية وعدم وجود قياس لتسرب الخصوصية في موضع واحد واضح، مع إبقاء شرط رفض القيم.

**Retained information:** ['P361', 'P362', 'Evidence_Companion / Security scope']

**Original wording (historical):**

Parameter checks rejected non-finite values and unweighted values whose absolute magnitude exceeded 8. The tests did not cover every numerical boundary or attack. The aggregate, shared model, reported metrics, counts, plaintext preprocessing summaries and researcher-side calibration were outside SecAgg+’s protection of individual updates.

**Revised wording before appendix renumbering:**

Parameter checks rejected non-finite values and unweighted values with absolute magnitude above 8. SecAgg+ protected individual updates; aggregates, shared models, reported metrics, counts, plaintext preprocessing summaries and researcher-side calibration remained outside that protection. Privacy leakage from the EHR model updates, aggregate or final model was not quantified.

### P362 — REWRITE

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** دمج تعريف الاختبارات اللاحقة وحدودها في فقرة منهجية واحدة دون تاريخ يومي أو رمز ME-06، مع إبقاء الفصل الصريح بين العلم الأصلي والتحقق اللاحق.

**Retained information:** ['P362', 'P363–P365 original → Evidence_Companion', 'Results §4.11']

**Original wording (historical):**

Later bounded security validation (11 October 2026). After the historical benchmark and ME-06 replay, seven groups of implementation checks were executed against the retained Flower 1.22.0+mai.prg7570.1 environment. Acceptance contracts and script identities were sealed before these new executions, after the original results were already known. This was a separately dated implementation audit, not retrospective prespecification of the main study.

**Revised wording before appendix renumbering:**

After the main benchmark and computational replay, a separate local suite exercised seven groups of security-related implementation checks in the retained Flower 1.22.0+mai.prg7570.1 environment. Acceptance contracts and script identities were fixed before these executions, after the original benchmark results were known. Public arrays, in-memory participant contexts and single-round toy fits were used instead of EHR training, inference or learned checkpoints. The suite examined helper conformance, numerical aggregation, message fields, cohort/stage/round guards, malformed requests, context freshness and diagnostic exports. It exercised installed Flower ClientApp/SecAgg code and selected project validators through fixtures, rather than the complete benchmark application or a network deployment. Historical refusal evidence counted aggregation calls; the later fixtures recorded local-fit and accepted-aggregate callbacks separately, including local work before late-stage rejection. Detailed fixture paths, controls and retained attempts are documented in the Evidence Companion.

### P363 — MOVE_TO_COMPANION

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** تفاصيل fixture تعيد إعدادات البروتوكول الموجودة في Table 3.5؛ يبقى في P362 الاختصار الذي يحدد طبيعة البيانات العامة والميزانية الصغيرة وعدم تشغيل benchmark.

**Retained information:** ['Evidence_Companion / Security protocol fixtures', 'P362 revised', 'Table 3.5 / T8 rows 2–6']

**Original wording (historical):**

The checks used public arrays, in-memory participant contexts and selected direct calls to project validators. Protocol fixtures used three clients, three shares, threshold two, maximum weight 4096, clipping range 8, quantization range 2^22 and modulus 2^31. All three participants remained required. Tiny public fit budgets and one round per protocol case replaced the benchmark workload; no benchmark training, inference or learned-checkpoint loading was performed.

### P364 — MOVE_TO_COMPANION

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** قائمة رموز الاختبارات سجل تحقق؛ يبقى نطاق المجموعات في P362 ونتائجها في §4.11، وتفصيل كل fixture وعقده في ملف الأدلة.

**Retained information:** ['Evidence_Companion / SV-01–SV-07 fixture and acceptance-contract map', 'P362 revised', 'Results §4.11 / Table 4.16']

**Original wording (historical):**

SV-01 checked the installed helper, wheel contents, public HMAC/decoder vectors and a constructed legacy-fold collision control. SV-02 checked numerical aggregation and range/weight/shape boundaries. SV-03 observed replies at server ingress and exercised named field allowlists. SV-04 exercised cohort, stage and round guards. SV-05 injected selected malformed keys, encrypted shares and routing lists. SV-06 compared freshly generated contexts in memory. SV-07 exercised the measurement observer and failure capsule with public canaries.

### P365 — MOVE_TO_COMPANION

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** تفصيل بدائل harness ونقاط الاستدعاء والمحاولات مناسب لسجل الأدلة؛ لا يحذف من حدود الاستدلال لأن P362 يحتفظ بأن الاختبارات fixtures لمسارات مختارة وليست التطبيق الكامل.

**Retained information:** ['Evidence_Companion / Harness execution paths and substitutions', 'P362 revised', 'Results §4.11']

**Original wording (historical):**

The harness executed installed Flower ClientApp/SecAgg code and the project StrictSecAggPlusWorkflow and named cohort, wire, range and restoration validators. Its toy strategy and client guard were fixtures; the guard mirrored selected project rules with a public-budget exception. The B positive control was a plain Flower reply rather than the complete EHR B application. Export tests substituted only measurement_scope() with a public fixture. These checks therefore cover selected implementation paths rather than the full benchmark application or a network-deployment test. Appendix D.9 records the execution paths, criteria, retained attempts and unexecuted scope.

### P366 — REWRITE

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** شرح تصحيح التنفيذ وطريقة اختباره، ونقل التاريخ وأعداد نجاح الحالات إلى النتائج والسجل؛ إبقاء أن الإصلاح منفصل عن مصدر benchmark وعن المكوّن التشفيري.

**Retained information:** ['P366', 'Results §4.11 / P520–P521', 'Evidence_Companion / SV-05 source revision']

**Original wording (historical):**

SV-05 remediation and retesting (12 October 2026). A separate project copy added collection-request validation before the upstream fit callback. It requires equal ciphertext/source-list lengths and each retained external peer exactly once, while accepting aligned permutations. The original 59-case contract and mutation were retained. Its toy guard invoked the same new project validator. Twelve additional cases exercised the actual project guard with public arrays and configuration-valid acknowledgement fields. These were implementation fixtures, without EHR optimisation, network deployment or changes to the installed cryptographic helper.

**Revised wording before appendix renumbering:**

A subsequent, separately versioned patch added collection-request validation before the upstream fit callback. It required equal ciphertext/source-list lengths and exactly one entry for each retained external peer, while accepting aligned permutations. Retesting reused the original acceptance contract and malformed-request mutation and added public-array cases against the actual project guard. The patch changed a project input-validation guard, not the installed cryptographic helper; the retest did not perform EHR optimisation or network deployment.

### P373 — REWRITE

**Source section:** 3.9 Experimental design and training controls

**Reason:** اختصار تاريخ الإصلاحات إلى ما يؤثر في ثبات المقارنة، ونقل التسلسل والتواريخ غير المعروفة إلى سجل الأدلة.

**Retained information:** ['P373', 'P368/P371: fixed matched inputs', 'Evidence_Companion / Campaign chronology']

**Original wording (historical):**

Preprocessing, model-learning, federated-training, aggregation, full-size execution, timing and inference checks preceded the main runs included in the results. Records of earlier incomplete blocks and code repairs were kept separately. Corrected campaigns reused the fixed inputs, initial model states and sampling draws; earlier outcomes were not chosen because they gave better results. Appendix C.5 records the available chronology and identifies unknown dates.

**Revised wording before appendix renumbering:**

The accepted main runs followed preprocessing, model-learning, aggregation, full-size execution, timing and inference checks. Corrected campaigns reused the fixed inputs, initial model states and sampling draws. Earlier incomplete blocks and code repairs were retained separately; their available chronology and the exclusion of incomplete attempts are documented in the Evidence Companion.

### P377 — REWRITE

**Source section:** 3.10 Evaluation metrics

**Reason:** إضافة مبرر worst-client المنقول من P267 إلى تعريف المقياس نفسه، وحذف تكرار وصف المقياس داخل الجمل.

**Retained information:** ['P377', 'P267 rationale consolidated here']

**Original wording (historical):**

Table 3.7 summarises the evaluation measures. Threat sessions were positive cases, while routine and unusual legitimate sessions were negative cases. Average precision (AP) was the primary detection measure, with AUROC reported as a supporting measure. For global AP and AUROC, scores were transformed using each client’s routine-validation calibration and then pooled across clients. Global metrics based on raw scores were reported as secondary results. Client-level AP and AUROC used raw scores. For each model run and test set, worst-client AP was the minimum of the three client AP values, with the corresponding client identity retained. AP was calculated as average precision rather than trapezoidal area under the precision–recall curve. The original class proportions were preserved in each test set.

**Revised wording before appendix renumbering:**

Table 3.7 summarises the evaluation measures. Threat sessions were positive cases, and routine and unusual legitimate sessions were negative cases. Average precision (AP) was primary, with AUROC as a supporting measure. Global AP and AUROC pooled scores transformed using each client’s routine-validation calibration; raw global scores were secondary results. Client-level AP and AUROC used raw scores. For each model run and test set, worst-client AP was the minimum of the three client AP values, with its client identity retained, so that poor performance for one participant remained visible alongside global metrics. AP was calculated as average precision rather than trapezoidal area under the precision–recall curve. Each test set retained its original class proportions.

### P379 — REWRITE

**Source section:** 3.10 Evaluation metrics

**Reason:** ترك عقد اكتمال التقييم في قسم المقاييس، ونقل التدقيق الحسابي وتفاصيل replay والإفصاح عن المساعدة البرمجية إلى قسم إعادة الإنتاج.

**Retained information:** ['P379', 'P393 revised', 'Results §4.10', 'Evidence_Companion / Replay']

**Original wording (historical):**

Each expected test session was required to have exactly one score, with matching client, partition, scenario and label information. After the original evaluation, a separate implementation developed with programming assistance recalculated metrics from saved scores and calibration records without rerunning inference. That arithmetic audit was followed on 11 October 2026 by a fresh-environment replay of training, validation calibration and complete test inference on the same host (Sections 4.10 and 5.7.5; Appendix D.8). Neither verification was a blinded review by an independent researcher.

**Revised wording before appendix renumbering:**

Each expected test session was required to have exactly one score, with matching client, partition, scenario and label information. Section 3.12 describes the separate post-evaluation metric check and computational replay.

### P385 — REWRITE

**Source section:** 3.11 Statistical analysis

**Reason:** الإبقاء على الوحدة الإحصائية والخلاصات مع استبدال إحالة فهرس ملفات داخلي بإحالة عامة لملف الأدلة.

**Retained information:** ['P385', 'Evidence_Companion / Seed-level results']

**Original wording (historical):**

Results were summarised separately for each configuration, sampling condition and test set. All five seed-level values were retained alongside the mean, sample standard deviation, median and range. Differences were calculated as B−A and C−B within each seed. Sessions, clients and rounds were not treated as independent replicates, and the test sets were analysed separately. Appendix D.6 identifies the detailed result files.

**Revised wording before appendix renumbering:**

Results were summarised separately for each configuration, sampling condition and test set. All five seed-level values were retained alongside the mean, sample standard deviation, median and range. Differences were calculated as B−A and C−B within each seed. Sessions, clients and rounds were not treated as independent replicates, and the test sets were analysed separately. Detailed seed-level results are indexed in the Evidence Companion.

### P386 — REWRITE

**Source section:** 3.11 Statistical analysis

**Reason:** الحفاظ على الإجراء الإحصائي كاملاً وحدود الاستدلال؛ نقل تاريخ استبدال تحليل المقترح إلى سجل التصميم المنفذ.

**Retained information:** ['P386', 'Evidence_Companion / Design changes']

**Original wording (historical):**

Exploratory 95% intervals for the mean paired differences in global and worst-client AP were calculated as mean(d) ± t(0.975, 4) × SD(d)/√5. Here, d denotes the five within-seed differences for one comparison, and SD(d) is their sample standard deviation. The term t(0.975, 4) is the 97.5th percentile of Student’s t distribution with four degrees of freedom. The reporting rule required five finite matched pairs and omitted an interval if the differences had zero variance. These intervals describe training-seed variability on the fixed benchmark, not variation across independent hospitals or clinical populations. Appendix E documents the change from P1’s proposed hierarchical bootstrap.

**Revised wording before appendix renumbering:**

Exploratory 95% intervals for the mean paired differences in global and worst-client AP were calculated as mean(d) ± t(0.975, 4) × SD(d)/√5. Here, d denotes the five within-seed differences for one comparison, and SD(d) is their sample standard deviation. The term t(0.975, 4) is the 97.5th percentile of Student’s t distribution with four degrees of freedom. The reporting rule required five finite matched pairs and omitted an interval if the differences had zero variance. These intervals describe training-seed variability on the fixed benchmark, not variation across independent hospitals or clinical populations.

### P387 — REWRITE

**Source section:** 3.11 Statistical analysis

**Reason:** جمع قيد عدم تحديد تكلفة مقبولة مسبقاً من P228 مع طريقة تفسير النتائج بدلاً من تكراره في مشكلة البحث.

**Retained information:** ['P387', 'P228 cost-criterion fact consolidated here']

**Original wording (historical):**

Other measures were summarised descriptively. For each cost measure, the percentage increase was calculated within each seed as 100 × (C−B)/B when B > 0, then averaged across seeds; B and C denote the corresponding measured costs. The value of 0.02 AP was a practical reference, not a validated non-inferiority margin. The analysis did not include confirmatory p-values or an equivalence test. No operational cost limit was specified, so completion of a run or similar detection scores did not establish that its overhead was acceptable for deployment.

**Revised wording before appendix renumbering:**

Other measures were summarised descriptively. For each cost measure, the percentage increase was calculated within each seed as 100 × (C−B)/B when B > 0, then averaged across seeds; B and C denote the corresponding measured costs. The value of 0.02 AP was a practical reference, not a validated non-inferiority margin. The analysis included neither confirmatory p-values nor an equivalence test. No maximum acceptable execution or communication cost was specified before the experiments, so completion or similar detection scores did not establish deployment acceptability.

### P393 — REWRITE

**Source section:** 3.12 Reproducibility, ethics, and validity

**Reason:** جمع وصف إجراءات إعادة الإنتاج والإفصاح البرمجي في موضع واحد، وحذف التاريخ وفهارس الحزم من متن المنهجية.

**Retained information:** ['P393', 'P379 post-evaluation disclosure moved here', 'Evidence_Companion / Replay chronology']

**Original wording (historical):**

The experiment records linked each configuration, sampling condition and seed to its sampling schedules, trained parameters, calibration records and results. Appendix D distinguishes the historical examiner-companion index and supplementary archives from the completed computational replay. On 11 October 2026, the preserved scientific source and adopted design were executed in a newly created Python 3.12.3 environment on the same Ubuntu 24.04 WSL host. The supplied raw CSV snapshot was used to regenerate preprocessing inputs, five initial model states and ten sampling schedules before fresh training. Historical learned model weights were not used as training inputs.

**Revised wording before appendix renumbering:**

Experiment records linked each configuration, sampling condition and seed to its sampling schedules, trained parameters, calibration and results. After the original evaluation, separate metric-calculation code developed with programming assistance recalculated metrics from saved scores and calibration records without rerunning inference. A subsequent replay rebuilt Python 3.12.3 on the same Ubuntu 24.04 WSL host and used the supplied raw CSV snapshot to regenerate preprocessing inputs, five initial model states and ten sampling schedules before fresh training. Historical learned weights were not used as training inputs. These were local verification exercises, not blinded review by an independent researcher.

### P394 — REWRITE

**Source section:** 3.12 Reproducibility, ethics, and validity

**Reason:** فصل طريقة replay وحدّه عن نتيجة اكتمال 30 تشغيل/60 خلية، مع إبقاء استثناء scaler في المتن وعدم إخفائه داخل السجلات.

**Retained information:** ['P394', 'Results §4.10 / P513–P514', 'Evidence_Companion / Replay diagnostics']

**Original wording (historical):**

The replay completed 30 training runs across A/B/C, two sampling conditions and five prespecified seeds, using the fixed budget of 30 centralised epochs or federated rounds. Selected checkpoints and validation-only calibration records were sealed before evaluation on both test partitions, giving 60 model–test cells. Full-precision comparisons covered initial and selected tensor states, selected rounds, validation scores, calibration, test scores, metrics and paired-seed summaries. A disclosed compatibility step reused the historical scaler JSON representation while retaining the regenerated arrays; Appendix D.8 details the diagnostic difference, preserved raw outputs and execution receipts. This procedure reconstructed a fresh environment on the existing host, rather than the complete historical operating-system image or an independent external host.

**Revised wording before appendix renumbering:**

The replay used the adopted design and fixed budget of 30 centralised epochs or federated rounds. Selected checkpoints and validation-only calibration records were sealed before evaluation on both test partitions. Full-precision comparisons covered initial and selected tensor states, selected rounds, validation scores, calibration, test scores, metrics and paired-seed summaries. A disclosed compatibility view reused the historical scaler JSON representation with regenerated arrays, while raw preprocessing outputs were preserved. This rebuilt a Python environment on the existing host rather than the complete historical operating-system image or an independent external host. Section 4.10 reports the comparison outcomes; the Evidence Companion retains the compatibility diagnostics and execution receipts.

### T6R5C1P0 — REWRITE

**Source section:** 3.3 Data preparation

**Reason:** إزالة نفي شهادة FHIR التي لا يدعيها وصف الحقل؛ يبقى معنى الحقل كما هو.

**Retained information:** ['T6R5C1P0']

**Original wording (historical):**

Resource-category label; no FHIR certification implied

**Revised wording before appendix renumbering:**

Resource-category label

### T8R10C0P0 — REWRITE

**Source section:** 3.8 Secure aggregation of model updates

**Reason:** استبدال عنوان دفاعي بحدّ نطاق مباشر؛ تبقى قائمة TLS/active adversary/DP/certification دون تغيير.

**Retained information:** ['T8R10C0P0', 'T8R10C1P0 unchanged']

**Original wording (historical):**

Excluded claims

**Revised wording before appendix renumbering:**

Outside validation scope

### T11R9C1P0 — REWRITE

**Source section:** 3.12 Reproducibility, ethics, and validity

**Reason:** إزالة اسم JSON الداخلي من جدول بيئة التنفيذ مع حفظ عدد الحزم وأنواع سجلات البناء المطلوبة للإعادة.

**Retained information:** ['T11R9C1P0', 'Evidence_Companion / Runtime and build inventory']

**Original wording (historical):**

Recorded package versions and Flower file digests; the 48-package wheel-hash lock, wheel inventory, helper diff and build recipe are located in Appendix D.4 and artefact_mapping.json

**Revised wording before appendix renumbering:**

Recorded package versions and Flower file digests; the 48-package wheel-hash lock and supporting wheel, helper-diff and build records are indexed in the Evidence Companion

### P398 — REWRITE

**Source section:** 4.1 Introduction

**Reason:** تحديد وظيفة فصل النتائج؛ السجل المرافق يفهرس النتائج التفصيلية ويحفظ سجلات التحقق دون ادعاء إدراج جميع ملفات النتائج داخله.

**Retained information:** ['§4.2–4.11; Evidence Companion']

**Original wording (historical):**

This chapter reports the completed experiments, detection performance and additional system costs associated with SecAgg+. Final-test evaluation followed checkpoint selection and score calibration using routine-validation data. Tables summarise all three configurations; seed-level results and detailed checks are provided in the Examiner Companion.

**Revised wording before appendix renumbering:**

This chapter reports detection performance, system costs and the completed computational and bounded security checks. Final-test evaluation followed checkpoint selection and score calibration using routine-validation data. The Evidence Companion indexes individual-seed results and detailed verification records.

### P404 — REWRITE

**Source section:** 4.2.1 Execution and aggregation evidence

**Reason:** الإبقاء على نتائج التنفيذ الفعلية ونقل جرد البيئة والمحاولات غير الداخلة في المقارنة إلى السجل الخارجي.

**Retained information:** ['§4.2.1, P404 (execution totals)', 'Evidence Companion / Execution inventory and excluded campaigns']

**Original wording (historical):**

The experiments completed 153,600 optimiser steps across A, B and C, and 600 aggregation operations across B and C. Configuration C completed 1,200 protocol stages, with all three clients participating at each stage and no fallback to ordinary FedAvg. Environment inventories were unchanged between the before- and after-run checks. Earlier incomplete campaigns were retained separately and were not included in these totals.

**Revised wording before appendix renumbering:**

The experiments completed 153,600 optimiser steps across A, B and C, and 600 aggregation operations across B and C. Configuration C completed 1,200 protocol stages, with all three clients participating at each stage and no fallback to ordinary FedAvg.

### P405 — REWRITE

**Source section:** 4.2.1 Execution and aggregation evidence

**Reason:** إنهاء الفقرة بما أثبتته الاختبارات نفسها؛ جمع حدود تسرب الخصوصية والهجمات والشهادة الأمنية في مناقشة الصلاحية بدلاً من تكرارها بعد كل قياس.

**Retained information:** ['§4.2.1, P405 (all numerical fixture results)', '§5.3, P537; §5.7.5, revised P580 (privacy and security scope)']

**Original wording (historical):**

An earlier public-vector test using the main-run client counts as aggregation weights recorded an error of 1.474 × 10⁻⁶, below the acceptance limit of 1.056 × 10⁻⁵. Tests with missing replies or mismatched identifiers recorded no calls to the aggregation function (Tables C.2 and C.5). These results support the tested calculations and refusal behaviour; they do not quantify privacy leakage, establish resistance to reconstruction attacks or provide security certification.

**Revised wording before appendix renumbering:**

An earlier public-vector test using the main-run client counts as aggregation weights recorded an error of 1.474 × 10⁻⁶, below the acceptance limit of 1.056 × 10⁻⁵. Tests with missing replies or mismatched identifiers recorded no calls to the aggregation function (Tables C.2 and C.5). These public-fixture results support numerical agreement and the tested refusal behaviour.

### P411 — REWRITE

**Source section:** 4.2.2 Test composition and unit of analysis

**Reason:** دمج نتائج فحص التقسيم المنقولة من P315 مع الفحص الوصفي الحالي؛ الحفاظ على توقيت الفحص بعد الاختبار وحدود الجهاز والهوية وعدم استنتاج أثر سببي.

**Retained information:** ['§4.2.2, revised P411; source P315; §5.7.2, P570–571']

**Original wording (historical):**

A descriptive check after final evaluation found that every threat session and every longitudinal_follow_up session in the held-out test contained exactly five events. Routine sessions in that test contained 6–23 events, with a mean of 9.93. Actor and patient identifiers also occurred in more than one data partition. The effects of these session-length patterns and recurring actors and patients on detection performance were not isolated experimentally.

**Revised wording before appendix renumbering:**

Descriptive checks after final evaluation found no shared session IDs between partitions and ordered, non-overlapping recorded UTC time ranges. Actor and patient IDs occurred in more than one partition. The original partitioning algorithm was unavailable, and physical-device overlap could not be assessed because the event table lacked individual-device identifiers. Every threat session and every longitudinal_follow_up session in the held-out test contained exactly five events. Routine sessions in that test contained 6–23 events, with a mean of 9.93. The effects of session length and recurring actors and patients on detection performance were not isolated experimentally.

### P414 — REWRITE

**Source section:** 4.2.3 Scores, decisions and uncertainty

**Reason:** نقل فهرس الملفات إلى السجل المرافق مع إبقاء وصف التلخيص وعدم اليقين في موضعهما.

**Retained information:** ['4.2.3 Scores, decisions and uncertainty, P414']

**Original wording (historical):**

Values are five-seed means and sample SDs unless stated otherwise. Exploratory 95% intervals for mean AP differences were based on runs paired by seed on the fixed dataset, not on samples from independent hospitals. Appendix D.6 identifies the files containing medians, ranges and individual seed-level results.

**Revised wording before appendix renumbering:**

Values are five-seed means and sample SDs unless stated otherwise. Exploratory 95% intervals for mean AP differences were based on runs paired by seed on the fixed dataset, not on samples from independent hospitals. The Evidence Companion indexes the files containing medians, ranges and individual seed-level results.

### P417 — REWRITE

**Source section:** 4.2.4 Verification of reported metrics

**Reason:** اختصار تاريخ التحقق إلى النتيجة العلمية؛ نقل التاريخ والسجل التفصيلي، ووضع صلاحية الوسوم السريرية والاستقلال البحثي في موضعهما ضمن الصلاحية.

**Retained information:** ['§4.10, P513–515', '§5.7.1, P566; §5.7.5, revised P581', 'Evidence Companion / Metric verification and replay chronology']

**Original wording (historical):**

The earlier arithmetic audit used separate calculation code to reproduce ranking and decision metrics from stored scores, rederive validation calibration and reconcile selection and B/C cost records. A subsequent fresh-environment replay completed all training and final inference on the same host on 11 October 2026. Its full-precision comparison found no differences in the compared predictive results (Section 4.10; Appendix D.8). Using separate calculation code and obtaining agreement with the supplied labels do not establish independent-researcher review or clinical validity of those labels.

**Revised wording before appendix renumbering:**

Separate calculation code reproduced ranking and decision metrics from stored scores, rederived validation calibration and reconciled model selection and B/C cost records. A subsequent fresh-environment replay recovered the compared predictive results after full training and final inference on the same host (Section 4.10).

### P422 — REWRITE

**Source section:** 4.3 Routine-validation losses and checkpoint selection

**Reason:** جمع وصف المنحنيات وحدود تفسيرها في فقرة نتائج واحدة، دون مساواة خسارة إعادة البناء بجودة الكشف.

**Retained information:** ['§4.3, revised P422; Figures 4.1–4.2']

**Original wording (historical):**

At the selected checkpoints, A had a lower mean routine-validation reconstruction loss than B and C under both sampling conditions. The mean training and validation curves for B and C were close. These losses describe reconstruction of routine sessions, not the ability to distinguish threats from legitimate activity. The curves generally continued to decline near the end of the fixed budget; this does not establish convergence or show whether further training would improve detection performance.

**Revised wording before appendix renumbering:**

At the selected checkpoints, A had a lower mean routine-validation reconstruction loss than B and C under both sampling conditions. The mean training and validation curves for B and C were close and generally continued to decline near the end of the fixed budget. These curves measure reconstruction of routine sessions; neither convergence nor an effect of further training on detection performance was established.

### P449 — REWRITE

**Source section:** 4.5 Secondary known-scenario results

**Reason:** الإبقاء على المرجع الحسابي وجميع قيمه، وحذف التنبيه المتكرر بأن هذا المرجع لا يستبدل قاعدة القرار المنفذة؛ كلمة calculated reference تحدد دوره بالفعل.

**Retained information:** ['§4.5, revised P449 (calculated reference)', '§4.2.3, P413; §4.8.3, revised P485 (primary rule unchanged)']

**Original wording (historical):**

As a calculated reference, flagging every secondary-test session would give TP = 378, FP = 267 and FN = 0, yielding F1 = 756/1,023 ≈ 73.90% and FPR = 100%. This is close to A’s mean F1 of 74.01% under Reference sampling and 74.05% under controlled Non-IID sampling. The comparison shows why F1 must be interpreted with the false-positive rate in this test; it does not replace the evaluated decision rule.

**Revised wording before appendix renumbering:**

As a calculated reference, flagging every secondary-test session would give TP = 378, FP = 267 and FN = 0, yielding F1 = 756/1,023 ≈ 73.90% and FPR = 100%. This is close to A’s mean F1 of 74.01% under Reference sampling and 74.05% under controlled Non-IID sampling, illustrating why F1 must be read alongside FPR in this test.

### P451 — REWRITE

**Source section:** 4.6 Client-level and worst-client performance

**Reason:** حماية تعريف worst-client الضروري لفهم الجدول، مع نقل المسار المحلي وتاريخ توافر ملف الهوية إلى ملحق الأدلة وعدم إخفاء أن توافره غير متحقق.

**Retained information:** ['§4.6, revised P451 (metric definition and unresolved availability pointer)', 'Evidence Companion / Client-level files and unresolved identity listing']

**Original wording (historical):**

Table 4.8 summarises client-level AP on the primary held-out test. For each configuration, sampling condition and seed, the lowest AP among the three clients and the corresponding client identity were recorded. The worst-client column reports the mean and sample standard deviation of these minimum values across the five seeds, rather than selecting the client with the lowest mean AP. Per-seed client AP values are available in results/tables/recomputed_rank_metrics.csv in the supplied study archive. The historical companion file listing the minimum-client identities was not identified in the supplied files, so its availability remains unverified (Appendix D.6).

**Revised wording before appendix renumbering:**

Table 4.8 summarises client-level AP on the primary held-out test. For each configuration, sampling condition and seed, the minimum AP among the three clients and the corresponding client identity were recorded. The worst-client column reports the mean and sample standard deviation of these minima across the five seeds, rather than the lowest client mean. Individual-seed values and the unresolved availability of the historical minimum-client identity file are documented in the Evidence Companion.

### P466 — REWRITE

**Source section:** 4.8.1 Post-test descriptive breakdown

**Reason:** فصل تعريف التحليل الوصفي ومقام النسب عن أسماء ملفات المستودع؛ حفظ حالة الملف المفقود في موضع يمكن مراجعته دون تحميل متن النتائج سرداً إدارياً.

**Retained information:** ['§4.8.1, revised P466 (post-test status, frozen decisions and denominators)', 'Evidence Companion / Scenario-summary inventory and unavailable historical file']

**Original wording (historical):**

Table 4.10 and Figure 4.5 show false-positive rates for configuration C by type of legitimate activity. This descriptive breakdown was performed after final evaluation using the existing alert decisions; no thresholds were changed. Five-seed descriptive summaries for A and B are available in the supplied repository snapshot, as identified in Appendix D.6; the historical individual-seed scenario file was not identified. The same snapshot includes results/tables/descriptive_class_error_summary.csv, with post-test descriptive class and scenario summaries for A, B and C at q = 0.99 and sessions_per_model denominators. In positive-only threat groups, the alert rate is recall; in negative-only legitimate groups, it is FPR. AP and AUROC are not assigned to these one-class groups.

**Revised wording before appendix renumbering:**

Table 4.10 and Figure 4.5 show configuration C’s false-positive rates by type of legitimate activity. The breakdown was performed after final evaluation using the existing alert decisions at q = 0.99, without changing thresholds. Summaries use sessions_per_model denominators. In positive-only threat groups, the alert rate is recall; in negative-only legitimate groups, it is FPR. AP and AUROC are not assigned to these one-class groups. The Evidence Companion identifies the available A/B/C summaries and the historical individual-seed scenario file that was not located.

### P473 — REWRITE

**Source section:** 4.8.1 Post-test descriptive breakdown

**Reason:** الإبقاء على النتيجة المقارنة السلبية، وتجميع عدم عزل أسباب الخطأ في فقرة الصلاحية الداخلية التي تسمي العوامل المرشحة.

**Retained information:** ['§4.8.1, revised P473; §5.7.2, P571']

**Original wording (historical):**

High false-positive rates on unusual legitimate activity also occurred in A and B on the secondary test (Table 4.7), so the problem was not unique to C. The causes of these errors were not isolated experimentally.

**Revised wording before appendix renumbering:**

High false-positive rates on unusual legitimate activity also occurred in A and B on the secondary test (Table 4.7), so the problem was not unique to C.

### P485 — REWRITE

**Source section:** 4.8.3 Prespecified threshold sensitivity

**Reason:** جمع نتيجة الحساسية وحالة القاعدة الأولية في صياغة مباشرة، مع الحفاظ على عدم تغيير الدرجات أو إجراء بحث لاحق عن العتبة.

**Retained information:** ['§4.8.3, revised P485']

**Original wording (historical):**

Within the tested settings, reducing false-positive rates came at the cost of lower recall, and most unusual legitimate sessions in the secondary test were still flagged at q = 0.995. Applying the alternative thresholds did not change the saved scores or their ordering. The primary decision rule remained at q = 0.99; no additional threshold search or score reversal was performed.

**Revised wording before appendix renumbering:**

Within the tested settings, lower false-positive rates came at the cost of lower recall, and most unusual legitimate sessions in the secondary test were still flagged at q = 0.995. The saved scores and their ordering were unchanged. The primary decision rule remained at q = 0.99; no additional threshold search or score reversal was performed.

### P505 — REWRITE

**Source section:** 4.9.1 Training-path time and record-content volume

**Reason:** حصر فقرة النتائج في حد القياس الفعلي؛ إبقاء غياب معيار القبول التشغيلي في تفسير الكلفة في P540.

**Retained information:** ['§4.9.1, revised P505; §5.3, revised P540']

**Original wording (historical):**

The recorded time included model fitting, waiting for client replies, protocol operations, saving data and diagnostic checks that differed between B and C. The increase therefore describes the implemented workflows rather than cryptographic computation alone. No operational cost limit was specified for judging acceptability.

**Revised wording before appendix renumbering:**

The recorded time included model fitting, waiting for client replies, protocol operations, saving data and diagnostic checks that differed between B and C. The increase therefore measures the implemented workflows rather than cryptographic computation alone.

### P513 — REWRITE

**Source section:** 4.10 Computational reproduction check

**Reason:** تنظيم فقرة إعادة الإنتاج حول ما تطابق فعلاً، مع إبقاء وحدة التحليل وعدم تحويل صفوف التنبؤ إلى عينات مستقلة؛ نقل تاريخ التشغيل إلى سجل الأدلة.

**Retained information:** ['§4.10, revised P513; Evidence Companion / Replay execution chronology']

**Original wording (historical):**

The fresh-environment replay completed all 30 training runs and 60 final model–test evaluations on 11 October 2026. The initial and selected tensor states included in the comparison matched the historical reference, as did the selected rounds. No differences were found in validation scores, calibration, raw or calibrated test scores, predictive metrics or paired-seed summaries. All 90,270 model–test score rows agreed, including alert decisions at q = 0.98, 0.99 and 0.995. These rows comprise repeated model evaluations of 3,009 test sessions; they are not 90,270 independent observations.

**Revised wording before appendix renumbering:**

The fresh-environment replay completed all 30 training runs and 60 final model–test evaluations on the same host. The compared initial and selected tensor states and selected rounds matched the historical reference. No differences were found in validation scores, calibration, raw or calibrated test scores, predictive metrics or paired-seed summaries. All 90,270 model–test score rows agreed, including alert decisions at q = 0.98, 0.99 and 0.995. These rows are repeated model evaluations of 3,009 test sessions, not independent observations.

### P514 — REWRITE

**Source section:** 4.10 Computational reproduction check

**Reason:** عرض الاستثناء المادي مباشرة بدلاً من افتتاح إداري عن الإبقاء على الجداول؛ لم يتحول التطابق التنبؤي إلى ادعاء بتطابق كل ملفات المعالجة.

**Retained information:** ['§4.10, revised P514; §5.7.5, revised P582; Appendix D.8']

**Original wording (historical):**

The predictive results in the original tables are retained. The replay did not reproduce every byte of the historical preprocessing metadata: one scaler diagnostic differed by one adjacent float64 value, and the unchanged runtime hash contract required the disclosed compatibility binding in Appendix D.8. The applied scaling parameters and all 30 regenerated arrays matched the reference.

**Revised wording before appendix renumbering:**

One scaler diagnostic differed by one adjacent float64 value, although the applied scaling parameters and all 30 regenerated arrays matched the historical reference. The original runtime hash contract therefore required the compatibility binding documented in Appendix D.8. Exact agreement applies to the compared predictive results, not every byte of the preprocessing metadata.

### P515 — REWRITE

**Source section:** 4.10 Computational reproduction check

**Reason:** الاحتفاظ بجميع فروق الموارد وحدود المقارنة، ونقل اسم CSV وتعليمات عدم استبدال الجداول إلى الوثيقة المساندة.

**Retained information:** ['§4.10, revised P515; Evidence Companion / Replay resource differences and original-table status']

**Original wording (historical):**

Recorded resource measurements differed. Across ten runs per method, mean elapsed time changed by +16.907% for A, +9.758% for B and +5.917% for C relative to the historical measurements. These are within-method descriptive changes; A and B/C use different elapsed-time boundaries. B application-fit-record byte counts were unchanged, while C changes ranged from −90 to +180 bytes. Historical system-cost tables and figures remain unchanged; the new measurements are supplied separately in ME06_System_Costs_Descriptive.csv. No controlled causal explanation of these differences was established.

**Revised wording before appendix renumbering:**

Resource measurements differed from the historical runs. Across ten runs per method, mean elapsed time changed by +16.907% for A, +9.758% for B and +5.917% for C. These are within-method descriptive changes because A and B/C use different elapsed-time boundaries. B application-fit-record byte counts were unchanged, while C changes ranged from −90 to +180 bytes. No controlled causal explanation of these differences was established; the replay measurements are reported separately in the Evidence Companion.

### P517 — REWRITE

**Source section:** 4.11 Bounded security-validation results

**Reason:** استبدال بادئة التاريخ بالتسلسل العلمي وحفظ التاريخ في الأدلة؛ إبقاء عدد الحالات ووحدة العد والبيئة وافتراضاتها دون صياغة ضمان أمني عام.

**Retained information:** ['§4.11, revised P517; §5.7.5, revised P580', 'Evidence Companion / Historical security execution chronology']

**Original wording (historical):**

The seven groups completed on 11 October 2026 in the retained local environment. The historical selected result set contains 101 case records: 99 PASS, one FAIL and one OBSERVED_BOUNDARY (Table 4.16). Case records, rather than assertions or repeated sessions, are the counting unit. No selected contract case was NOT_RUN. These outcomes describe tested implementation behaviour under the local trusted-host assumptions; they do not establish a general security guarantee.

**Revised wording before appendix renumbering:**

After the main benchmark, seven bounded security-validation groups were executed in the retained local environment. The historical selected set contains 101 case records: 99 PASS, one FAIL and one OBSERVED_BOUNDARY (Table 4.16). Case records, rather than assertions or repeated sessions, are the counting unit. No selected contract case was NOT_RUN. The outcomes describe implementation behaviour under the local trusted-host assumptions.

### T27R0C1P0 — REWRITE

**Source section:** 4.11 Bounded security-validation results

**Reason:** التمييز العلمي المطلوب هو الحملة الأصلية مقابل إعادة اختبار الإصلاح؛ تاريخ اليوم محفوظ في السجلات ولا يلزم في رأس جدول النتائج.

**Retained information:** ['4.11 Bounded security-validation results, T27R0C1P0']

**Original wording (historical):**

11 Oct baseline / SV-05 retest

**Revised wording before appendix renumbering:**

Original suite / SV-05 retest

### T27R5C1P0 — REWRITE

**Source section:** 4.11 Bounded security-validation results

**Reason:** حفظ نتائج الفشل والإصلاح وأعداد الحالات حرفياً، مع استبدال تاريخ اليوم بوصف النسخة الأصلية وإعادة الاختبار.

**Retained information:** ['4.11 Bounded security-validation results, T27R5C1P0']

**Original wording (historical):**

11 Oct: 6 PASS; 1 FAIL. 12 Oct: 7 PASS.

**Revised wording before appendix renumbering:**

Original: 6 PASS; 1 FAIL. Retest: 7 PASS.

### P520 — REWRITE

**Source section:** 4.11 Bounded security-validation results

**Reason:** اختصار وصف العطل والإصلاح مع حفظ الاستثناء والمرحلة وعدد الاستدعاءات ومعيار الرفض واختلاف النسخة؛ عدم إعادة كتابة النتيجة التاريخية على أنها PASS.

**Retained information:** ['§4.11, revised P520; companion baseline and repair records']

**Original wording (historical):**

The historical failure was SV05_PARALLEL_LIST_LENGTH_MISMATCH. Removing one source ID while retaining its ciphertext list caused KeyError at UNMASK after three toy fit callbacks; the recorded exception message was 22. No aggregate callback was accepted and the toy aggregate state did not advance. The sealed criterion required controlled ValueError or RuntimeError rejection. A baseline replay reproduced the failure. In the separately versioned repair, the unchanged malformed-list fixture raised ValueError during collection, before the affected client fit callback and before UNMASK, with zero accepted aggregates. The repaired copy therefore meets the rejection criterion for this finding and the tested inputs; the original FAIL record is retained.

**Revised wording before appendix renumbering:**

The historical failure was SV05_PARALLEL_LIST_LENGTH_MISMATCH. Removing one source ID while retaining its ciphertext list caused KeyError at UNMASK after three toy fit callbacks; the exception message was 22. No aggregate was accepted and the toy aggregate state did not advance, but the sealed criterion required controlled ValueError or RuntimeError rejection. A baseline replay reproduced the failure. In the separately versioned repair, the unchanged fixture raised ValueError during collection, before the affected client fit callback and UNMASK, with zero accepted aggregates. This meets the named rejection criterion for the tested inputs; the historical FAIL remains retained.

### P521 — REWRITE

**Source section:** 4.11 Bounded security-validation results

**Reason:** تجميع نتائج الإصلاح بحسب وحدات العد: 59 حالة عقد و12 حالة حراسة و75 اختباراً مستقلاً؛ الحفاظ على حدود ترتيب الاستدعاءات وعدم جمعها مع 101 كأنها حملة كاملة معادة.

**Retained information:** ['§4.11, revised P521; Evidence Companion / SV-05 selected retest runs']

**Original wording (historical):**

The repaired copy passed all 59 cases under the original contract, including all seven SV-05 fixtures. The 12 additional production-guard cases also passed: three complete controls (normal order, reversed aligned pairs and nonsequential node IDs) and nine malformed-routing cases. Each positive control completed four stages and one aggregate within its numerical bound. The malformed requests were rejected before the affected client fit callback, and no aggregate was accepted. The observed total fit count for the original malformed-list fixture was zero; earlier clients may still fit under a different request order. Separately, 75 unit/regression tests passed without failures, errors or skips. These counts do not represent a rerun of the complete historical 101-case suite.

**Revised wording before appendix renumbering:**

The repaired copy passed all 59 original-contract cases, including all seven SV-05 fixtures, and all 12 additional production-guard cases. The latter comprised three complete controls (normal order, reversed aligned pairs and nonsequential node IDs) and nine malformed-routing cases. Each positive control completed four stages and one aggregate within its numerical bound. Malformed requests were rejected before the affected client fit callback, with no accepted aggregate. The original malformed-list fixture had zero total fit callbacks; earlier clients may still fit under a different request order. Separately, 75 unit/regression tests passed without failures, errors or skips. These are separate selected runs, not a rerun of the complete historical 101-case suite.

### P523 — MOVE_TO_COMPANION

**Source section:** 4.11 Bounded security-validation results

**Reason:** هذه الفقرة سجل محاولات وحالة خروج وجرد ملفات؛ النتائج المختارة والعطل الفعلي وإصلاحه موجودة في P517 وP520–522. نقلها كاملة يمنع خلط تاريخ حزمة التحقق بالتجربة العلمية.

**Retained information:** ['§4.11, P517/P520–522 (selected scientific outcomes)', 'Evidence Companion / Historical security attempts and source inventories']

**Original wording (historical):**

Both 11 October protocol attempts are retained. Attempt 01 had 57 PASS and two FAIL records; one failure was a harness decoder call missing keep_input=True. Only that API call was repaired. Attempt 02 had 58 PASS and one target FAIL, with the acceptance contract and target code unchanged. Both exited with code 2 because an unmet criterion remained. The other groups completed in their first attempts. The original 299 source/preprocessing inventory entries and the four sealed runtime/build files matched before and after execution. Performance and system-cost tables were not recalculated or replaced.

### P524 — MOVE_TO_COMPANION

**Source section:** 4.11 Bounded security-validation results

**Reason:** تفاصيل ZIP وبوابات المصدر وأخطاء اكتشاف الاختبارات وتصحيح افتراض ترتيب callbacks تخص سجل الأدلة؛ تبقى نتيجة إصلاح الحراسة وعدد الحالات وحدودها في P520–521.

**Retained information:** ['§4.11, revised P520–521 (repair result and tested scope)', 'Evidence Companion / SV-05 repair attempts, source gates and preserved hashes']

**Original wording (historical):**

SV05_Repair_Evidence.zip retains the new baseline, candidate and regression attempts, executed programs, contracts, timestamps, exit codes and stdout/stderr. The initial unit discovery error and predecessor whole-file equality failure are disclosed, together with their corrections. The successor source gate pins the exact repaired file and verifies that the previous response-validator function remains unchanged. A supplementary callback-order assumption was corrected before the selected production rerun; the original 59-case rejection criterion was unchanged. All 299 original source/preprocessing entries and four protected runtime/build files still matched their preserved hashes.

### P527 — REWRITE

**Source section:** 5.1 The architectural trade-off

**Reason:** بدء المناقشة بالتفسير المركزي بدلاً من إعادة تعداد تصميم الدراسة وإعلان طريقة التفسير؛ إبقاء الفصل بين نجاح التكامل والأداء والكلفة.

**Retained information:** ['§4.2.1, P401/Table 4.1; §5.1, revised P527; §5.4–5.6']

**Original wording (historical):**

The study compared pooled centralised training, Flower FedAvg with local training at simulated clients, and FedAvg with SecAgg+ to mask individual client updates. Both federated workflows completed on the shared research computer. B and C showed small observed differences in mean global AP, whereas C required more recorded training-workflow time and application-message content (Tables 4.9 and 4.14). I interpret integration, overhead and alert usefulness separately: successful integration of SecAgg+ does not establish negligible overhead, and similar mean AP values do not establish that the alerts are operationally useful.

**Revised wording before appendix renumbering:**

The comparison exposes a trade-off between protected aggregation, system cost and alert usefulness. On the shared research computer, B and C showed small observed differences in mean global AP, while C required more recorded training-workflow time and application-message content (Tables 4.9 and 4.14). Successful SecAgg+ integration therefore coexisted with appreciable workflow overhead and poor handling of unusual legitimate activity.

### P530 — DELETE_REDUNDANT

**Source section:** 5.2 RQ1: federated detection relative to the centralised reference

**Reason:** فقرة تسرد قيماً سبق عرضها في النتائج دون تفسير إضافي. تبقى قيم AP وworst-client وFPR كاملة في الجداول وتناقش مفاضلة القرارات في P531.

**Retained information:** ['Tables 4.4, 4.5 and 4.8; P531']

**Original wording (historical):**

On the primary held-out test, B’s mean global AP was 0.4161 under Reference sampling and 0.4293 under controlled Non-IID sampling. Corresponding mean worst-client AP values were 0.3938 and 0.4077, and mean FPRs at q = 0.99 were 8.75% and 7.19%, respectively (Tables 4.4, 4.5 and 4.8).

### P534 — DELETE_REDUNDANT

**Source section:** 5.2 RQ1: federated detection relative to the centralised reference

**Reason:** تنتقل دلالة precision والإنذارات الكاذبة إلى تقييم الأهمية العملية في P562؛ الفقرة الحالية تشتت تفسير RQ1 بإعادة مناقشة C.

**Retained information:** ['Revised P562 (46–50% and 72–87 per 1,000 retained); P563; Table 4.7']

**Original wording (historical):**

Privacy was the motivation for the architecture, but the quality of its alerts still matters. For the protected configuration C, primary-test mean precision was approximately 46–50%, with about 72–87 false alerts per 1,000 legitimate sessions across the two sampling conditions. All three configurations showed high false-positive rates on unusual legitimate activity in the secondary test (Table 4.7). These results do not establish suitability for operational EHR monitoring.

### P535 — DELETE_REDUNDANT

**Source section:** 5.2 RQ1: federated detection relative to the centralised reference

**Reason:** حقيقة AUROC دون 0.5 داخل العملاء موجودة في P454، وتفسير عدم كفاية pooling في P548؛ لا تضيف إعادة سردها في RQ1 دليلاً جديداً.

**Retained information:** ['§4.6, P454; §5.4, revised P548']

**Original wording (historical):**

The raw client-level results further show that poor ranking was not confined to pooled evaluation. On the secondary test, every client-level AUROC for C was below 0.5 across both sampling conditions and all five seeds (Section 4.6). This pattern cannot be explained solely by pooling calibrated scores, although its cause was not isolated.

### P537 — REWRITE

**Source section:** 5.3 RQ2: secure aggregation, detection differences and overhead

**Reason:** جمع تفسير دليل الحماية وحدوده في فقرة واحدة وإحالة نتائج التحقق إلى فصل النتائج، بدلاً من إعادة سرد تاريخ العطل والإصلاح في P538.

**Retained information:** ['§5.3, revised P537; §4.11, revised P520–522; §5.7.5, revised P580']

**Original wording (historical):**

In C, clients returned masked aggregation messages instead of the individual plaintext contributions used in B, under the honest-participant and trusted-endpoint assumptions in Section 3.8. Source-code checks, predefined tests and completed protocol stages support the reported implementation. They do not demonstrate reduced reconstruction-attack success or confidentiality from the shared host’s administrator.

**Revised wording before appendix renumbering:**

In C, clients returned masked aggregation messages instead of the individual plaintext contributions used in B, under the honest-participant and trusted-endpoint assumptions in Section 3.8. Source-code checks, completed protocol stages and the bounded tests in Section 4.11 support this implementation claim. They do not measure privacy leakage or reconstruction-attack success, or establish confidentiality from the shared host’s administrator.

### P538 — DELETE_REDUNDANT

**Source section:** 5.3 RQ2: secure aggregation, detection differences and overhead

**Reason:** أُبقيت المشاهدات الأمنية والعطل وإصلاحه وحد metadata في نتائج P520–522، وحدود الاستدلال الأمني في P537/P580. إعادة التاريخ هنا لا تضيف تفسيراً لـRQ2.

**Retained information:** ['§4.11, P520–522; revised P537/P580; Evidence Companion / Historical security execution chronology']

**Original wording (historical):**

The later validation in Section 4.11 adds direct server-ingress observations for public fixtures and selected negative tests. The 11 October audit recorded a late malformed-list error and a diagnostic-metadata boundary. The 12 October repair resolved the named error in the separate tested copy; the metadata boundary remains. The tested C interface omitted populated plaintext parameter records. The checks established neither inference resistance nor comprehensive malformed-message handling, and did not measure attack success or privacy loss.

### P540 — REWRITE

**Source section:** 5.3 RQ2: secure aggregation, detection differences and overhead

**Reason:** ربط الأرقام بتفسير حجم العبء ومعيار القبول المفقود في موضع مناقشة الكلفة؛ تجنب فصل النتيجة عن دلالتها بجملة تعلن رأي الكاتب.

**Retained information:** ['§5.3, revised P540']

**Original wording (historical):**

C took longer than B in every matched run. Mean paired increases in recorded training-workflow time were 132.78% under Reference sampling and 128.64% under controlled Non-IID sampling, with approximately 49.90% more application-message content (Table 4.14). Mean additional time was approximately 555–565 s per 30-round run. I regard this as appreciable overhead for the tested workload. Its operational acceptability remains unresolved because no resource budget or operating schedule was specified.

**Revised wording before appendix renumbering:**

C took longer than B in every matched run. Mean paired increases in recorded training-workflow time were 132.78% under Reference sampling and 128.64% under controlled Non-IID sampling, with approximately 49.90% more application-message content (Table 4.14). Mean additional time was approximately 555–565 s per 30-round run. This was appreciable overhead for the tested workload, although its operational acceptability remains unresolved because no resource budget or operating schedule was specified.

### T28R2C1P0 — REWRITE

**Source section:** 5.3 RQ2: secure aggregation, detection differences and overhead

**Reason:** تحديد نسخة المصدر المصححة بوظيفتها بدلاً من التاريخ الإداري؛ تبقى نتيجة الفشل السابق وحدود التحقق واضحة.

**Retained information:** ['5.3 RQ2: secure aggregation, detection differences and overhead, T28R2C1P0']

**Original wording (historical):**

Execution of the pinned SecAgg+ path under the stated trusted-host and honest-participant assumptions. Later public-fixture checks: Section 4.11 and Appendix D.9; the historical controlled-rejection failure was resolved in the separately tested 12 October source copy.

**Revised wording before appendix renumbering:**

Execution of the pinned SecAgg+ path under the stated trusted-host and honest-participant assumptions. Later public-fixture checks: Section 4.11 and Appendix D.9; the historical controlled-rejection failure was resolved in the separately tested guarded source copy.

### P544 — DELETE_REDUNDANT

**Source section:** 5.3 RQ2: secure aggregation, detection differences and overhead

**Reason:** ثبات المعمارية والمدخلات بين B وC موثق في التصميم والمساهمة P560؛ أثره التفسيري أن حماية التجميع لم تعالج الإنذارات الكاذبة ظاهر في P527/P546. لا حاجة لفقرة انتقالية تعيدهما.

**Retained information:** ['§5.1, revised P527; §5.4, P546; revised P560; Table 4.1']

**Original wording (historical):**

SecAgg+ was introduced to protect individual updates. It changed how client parameters were aggregated, while the detector architecture, input features and dataset labels remained unchanged between B and C. Successful integration therefore coexisted with the detector’s difficulty in handling unusual legitimate activity.

### P548 — REWRITE

**Source section:** 5.4 Interpreting false positives on legitimate exceptions

**Reason:** حصر عدم التحقق في نطاق الدراسة، مع حفظ ملاحظة تطابق الوسوم مع المصدر دون تقرير عدم وجود تحكيم في أي مكان.

**Retained information:** ['§4.6, P454; §5.4, revised P548; §5.7.1, P566']

**Original wording (historical):**

On the secondary test, C showed poor global ranking with both raw and calibrated scores, and poor ranking within clients using raw scores (Section 4.6). Evaluation labels matched the supplied source; their validity was not independently established. Calibration alone therefore cannot explain the pattern. The relative contributions of routine-only training, incomplete context and synthetic-data construction remain unresolved.

**Revised wording before appendix renumbering:**

C’s poor secondary-test ranking occurred with both raw and calibrated global scores and with raw scores within clients (Section 4.6). Calibration alone therefore cannot explain the pattern. The relative contributions of routine-only training, incomplete context and synthetic-data construction remain unresolved; evaluation labels matched the supplied source, but their clinical validity was not independently established in this study (Section 5.7.1).

### P549 — REWRITE

**Source section:** 5.4 Interpreting false positives on legitimate exceptions

**Reason:** الإبقاء على تفسير الحساسية هنا وحذف إعادة إعلان عدم البحث عن العتبة أو قلب الدرجات، المحفوظ صراحة في P485.

**Retained information:** ['§5.4, revised P549; §4.8.3, revised P485']

**Original wording (historical):**

For C, raising q from 0.99 to 0.995 reduced false-positive rates but also lowered recall, while most unusual legitimate sessions in the secondary test were still flagged (Table 4.11). The tested alternatives did not resolve this problem. No additional threshold search or score reversal replaced the primary evaluation, since either would define a different decision rule.

**Revised wording before appendix renumbering:**

For C, raising q from 0.99 to 0.995 reduced false-positive rates but also lowered recall, while most unusual legitimate sessions in the secondary test were still flagged (Table 4.11). The tested threshold alternatives therefore did not resolve the detector’s difficulty with legitimate exceptions.

### P550 — DELETE_REDUNDANT

**Source section:** 5.4 Interpreting false positives on legitimate exceptions

**Reason:** العوامل الثلاثة ليست نتائج سببية: تفاصيل طول الجلسات محفوظة في P411، ومعدلات الاستبعاد في P490، ومشكلة المدخلات المكررة وعدم عزلها مجمعة في P571 وخطة اختبارها في P585.

**Retained information:** ['Revised P411; P490; §5.7.2, P571; §5.8, P585']

**Original wording (historical):**

In the primary test, both threat and longitudinal follow-up sessions contained five events, compared with 6–23 for routine sessions. Categorical-target exclusions and the duplicated information in department and ward_or_location also warrant investigation (Sections 3.3 and 4.8.4). None was varied independently, so their effects and any benefit from changing them remain untested.

### P552 — REWRITE

**Source section:** 5.5 Relationship to the literature

**Reason:** مقارنة الدليل الذي توفره الدراستان بدلاً من إعلان مساهمة ثم إلحاق عدة تنبيهات؛ حفظ الفرق بين السجلات الحقيقية والوسوم الاصطناعية وعدم ادعاء التفوق.

**Retained information:** ['§5.5, revised P552; citation Martínez Llamas et al. (2025) unchanged']

**Original wording (historical):**

Martínez Llamas et al. (2025) combined an LSTM autoencoder with Flower and FedAvg using real hospital logs, but lacked anomaly ground truth for verifying detection and false-positive rates. In this study, supplied synthetic labels enabled threat-versus-legitimate evaluation, while the B–C comparison separately measured detection differences and the system costs associated with SecAgg+. The findings add evidence on protected aggregation, but the synthetic source limits generalisation to operational EHR settings and does not support numerical superiority over their study.

**Revised wording before appendix renumbering:**

Martínez Llamas et al. (2025) combined an LSTM autoencoder with Flower and FedAvg using real hospital logs, but lacked anomaly ground truth for verifying detection and false-positive rates. Here, supplied synthetic labels enabled threat-versus-legitimate evaluation, and the B–C comparison measured detection differences and SecAgg+ system costs. The different data sources preclude a direct numerical comparison, while the synthetic benchmark limits generalisation to operational EHR settings.

### P553 — REWRITE

**Source section:** 5.5 Relationship to the literature

**Reason:** تركيز الفقرة على المقارنة العلمية ذات الصلة وحفظ اختلاف التدخل والميزانية؛ حذف النفي الإنشائي للتفوق والأولوية العالمية لأن الفقرة لا تدعيهما.

**Retained information:** ['§5.5, revised P553; Shamim et al. (2026), Qazi et al. (2026); local contribution defined in P560/P597']

**Original wording (historical):**

Shamim et al. (2026) compare two encrypted SDN intrusion-detection implementations, while Qazi et al. (2026) evaluate a private federated ERP anomaly detector using component ablations and utility/cost measures. These studies provide substantive precedents for utility–cost evaluation of protected federated detection. Their tasks and interventions differ from this experiment: the first changes the cryptographic stack, and Qazi et al.’s headline communication contrast uses different round budgets. The present B–C estimates therefore contribute evidence for the implemented Flower workflows on this benchmark; they do not establish general numerical superiority or global priority.

**Revised wording before appendix renumbering:**

Shamim et al. (2026) compare two encrypted SDN intrusion-detection implementations, while Qazi et al. (2026) evaluate a private federated ERP anomaly detector using component ablations and utility/cost measures. They provide precedents for evaluating both utility and cost in protected federated detection. Direct comparison with the present B–C estimates is limited by their different tasks and interventions: Shamim et al. change the cryptographic stack, and Qazi et al.’s headline communication contrast uses different round budgets.

### P554 — REWRITE

**Source section:** 5.5 Relationship to the literature

**Reason:** حفظ المقارنة الدقيقة لافتراضات Bell/Li وحدود قياس الكلفة دون تكرار نفي تقديم خوارزمية جديدة؛ هذا النفي موجود في فقرة المساهمة.

**Retained information:** ['§5.5, revised P554; §5.6, revised P560; §6.3, P597']

**Original wording (historical):**

FedAvg (McMahan et al., 2017) and secure aggregation (Bonawitz et al., 2017; Bell et al., 2020; Li et al., 2022) provide established foundations. Bell et al. (2020) establish sparse-graph protocol efficiency through security proofs, numerical parameter bounds and component benchmarks. Their guarantees depend on client corruptions fixed before execution and specified dropout bounds; the semi-malicious analysis requires honest public-key collection and commitment, or an external public-key infrastructure. The supplied full IACR version leaves a system implementation for future work. Li et al. (2022) assume encrypted, authenticated links and exclude communication latency from their simulation; these cost analyses do not directly establish the present B–C overhead, measured for the implemented no-TLS workflows and their diagnostic checks. This study evaluated FedAvg with and without Flower’s SecAgg+ under matched EHR training conditions, rather than proposing a new algorithm or protocol. Published protocol analyses do not by themselves validate every component of the locally modified implementation.

**Revised wording before appendix renumbering:**

FedAvg (McMahan et al., 2017) and secure aggregation (Bonawitz et al., 2017; Bell et al., 2020; Li et al., 2022) provide the foundations for this implementation comparison. Bell et al. (2020) establish sparse-graph protocol efficiency through security proofs, numerical parameter bounds and component benchmarks. Their guarantees require client corruptions fixed before execution and specified dropout bounds; the semi-malicious analysis also requires honest public-key collection and commitment, or an external public-key infrastructure. Their full IACR version leaves a system implementation for future work. Li et al. (2022) assume encrypted, authenticated links and exclude communication latency from their simulation. These different assumptions and cost boundaries prevent their analyses from establishing the present B–C overhead for the locally modified, no-TLS Flower workflows and their diagnostics. Protocol-level analyses also do not validate every component of that local implementation.

### P560 — REWRITE

**Source section:** 5.6 Contribution and practical significance

**Reason:** تحديد المساهمة وما يجعل المقارنة قابلة للتفسير بدلاً من إعادة عرض قائمة ملفات الحزمة؛ عدم تحويل ضبط التصميم إلى عزل سببي كامل.

**Retained information:** ['§5.6, revised P560; §4.10; Evidence Companion / Code and result inventory']

**Original wording (historical):**

The study contributes an implementation and evaluation of Flower-based EHR anomaly detection with training at simulated clients and SecAgg+ aggregation. The comparison used the same model architecture, matched sampling schedules and a common calibration procedure. It assessed detection performance and system cost rather than introducing a new algorithm. Source code, the local patch and seed-level results support inspection of the comparison.

**Revised wording before appendix renumbering:**

The contribution is an implementation-level evaluation of Flower-based EHR anomaly detection with training at simulated clients and SecAgg+ aggregation. Using the same model architecture, matched sampling schedules and a common calibration procedure made the B–C comparison interpretable as a comparison of the implemented workflows. Its evidence includes both detection and system-cost outcomes, including the detector’s false-positive failure.

### P561 — DELETE_REDUNDANT

**Source section:** 5.6 Contribution and practical significance

**Reason:** نتيجة replay معروضة كاملة في P513–515 وحدودها في P581–582؛ الإنذارات السلبية لم تختف وتبقى في P562/598. لا تضيف إعادة replay في المساهمة استنتاجاً جديداً.

**Retained information:** ['§4.10, revised P513–515; §5.7.5, revised P581–582; revised P562; P598']

**Original wording (historical):**

The completed replay recovered both favourable and adverse predictive outcomes for this fixed comparison, strengthening its computational evidence without changing the scientific design or retuning against the tests. The high false-positive rates on unusual legitimate activity therefore remain part of the reproduced result. The replay addresses execution reproducibility within the existing host; it adds no independent hospital sample or new estimate of clinical usefulness.

### P562 — REWRITE

**Source section:** 5.6 Contribution and practical significance

**Reason:** دمج التفسير العملي المنقول من P534 في موضعه الطبيعي؛ إبقاء الأرقام السلبية الأساسية والفصل بين نجاح حماية التدريب وصلاحية الإنذارات للتشغيل.

**Retained information:** ['§5.6, revised P562; source P534; P563; Tables 4.5/4.7']

**Original wording (historical):**

False alerts on unusual legitimate activity limit the detector’s demonstrated practical value. They remain an outcome of the same privacy-motivated evaluation: the study implemented protected training, but did not establish that its alerts were suitable for operational use.

**Revised wording before appendix renumbering:**

The detector’s alert quality limits its demonstrated practical value. For C, primary-test mean precision was approximately 46–50%, with about 72–87 false alerts per 1,000 legitimate sessions across the two sampling conditions. All three configurations also had high false-positive rates on unusual legitimate activity in the secondary test (Table 4.7). Protected training was implemented, but these outcomes do not establish suitability for operational EHR monitoring.

### P567 — DELETE_REDUNDANT

**Source section:** 5.7.1 Construct validity

**Reason:** تجمع فقرة P580 المنقحة حدود الخصوصية والصلاحية الأمنية نفسها، مع افتراض المضيف المشترك والبيانات المرئية؛ تظل فقرة صلاحية البناء P566 مخصصة لمعنى الوسوم.

**Retained information:** ['§5.3, revised P537 and P541; §5.7.5, revised P580']

**Original wording (historical):**

The SecAgg+ stage and masked-reply checks documented how individual updates were handled during aggregation; they did not quantify information leakage. Aggregate outputs and metadata remained visible, while the researcher retained access to local client files. The evidence therefore concerns the implemented aggregation interface, not complete privacy preservation (Section 3.8).

### P570 — REWRITE

**Source section:** 5.7.2 Internal validity

**Reason:** إصلاح الإحالة بعد نقل التاريخ التطويري كاملاً إلى السجل الخارجي؛ توقيت الفحوص بالنسبة للنتائج يبقى معلناً.

**Retained information:** ['5.7.2 Internal validity, P570']

**Original wording (historical):**

The structure of the source data was inspected before final-test scoring, but the date of the first inspection was not fully documented. The original generation and partitioning rules were unavailable. The partitions had disjoint session IDs and chronologically ordered, non-overlapping time ranges, but included recurring actors and patients. Excluding their identifiers from model inputs did not rule out reliance on repeated behavioural patterns. Appendix C.5 documents the available chronology of data inspection, fixed inputs and code repairs.

**Revised wording before appendix renumbering:**

The structure of the source data was inspected before final-test scoring, but the date of the first inspection was not fully documented. The original generation and partitioning rules were unavailable. The partitions had disjoint session IDs and chronologically ordered, non-overlapping time ranges, but included recurring actors and patients. Excluding their identifiers from model inputs did not rule out reliance on repeated behavioural patterns. The Evidence Companion documents the available chronology of data inspection, fixed inputs and code repairs.

### P572 — REWRITE

**Source section:** 5.7.2 Internal validity

**Reason:** الإبقاء على تهديد الصلاحية الفعلي، ونقل تاريخ توافر ملفات validation والفحوص الحسابية إلى أدلة التحقق بدلاً من إقحامه بين الخطر وتفسيره.

**Retained information:** ['§5.7.2, revised P572; §4.2.4, revised P417', 'Evidence Companion / Validation-score availability and calibration checks']

**Original wording (historical):**

The same routine-validation sessions were used for checkpoint selection and calibration, which may have made calibration optimistic. Complete validation-score files were subsequently supplied, allowing separate arithmetic checks of calibration parameters, thresholds and empirical validation exceedance rates. A threshold derived at q = 0.99 from validation scores does not guarantee a 1% false-positive rate on test data.

**Revised wording before appendix renumbering:**

The same routine-validation sessions were used for checkpoint selection and calibration, which may have made calibration optimistic. A threshold derived at q = 0.99 from validation scores does not guarantee a 1% false-positive rate on test data.

### P579 — REWRITE

**Source section:** 5.7.5 Reproducibility, provenance and security validity

**Reason:** تخصيص الفقرة للفجوة الفعلية في الأصل والحقوق والأخلاقيات؛ جمع حدود المضيف والمساعد الأمني في الفقرة الأمنية التالية.

**Retained information:** ['§5.7.5, revised P579–580']

**Original wording (historical):**

The dataset’s creator, generation process and redistribution rights remain unverified, as does the study’s formal ethics status. Recorded file hashes support consistency checks, not verification of these matters. Trust in the shared host did not establish client isolation, and the locally modified mask-generation helper was not cryptographically certified by this study.

**Revised wording before appendix renumbering:**

The dataset’s creator, generation process and redistribution rights remain unverified, as does the study’s formal ethics status. Recorded file hashes establish file consistency, not provenance, permission or ethical approval.

### P580 — REWRITE

**Source section:** 5.7.5 Reproducibility, provenance and security validity

**Reason:** توحيد حدود الصلاحية الأمنية المكررة من P567/P579 ونتيجة الإصلاح في فقرة واحدة؛ حفظ كل الاستثناءات المادية وعدم الادعاء بحماية شاملة.

**Retained information:** ['§5.7.5, revised P580; source P567/P579; §4.11, revised P520–522']

**Original wording (historical):**

The later bounded suite provides additional evidence on helper conformance, selected message checks, numerical aggregation and observed context freshness. The subsequent repair and targeted retest closed the named SV-05 finding in a separate source version. Permitted diagnostic metadata is still assumed public and trusted. No formal cryptographic certification, arbitrary-collusion test, shared-host isolation test or TLS deployment validation was performed. These tests do not resolve the separate data-provenance, clinical-label or ethics uncertainties.

**Revised wording before appendix renumbering:**

The bounded suite supports helper conformance, selected message checks, numerical aggregation and observed context freshness. A separately versioned repair and targeted retest resolved the named SV-05 rejection failure, while permitted diagnostic metadata remains assumed public and trusted. Aggregated outputs and metadata remain visible, and the researcher retained access to client files on the shared host. The evidence does not quantify information leakage or establish cryptographic certification, arbitrary-collusion resistance, shared-host isolation or TLS deployment protection. These implementation checks leave the separate provenance, clinical-label and ethics uncertainties unresolved.

### P581 — REWRITE

**Source section:** 5.7.5 Reproducibility, provenance and security validity

**Reason:** إبقاء دلالة replay وحدود استقلاله هنا، ونقل تاريخ الفحوص السابقة وتفصيل NumPy إلى سجل إعادة الإنتاج.

**Retained information:** ['§5.7.5, revised P581; §4.10', 'Evidence Companion / Pre-replay checks and NumPy comparison']

**Original wording (historical):**

Earlier checks recalculated stored-score metrics, reproduced calibration and linked model assets, including a separate NumPy check of nine validation sessions across all 30 models. The subsequent replay rebuilt the environment, regenerated numerical inputs, trained all 30 models and completed validation and test inference on the same host. The compared predictive outputs and selected tensor states matched exactly (Section 4.10). This was a controlled replay of the fixed experiment after its results were known; it supplies no new independent test sample and is not a blinded external-researcher replication.

**Revised wording before appendix renumbering:**

The fresh-environment replay regenerated numerical inputs, trained all 30 models and completed validation and test inference on the existing host. The compared predictive outputs and selected tensor states matched exactly (Section 4.10). Because the fixed experiment was replayed after its results were known, this establishes same-host execution reproducibility, not a blinded external-researcher replication or evidence from a new independent test sample.

### P582 — REWRITE

**Source section:** 5.7.5 Reproducibility, provenance and security validity

**Reason:** حفظ استثناء ULP وحدود التطابق والموارد وعدم وجود مولد أصلي؛ نقل وصف تجميع view وحفظ الملفات إلى الوثيقة المساندة.

**Retained information:** ['§5.7.5, revised P582; §4.10, revised P514–515', 'Evidence Companion / Scaler-metadata compatibility binding']

**Original wording (historical):**

The replay retained a material metadata boundary. One local scaler diagnostic differed by one float64 ULP although all applied scaling parameters and encoded arrays matched. To satisfy the original identity check, a separately sealed compatibility view combined the fresh arrays with the historical scaler JSON representation. Raw preprocessing and its replay were preserved unchanged (Appendix D.8). Accordingly, exact agreement is claimed for the compared predictive outputs, not every preprocessing byte or intermediate training trajectory. Resource timings and C record-content measurements also differed and were not causally isolated. Independent external-host replication and original-generator reconstruction remain unverified.

**Revised wording before appendix renumbering:**

The scaler-metadata exception qualifies the replay agreement. One diagnostic differed by one float64 ULP, although all applied scaling parameters and encoded arrays matched; the original identity check required the compatibility binding described in Appendix D.8. Exact agreement therefore concerns the compared predictive outputs, not every preprocessing byte or intermediate training trajectory. Resource timings and C record-content measurements also differed without a controlled causal explanation. Independent external-host replication and reconstruction from the original data generator remain unverified.

### P585 — REWRITE

**Source section:** 5.8 Implications and bounded future work

**Reason:** إبقاء التجارب التالية المحددة وحاجة البيانات الجديدة، وحذف تنبيه أن future work ليس نتيجة؛ مكان الفقرة وصيغتها الشرطية يحددان ذلك.

**Retained information:** ['§5.8, revised P585; §5.7.2, P571']

**Original wording (historical):**

Further methodological work should isolate session length, recurring actor and patient patterns, categorical-target exclusions and duplicated location information where these are proposed explanations of the observed errors. A local-only baseline would be needed to assess whether collaboration benefits clients relative to training independently. Any resulting representation or threshold changes should be assessed on fresh evaluation data. These are proposed follow-up experiments, not findings of the present study.

**Revised wording before appendix renumbering:**

Further methodological work should isolate session length, recurring actor and patient patterns, categorical-target exclusions and duplicated location information where these are proposed explanations of the observed errors. A local-only baseline would assess whether collaboration benefits clients relative to training independently. Any resulting representation or threshold changes should be evaluated on fresh data.

### P592 — REWRITE

**Source section:** 6.2 Conclusions in relation to the research questions

**Reason:** دمج إجابة RQ1 ومفاضلة AP/قرارات P593 في فقرة واحدة دون إسقاط عدم وجود baseline محلي أو عدم اليقين أو النتيجة السلبية.

**Retained information:** ['§6.2, revised P592; source P593']

**Original wording (historical):**

For RQ1, FedAvg (B) showed no consistent observed global AP advantage over pooled centralised training (A) in this benchmark (Tables 4.4, 4.6 and 4.9). On the primary held-out test, the mean paired difference (B−A) was −0.0697 under Reference sampling and +0.0238 under controlled Non-IID sampling; both exploratory 95% intervals included zero. All three configurations had high mean false-positive rates on unusual legitimate sessions in the secondary test (Table 4.7). No local-only baseline was evaluated, so gains over independently trained client models were not established.

**Revised wording before appendix renumbering:**

For RQ1, FedAvg (B) showed no consistent observed global AP advantage over pooled centralised training (A) in this benchmark (Tables 4.4, 4.6 and 4.9). On the primary held-out test, the mean paired difference (B−A) was −0.0697 under Reference sampling and +0.0238 under controlled Non-IID sampling; both exploratory 95% intervals included zero. Under controlled Non-IID sampling, B’s higher AP accompanied lower recall and F1 at q = 0.99, so ranking did not imply uniform improvement in alert decisions (Tables 4.4 and 4.5). All three configurations had high mean false-positive rates on unusual legitimate sessions in the secondary test (Table 4.7). No local-only baseline was evaluated, so gains over independently trained client models were not established.

### P593 — DELETE_REDUNDANT

**Source section:** 6.2 Conclusions in relation to the research questions

**Reason:** دمج مضمون الفقرة وجميع إحالاتها في إجابة RQ1 المنقحة P592؛ لا حاجة لإجابة ثانية منفصلة تكرر نقطة المفاضلة.

**Retained information:** ['§6.2, revised P592 (includes q = 0.99, Tables 4.4/4.5); §5.2, P531']

**Original wording (historical):**

Under controlled Non-IID sampling, the higher primary-test global AP for B was accompanied by lower recall and F1 at q = 0.99. Ranking performance therefore did not imply a uniform improvement in alert decisions (Tables 4.4 and 4.5; Section 5.2).

### P595 — REWRITE

**Source section:** 6.2 Conclusions in relation to the research questions

**Reason:** قصر إجابة RQ2 على معنى الحماية ومعنى تقدير الكلفة وحد القبول؛ الإحالة إلى inference المفصل لا تحتاج إعادة عرضه في الاستنتاج.

**Retained information:** ['§6.2, revised P595; §4.9.2, P507/P511; §5.3, revised P537/P540/P541']

**Original wording (historical):**

Under the stated security assumptions, SecAgg+ masked individual client updates during aggregation. Privacy leakage was not quantified, and no operational cost limit was specified. The timing comparison concerns the implemented training workflows, including their differing diagnostics, rather than cryptographic computation alone (Section 4.9.1). Prepared-input inference was measured separately, with no SecAgg+ execution during inference (Section 4.9.2). The study documents this implementation and its measured detection and cost outcomes. It does not establish comprehensive privacy protection or whether the additional cost is acceptable for deployment.

**Revised wording before appendix renumbering:**

SecAgg+ masked individual client updates under the stated security assumptions, but privacy leakage was not quantified. The cost contrast concerns the implemented training workflows and their differing diagnostics, rather than cryptographic computation alone (Section 4.9.1). With no operational cost limit specified, deployment acceptability remains unresolved.

### P599 — REWRITE

**Source section:** 6.3 Contribution and limits of the evidence

**Reason:** إبقاء نتيجة إعادة الإنتاج والاستثناء المادي في خلاصة قصيرة؛ حذف قائمة حدود سريرية وتعميمية مكررة محفوظة في الصلاحية وتعريف نطاق الاستنتاج.

**Retained information:** ['§6.3, revised P599; §5.7.1, P566; §5.7.3, P574; revised P581–582; P590']

**Original wording (historical):**

The fresh-environment replay recovered the compared predictive results and selected model tensor states exactly on the supplied fixed snapshot and existing host (Section 4.10; Appendix D.8). This agreement supports execution of the reported RQ comparisons; their conclusions are unchanged. The scaler-metadata compatibility exception and nonidentical resource measurements remain disclosed; clinical label validity, external-data generalisation and replication on an independent host remain unestablished.

**Revised wording before appendix renumbering:**

A fresh-environment replay exactly recovered the compared predictive results and selected model tensor states on the supplied fixed snapshot and existing host (Section 4.10; Appendix D.8). The scaler-metadata compatibility exception and nonidentical resource measurements qualify this agreement. The original RQ conclusions are unchanged.

### P600 — REWRITE

**Source section:** 6.3 Contribution and limits of the evidence

**Reason:** إبقاء الخلاصة الأمنية الفعلية وحدها بدلاً من إعادة التاريخ وأعداد مجموعات الاختبارات في الخاتمة؛ تبقى كل الأعداد ووحدات عدها صريحة في P517/P521 والجدول 4.16.

**Retained information:** ['§4.11, revised P517 (101 = 99 PASS + one FAIL + one OBSERVED_BOUNDARY)', '§4.11, revised P521 (59 contract + 12 guard cases; separately 75 tests)', 'Table 4.16; §5.7.5, revised P580']

**Original wording (historical):**

The 11 October audit completed seven bounded groups, retaining 99 PASS, one controlled-rejection FAIL and one diagnostic-metadata boundary among 101 selected records (Section 4.11; Appendix D.9). The 12 October source revision resolved the named SV-05 failure: 59 original-contract cases, 12 additional production-guard cases and 75 unit/regression tests passed in their selected runs. This supports the specific input-validation correction while preserving the historical failure and metadata limitation. It does not establish quantified privacy protection, comprehensive replay resistance or security against the shared-host administrator. Original RQ utility and cost conclusions remain unchanged.

**Revised wording before appendix renumbering:**

The bounded security checks identified a controlled-rejection defect that was resolved in a separately versioned SV-05 repair and targeted retest; the diagnostic-metadata boundary remains (Section 4.11; Appendix D.9). This supports the specific input-validation correction, while leaving quantified privacy protection, comprehensive replay resistance and protection from the shared-host administrator unestablished. The original RQ utility and cost conclusions are unchanged.

### P605 — REWRITE

**Source section:** 6.4 Bounded future work and final statement

**Reason:** إنهاء البحث بالاستنتاج العلمي المركزي ضمن نطاقه، دون إعادة تعداد Flower والعملاء وAP وحجم الرسائل المكررة في إجابات RQ.

**Retained information:** ['§6.1, P589–590; §6.2, P594–595; §6.3, P598; revised P605']

**Original wording (historical):**

The study implemented Flower-based EHR anomaly detection with training at simulated clients and SecAgg+ masking of individual updates during aggregation, under the stated assumptions. B and C showed small observed differences in mean global AP, while C had higher recorded training-workflow time and application-message content. The usefulness of its alerts and the acceptability of the additional cost for operational use remain unresolved.

**Revised wording before appendix renumbering:**

The implemented SecAgg+ workflow supports protected aggregation under the stated assumptions. High false-positive rates on legitimate exceptions and higher training-workflow costs leave alert usefulness and cost acceptability for operational EHR monitoring unresolved.

### P651 — REWRITE

**Source section:** APPENDIX A: LITERATURE SEARCH DETAILS

**Reason:** يجمع حدود البحث التاريخي الضرورية في موضع واحد، مع إبقاء الأعداد والفجوات ظاهرة، ونقل تاريخ متابعة الملفات إلى المرافق.

**Retained information:** ['P651', 'Evidence_Companion: historical searches and source-access history; original P651/P691 and T32–T47']

**Original wording (historical):**

This appendix distinguishes the historical searches in Appendix B from later source verification and search updates. On 11 October 2026, the supplied native-export files were structurally inspected and their record counts reconciled against the historical entries where possible. This verified the contents of the received files, but did not independently authenticate every original query execution, filter setting, total-hit count or screening decision. PubMed export gaps and ACM all-results coverage remain explicitly unresolved. A focused full-text retrieval of Martínez Llamas et al. (2025) on 11 September 2026 completed the comparison in Sections 2.3, 2.8 and 5.5. This later check did not replace the August search history, add reconstructed screening decisions or establish a systematic review.

**Revised wording before appendix renumbering:**

The literature review combines historical August searches with separately dated source checks and narrative updates. Inspection of the received native exports on 11 October 2026 verified their file contents, not every original query execution, interface setting or screening decision. PubMed S1 contains 10 received records against 15 recorded hits, leaving five unreconciled; the recorded 12-result S3 export is unavailable, and S2 lacks a contemporaneous response authenticating its zero-result entry. Each of the three received ACM exports contains 20 records, with total-hit and all-results coverage unverified. Historical queries, counts and reconciliation details are retained in the Evidence Companion. Later searches do not replace these records or establish a systematic review.

### P653 — REWRITE

**Source section:** A.1 Databases, time coverage, and search date

**Reason:** يبقي تاريخ البحث ونطاقه والفلاتر غير المحفوظة، ويحذف إحالة إلى ملحق انتقل إلى المرافق.

**Retained information:** ['P653', 'P651']

**Original wording (historical):**

The records date PubMed/MEDLINE searches to 10 August 2026 and Scopus, Web of Science Core Collection, IEEE Xplore and ACM Digital Library to 11 August 2026. The intended scope was January 2000 onward for direct EHR work and January 2016 onward for federated methods, with English full texts retained. Scopus year and field restrictions are visible in the displayed expressions. Equivalent interface date/language settings for the remaining searches were not fully retained; they are not assumed. In particular, the Web of Science S2 expression inherits #1 and does not establish a separate 2016 restriction. Appendix B preserves raw-hit versus exported-record distinctions.

**Revised wording before appendix renumbering:**

The historical records date PubMed/MEDLINE searches to 10 August 2026 and Scopus, Web of Science Core Collection, IEEE Xplore and ACM Digital Library searches to 11 August 2026. The intended scope was January 2000 onward for direct EHR work and January 2016 onward for federated methods, with English full texts retained. Scopus year and field restrictions are visible in the expressions; equivalent interface restrictions for other databases were incompletely retained. Web of Science S2 inherits S1 and does not establish a separate 2016 restriction.

### P654 — DELETE_REDUNDANT

**Source section:** A.1 Databases, time coverage, and search date

**Reason:** تكرار مباشر لحد عدم مصادقة البحث التاريخي، بعد جمعه في افتتاح الملحق مع أمثلة كمية واضحة.

**Retained information:** ['P651', 'P653', 'Evidence_Companion: historical search records']

**Original wording (historical):**

The dates, queries, restrictions and counts below are historical recorded values. Listing a query expression in this appendix does not authenticate its original execution, interface settings, export coverage or screening decisions. Any later search update is documented separately from this record.

### P656 — REWRITE

**Source section:** A.2 Inclusion and exclusion criteria

**Reason:** يحدد صراحة الفرق بين موضوعات البحث الأدبي وما نُفذ، دون شرح دفاعي إضافي.

**Retained information:** ['P656']

**Original wording (historical):**

Note. The historical search included transferable topics broader than the final experimental scope. Those searches do not mean that personalisation, explainability or additional frameworks were implemented.

**Revised wording before appendix renumbering:**

Note. Historical searches also covered personalisation, explainability and additional frameworks, which were not implemented in this study.

### P657 — REWRITE

**Source section:** A.2 Inclusion and exclusion criteria

**Reason:** يبقي وظيفة كل عائلة أدلة والفجوات الأصلية، وينقل اسم ملف الاكتشاف المفقود إلى الجرد المرافق.

**Retained information:** ['P657', 'Evidence_Companion: original P657 and literature discovery inventory']

**Original wording (historical):**

The retained bibliography contains two overlapping evidence families: direct-domain EHR studies and transferable method/protocol/metric sources. Lazzarini et al. supply non-EHR federated intrusion-detection context; McMahan et al. supply FedAvg; Bonawitz et al., Bell et al. and Li et al. supply aggregation foundations; inversion and metric references support boundaries and evaluation. This clarification explains their role in the final synthesis; it is not a reconstructed historical screening rule. The record does not preserve complete deduplication totals, article-level exclusion reasons or whether each foundational paper entered through a database query or citation chasing. The historical index names tables/literature_source_discovery_map.csv for these links, but that file was not identified in the bounded supplied-archive inspection. The missing discovery links remain unknown; they have not been reconstructed.

**Revised wording before appendix renumbering:**

The retained bibliography serves two overlapping roles: direct-domain EHR evidence and transferable method, protocol and metric evidence. Lazzarini et al. provide non-EHR federated intrusion-detection context; McMahan et al. provide FedAvg; Bonawitz et al., Bell et al. and Li et al. provide aggregation foundations; inversion and metric references inform evaluation and its limits. These roles describe the final synthesis rather than reconstructed historical screening rules. Complete historical deduplication totals, article-level exclusion reasons and query-versus-citation-chaining discovery links were not retained.

### P658 — MOVE_TO_COMPANION

**Source section:** A.2 Inclusion and exclusion criteria

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: source-access and dated literature-update history / original P658']

**Original wording (historical):**

Separate literature update — 10 October 2026. A targeted web search revisited recent direct EHR access-monitoring candidates and transferable sequence, federated-optimisation, synthetic-data-validity and privacy methods. It used web indexing followed by original publisher, author or proceedings sources. This was a bounded narrative update, not a systematic review, a rerun of the August database searches or a repair of their missing exports.

### P659 — MOVE_TO_COMPANION

**Source section:** A.2 Inclusion and exclusion criteria

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: exact executed literature queries and source-access records / original P659']

**Original wording (historical):**

Broad discovery expressions included: "EHR" "access logs" "anomaly" "2026" "federated" "secure aggregation"; and "electronic health record" "audit logs" "anomaly detection" "2026". Candidate-specific follow-ups used titles, DOIs and publisher domains. The accompanying front_literature_update_20261010.json records the exact executed expressions, access decisions and section-level receipts; no total-hit count, deduplication count or exhaustive screening denominator is claimed.

### P660 — REWRITE

**Source section:** A.2 Inclusion and exclusion criteria

**Reason:** يبقي ما قُرئ بالفعل وحدود التغطية، وينقل تواريخ الوصول وأعداد صفحات النسخ إلى سجل المصادر بدل تحويلها إلى سرد إصلاح.

**Retained information:** ['P660', 'Evidence_Companion: original P660, source versions and access/read matrix']

**Original wording (historical):**

Original relevant sections were checked for Malhotra et al. (2016), Li et al. (2020), Achterberg et al. (2024), Ngo et al. (2024), Matos et al. (2026), Iqbal et al. (2026), Segar and Vijayan (2026) and Tanvir et al. (2026). Malhotra and Ngo are cited in their arXiv versions. A full-text follow-up on 10 October 2026 checked the three subsequently supplied papers: the 24-page IACR ePrint 2020/704 version of Bell et al. (2020), revised on 10 November 2020; the nine-page IEEE conference paper by Senturk et al. (2025); and the 21-page published article by Sutradhar et al. (2026). Their source-access limitation is resolved for this revision. Claims attributed to these papers were checked against their methods, results and limitations; this does not independently validate their experiments or certify the cryptographic proofs. Subsequent source follow-ups checked the full texts of the retained BFL-STPC and Kamatchi papers, including all their figures and tables, and the six-page Abbasi conference paper. Their unresolved numerical and methodological qualifications remain recorded; source availability does not establish correctness or independent replication. The related Abbasi master's thesis was excluded from the review scope. Other candidate access levels are reported individually in the current source-evidence matrix and candidate access records. These targeted checks do not constitute a complete Source Coverage Audit of the bibliography.

**Revised wording before appendix renumbering:**

Targeted source checks covered the relevant original sections of Malhotra et al. (2016), Li et al. (2020), Achterberg et al. (2024), Ngo et al. (2024), Matos et al. (2026), Iqbal et al. (2026), Segar and Vijayan (2026) and Tanvir et al. (2026); Malhotra and Ngo are cited in their arXiv versions. Subsequent full-text checks covered Bell et al. (2020), Senturk et al. (2025), Sutradhar et al. (2026), the retained BFL-STPC and Kamatchi papers, including their figures and tables, and the Abbasi conference paper. The Abbasi master’s thesis was outside scope. Source-specific versions, read scopes and unresolved qualifications are retained in the Evidence Companion. These targeted checks are not complete full-text verification of the bibliography or independent replication of the cited experiments.

### P662 — REWRITE

**Source section:** A.3 Documented literature refresh of 11 October 2026

**Reason:** يبقي طريقة التحديث وجميع مقامات البحث الأساسية، وينقل أسماء السجلات والهاشات وتفاصيل الإيصالات إلى المرافق.

**Retained information:** ['P662', 'Evidence_Companion: refresh registers and original P662']

**Original wording (historical):**

Literature refresh of 11 October 2026. A documented targeted narrative update used four query families separately in PubMed E-utilities and Europe PMC, supplemented by web-index discovery and source chaining. Refresh identifiers are distinct from the historical August S1–S4 identifiers. All returned public-API identifiers and bibliographic records were preserved for the exact executed queries, together with request URLs, query translations, warnings, timestamps and raw-response hashes. The query-hit sum was 498; after within-database merging there were 488 database records, corresponding to 281 stable source identifiers before final DOI/title reconciliation. Web responses preserve returned top results and batch provenance; search-engine total hits were not supplied. Eligibility decisions, duplicates, full-text access levels and the closest-study comparison are retained in the 11 October refresh package. This is a narrative update and does not retrospectively authenticate or replace the historical August searches.

**Revised wording before appendix renumbering:**

A targeted narrative refresh on 11 October 2026 used four query families in PubMed E-utilities and Europe PMC, supplemented by web-index discovery and source chaining. Its identifiers were separate from the historical August searches. The API query-hit sum was 498; within-database merging yielded 488 records corresponding to 281 stable source identifiers before final DOI/title reconciliation. Complete returned API identifiers and request records were preserved. Web discovery retained returned top results, without a search-engine total-hit denominator. Candidate decisions, duplicates and full-text access levels are documented in the Evidence Companion.

### P666 — REWRITE

**Source section:** A.3 Documented literature refresh of 11 October 2026

**Reason:** يحفظ عدد الاستعلامات والعناقيد ومعناها وحدودها، ويستبدل قائمة أسماء الملفات بإحالة واحدة قابلة للتنفيذ.

**Retained information:** ['P666', 'Evidence_Companion: original P666 and full literature refresh inventory']

**Original wording (historical):**

The supplementary archive Literature_Refresh_ME04_ME05_20261011.zip retains Unified_Search_Register.csv and .json with all 51 exact query strings; public_api/Search_Result_Manifest.json and HTTP_Request_Receipts.json with executed translations, complete API identifiers and request receipts; public_api/Screening_Union.csv and web/Unified_Web_Returned_Records.csv with candidate decisions and reasons; and Literature_Novelty_Evidence_Matrix.csv with individual source access/read scopes. Cross_Channel_Candidate_Catalog.json retains 452 identifier-linked clusters, which are not a verified unique-study count. Raw responses and hashes are retained with these registers. The archive supplements the historical evidence rather than reconstructing it.

**Revised wording before appendix renumbering:**

The Evidence Companion retains all 51 exact query strings, API request and translation records, candidate decisions with reasons, source-access/read scopes and raw-response identities. Its cross-channel catalogue contains 452 identifier-linked clusters, which are not a verified unique-study count. The historical August query tables and export reconciliations are preserved separately from this refresh.

### P667 — MOVE_TO_COMPANION

**Source section:** APPENDIX B: DATABASE-SPECIFIC SEARCH STRINGS AND COUNTS

**Reason:** التعبيرات التاريخية الطويلة وجرد مطابقة التصدير تحفظ كاملة بالمرافق؛ منهج البحث وحدوده وأعداده غير المصادق عليها باقية في Appendix A، فلا يبقى عنوان فارغ.

**Retained information:** ['Evidence_Companion: Historical database-specific query tables (old Appendix B) / original P667']

**Original wording (historical):**

APPENDIX B: DATABASE-SPECIFIC SEARCH STRINGS AND COUNTS

### P668 — MOVE_TO_COMPANION

**Source section:** APPENDIX B: DATABASE-SPECIFIC SEARCH STRINGS AND COUNTS

**Reason:** التعبيرات التاريخية الطويلة وجرد مطابقة التصدير تحفظ كاملة بالمرافق؛ منهج البحث وحدوده وأعداده غير المصادق عليها باقية في Appendix A، فلا يبقى عنوان فارغ.

**Retained information:** ['Evidence_Companion: Historical database-specific query tables (old Appendix B) / original P668']

**Original wording (historical):**

The following entries preserve the recorded queries, dates and counts. Their labels describe the historical record rather than independently authenticated database execution. Where an export or complete reconciliation was unavailable, that limitation is retained rather than converting missing rows into assumed exclusions.

### P669 — MOVE_TO_COMPANION

**Source section:** B.1 Scopus

**Reason:** التعبيرات التاريخية الطويلة وجرد مطابقة التصدير تحفظ كاملة بالمرافق؛ منهج البحث وحدوده وأعداده غير المصادق عليها باقية في Appendix A، فلا يبقى عنوان فارغ.

**Retained information:** ['Evidence_Companion: Historical database-specific query tables (old Appendix B) / original P669']

**Original wording (historical):**

B.1 Scopus

### P674 — MOVE_TO_COMPANION

**Source section:** B.2 Web of Science

**Reason:** التعبيرات التاريخية الطويلة وجرد مطابقة التصدير تحفظ كاملة بالمرافق؛ منهج البحث وحدوده وأعداده غير المصادق عليها باقية في Appendix A، فلا يبقى عنوان فارغ.

**Retained information:** ['Evidence_Companion: Historical database-specific query tables (old Appendix B) / original P674']

**Original wording (historical):**

B.2 Web of Science

### P678 — MOVE_TO_COMPANION

**Source section:** B.3 PubMed/MEDLINE

**Reason:** التعبيرات التاريخية الطويلة وجرد مطابقة التصدير تحفظ كاملة بالمرافق؛ منهج البحث وحدوده وأعداده غير المصادق عليها باقية في Appendix A، فلا يبقى عنوان فارغ.

**Retained information:** ['Evidence_Companion: Historical database-specific query tables (old Appendix B) / original P678']

**Original wording (historical):**

B.3 PubMed/MEDLINE

### P682 — MOVE_TO_COMPANION

**Source section:** B.4 IEEE Xplore

**Reason:** التعبيرات التاريخية الطويلة وجرد مطابقة التصدير تحفظ كاملة بالمرافق؛ منهج البحث وحدوده وأعداده غير المصادق عليها باقية في Appendix A، فلا يبقى عنوان فارغ.

**Retained information:** ['Evidence_Companion: Historical database-specific query tables (old Appendix B) / original P682']

**Original wording (historical):**

B.4 IEEE Xplore

### P686 — MOVE_TO_COMPANION

**Source section:** B.5 ACM Digital Library

**Reason:** التعبيرات التاريخية الطويلة وجرد مطابقة التصدير تحفظ كاملة بالمرافق؛ منهج البحث وحدوده وأعداده غير المصادق عليها باقية في Appendix A، فلا يبقى عنوان فارغ.

**Retained information:** ['Evidence_Companion: Historical database-specific query tables (old Appendix B) / original P686']

**Original wording (historical):**

B.5 ACM Digital Library

### P690 — REWRITE

**Source section:** APPENDIX C: STUDY EVIDENCE REGISTER

**Reason:** عنوان مختصر يطابق محتوى الملحق ويمنع التصاق عنوان الفهرس برقم الصفحة.

**Retained information:** ['P690']

**Original wording (historical):**

APPENDIX C: STUDY EVIDENCE REGISTER

**Revised wording before appendix renumbering:**

APPENDIX B: IMPLEMENTATION AND NUMERICAL CHECKS

### P691 — DELETE_REDUNDANT

**Source section:** APPENDIX C: STUDY EVIDENCE REGISTER

**Reason:** أعداد PubMed/ACM وحدودها أُدمجت كاملة في P651؛ لا حاجة لتكرارها في ملحق التنفيذ.

**Retained information:** ['P651', 'Evidence_Companion: historical query tables T32–T47']

**Original wording (historical):**

The supplied PubMed S1 CSV was inspected on 11 October 2026 and contains 10 records, compared with 15 hits in the historical search record. Five records remain unreconciled, and PubMed S3 still lacks its recorded 12-result export. These are evidence gaps, not screened exclusions. The three supplied ACM BibTeX exports each contain 20 records, but their database total hits and complete coverage remain unverified. Other supplied platform exports were reconciled at the file-content level as documented in the 11 October verification record. Later search results are reported as a new dated search and are not substituted for the historical values.

### P692 — MOVE_TO_COMPANION

**Source section:** APPENDIX C: STUDY EVIDENCE REGISTER

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Source identities and historical evidence register (old C.1/Table C.1) / original P692']

**Original wording (historical):**

Internal identifiers E1–E9 identify the historical study records in Table C.1. They are traceability references, not external academic citations. Supplementary review archives and later verification reports are identified separately in Appendix D.4. Numerical validation tests and repair history remain distinct from the main detector results.

### P693 — MOVE_TO_COMPANION

**Source section:** APPENDIX C: STUDY EVIDENCE REGISTER

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Source identities and historical evidence register (old C.1/Table C.1) / original P693']

**Original wording (historical):**

Table C.1: Internal evidence identifiers and reporting roles

### P694 — MOVE_TO_COMPANION

**Source section:** C.1 Source and execution identities

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Source identities and historical evidence register (old C.1/Table C.1) / original P694']

**Original wording (historical):**

C.1 Source and execution identities

### P695 — REWRITE

**Source section:** C.1 Source and execution identities

**Reason:** يضع تعريف النسخة التنفيذية وإفصاح تعديل الأسئلة/الهدف بعد المراجعة في مقدمة علمية قصيرة؛ لا يُطمس تغير البروتوكول أو يُدّعى prespecification.

**Retained information:** ['P695', 'Evidence_Companion: original P695/P789; full Table E.1; §3.2 P310/P311']

**Original wording (historical):**

The benchmark is the preserved eleven-table synthetic snapshot with internal profile 2.0.0-full-reference_seed_01, not a verified Kaggle version (Table D.2). The executed local Flower identity is 1.22.0+mai.prg7570.1. Its masking-helper backport is pinned to contributor commit e87804ad00c46bff6dc3f058b73de81529e50bc0. Appendix C.2 identifies the actual source files and numerical evidence; no current upstream merge status is inferred from a historical record.

**Revised wording before appendix renumbering:**

The numerical specification uses the preserved eleven-table synthetic snapshot with internal profile 2.0.0-full-reference_seed_01 and the locally modified Flower version 1.22.0+mai.prg7570.1. Source and helper identities are retained in the Evidence Companion. The final research questions and fourth objective operationally clarify the P1 proposal to match the comparisons and outcomes measured. These post-review formulations are not presented as wording recorded before execution; the original proposal and a complete proposal-to-execution comparison remain in the Evidence Companion.

### P696 — MOVE_TO_COMPANION

**Source section:** C.1 Source and execution identities

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Source identities and historical evidence register (old C.1/Table C.1) / original P696']

**Original wording (historical):**

The following SHA-256 identifies EHR_FL_Main_Experiments_Package_v1_0_3.zip specifically (executed source release 1.0.3), not the benchmark, Decision Closure or every archive in Table C.1:

### P697 — MOVE_TO_COMPANION

**Source section:** C.1 Source and execution identities

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Source identities and historical evidence register (old C.1/Table C.1) / original P697']

**Original wording (historical):**

433a26789afd362dad4316c96379017d2808969925fa5df1d61e332d94cb6c84

### P698 — MOVE_TO_COMPANION

**Source section:** C.1 Source and execution identities

**Reason:** تاريخ المحاولات والتوقيت ومراحل المراجعة مناسب للمرافق؛ حد عدم الانتقاء ومشاهدة البنية سابقًا باقٍ في §3.9 P373–375 و§5.7.2 P570.

**Retained information:** ['Evidence_Companion: Development chronology and outcome-selection record / original P698']

**Original wording (historical):**

Incomplete main blocks and corrected successor campaigns are distinguished in Table C.6. Dates from run identifiers are local-record start markers, not independently authenticated timestamps or proof of first-ever access. The release records bind source and input digests; unknown freeze/access times remain explicit. Previous complete A outcomes and partial B outcomes were not compared for favourable selection against the accepted campaign. That historical post-test audit recalculated metrics from saved scores without rerunning inference. The separately dated 11 October 2026 replay subsequently completed fresh training and complete test inference on the same host (Appendix D.8).

### P700 — REWRITE

**Source section:** C.2 Public-vector results and attributed helper change

**Reason:** يحفظ تصميم الاختبار وتوقعاته وحدوده، ويزيل إعادة سرد مرحلة التدقيق السابقة وعدم تشغيلها.

**Retained information:** ['P700']

**Original wording (historical):**

The results below are historical candidate-build public-protocol records, distinct from the later bounded suite in Section 4.11 and Appendix D.9. These historical fixtures were not rerun during the earlier source-only audit. Equal- and unequal-weight lattice fixtures were expected to reproduce the exact quantised integer sum. The non-lattice case was allowed bounded approximation. Deliberate missing-response and mismatched-identifier cases were expected to stop before aggregation. The transport was in-memory; no benchmark data or secret state was exported.

**Revised wording before appendix renumbering:**

These historical candidate-build fixtures checked public numerical inputs through an in-memory protocol, separately from the later security suite in Section 4.11. Equal- and unequal-weight lattice fixtures were expected to reproduce the exact quantised integer sum; non-lattice inputs allowed bounded approximation. Missing-response and mismatched-identifier fixtures were expected to stop before aggregation. No benchmark data or secret state was exported.

### P702 — REWRITE

**Source section:** C.2 Public-vector results and attributed helper change

**Reason:** يبقي قيد تفسير الخطأ وقيد callback المهمين، وينقل تدقيق أسماء الملفات المفقودة والموجودة إلى المرافق.

**Retained information:** ['P702', 'Evidence_Companion: original P702 and fixture/source mapping']

**Original wording (historical):**

Note. Errors concern averaged parameter coordinates, not loss or AP. Main-weight evidence comes from the earlier full-size public-vector check, not a new experiment. Zero aggregate calls establish the exported refusal boundary, not an independently counted absence of data-callback invocation. The historical index names evidence/public_vector_fixture_specification.json and methods/SecAgg_Public_Fixture_Specification.md; these exact files were not identified in the supplied archives. The supplied full-size report retains public_protocol_full_weights.json, and the accepted main-preparation report retains public_protocol.json. The preserved source validation_support/prg_validation/public_protocol.py defines the fixture construction. Their physical identities and related-content limits are listed in artefact_mapping.json.

**Revised wording before appendix renumbering:**

Note. Errors concern averaged parameter coordinates, not loss or AP. The main-weight result is from the earlier full-size public-vector check. Zero aggregate calls establish refusal at aggregation, not independently counted absence of a data-callback invocation. The fixture construction and original numerical records are identified in the Evidence Companion.

### P703 — MOVE_TO_COMPANION

**Source section:** C.2 Public-vector results and attributed helper change

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Attributed helper sources, build recipe and historical file-identity limits / original P703']

**Original wording (historical):**

The source snapshot ehr-fl-secagg-study-main.zip preserves the package under ehr-fl-secagg-study-main/executed/EHR_FL_Main_Experiments_Package_v1_0_3/. Its validation_support/sources/ directory contains flower_v1_22_0_secaggplus_utils.py, UNMERGED_PR_7570_e87804ad_secaggplus_utils.py and backport_secaggplus_utils.py. The same validation_support/ directory contains CHANGE_MANIFEST.json, NOTICE.md and LICENSE-Flower-Apache-2.0.txt; build logic is preserved in prg_validation/build.py. Source and function identities were checked against the recorded build identity. The historical filenames executed_helper_change.diff and build_local_wheel.py are absent from this snapshot. The supplied original PRG package instead retains reference/helper_change.diff, while the preserved build implementation is validation_support/prg_validation/build.py. Inspection established related content, but not that the historical files had been renamed. The installed historical wheel payload was not supplied. Preserved source comparison does not certify the historical installed wheel or cryptographic security. That earlier source inspection did not rebuild dependencies or execute the protocol; the subsequent ME-06 rebuild and replay are documented in Appendix D.8.

### P707 — REWRITE

**Source section:** C.3 Department distributions and recorded sampling checks

**Reason:** يبقي جميع تفسيرات الجدول وأعداد العملاء، وينقل البحث عن CSV غير متاح إلى الجرد.

**Retained information:** ['P707', 'Evidence_Companion: original P707 and sampling archive mapping']

**Original wording (historical):**

Note. Ref. = original training-session distribution; NI = expected Non-IID sampling probability. C1/C2/C3 contain 3,609/3,548/3,676 original training sessions. The centralised stream also changes because it pools these same draw occurrences. The historical index names tables/department_profiles.csv for full values; that exact file was not identified in the inspected supplied archives. Proportions may not sum to exactly 100 after rounding. Related original sampling records are identified in artefact_mapping.json.

**Revised wording before appendix renumbering:**

Note. Ref. denotes the original training-session distribution; NI denotes expected Non-IID sampling probability. C1/C2/C3 contain 3,609/3,548/3,676 original training sessions. The centralised stream also changes because it pools the same draw occurrences. Proportions may not sum to exactly 100 after rounding.

### P711 — REWRITE

**Source section:** C.4 Exact sampling, construction and measurement specification

**Reason:** يمهد لتفاصيل علمية قابلة للتنفيذ بدل ذكر مسار ZIP في متن الملحق.

**Retained information:** ['P711', 'Evidence_Companion: source/build inventory']

**Original wording (historical):**

The preserved executed source is supplied in ehr-fl-secagg-study-main.zip under ehr-fl-secagg-study-main/executed/EHR_FL_Main_Experiments_Package_v1_0_3/, with its file manifest. The following specification resolves seed and timing ambiguities without replacing that code.

**Revised wording before appendix renumbering:**

The following specification documents the sampling seeds, training randomness, model-construction order and public numerical fixtures. Exact source functions and configuration records are indexed in the Evidence Companion.

### P712 — REWRITE

**Source section:** C.4 Exact sampling, construction and measurement specification

**Reason:** يحفظ الخوارزمية كاملة وأسماء الدوال، ويضع مسارات الوحدات البرمجية في المرافق.

**Retained information:** ['P712', 'Evidence_Companion: original P712 and source function index']

**Original wording (historical):**

Seed derivation serialises ordered components with “|”, encodes UTF-8, takes SHA-256, interprets the first eight digest bytes as unsigned little-endian and reduces modulo 2³². Client-round sampling uses (main seed, condition, client, round). Pooled shuffling uses (main seed, condition, “pooled”, epoch) over occurrences sorted by client and client-draw position, including duplicates. Sessions are sorted by session_id before sampling. The exact functions are app/central_smoke/sampling.py:derived_seed and main_study/design.py:make_draws/pooled_round.

**Revised wording before appendix renumbering:**

Seed derivation serialises ordered components with “|”, encodes UTF-8, takes SHA-256, interprets the first eight digest bytes as unsigned little-endian and reduces modulo 2³². Client-round sampling uses (main seed, condition, client, round). Pooled shuffling uses (main seed, condition, “pooled”, epoch) over occurrences sorted by client and client-draw position, including duplicates. Sessions are sorted by session_id before sampling. The corresponding derived_seed, make_draws and pooled_round functions are identified in the Evidence Companion.

### P714 — REWRITE

**Source section:** C.4 Exact sampling, construction and measurement specification

**Reason:** يحفظ ترتيب الوحدات والحالات الابتدائية ويستبعد فحص اسم مستند مفقود والتكرار العام عن clean-host.

**Retained information:** ['P714', 'Evidence_Companion: original P714/source index', 'Appendix D.8 P763–768']

**Original wording (historical):**

Model module-construction order is fixed in app/pilot_core/model.py: encoder, latent projection, decoder, hidden/cell projections, dropout, categorical heads in schema order, binary head and temporal head. Encoder recurrent states start at zero; decoder states are projected from the latent code. The source functions named above specify the RNG and construction context. The historical index also names methods/Deterministic_Implementation.md, but that exact file was not identified in the inspected supplied archives. Seed values alone are not a clean-host reproducibility guarantee.

**Revised wording before appendix renumbering:**

Model module-construction order is fixed: encoder, latent projection, decoder, hidden/cell projections, dropout, categorical heads in schema order, binary head and temporal head. Encoder recurrent states start at zero; decoder states are projected from the latent code. The source function index in the Evidence Companion fixes the construction and RNG context.

### P715 — REWRITE

**Source section:** C.4 Exact sampling, construction and measurement specification

**Reason:** تحديد مكان فهرسة السجلات الأصلية بدقة دون إيحاء بأن كل ملف JSON مضمن داخل Word.

**Retained information:** ['P715']

**Original wording (historical):**

For public-vector checks, the base vectors are [−1,0,1,2], [2,1,−2,0] and [0,3,1,−1]. Non-lattice cases add (i+1)[0.001,0.023,−0.041,0.079] in float32. Each client contributes four coordinates. Expected averages are calculated in float64 from those actual float32 inputs. Table C.5 and the attached JSON make the assumptions and scale explicit.

**Revised wording before appendix renumbering:**

For public-vector checks, the base vectors are [−1,0,1,2], [2,1,−2,0] and [0,3,1,−1]. Non-lattice cases add (i+1)[0.001,0.023,−0.041,0.079] in float32. Each client contributes four coordinates. Expected averages are calculated in float64 from those actual float32 inputs. Table C.5 and the original JSON records indexed in the Evidence Companion make the assumptions and scale explicit.

### P717 — DELETE_REDUNDANT

**Source section:** C.4 Exact sampling, construction and measurement specification

**Reason:** يعيد التمييز بين تدقيق سابق وتشغيل لاحق وتحديد المدخلات العامة؛ المعلومات العلمية والحدود محفوظة في مواضعها الأقرب.

**Retained information:** ['P700', 'P702', 'Appendix D.8 P763–768', 'Appendix D.9 P776–780']

**Original wording (historical):**

Note. No new protocol execution was performed during that earlier source-only audit; the subsequent ME-06 execution is documented in Appendix D.8. Public inputs, expected averages and recorded outcomes are attached; individual real client updates remain excluded. The later bounded security-validation execution is documented separately in Section 4.11 and Appendix D.9.

### P718 — MOVE_TO_COMPANION

**Source section:** C.5 Recorded development and evaluation chronology

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Recorded development chronology (old C.5/Table C.6) / original P718']

**Original wording (historical):**

C.5 Recorded development and evaluation chronology

### P719 — MOVE_TO_COMPANION

**Source section:** C.5 Recorded development and evaluation chronology

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Recorded development chronology (old C.5/Table C.6) / original P719']

**Original wording (historical):**

Table C.6: Recorded milestones and limits of chronology

### P720 — MOVE_TO_COMPANION

**Source section:** C.5 Recorded development and evaluation chronology

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Recorded development chronology (old C.5/Table C.6) / original P720']

**Original wording (historical):**

Note. Recorded milestones are distinct from independently verified dates. The historical index names tables/recorded_chronology.csv and tables/source_archive_identities.csv; these exact files were not identified in the inspected supplied archives. Original release/amendment records remain distinct from the retrospective member identities documented in artefact_mapping.json, which do not authenticate historical dates.

### P722 — REWRITE

**Source section:** C.6 Detailed execution controls

**Reason:** يبقي تسلسل التجربة الكامل وتبريره، وينقل مسار CSV إلى المرافق.

**Retained information:** ['P722', 'Evidence_Companion: exact configuration/run-order records']

**Original wording (historical):**

The fixed block order was 11/Reference, 11/Non-IID, 29/Non-IID, 29/Reference, 47/Reference, 47/Non-IID, 71/Non-IID, 71/Reference, 97/Reference and 97/Non-IID. Configuration order was A/B/C for seeds 11 and 71, B/C/A for 29 and 97, and C/A/B for 47. These were fixed rotations, not outcome-dependent choices. The exact file is protocol/decisions/config/main_run_order.csv in the executed source.

**Revised wording before appendix renumbering:**

The fixed block order was 11/Reference, 11/Non-IID, 29/Non-IID, 29/Reference, 47/Reference, 47/Non-IID, 71/Non-IID, 71/Reference, 97/Reference and 97/Non-IID. Configuration order was A/B/C for seeds 11 and 71, B/C/A for 29 and 97, and C/A/B for 47. These were fixed rotations, not outcome-dependent choices.

### P724 — REWRITE

**Source section:** C.6 Detailed execution controls

**Reason:** يبقي وصفة بناء الإعدادات والميزانية والتمييز العلمي/التشغيلي، وينقل قوائم المسارات وتاريخ الفحص والتنفيذ المكرر إلى المرافق/موضع إعادة الإنتاج.

**Retained information:** ['P724', 'Evidence_Companion: original P724 and reproducibility recipe', 'Appendix D.8 P763/P764']

**Original wording (historical):**

Scientific job configurations are constructed by main_study/design.py:cell_config and stage_cell from the preserved reference settings, protocol/decisions/config/main_protocol_decisions.json, protocol/decisions/config/main_run_order.csv, frozen development inputs, initial states and sampling schedules. main_study/campaign.py calls cell_config(seed, condition, 30); stage_cell binds that budget in fixed_config.json, job.json, runtime.json, embedded app resources and the Flower project configuration. Runtime tokens are freshly generated UUIDs and staged paths depend on the new workspace, so regenerated operational identifiers need not reproduce historical bytes. This recipe was initially inspected statically. The subsequent 11 October 2026 replay executed the configuration preparation, rebuilt and installed the local Flower package, and completed fresh training and evaluation; Appendix D.8 distinguishes those execution receipts from the historical recipe.

**Revised wording before appendix renumbering:**

Scientific job configurations combine the preserved reference settings, adopted decisions, run order, frozen development inputs, initial states and sampling schedules. The campaign constructs each seed–condition cell with a budget of 30 epochs or rounds and binds it consistently across staged job and application settings. The Evidence Companion identifies the cell_config and stage_cell implementations and exact operational configuration records. Regenerated runtime tokens and workspace paths are operational identifiers; they need not reproduce historical bytes.

### P725 — REWRITE

**Source section:** APPENDIX D: RESEARCH ARTEFACT INVENTORY

**Reason:** يعكس المحتوى العلمي الباقي بدل عنوان جرد الأرشيفات؛ يعاد D إلى C بخريطة منفصلة.

**Retained information:** ['P725']

**Original wording (historical):**

APPENDIX D: RESEARCH ARTEFACT INVENTORY

**Revised wording before appendix renumbering:**

APPENDIX D: SUPPLEMENTARY DATA, ANALYSES AND VALIDATION

### P726 — MOVE_TO_COMPANION

**Source section:** D.1 Research artefact inventory

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Research artefact inventory and access conditions (old D.1/Table D.1) / original P726']

**Original wording (historical):**

D.1 Research artefact inventory

### P727 — MOVE_TO_COMPANION

**Source section:** D.1 Research artefact inventory

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Research artefact inventory and access conditions (old D.1/Table D.1) / original P727']

**Original wording (historical):**

This research report presents results rather than embedding model binaries, raw score tables or installed Python environments. Table D.1 distinguishes the retained artefacts. Sections D.2–D.4 provide provenance and the exact filenames supplied with this revision, so that references to companion evidence are directly inspectable.

### P728 — MOVE_TO_COMPANION

**Source section:** D.1 Research artefact inventory

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Research artefact inventory and access conditions (old D.1/Table D.1) / original P728']

**Original wording (historical):**

Table D.1: Retained research artefacts and their role

### P729 — MOVE_TO_COMPANION

**Source section:** D.1 Research artefact inventory

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Research artefact inventory and access conditions (old D.1/Table D.1) / original P729']

**Original wording (historical):**

The accepted local campaign is /home/mai/EHR_FL_Main_v1/campaigns/20260909T142009Z_2ad79bf6/. It references external preprocessing and environment directories. A code-repository clone alone is not a complete rerun package. The original examiner companion excluded raw data and trained weights; supplementary review archives now supply these and the saved scores, calibrations, frozen development inputs and recorded training evidence listed below. Private keys and protocol masks are not required review artefacts. Dataset redistribution rights remain unresolved.

### P731 — REWRITE

**Source section:** D.2 Dataset provenance

**Reason:** ينقل جدول الهوية الإدارية كاملًا للمرافق، مع بقاء كل حقائق المصدر وحقوقه وفجوات التوليد في فقرة واضحة بالمخطوط.

**Retained information:** ['P731', 'Evidence_Companion: full Table D.2 and original P731', '§3.12 P395: formal ethics status remains unverified']

**Original wording (historical):**

Table D.2 states the identity and availability of the data used. Unknown fields remain unknown; approval to use a dataset does not, by itself, grant a redistribution licence. The original companion excluded the benchmark, which was subsequently supplied separately in 04_EHR_FL_Benchmark_Release_Candidate_v1_0.zip. Its package name does not establish public release, verified Kaggle derivation or redistribution rights.

**Revised wording before appendix renumbering:**

The executed benchmark was supplied for the project and marked synthetic, with internal profile full_reference_balanced, version 2.0.0-full-reference_seed_01. It contains 181,805 events and 17,464 sessions across three simulated clients. The original creator, public source/version, executable generator, verified Kaggle derivation and redistribution licence were not established. Source-file identities are retained in the Evidence Companion. The completed same-host replay reproduced processing, training, calibration and test inference on the supplied snapshot, with the metadata exception in D.8; it did not regenerate the original data.

### P732 — MOVE_TO_COMPANION

**Source section:** D.2 Dataset provenance

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Dataset provenance inventory (old Table D.2) / original P732']

**Original wording (historical):**

Table D.2: Provenance of the executed eleven-table benchmark

### P733 — REWRITE

**Source section:** D.2 Dataset provenance

**Reason:** يحفظ البذور كاملة والفرق بين مطابقة السجل والتحقق من التوليد، وينقل المسارات والهاشات إلى المرافق.

**Retained information:** ['P733', 'Evidence_Companion: original P733 and configuration hashes']

**Original wording (historical):**

A custodial configuration is supplied in Primary_Synthetic_Benchmark_Full_v2_Custodian_Ground_Truth.zip at releases/reference_seed_01/manifests/config_resolved.yaml. Its bytes match the corresponding local outputs/full/reference_seed_01/manifests/config_resolved.yaml record. It records root seed 361001 and partition seeds 361102, 361203, 361304 and 361405 for training, validation, test_known and test_held_out, respectively. The SHA-256 and physical path are retained in artefact_mapping.json. This matching record does not establish that an independently inspected original generator produced the executed eleven-table snapshot, validate scenario-authorisation rules, prove Kaggle derivation or demonstrate original-data regeneration.

**Revised wording before appendix renumbering:**

A supplied custodial configuration matches the corresponding local configuration record. It records root seed 361001 and partition seeds 361102, 361203, 361304 and 361405 for training, validation, test_known and test_held_out, respectively. This match establishes configuration consistency, not independent verification of the original generator, scenario-authorisation rules, Kaggle derivation or original-data regeneration.

### P737 — REWRITE

**Source section:** D.3 Categorical coverage by labelled class

**Reason:** يحتفظ بالمقام الصحيح ولا يعيد جرد غياب CSV ووجود JSON بديل.

**Retained information:** ['P737', 'Evidence_Companion: original P737 and coverage evidence mapping']

**Original wording (historical):**

Note. This denominator counts thirteen target opportunities per event; it is not the fraction of sessions discarded. No session was removed. The historical coverage_by_class.csv was not identified in the inspected supplied archives. Table D.3 retains the recorded target-opportunity denominator; related test/client/field counts are supplied separately in 02_Final_Evaluation_Original.zip: encoding_coverage.json, and the later descriptive source-audit receipt records class-level coverage.

**Revised wording before appendix renumbering:**

Note. The denominator counts thirteen categorical target opportunities per event, not the fraction of sessions discarded. No session was removed.

### P738 — MOVE_TO_COMPANION

**Source section:** D.4 Examiner companion supplied with this research report

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Historical companion index, supplied assets and environment records (old D.4/Table D.4) / original P738']

**Original wording (historical):**

D.4 Examiner companion supplied with this research report

### P739 — MOVE_TO_COMPANION

**Source section:** D.4 Examiner companion supplied with this research report

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Historical companion index, supplied assets and environment records (old D.4/Table D.4) / original P739']

**Original wording (historical):**

Table D.4 distinguishes the historical companion index from supplementary review archives. Unprefixed tables/, evidence/, methods/ and literature/ paths denote historical index entries. Their original companion byte streams are not assumed to be supplied. The revision supplement artefact_mapping.json records each historical reference, an actual supplied archive/member where related content was identified, its SHA-256, row unit and scope, and the limits of the relationship. A matching filename or row count does not establish historical byte identity or a rename. Raw data, test scores, selected checkpoints, validation scores, calibrations, frozen inputs and recorded training evidence were supplied separately. These historical and supplied records support inspection within their stated scope. The subsequent fresh-environment replay and its evidence are separately identified in D.8; they establish completed same-host execution, with the disclosed metadata exception, rather than independent external-host replication.

### P740 — MOVE_TO_COMPANION

**Source section:** D.4 Examiner companion supplied with this research report

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Historical companion index, supplied assets and environment records (old D.4/Table D.4) / original P740']

**Original wording (historical):**

Table D.4: Historical companion index and supplementary review files

### P741 — MOVE_TO_COMPANION

**Source section:** D.4 Examiner companion supplied with this research report

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Historical companion index, supplied assets and environment records (old D.4/Table D.4) / original P741']

**Original wording (historical):**

Environment reconstruction records are available separately. Patched_BC_Report_20260908T051118Z_5aa99ec3.zip retains full_requirements.lock with 48 pinned wheel-hash entries and full_wheel_inventory.json with the corresponding filenames, versions and hashes. EHR_FL_PRG_Validation_Package_v1_0.zip retains EHR_FL_PRG_Validation_Package_v1_0/reference/helper_change.diff. The repository source preserves the attributed helper sources and validation_support/prg_validation/build.py, which checks a pinned stock Flower wheel, changes the approved helper and local version/provenance metadata, and regenerates RECORD. Their archive/member paths and full digests are recorded in artefact_mapping.json. The historical installed wheel payload was not supplied. The lock and builder were subsequently used to reconstruct and install the local Flower package in a new environment for the completed 11 October replay. Build and installation receipts are supplied with D.8; independent external-host execution is not claimed.

### P742 — DELETE_REDUNDANT

**Source section:** D.4 Examiner companion supplied with this research report

**Reason:** يعيد وصف أدوار الأرشيفات وحدود التوليد والحقوق وصورة النظام؛ تبقى الحقائق في المنهجية وإعادة الإنتاج والمرافق.

**Retained information:** ['§3.12 P394/P395', '§5.7.5 P579/P581/P582', 'P731', 'Appendix D.8 P763–768', 'Evidence_Companion: full original P742']

**Original wording (historical):**

The supplementary historical archives and the new execution evidence have distinct roles. Historical inventories identify the preserved source, environment recipe, data and model assets, while D.8 records the completed fresh-environment training, full inference, comparison and new descriptive resource measurements. The replay did not reconstruct the complete historical operating-system image, recover unknown original data-generation steps or establish redistribution rights. Source and archive hashes support consistency and traceability within these boundaries.

### P744 — REWRITE

**Source section:** D.5 Observed sessions, partitions and scenario annotations

**Reason:** يجمع التعريف والحدود المنهجية الضرورية دون تكرار منفصل أن النتائج لم تتغير.

**Retained information:** ['P744']

**Original wording (historical):**

These are post-test descriptive measurements of the fixed eleven-table snapshot, not a new split, model, label rule or causal experiment. These measurements leave the original outcome values unchanged. The session unit follows the supplied IDs and sequence positions; the original generator’s inactivity rule, scenario injection thresholds and authorisation decisions were not available. Every affected-event identifier was checked only for membership in its labelled session, not for clinical or security truth.

**Revised wording before appendix renumbering:**

These post-test descriptive measurements characterise the fixed eleven-table snapshot without changing its partitions, models, label rule or reported outcomes. Sessions follow the supplied IDs and sequence positions; original inactivity rules, injection thresholds and authorisation decisions were unavailable. Affected-event identifiers were checked for membership in their labelled sessions, not independently adjudicated clinical or security truth.

### P746 — REWRITE

**Source section:** D.5 Observed sessions, partitions and scenario annotations

**Reason:** يحفظ تفسير الترتيب الزمني، وينقل غياب اسم ملف تاريخي إلى المرافق.

**Retained information:** ['P746', 'Evidence_Companion: original P746 and partition evidence']

**Original wording (historical):**

Note. Ranges are ordered and non-overlapping in this snapshot. Original split-generation rules and contemporaneous pre-split decisions are not thereby established. The historical index names tables/partition_time_ranges.csv for full per-client values, but that exact file was not identified in the inspected supplied archives. The values above retain the prior descriptive source-audit record; the underlying CSV partitions and later review receipts are separate evidence.

**Revised wording before appendix renumbering:**

Note. Event-time ranges are ordered and non-overlapping in this snapshot. They describe the observed partitions without establishing the original split-generation rules or contemporaneous pre-split decisions.

### P748 — REWRITE

**Source section:** D.5 Observed sessions, partitions and scenario annotations

**Reason:** يحفظ وحدة القياس وحدود التداخل والتعريف المادي للأجهزة، دون سرد عملية الجرد.

**Retained information:** ['P748']

**Original wording (historical):**

Note. Counts are distinct shared identifiers, not events. The later descriptive source audit records pooled cross-partition identifier intersections, including encounter and resource IDs. Full within-client/between-client intersection tables and set sizes were not identified in the inspected companion files. Events lack unique device IDs; device-type overlap cannot establish physical-device overlap.

**Revised wording before appendix renumbering:**

Note. Counts are distinct shared identifiers, not events. The supplied record contains pooled intersections; full within-client/between-client intersection tables and set sizes were not identified in the inspected companion files. Events lack unique device IDs, so device-type overlap cannot establish physical-device overlap.

### P750 — REWRITE

**Source section:** D.5 Observed sessions, partitions and scenario annotations

**Reason:** يحفظ الاختلاف البنيوي المهم وحدود التحليل؛ ينقل غياب quantiles/per-client files إلى المرافق.

**Retained information:** ['P750', 'Evidence_Companion: original P750 and descriptive source records']

**Original wording (historical):**

Note. Both nonroutine held-out classes are uniformly five events. Within-session duration is last minus first event, not total campaign duration. The later descriptive source-audit receipt records pooled partition/class session-length and duration summaries. Additional quantiles and per-client summaries were not identified in the supplied historical companion files. No length-controlled re-estimation was undertaken.

**Revised wording before appendix renumbering:**

Note. Both nonroutine held-out classes contain exactly five events per session. Within-session duration is last minus first event, not campaign duration. The summaries are pooled by partition and class; no length-controlled re-estimation was performed.

### P752 — REWRITE

**Source section:** D.5 Observed sessions, partitions and scenario annotations

**Reason:** يبقي صلاحية الوسوم غير المحسومة في مكان تفسير الجدول، وينقل غياب ملف القاموس إلى المرافق.

**Retained information:** ['P752', 'Evidence_Companion: original P752 and scenario record mapping']

**Original wording (historical):**

Note. Names are source identifiers, not recovered generation rules. The historical index names tables/scenario_dictionary_observed.csv for exact labels, template identifiers, client counts and unknown injection/authorisation criteria; that exact file was not identified in the inspected supplied archives. The later descriptive source-audit receipt and raw labels remain separately identified evidence. Affected events are source annotations, not independently adjudicated truth.

**Revised wording before appendix renumbering:**

Note. Scenario names are source identifiers rather than recovered generation rules. Affected events are supplied annotations, not independently adjudicated truth; injection and authorisation criteria were unavailable.

### P753 — REWRITE

**Source section:** D.6 Statistical and subgroup output index

**Reason:** عنوان علمي بدل عنوان جرد ملفات؛ يخضع رقم القسم لخريطة الأب.

**Retained information:** ['P753']

**Original wording (historical):**

D.6 Statistical and subgroup output index

**Revised wording before appendix renumbering:**

D.6 Supplementary statistical and subgroup results

### P754 — REWRITE

**Source section:** D.6 Statistical and subgroup output index

**Reason:** يبقي التحليل ووحدة التكرار وتفسير المقاييس، وينقل عدد صفوف ملفات الجرد ومساراتها ومقارنة أسماء النسخ إلى المرافق.

**Retained information:** ['P754', 'Evidence_Companion: full original P754 and output index; no numeric file record discarded']

**Original wording (historical):**

The supplied repository archive ehr-fl-secagg-study-main.zip retains results under ehr-fl-secagg-study-main/results/tables/. seed_summary.csv contains 144 condition/test/endpoint/configuration summaries, with the mean, sample SD, median and range across the five seeds. paired_contrasts.csv contains 96 condition/test/endpoint/contrast summaries and their five explicit difference_seed_* values, rather than the historical 480-row paired_differences_by_seed.csv. The historical worst_client_by_seed.csv and scenario_error_by_seed.csv/scenario_error_summary.csv were not identified in the inspected supplied archives. recomputed_rank_metrics.csv supplies client AP values, but does not replace a packaged table retaining every within-seed minimum-client identity. Table D.9 retains the exploratory worst-client AP intervals, and Table D.10 retains the post-test AUROC decomposition. Related subgroup output is supplied as descriptive_class_error_summary.csv: 108 five-seed summaries at q = 0.99 with a sessions_per_model denominator. Alert rate is recall in positive-only threat groups and FPR in negative-only legitimate groups; no AP or AUROC is assigned to a one-class subgroup. These summaries are post-test descriptive outputs, not newly executed or prespecified experiments. artefact_mapping.json records the member hashes and the limits of each historical-to-supplied relationship.

**Revised wording before appendix renumbering:**

Seed-level summaries retain the mean, sample SD, median and range across five seeds; paired contrasts retain the five within-seed differences. Table D.9 reports exploratory worst-client AP intervals, and Table D.10 decomposes held-out AUROC. At q = 0.99, one-class subgroup alert rates are recall for threat groups and FPR for legitimate groups; AP and AUROC are not assigned to one-class subgroups. These additional subgroup summaries are post-test descriptive outputs. Detailed output indices, constituent client values and unavailable historical file identities are documented in the Evidence Companion.

### P756 — REWRITE

**Source section:** D.6 Statistical and subgroup output index

**Reason:** يبقي هدف عدم اليقين وقيد توافر هوية أسوأ عميل، وينقل أسماء ملفات المقارنة والهاشات إلى المرافق.

**Retained information:** ['P756', 'Evidence_Companion: original P756, full-precision contrasts and constituent client output']

**Original wording (historical):**

Note. Five paired seed differences, t with four degrees of freedom, conditional on this fixed snapshot. Neither zero-crossing intervals nor small differences establish equivalence. Full-precision contrast values are in the supplied results/tables/paired_contrasts.csv member. The historical CSV retaining minimum-client identities was not identified in the inspected supplied archives; related client ranking values are identified in artefact_mapping.json.

**Revised wording before appendix renumbering:**

Note. Intervals use five paired seed differences and Student’s t with four degrees of freedom, conditional on the fixed snapshot. Zero-crossing intervals and small differences do not establish equivalence. The supplied record contains constituent client AP values; a packaged table retaining every within-seed minimum-client identity was not identified in the inspected supplied archives.

### P758 — REWRITE

**Source section:** D.6 Statistical and subgroup output index

**Reason:** يحفظ معادلة إعادة التركيب ومقاماتها ونطاق saved-score، وينقل أسماء CSV وعلاقات الهوية التاريخية إلى المرافق.

**Retained information:** ['P758', 'Evidence_Companion: original P758 and AUROC decomposition records']

**Original wording (historical):**

Note. Post-test descriptive means across the same five seeds. For each seed, overall AUROC = (1,986 × routine AUROC + 189 × unusual AUROC)/2,175. The recomposed and original overall means agree before rounding; the historical CSV is not asserted to be supplied under its earlier filename. Related recorded ordering summaries are in ehr-fl-secagg-study-main.zip: ehr-fl-secagg-study-main/analysis/final_score_audit/descriptive_AUROC_mixture_checks.csv and descriptive_pairwise_ordering_summary.csv; their scope is the saved-score post-test audit.

**Revised wording before appendix renumbering:**

Note. These are post-test descriptive means across the same five seeds. For each seed, overall AUROC = (1,986 × routine AUROC + 189 × unusual AUROC)/2,175. Recomposed and original overall means agree before rounding. The decomposition uses saved scores rather than new model inference.

### P759 — REWRITE

**Source section:** D.7 Event-time context, calibration and audit boundaries

**Reason:** عنوان يصف المسألة العلمية بدل نطاق الجرد.

**Retained information:** ['P759']

**Original wording (historical):**

D.7 Event-time context, calibration and audit boundaries

**Revised wording before appendix renumbering:**

D.7 Retrospective context and calibration

### P760 — REWRITE

**Source section:** D.7 Event-time context, calibration and audit boundaries

**Reason:** يبقي تأخر التسجيل وقيد توافر الحقول في تفسير النموذج، وينقل اسم ملف semantics المفقود إلى المرافق.

**Retained information:** ['P760', 'Evidence_Companion: original P760 and context evidence']

**Original wording (historical):**

The historical index names tables/context_field_semantics.csv for context fields and their unknown original meanings; that exact file was not identified in the inspected supplied archives. The source schema, recorded audit and limitations below remain the stated evidence boundary. The recording timestamp follows the event timestamp in this snapshot (median delay 14.98 seconds; range approximately 0.000045–30.00 seconds), but that does not establish when assignment, shift, relationship or outcome values became available. Retrospective full-session scoring is the supported task. No real-time enforcement claim or retrospective historical join is inferred.

**Revised wording before appendix renumbering:**

The recording timestamp follows the event timestamp in this snapshot, with a median delay of 14.98 seconds and a range of approximately 0.000045–30.00 seconds. The availability times of assignment, shift, relationship and outcome values were not established. The supported task is retrospective full-session scoring; the record does not establish real-time enforcement or retrospective historical joins.

### P761 — REWRITE

**Source section:** D.7 Event-time context, calibration and audit boundaries

**Reason:** يحفظ الأعداد والإفصاح الحقيقي عن المساعدة البرمجية وحد calibration reuse، وينقل اسم الأرشيف ويزيل تكرار عدم الاستقلال البشري المثبت في المنهجية.

**Retained information:** ['P761', 'Evidence_Companion: original P761 and calibration assets', '§3.10 P379; §5.7.5 P581']

**Original wording (historical):**

Routine-validation scores, model-linked calibration records and selected checkpoints were subsequently supplied in EHR_Ubuntu_Deep_Audit_Assets_20261003.zip. Separate arithmetic checks reproduced the 90 client calibrations and 270 thresholds at q = 0.98, 0.99 and 0.995 from validation scores and calculated empirical validation exceedance rates. These checks supplement the earlier saved-score audit, which was prepared with programming assistance. Those historical checks support the preserved calibration calculations and model associations. The later fresh-environment replay separately completed training and full inference (D.8); neither constitutes a blinded review by an independent researcher. Reusing routine-validation sessions for model selection and calibration remains a methodological limitation.

**Revised wording before appendix renumbering:**

Routine-validation scores, model-linked calibration records and selected checkpoints supported separate arithmetic reproduction of 90 client calibrations and 270 thresholds at q = 0.98, 0.99 and 0.995, with empirical validation exceedance rates calculated. The earlier saved-score audit was prepared with programming assistance. These checks establish preserved calculations and model associations; D.8 reports the subsequent training and full-inference replay. Reusing routine-validation sessions for both model selection and calibration remains a methodological limitation.

### P762 — REWRITE

**Source section:** D.8 Completed computational reproduction and evidence

**Reason:** يحذف كود الملاحظة الإدارية من العنوان مع بقاء مضمون إعادة الإنتاج.

**Retained information:** ['P762']

**Original wording (historical):**

D.8 Completed computational reproduction and evidence

**Revised wording before appendix renumbering:**

D.8 Computational reproduction

### P763 — REWRITE

**Source section:** D.8 Completed computational reproduction and evidence

**Reason:** الإبقاء على نتيجة إعادة الإنتاج ونطاقها؛ تاريخ التنفيذ محفوظ في السجل الخارجي ولا يمثل متغيراً في الدراسة.

**Retained information:** ['P763', 'Evidence_Companion: original P763 and run receipts']

**Original wording (historical):**

ME-06 status: COMPLETED WITH DISCLOSED METADATA EXCEPTION. The previous absence of an executed fresh-environment reconstruction has been addressed for the supplied snapshot on the same host. The run ended successfully on 11 October 2026 at 02:39:59 UTC, with zero exit codes for both training stages, final evaluation and full-precision comparison. This status concerns computational execution; independent external-host replication remains unverified.

**Revised wording before appendix renumbering:**

Fresh-environment computational reproduction completed for the supplied snapshot on the existing host. Training, final evaluation and full-precision comparison ended successfully. The reconstruction includes the scaler-metadata compatibility exception described below; it is not independent external-host replication.

### P765 — REWRITE

**Source section:** D.8 Completed computational reproduction and evidence

**Reason:** يحفظ كل نتائج المطابقة ومقاماتها وشرط الاستقلال، وينقل تفاصيل QA seals/model associations إلى المرافق.

**Retained information:** ['P765', 'Evidence_Companion: original P765 and replay QA']

**Original wording (historical):**

The comparison covered 90,270 model–test rows from repeated evaluation of 2,364 held-out and 645 known-test sessions. Initial and selected tensor states, selected rounds, validation scores, calibration values, test scores, metrics and paired-seed summaries matched exactly. Alert decisions agreed at all three fixed quantiles. Independent read-only evidence QA checked the source and campaign seals, model/evaluation associations and all comparison rows. This was evidence verification within the review workflow, not a new independent-researcher replication.

**Revised wording before appendix renumbering:**

The comparison covered 90,270 model–test score rows from repeated evaluation of 2,364 held-out and 645 known-test sessions. Initial and selected tensor states, selected rounds, validation scores, calibration values, test scores, metrics and paired-seed summaries matched exactly. Alert decisions agreed at all three fixed quantiles. These comparisons verify the replayed outputs within the review workflow, not a blinded independent-researcher replication.

### P766 — MOVE_TO_COMPANION

**Source section:** D.8 Completed computational reproduction and evidence

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Computational replay evidence index (old Table D.11) / original P766']

**Original wording (historical):**

Table D.11: Completed replay checks and their evidence

### P769 — MOVE_TO_COMPANION

**Source section:** D.8 Completed computational reproduction and evidence

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Computational replay package inventory, receipts and derivative-redaction record / original P769']

**Original wording (historical):**

ME06_Evidence.zip accompanies this report. Its README_AR.md describes the selected records, and MANIFEST.json lists payload sizes and SHA-256 identities. It includes the completion and comparison records in Table D.11, the 60-cell metric and paired-seed CSV summaries, environment/build/preparation receipts, eight high-level execution logs and the reproduction guide. One training command receipt is a labelled derivative omitting process-tree identity metadata; its original hash is retained and the full original remains in the private run directory. This evidence attachment excludes raw benchmark data, trained weights, per-session scores and secret protocol state. The complete private run inventory is retained separately.

### P770 — DELETE_REDUNDANT

**Source section:** D.8 Completed computational reproduction and evidence

**Reason:** تكرار لحدود نفس المضيف ومعرفة النتائج والاستثناء والتوقيت والحقوق؛ كل حد باقٍ في موضع تفسيره، ولا يخفي حذف الفقرة أي نتيجة سلبية.

**Retained information:** ['P763–768', '§4.10 P515', '§5.7.3 P574', '§5.7.5 P579/P581/P582', 'Evidence_Companion: original P770']

**Original wording (historical):**

The replay used the existing host and supplied fixed snapshot after the historical results were known. It supports computational reproduction under those conditions, with the stated metadata exception. It does not reconstruct the original generator or validate clinical labels, generalisation to independent hospitals, security guarantees or identical intermediate training trajectories. New timings and record-content measurements are descriptive and remain separate from the original cost tables.

### P771 — REWRITE

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** عنوان موجز؛ تبقى النتائج التاريخية والفشل والإصلاح في الفقرات التالية.

**Retained information:** ['P771']

**Original wording (historical):**

D.9 Executed bounded security validation and retained findings

**Revised wording before appendix renumbering:**

D.9 Bounded security validation

### P772 — REWRITE

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** الإبقاء على الأعداد ووحدة العد وتعريف PASS دون تكرار تاريخ تنفيذ إداري.

**Retained information:** ['P772']

**Original wording (historical):**

Historical execution status (11 October 2026): all seven named groups and all 101 selected contract records were executed. Selected status totals are 99 PASS, 1 FAIL and 1 OBSERVED_BOUNDARY; no selected case was NOT_RUN. PASS means that the case-specific contract was met. For negative fixtures it means the expected refusal was observed, while the SETUP-restart case records allowed behaviour. The 20 freshness sessions are one grouped diagnostic case, not 20 independent security experiments.

**Revised wording before appendix renumbering:**

All seven named groups and 101 selected contract records were executed: 99 PASS, 1 FAIL and 1 OBSERVED_BOUNDARY, with no selected case NOT_RUN. PASS means the case-specific contract was met: expected refusal for negative fixtures or allowed behaviour for the SETUP-restart case. The 20 freshness sessions form one grouped diagnostic case, not 20 independent security experiments.

### P773 — MOVE_TO_COMPANION

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Security acceptance contracts, seals and exact execution receipts / original P773']

**Original wording (historical):**

Acceptance and timing. The PRG/freshness contract SHA-256 is 133172442839c69da1553dc538fdb6e8dfc1bab673549e7f27391cbbd8bd5a22; protocol contract ad167328e3ebd66e191bccfe37b56a1245ef1c77a4af9016ebe2f9c45f826ea7; export contract 1a07f4601d6132c9db4dd8aa6c9c33ec81d0ed80e45a69511e85268bf5c3166b. New executions occurred on 11 October 2026 at 15:42–15:44 UTC (23:42–23:44 Asia/Singapore). Exact receipt times and script hashes are retained. These contracts preceded these tests, not the historical benchmark.

### P774 — REWRITE

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** يبقي البيئة وحد استخدام البيانات والأسرار، وينقل هاش helper وأعداد فحوص wheel/inventory إلى جرد الإيصالات.

**Retained information:** ['P774', 'Evidence_Companion: original P774 and runtime/source verification receipts']

**Original wording (historical):**

Environment and data boundary. The suite used Python 3.12.3 in the preserved Ubuntu-24.04 environment and installed Flower 1.22.0+mai.prg7570.1. The installed helper SHA-256 was 62935b91cf10f41f2036f8ccdbe65f257de86d4ada65cff7ff9fe254927c361c. A wheel/RECORD check matched 424 runtime files. Raw benchmark data and learned weights were not needed. Generated protocol secrets were compared in memory only; no secret values or digests were exported. The inventory check covered 299 sealed source/preprocessing entries and four listed runtime/build files, rather than every file on the host.

**Revised wording before appendix renumbering:**

The suite used Python 3.12.3, Ubuntu 24.04 and Flower 1.22.0+mai.prg7570.1. Public fixtures required no raw benchmark data or learned weights. Generated protocol secrets were compared only in memory; no secret values or digests were exported. Installed-code identities, wheel checks and the bounded source/runtime inventory are retained in the Evidence Companion.

### P775 — MOVE_TO_COMPANION

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Security-validation evidence inventory (old Table D.12) / original P775']

**Original wording (historical):**

Table D.12: Security-validation evidence inventory

### P778 — REWRITE

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** التفريق بين نسخة الإصلاح والنسخة الأصلية لازم علمياً؛ التاريخ الدقيق محفوظ مع الأدلة.

**Retained information:** ['P778']

**Original wording (historical):**

SV-05 remediation status (12 October 2026): FIXED WITHIN THE TESTED PROJECT BOUNDARY. The original unequal-list fixture and its FAIL records remain preserved. The repaired project copy validates lengths and the complete unique external-peer set before upstream fitting. The unchanged fixture now raises ValueError during COLLECT, with no affected-client fit, no UNMASK and no accepted aggregate. The separate production-guard malformed-list case confirms the same behaviour. The original benchmark source was not overwritten, and no evidence shows that its training contained this malformed request. The repair is a project policy guard, not a change to the cryptographic wheel.

**Revised wording before appendix renumbering:**

The separately versioned SV-05 correction validates collection-request lengths and the complete unique external-peer set before upstream fitting. The original unequal-list fixture, whose FAIL record remains preserved, now raises ValueError during COLLECT with no affected-client fit, no UNMASK and no accepted aggregate; the actual production-guard malformed-list case confirms the behaviour. The correction changes a separate project policy guard rather than the cryptographic wheel or original benchmark source. No evidence shows that the benchmark training contained this malformed request.

### P780 — REWRITE

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** صياغة أثر حدود metadata بصوت البحث، مع حفظ كل الأعداد والضوابط والنتيجة السلبية.

**Retained information:** ['P780']

**Original wording (historical):**

SV-07 metadata boundary. Nine designated output JSONs contained none of nine literal public payload canaries; the scanner positive control detected 9/9. Two separately retained artifacts contained the permitted public-metadata marker in request ID, exception class or traceback file/function fields. The result is OBSERVED_BOUNDARY, not a universal sanitization PASS. Review permitted metadata before external release, or implement a separately tested stricter metadata policy if such fields may contain sensitive content. All fixture canaries and deliberately unsafe control files in this attachment are public synthetic markers, not real EHR data or real protocol secrets.

**Revised wording before appendix renumbering:**

SV-07 metadata boundary. Nine designated output JSONs contained none of nine literal public payload canaries; the scanner positive control detected 9/9. Two separately retained artifacts contained the permitted public-metadata marker in request ID, exception class or traceback file/function fields. The result is OBSERVED_BOUNDARY, not a universal sanitization PASS. External release therefore requires review of the permitted metadata, or a stricter separately tested policy where those fields could contain sensitive content. All fixture canaries and deliberately unsafe control files in this attachment are public synthetic markers, not real EHR data or real protocol secrets.

### P781 — MOVE_TO_COMPANION

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** تفاصيل محاولة harness غير الناجحة و57/2 ثم58/1 وإيصالات 244 فحص محفوظة كاملة بالمرافق؛ الفشل العلمي المستهدف والحد الحالي باقيا في P772/P778–780 و§4.11.

**Retained information:** ['Evidence_Companion: Retained security attempts, harness correction and read-only evidence QA / original P781']

**Original wording (historical):**

Attempt retention and evidence review. The first protocol run retained 57 PASS and 2 FAIL records. A missing keep_input=True argument in the harness B-control decoder caused one of those failures; only that API call was repaired. The selected second run retained 58 PASS and the same target FAIL; both exit codes were 2. Other groups completed on their first run. A separate read-only review completed 244 artifact/contract/hash/classification checks of SV-02–SV-05 and SV-07 with no discrepancies; these were evidence checks, not additional security tests. An additional evidence check covered SV-01/SV-06 code, contracts and observed results.

### P783 — DELETE_REDUNDANT

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** جدول متابعة ME-xx إداري يعيد حدود التسمية والبحث والخصوصية/الكلفة والأخلاق؛ تبقى جميع الحقائق في مواضعها العلمية المحددة.

**Retained information:** ['P651/P657', 'P731/P733', 'Appendix D.8 P763–768', 'Appendix D.9 P776–780 and Table D.13', '§3.12 P395', '§5.7.5 P579/P580', 'Evidence_Companion: original P783']

**Original wording (historical):**

Status of the earlier missing-evidence items. For ME-10, bounded implementation validation is now executed with the historical SV-05 finding, its separately verified repair and the continuing metadata limitation; broad privacy/security assurance remains unestablished. ME-11 is unchanged: these checks do not measure isolated cryptographic time or full-wire traffic. ME-06 remains the separately documented computational replay. The present validation also does not resolve ME-02 label validity, ME-04/05 historical discovery records, external generalisation or the formal ethics status.

### P784 — MOVE_TO_COMPANION

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Security and SV-05 repair attachment inventories and repetition receipts / original P784']

**Original wording (historical):**

Security_Validation_Evidence.zip accompanies this revision. Results.csv indexes every selected case and its underlying record. Both protocol attempts, acceptance contracts, executed harnesses, stdout/stderr, receipts, selected public output artifacts, source seals and independent evidence checks are retained. MANIFEST.json provides byte sizes and SHA-256 identities. The attachment depends on the preserved project/runtime identified in the receipts; it is not a standalone redistributed EHR dataset or a fresh-environment installation certificate. Keep ME06_Evidence.zip alongside this document for the earlier reproduction link.

### P785 — MOVE_TO_COMPANION

**Source section:** D.9 Executed bounded security validation and retained findings

**Reason:** سجل إداري/توثيقي أو تاريخ مراجعة، محفوظ كاملًا في الملف المرافق بدل شغل متن الملحق العلمي.

**Retained information:** ['Evidence_Companion: Security and SV-05 repair attachment inventories and repetition receipts / original P785']

**Original wording (historical):**

SV05_Repair_Evidence.zip accompanies the 12 October repair. It contains the base and repaired source snapshots, complete patch, source manifests, retained attempts and logs, per-case results, unit-test outcomes and correction records. Receipt commands identify the retained runtime and new output directories needed for repetition. This is a source-and-evidence package, not a new installation certificate. The dated repair records retain the earlier outcomes alongside the new retest results. Open repair evidence package.

### P786 — MOVE_TO_COMPANION

**Source section:** APPENDIX E: P1 INTENT AND EXECUTED-STUDY ALIGNMENT

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P786']

**Original wording (historical):**

APPENDIX E: P1 INTENT AND EXECUTED-STUDY ALIGNMENT

### P787 — MOVE_TO_COMPANION

**Source section:** E.1 Basis and scope of the alignment

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P787']

**Original wording (historical):**

E.1 Basis and scope of the alignment

### P788 — MOVE_TO_COMPANION

**Source section:** E.1 Basis and scope of the alignment

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P788']

**Original wording (historical):**

The P1 source supplied for this revision is the 60-page proposal Privacy-Enhanced Federated Learning for EHR Access Anomaly Detection Using Secure Aggregation. Sections 1.2–1.6 establish the original motivation and formal questions. It contains Chapters 1–3, not completed results. Accordingly, this report uses P1 for intent and the accepted code and experiment records for execution. The comparison does not recreate historical approval dates.

### P789 — MOVE_TO_COMPANION

**Source section:** E.1 Basis and scope of the alignment

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P789']

**Original wording (historical):**

Sections 1.3–1.4 operationally clarify the P1 questions and fourth objective to match the comparisons and outcomes actually measured. These post-review phrasings are not retrospectively presented as the wording recorded before execution; the original wording remains in the supplied P1. The report uses British English. P1 excludes transport protection and defines A/B/C without a local-only comparison. Privacy motivates the architecture, while the questions measure detection and system-workflow outcomes. No new privacy-leakage outcome is implied.

### P790 — MOVE_TO_COMPANION

**Source section:** E.2 Proposal and implementation differences

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P790']

**Original wording (historical):**

E.2 Proposal and implementation differences

### P791 — MOVE_TO_COMPANION

**Source section:** E.2 Proposal and implementation differences

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P791']

**Original wording (historical):**

Table E.1: P1 statements and the completed experimental record

### P792 — MOVE_TO_COMPANION

**Source section:** E.2 Proposal and implementation differences

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P792']

**Original wording (historical):**

Sources: supplied P1; executed MAIN_IMPLEMENTATION.md and main_protocol_decisions.json; completion and final-evaluation records; preserved companion methods and tables. This comparison records differences, not retrospective prespecification.

### P793 — MOVE_TO_COMPANION

**Source section:** E.3 Meaning of the final protection claim

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P793']

**Original wording (historical):**

E.3 Meaning of the final protection claim

### P794 — MOVE_TO_COMPANION

**Source section:** E.3 Meaning of the final protection claim

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P794']

**Original wording (historical):**

Privacy-enhanced describes the move from raw-log pooling to client-local training and from individual plaintext contributions to masked aggregation. The inspected interface and tested numerical behaviour support that implementation under the stated assumptions. They do not establish a quantified privacy gain, detection equivalence, an acceptable operating cost or confidentiality against the shared host administrator. The utility and overhead findings answer the formal questions without concealing the detector's legitimate-exception errors.

### P795 — MOVE_TO_COMPANION

**Source section:** E.3 Meaning of the final protection claim

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P795']

**Original wording (historical):**

The later security-validation evidence supports only the named implementation observations in Section 4.11. The historical controlled-rejection failure is retained, and its separately versioned SV-05 repair passed the targeted retest. The diagnostic-metadata boundary and untested scope remain. Neither the historical suite nor the repair supports a comprehensive-protection statement, quantified privacy assurance or independent production certification.

### P796 — MOVE_TO_COMPANION

**Source section:** E.3 Meaning of the final protection claim

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P796']

**Original wording (historical):**

The 10 October 2026 revision clarified the research questions and interpretation, qualified source and provenance claims, updated selected literature, and improved artefact references and figure readability. The 11 October literature revision added a separately dated targeted search update and inspection of native exports; those searches do not authenticate every historical execution or missing export. The subsequent ME-06 replay completed fresh training, validation calibration and test inference, as documented in Sections 3.12, 4.10 and 5.7.5 and Appendix D.8. Its predictive results match the historical reference; original performance and system-cost tables remain unchanged, with new resource measurements supplied separately. This later replay is not retrospectively presented as a prespecified independent confirmation study. Earlier evidence retains its original identity.

### P797 — MOVE_TO_COMPANION

**Source section:** E.3 Meaning of the final protection claim

**Reason:** توثيق الانحرافات والتاريخ محفوظ كاملًا بالمرافق؛ المنهج النهائي في الفصل3، والإفصاح الفريد عن تعديل صياغة RQs/Objective4 باقٍ في P695؛ لا يبقى ملحق تاريخ تحرير مستقل.

**Retained information:** ['Evidence_Companion: Proposal-to-execution alignment and dated revision history (old Appendix E) / original P797']

**Original wording (historical):**

The separately dated bounded security validation was executed later on 11 October 2026, after the ME-06 replay. It adds the actual outcomes, retained unsuccessful attempt and open input-validation finding in Section 4.11 and Appendix D.9. That 11 October suite changed neither the source nor the original predictive/system-cost tables. The 12 October repair changed a separate source copy; it did not retrain the main detector or recalculate those tables. The fixed-copy results therefore support input validation, not new performance or cost estimates.

## Complete relocated tables

Table labels below are historical identifiers. Their current manuscript references explicitly identify this companion rather than implying that they remain in the thesis.

### B.1 Scopus — unnumbered historical query table — T32

| Search family | S1: Direct EHR access/audit-log threat detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | TITLE-ABS-KEY( ( "electronic health record*" OR "electronic medical record*" OR EHR OR EMR OR "health information system*" OR "clinical information system*" ) AND ( "audit log*" OR "access log*" OR "audit trail*" OR "event log*" OR "activity log*" OR "transaction log*" OR "security log*" OR "record access event*" OR "access event*" OR "audit event*" ) AND ( "anomaly detect*" OR "anomalous access" OR "inappropriate access" OR "unauthorised access" OR "unauthorized access" OR "suspicious access" OR "illegitimate access" OR "insider threat*" OR misuse OR abuse OR "policy violation*" OR "compromised account*" OR "user behaviour analytics" OR "user behavior analytics" ) ) AND PUBYEAR > 1999 AND PUBYEAR < 2027 |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 64 |
| Integrity note in source record | The supplied Scopus S1 export was inspected on 11 October 2026 and contains 64 records, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. |

### B.1 Scopus — unnumbered historical query table — T33

| Search family | S2: Direct federated EHR access/audit-log detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | TITLE-ABS-KEY( ( "electronic health record*" OR "electronic medical record*" OR EHR OR EMR ) AND ( "audit log*" OR "access log*" OR "audit trail*" OR "access event*" OR "audit event*" ) AND ( anomaly OR "anomaly detection" OR threat OR misuse OR "inappropriate access" OR "unauthorized access" OR "unauthorised access" ) AND ( "federated learning" OR "federated machine learning" OR "cross-silo federated" OR "collaborative learning" OR "decentralised learning" OR "decentralized learning" ) ) AND PUBYEAR > 2015 AND PUBYEAR < 2027 |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 4 |
| Integrity note in source record | The supplied Scopus S2 export was inspected on 11 October 2026 and contains 4 records, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. The four-record file is scopus_export_Aug 11-2026_S2.ris. The file named 2026-08-11_scopus_S2.ris.ris is byte-identical to the 117-record S4 export and must not be treated as S2. |

### B.1 Scopus — unnumbered historical query table — T34

| Search family | S3: Synthetic audit-log datasets and benchmark generation |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | TITLE-ABS-KEY( ( "electronic health record*" OR "electronic medical record*" OR EHR OR EMR ) AND ( "audit log*" OR "access log*" OR "audit trail*" OR "access event*" OR "audit event*" ) AND ( "synthetic data" OR "synthetic log*" OR simulat* OR "workflow simulation" OR benchmark* OR generator OR "FHIR AuditEvent" ) ) AND PUBYEAR > 1999 AND PUBYEAR < 2027 |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 30 |
| Integrity note in source record | The supplied Scopus S3 export was inspected on 11 October 2026 and contains 30 records, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. |

### B.1 Scopus — unnumbered historical query table — T35

| Search family | S4: Non-IID FL, heterogeneity and personalisation |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | TITLE-ABS-KEY( ( "federated learning" OR "cross-silo federated" ) AND ( anomal* OR "log anomaly detection" OR "access log*" OR "security log*" ) AND ( "non-IID" OR noniid OR heterogene* OR personalised OR personalized OR "client-specific" OR "local fine-tun*" OR "client imbalance" OR "quantity skew" OR "feature skew" OR "workflow skew" OR "temporal skew" OR "domain shift" ) AND ( healthcare OR hospital* OR EHR OR "access log*" OR "security log*" ) ) AND PUBYEAR > 2015 AND PUBYEAR < 2027 |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 117 |
| Integrity note in source record | The supplied Scopus S4 export was inspected on 11 October 2026 and contains 117 records, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. Two records share DOI 10.1201/9781003393580-102 but have different Scopus identifiers; 117 is a raw-record count, not a verified unique-study count. |

### B.2 Web of Science — unnumbered historical query table — T36

| Search family | S1: Direct EHR access/audit-log threat detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | TS=( ( "electronic health record*" OR "electronic medical record*" OR EHR OR EMR OR "health information system*" OR "clinical information system*" ) AND ( "audit log*" OR "access log*" OR "audit trail*" OR "event log*" OR "activity log*" OR "transaction log*" OR "security log*" OR "record access event*" OR "access event*" OR "audit event*" ) AND ( "anomaly detect*" OR "anomalous access" OR "inappropriate access" OR "unauthorised access" OR "unauthorized access" OR "suspicious access" OR "illegitimate access" OR "insider threat*" OR misuse OR abuse OR "policy violation*" OR "compromised account*" ) ) |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 28 |
| Integrity note in source record | The supplied Web of Science S1 export was inspected on 11 October 2026 and contains 28 records, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. |

### B.2 Web of Science — unnumbered historical query table — T37

| Search family | S2: Direct federated EHR access/audit-log detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | #1 AND TS=( "federated learning" OR "federated machine learning" OR "cross-silo federated" OR "collaborative learning" OR "decentralised learning" OR "decentralized learning" ) #1 = Web of Science S1 query shown in the preceding row. |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 1 |
| Integrity note in source record | The supplied Web of Science S2 export was inspected on 11 October 2026 and contains 1 record, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. |

### B.2 Web of Science — unnumbered historical query table — T38

| Search family | S3: Synthetic audit-log datasets and benchmark generation |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | #1 AND TS=( "synthetic data" OR "synthetic log*" OR simulat* OR benchmark* OR generator OR "FHIR AuditEvent" ) #1 = Web of Science S1 query shown in the preceding row. |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 2 |
| Integrity note in source record | The supplied Web of Science S3 export was inspected on 11 October 2026 and contains 2 records, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. |

### B.3 PubMed/MEDLINE — unnumbered historical query table — T39

| Search family | S1: Direct EHR access/audit-log threat detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | (("Electronic Health Records"[Mesh] OR "electronic health record"[tiab] OR "electronic health records"[tiab] OR EHR[tiab] OR "electronic medical record"[tiab] OR "electronic medical records"[tiab] OR EMR[tiab] OR "health information system"[tiab] OR "health information systems"[tiab]) AND ("audit log"[tiab] OR "audit logs"[tiab] OR "access log"[tiab] OR "access logs"[tiab] OR "audit trail"[tiab] OR "audit trails"[tiab] OR "event log"[tiab] OR "event logs"[tiab] OR "record access event"[tiab] OR "record access events"[tiab] OR "access event"[tiab] OR "access events"[tiab] OR "security log"[tiab] OR "security logs"[tiab]) AND ("anomaly detection"[tiab] OR "anomalous access"[tiab] OR "inappropriate access"[tiab] OR "unauthorized access"[tiab] OR "unauthorised access"[tiab] OR "suspicious access"[tiab] OR "illegitimate access"[tiab] OR "insider threat"[tiab] OR "insider threats"[tiab] OR misuse[tiab] OR abuse[tiab] OR "policy violation"[tiab] OR "policy violations"[tiab])) |
| Recorded search date | 10 August 2026 |
| Recorded raw results | 15 |
| Integrity note in source record | The received PubMed S1 CSV was inspected on 11 October 2026 and contains 10 records. The historical 15-hit total remains unverified and five records remain unreconciled. They are not screened exclusions, and no missing historical records were reconstructed. |

### B.3 PubMed/MEDLINE — unnumbered historical query table — T40

| Search family | S2: Direct federated EHR access/audit-log detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | (("Electronic Health Records"[Mesh] OR "electronic health record"[tiab] OR "electronic health records"[tiab] OR EHR[tiab] OR "electronic medical record"[tiab] OR "electronic medical records"[tiab] OR EMR[tiab] OR "health information system"[tiab] OR "health information systems"[tiab]) AND ("audit log"[tiab] OR "audit logs"[tiab] OR "access log"[tiab] OR "access logs"[tiab] OR "audit trail"[tiab] OR "audit trails"[tiab] OR "event log"[tiab] OR "event logs"[tiab] OR "record access event"[tiab] OR "record access events"[tiab] OR "access event"[tiab] OR "access events"[tiab] OR "security log"[tiab] OR "security logs"[tiab]) AND ("anomaly detection"[tiab] OR "anomalous access"[tiab] OR "inappropriate access"[tiab] OR "unauthorized access"[tiab] OR "unauthorised access"[tiab] OR "suspicious access"[tiab] OR "illegitimate access"[tiab] OR "insider threat"[tiab] OR "insider threats"[tiab] OR misuse[tiab] OR abuse[tiab] OR "policy violation"[tiab] OR "policy violations"[tiab]) AND ("federated learning"[tiab] OR "federated machine learning"[tiab] OR "cross-silo federated"[tiab] OR "collaborative learning"[tiab] OR "decentralized learning"[tiab] OR "decentralised learning"[tiab])) |
| Recorded search date | 10 August 2026 |
| Recorded raw results | 0 |
| Integrity note in source record | The historical PubMed S2 zero-result entry lacks a contemporaneous preserved response establishing the original query and settings. No export is expected for a genuine zero-result search; a later search cannot independently authenticate this historical zero. |

### B.3 PubMed/MEDLINE — unnumbered historical query table — T41

| Search family | S3: Synthetic audit-log datasets and benchmark generation |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | (("Electronic Health Records"[Mesh] OR "electronic health record"[tiab] OR "electronic health records"[tiab] OR EHR[tiab] OR "electronic medical record"[tiab] OR "electronic medical records"[tiab] OR EMR[tiab]) AND ("audit log"[tiab] OR "audit logs"[tiab] OR "access log"[tiab] OR "access logs"[tiab] OR "audit trail"[tiab] OR "audit trails"[tiab] OR "access event"[tiab] OR "access events"[tiab] OR "audit event"[tiab] OR "audit events"[tiab]) AND ("synthetic data"[tiab] OR "synthetic log"[tiab] OR "synthetic logs"[tiab] OR simulated[tiab] OR simulation[tiab] OR benchmark[tiab] OR generator[tiab] OR "FHIR AuditEvent"[tiab])) |
| Recorded search date | 10 August 2026 |
| Recorded raw results | 12 |
| Integrity note in source record | The historical PubMed S3 count of 12 results still lacks its retained native export. This evidence gap is not resolved by the 11 October 2026 refresh. |

### B.4 IEEE Xplore — unnumbered historical query table — T42

| Search family | S1: Direct EHR access/audit-log threat detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | ( ("electronic health record" OR EHR OR "electronic medical record" OR EMR) AND ("audit log" OR "access log" OR "audit trail" OR "event log" OR "access event") AND ("anomaly detection" OR "inappropriate access" OR "unauthorized access" OR "unauthorised access" OR "suspicious access" OR "insider threat" OR misuse) ) |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 17 |
| Integrity note in source record | The supplied IEEE Xplore S1 export was inspected on 11 October 2026 and contains 17 records, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. |

### B.4 IEEE Xplore — unnumbered historical query table — T43

| Search family | S2: Direct federated EHR access/audit-log detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | ( ("electronic health record" OR EHR) AND ("audit log" OR "access log" OR "audit trail" OR "access event") AND ("federated learning" OR "federated machine learning" OR "cross-silo federated") AND (anomaly OR threat OR misuse OR "access control") ) |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 5 |
| Integrity note in source record | The supplied IEEE Xplore S2 export was inspected on 11 October 2026 and contains 5 records, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. |

### B.4 IEEE Xplore — unnumbered historical query table — T44

| Search family | S3: Synthetic audit-log datasets and benchmark generation |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | ( ("electronic health record" OR EHR) AND ("audit log" OR "access log" OR "audit event") AND (synthetic OR simulation OR benchmark OR generator OR "FHIR AuditEvent") ) |
| Recorded search date | 11 August 2026 |
| Recorded raw results | 9 |
| Integrity note in source record | The supplied IEEE Xplore S3 export was inspected on 11 October 2026 and contains 9 records, matching the historical entry. This verifies the received file contents, rather than independently authenticating every original query setting, total-hit count or complete database retrieval. |

### B.5 ACM Digital Library — unnumbered historical query table — T45

| Search family | S1: Direct EHR access/audit-log threat detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | ( "electronic health record" OR EHR OR "electronic medical record" OR EMR ) AND ( "audit log" OR "access log" OR "audit trail" OR "event log" OR "access event" ) AND ( "anomaly detection" OR "inappropriate access" OR "unauthorized access" OR "unauthorised access" OR "suspicious access" OR "insider threat" OR misuse ) |
| Recorded search date | 11 August 2026 |
| Recorded received-export count | 20; database total hits unverified |
| Integrity note in source record | The supplied BibTeX export was inspected on 11 October 2026 and contains 20 records. The database total-hit count, export range and complete all-results coverage remain unverified. Proceedings-volume records are not equivalent to individual research papers. |

### B.5 ACM Digital Library — unnumbered historical query table — T46

| Search family | S2: Direct federated EHR access/audit-log detection |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | ( "electronic health record" OR EHR ) AND ( "audit log" OR "access log" OR "access event" ) AND ( "federated learning" OR "cross-silo federated" ) AND ( anomaly OR threat OR misuse ) |
| Recorded search date | 11 August 2026 |
| Recorded received-export count | 20; database total hits unverified |
| Integrity note in source record | The supplied BibTeX export was inspected on 11 October 2026 and contains 20 records. The database total-hit count, export range and complete all-results coverage remain unverified. Proceedings-volume records are not equivalent to individual research papers. |

### B.5 ACM Digital Library — unnumbered historical query table — T47

| Search family | S4: Non-IID FL, heterogeneity and personalisation |
| --- | --- |
| Recorded query or reported history expression (execution not independently authenticated) | ( "federated learning" ) AND ( "log anomaly detection" OR "security log" OR "user behavior analytics" ) AND ( "non-IID" OR heterogeneity OR personalization OR personalisation OR "local fine-tuning" ) |
| Recorded search date | 11 August 2026 |
| Recorded received-export count | 20; database total hits unverified |
| Integrity note in source record | The supplied BibTeX export was inspected on 11 October 2026 and contains 20 records. The database total-hit count, export range and complete all-results coverage remain unverified. Proceedings-volume records are not equivalent to individual research papers. |

### Table C.1: Internal evidence identifiers and reporting roles — T48

| ID | Record | Role in this report |
| --- | --- | --- |
| E1 | Stored-score arithmetic audit: EHR_FL_Final_Score_Audit_Review_v1_0.zip | Final ranking, decision, seed-level and subgroup calculations; audit code and limitations. |
| E2 | Main completion report: a4eabf5e-947f-45b5-a072-4f5c2c50bb47.zip | Thirty-model registry, calibration identities and system_cost_analysis.json. |
| E3 | Executed source: EHR_FL_Main_Experiments_Package_v1_0_3.zip; adopted Decision Closure v1.1 | Model, schema, sampling, training, selection, metric definitions, measurement and security limits. |
| E4 | Source manuscript: Privacy_Enhanced_FL_EHR_P1_Corrected_Final.docx | Research-question wording, literature and historical search record; superseded proposal settings were aligned to E3. |
| E5 | Final evaluation report: 7e7c3043-b7fe-4a9f-848d-f384f1bdd962.zip | Original sixty metric cells and evaluation status, subsequently audited using E1. |
| E6 | Ten completed main-block reports for campaign 20260909T142009Z_2ad79bf6 | Validation histories, selected checkpoints, run-level costs and accepted block coverage. |
| E7 | Final evaluation encoding_coverage.json; fixed encoding_schema.json; source CSV manifest | Coverage counts, field definitions and snapshot identity; derived class breakdown labelled post-test. |
| E8 | Main preparation public_protocol.json and sampling_audits.json | Measured public-vector errors and first-five-round sampling checks in Tables C.2–C.4. |
| E9 | Historical examiner-companion index described in Appendix D.4 | Earlier per-seed contrasts, model registry, curves and patch index; supplementary archive identities and later verification are listed separately in D.4. |

### Table C.6: Recorded milestones and limits of chronology — T53

| Recorded UTC date / identifier | Milestone and evidence | What the record does not establish |
| --- | --- | --- |
| Unknown | Original generator, first structural inspection and original split creation | No first-ever creation/access timestamp is reconstructed |
| 7 Sep 2026, 05:29:16 | Preprocessing run 20260907T052916Z_328 | Run-ID time, not proof of when structural test knowledge first arose |
| 7 Sep 2026, 17:47:18 | Isolated local PRG validation | Not a full-model deployment or independent security certification |
| 8 Sep 2026, 05:11:18 | Patched B/C deployment revalidation | Not main experiments; later full-size/timing checks remained distinct |
| 9 Sep 2026, 04:02:30 | Original main preparation v1.0.0; later A completed and B staging failed | Exact subsequent failure wall-clock not reconstructed |
| 9 Sep 2026, 06:04:09 | v1.0.1 repair preparation; fixture-import tests failed | No new main training in that preparation |
| 9 Sep 2026, 07:18:24 | v1.0.2 successor; later A complete, B round 6 followed by scope failure | Partial outputs excluded from accepted outcome selection |
| 9 Sep 2026, 14:20:09 | v1.0.3 accepted preparation; source seal and byte-identical inputs; training release dated 9 Sep | Receipt/date is not independent time attestation |
| 11 Sep 2026 (receipt date) | Final-test release after the 30-model registry; 60 evaluations subsequently recorded | Exact first-score wall-clock and unreported outside scoring not independently established |
| After final evaluation; 11 Sep revision | Separate saved-score recalculation, then descriptive source audit | Later analyses are not evidence of original prespecification |

### Table D.1: Retained research artefacts and their role — T54

| Artefact | Example / recorded location | Purpose and boundary |
| --- | --- | --- |
| Executed source | ehr-fl-secagg-study-main.zip: ehr-fl-secagg-study-main/executed/EHR_FL_Main_Experiments_Package_v1_0_3/ | Preserves the code that produced the results; historical preparation instructions are not instructions to rerun the completed campaign. |
| Frozen inputs and schedules | EHR_Frozen_Inputs_and_Preparation.zip: campaign/frozen/ | Supplied training/validation arrays, schema, scaler, five initial states and ten sampling schedules. Initial states are not trained models. Complete historical runtime job files were not supplied; their scientific configuration recipe is preserved in main_study/design.py:cell_config/stage_cell (Appendix C.6). New runtime tokens and paths are operational identifiers. |
| Selected checkpoints | EHR_Ubuntu_Deep_Audit_Assets_20261003.zip: attempts/.../checkpoints/.../selected_state.pt (pattern within its named top-level directory) | Thirty historical selected parameter states linked to the registry. The separate 11 October 2026 replay trained 30 new models and recovered their selected tensor values exactly (D.8); original learned weights were not used as training inputs. |
| Validation calibration | EHR_Ubuntu_Deep_Audit_Assets_20261003.zip: attempts/.../calibration.json (pattern within its named top-level directory) | Thirty model-linked records containing 90 client calibrations and 270 quantile thresholds, independently rederived from validation scores. |
| Validation scores | EHR_Ubuntu_Deep_Audit_Assets_20261003.zip: attempts/.../LOCAL_ONLY/selected_validation_scores.json (pattern within its named top-level directory) | Thirty score files, each covering 3,622 routine-validation sessions; calibration parameters, thresholds and empirical exceedance rates checked. Reuse for selection and calibration remains a methodological limitation. |
| Session-level scores | 01_Saved_Score_Audit_Inputs_Original.zip: scores/*_scores.csv | Sixty historical score files supported arithmetic verification. The subsequent fresh replay completed all 60 model–test inference cells and compared 90,270 score rows exactly (D.8); repeated evaluations do not create independent sessions. |
| Environment records | Patched_BC_Report_20260908T051118Z_5aa99ec3.zip: full_requirements.lock and full_wheel_inventory.json; preserved external-environment identities | Pinned historical versions and input identities. The local Flower package was subsequently rebuilt and installed in a new environment for the completed same-host replay; fresh environment and build receipts accompany D.8. |
| Run and protocol logs | 05_Accepted_Preparation_and_10_Training_Blocks.zip: preparation/ and training_blocks/ | Historical preparation, training, selection and cost records remain distinct from the new execution logs and resource measurements in D.8. Secret protocol state is not a required handover item. |
| Model registry and completion | selected_models_manifest.json; main_completion_reports/ | Links all thirty chosen models and calibrations to completed experimental cells. |
| Final metrics and audit | EHR_FL_Verification_Update_20261003.zip; EHR_FL_Verification_Update_v2_20261003.zip | The October 3 archives document arithmetic, asset and limited-inference checks. The October 11 evidence separately documents the completed fresh-environment replay; neither is a blinded independent-person review. |
| Post-experiment source handover | 24211274/ehr-fl-secagg-study; recorded commit 874c372fc8619d0d4ef556bb1d8fd456c8d0e37c | Private review handover recorded after experiments; not original development history or complete backup of Ubuntu. |

### Table D.2: Provenance of the executed eleven-table benchmark — T55

| Provenance item | Recorded position |
| --- | --- |
| Source | Supplied for the project and marked synthetic; candidate is snapshot custodian. Original creator/provider identity not independently verified. |
| Internal snapshot | full_reference_balanced; 2.0.0-full-reference_seed_01. Not a verified Kaggle release. |
| Extent | 181,805 events; 17,464 sessions; three simulated clients. |
| Original file identity | All eleven CSV identities are supplied in 04_EHR_FL_Benchmark_Release_Candidate_v1_0.zip: EHR_FL_Benchmark_Release_Candidate_v1_0/metadata/source_file_manifest.csv. |
| Public URL / DOI / version | Not available in the study record; no public-access claim established. |
| Licence / redistribution permission | Not established. Do not infer a licence from a package filename or from the earlier Kaggle source. |
| Original executable generator / provenance | Not supplied; original regeneration not demonstrated. |
| Relation to earlier Kaggle files | Verified derivation not established; treated as a distinct source. |
| What can be reproduced | Processing, fresh training, calibration and complete test inference were replayed on the authorised preserved snapshot in a new environment on the same host, with the disclosed scaler-metadata binding (D.8). Original-generator reconstruction and independent external-host replication remain unverified. |

### Table D.4: Historical companion index and supplementary review files — T57

| Historical companion path or supplementary archive/member | Contents / scope |
| --- | --- |
| tables/paired_differences_by_seed.csv | Historical 480-row long-form file not supplied. Related physical output: ehr-fl-secagg-study-main.zip: ehr-fl-secagg-study-main/results/tables/paired_contrasts.csv, containing 96 summaries with five difference_seed_* columns (480 stored differences). Historical byte identity is unverified. |
| tables/paired_contrasts.csv | Related supplied member: ehr-fl-secagg-study-main.zip: ehr-fl-secagg-study-main/results/tables/paired_contrasts.csv. There are 96 condition/test/endpoint/contrast summaries with five stored seed differences and exploratory AP intervals. Historical companion byte identity is unverified. |
| tables/worst_client_by_seed.csv | Historical 60-row minimum-client table not supplied. Related constituent client AP values occur in ehr-fl-secagg-study-main.zip: ehr-fl-secagg-study-main/results/tables/recomputed_rank_metrics.csv; that table is not a replacement table of minimum-client identities. |
| tables/recomputed_rank_metrics.csv | Related supplied member: ehr-fl-secagg-study-main.zip: ehr-fl-secagg-study-main/results/tables/recomputed_rank_metrics.csv, with 300 configuration/condition/seed/test/scope rows, AP, AUROC and denominators. Historical companion byte identity is unverified. |
| tables/recomputed_decision_metrics.csv | Related supplied member: ehr-fl-secagg-study-main.zip: ehr-fl-secagg-study-main/results/tables/recomputed_decision_metrics.csv, with 720 configuration/condition/seed/test/quantile/scope rows and TP/TN/FP/FN. Historical companion byte identity is unverified. |
| EHR_Ubuntu_Deep_Audit_Assets_20261003.zip: EHR_Ubuntu_Deep_Audit_Assets_20261003/selected_models_manifest.json | Complete 30-model registry linked to the supplied selected weights and calibrations; file and model associations checked without full retraining. |
| EHR_Ubuntu_Deep_Audit_Assets_20261003.zip: attempts/.../LOCAL_ONLY/selected_validation_scores.json and attempts/.../calibration.json (patterns within its named top-level directory) | Thirty validation-score files and thirty calibration records; 90 client calibrations and 270 thresholds rederived, with empirical exceedance rates. This does not remove selection/calibration reuse. |
| 05_Accepted_Preparation_and_10_Training_Blocks.zip: training_blocks/*_Original.zip (nested archives); A/central_history.json, B/<condition>/server/history.json and C/<condition>/server/history.json | Thirty histories with initial state 0 and rounds 1–30, giving 930 recorded entries. Selection over rounds 1–30 was checked; intermediate losses were not rederived from candidate weights. |
| EHR_Frozen_Inputs_and_Preparation.zip: campaign/frozen/development/ | Thirty training/validation arrays, encoding_schema.json, relative_time_scaler.json and linkage records; schema and frozen numerical inputs checked against the raw snapshot. |
| tables/coverage_by_*.csv | Historical coverage CSV family not supplied. Related supplied content: 02_Final_Evaluation_Original.zip: encoding_coverage.json contains test/client/field counts; it does not replace every historical partition/class coverage CSV. |
| tables/department_profiles.csv; tables/sampling_gate_results.csv | Historical department_profiles.csv and sampling_gate_results.csv not supplied. Related sampling_audits.json is retained in Main_Preparation_Report_20260909T142009Z_2ad79bf6_539fef.zip. The original/expected profiles and first-five-round diagnostic remain distinct scopes. |
| tables/interpretive_baselines.csv | Historical interpretive_baselines.csv not supplied. The report retains the stated constant-score AP/prevalence and alert-all arithmetic references; they are not fitted comparators or a newly supplied CSV. |
| tables/secagg_public_vector_results.csv; evidence/public_protocol_original.json | Historical named CSV/JSON not supplied. Related original members are Main_Preparation_Report_20260909T142009Z_2ad79bf6_539fef.zip: public_protocol.json and FullSize_BC_Report_20260908T102557Z_d05f791a.zip: public_protocol_full_weights.json. These are recorded functional/numerical checks. |
| ehr-fl-secagg-study-main.zip: preserved package validation_support/ directory specified in C.2 | Three helper sources, CHANGE_MANIFEST.json, NOTICE.md, Apache 2.0 licence and prg_validation/build.py are preserved in validation_support/. The original PRG package additionally supplies reference/helper_change.diff; the installed historical wheel payload was not supplied. Exact member identities appear in artefact_mapping.json. |
| literature/Closest_Study_Verification.md | Historical Closest_Study_Verification.md not supplied in the inspected archive set. Its historical index entry is not evidence that an original full-text verification file accompanies this revision; source-access boundaries are stated separately. |
| 04_EHR_FL_Benchmark_Release_Candidate_v1_0.zip: EHR_FL_Benchmark_Release_Candidate_v1_0/data/ and metadata/source_file_manifest.csv | Eleven raw CSV files and preserved source identities; availability and hash consistency do not establish the creator, generator, Kaggle derivation or redistribution licence. |
| tables/per_client_rank_summary.csv | Related supplied member: ehr-fl-secagg-study-main.zip: ehr-fl-secagg-study-main/results/tables/per_client_rank_summary.csv, containing 36 test/condition/configuration/client summaries across five seeds. Historical companion byte identity is unverified. |
| 05_Accepted_Preparation_and_10_Training_Blocks.zip: training_blocks/*_Original.zip (nested archives); B/main_round_costs.csv and C/main_round_costs.csv, with their main_cost_summary.json records | Preserved B/C cost records for 20 runs and 600 rounds; totals and paired summaries rechecked in EHR_FL_Verification_Update_v2_20261003.zip, without a new timing measurement. A cost and inference timing were not rechecked. |
| tables/endpoint_output_index.csv | Historical endpoint_output_index.csv not supplied. The current artefact_mapping.json instead maps inspected physical members and their scopes; it is a new revision record, not a reconstruction of that historical file. |
| ehr-fl-secagg-study-main.zip: ehr-fl-secagg-study-main/executed/EHR_FL_Main_Experiments_Package_v1_0_3/ | The 215 preserved source files match their manifest. This repository snapshot is distinguished from the historical source ZIP container and complete execution environment. |
| EHR_Ubuntu_Deep_Audit_Assets_20261003.zip: campaign_manifest.json within its named top-level directory; EHR_Frozen_Inputs_and_Preparation.zip: campaign/campaign_manifest.json | Direct inventories and hashes of supplementary payloads; not authentication of generation dates, provenance or the complete historical environment. |
| EHR_FL_Verification_Update_20261003.zip; EHR_FL_Verification_Update_v2_20261003.zip | Verification reports: analysis/deep_audit/model_asset_verification.json and analysis/deep_audit/model_asset_calibration_checks.csv; analysis/followup_audit/training/training_selection_verification.json; analysis/followup_audit/cost/cost_checks.json. Limited numerical inference, selection and recorded B/C cost checks; no full retraining or inference campaign. |

### Table D.11: Completed replay checks and their evidence — T64

| Check | Completed result | Evidence file |
| --- | --- | --- |
| Training and final evaluation | 30 runs; 60 model–test cells; all stage exits zero | ME06_Full_Execution_Status.json |
| Predictive comparison | 90,270 score rows; zero compared predictive discrepancies | ME06_Comparison_Status.json |
| Model selection | 30 selected tensor states and selected rounds match | Completion_Independent_QA.json |
| Preprocessing | 30 arrays match; disclosed diagnostic metadata binding | ME06_Metadata_Binding.json |
| Resource measurements | Nonidentical times; C byte changes −90 to +180 | ME06_System_Costs_Descriptive.csv |

### Table D.12: Security-validation evidence inventory — T65

| Scope | Attachment location | Retained evidence |
| --- | --- | --- |
| SV-01 / SV-06 | prg/ | contract.json; sealed_before_execution_attempt_01.json; execution_receipt_attempt_01.json; results_attempt_01.json; stdout/stderr; run_checks.py. |
| SV-02 to SV-05 | protocol/ | Acceptance_Contract/Seal; both attempt folders with executed scripts, receipts, logs and 59 case JSONs each; Harness_Repair_01; final report and summary. |
| SV-07 | exports/ | attempt_01 contract, receipt, logs, source seals, 13 case records, nine selected outputs, positive control and two metadata-boundary artifacts. |
| Consolidated evidence | Root of security attachment | Results.csv; Security_Validation_Summary.json; Arabic report; independent read-only evidence checks; MANIFEST.json with payload sizes and SHA-256 identities. |
| SV-05 repair and retest | SV05_Repair_Evidence.zip | Base/repaired sources; patch and manifests; runs/ receipts, executed scripts, contracts, stdout/stderr and results; Repair_Summary/Results; correction records. |

### Table E.1: P1 statements and the completed experimental record — T67

| Topic | P1 statement | Executed record and interpretation |
| --- | --- | --- |
| Research aim and comparisons | P1 §§1.2–1.6 and 3.1: client-local FL, pooled reference and SecAgg+ utility–cost evaluation. | Retained. A/B answers RQ1; B/C answers RQ2. Detection is the application workload, not a replacement research aim. |
| Data source and rights | P1 §3.2 attributes the data to a Kaggle adaptation and MIT; its provenance appendix leaves version/licence unresolved. | That derivation and licence are not established for the executed eleven-table snapshot. The report identifies the preserved files and source-history gaps (D.2). |
| Input representation | P1 §§3.3/3.5: 107 input dimensions, including 98 categorical positions. | Executed schema: 84 observed levels + 26 reserved positions = 110 categorical; +3 binary and 6 temporal = 119. The frozen model uses 119, not the provisional total. |
| Time and contextual fields | P1 describes UTC time, generator-defined schema and local summary statistics. | Elapsed times use UTC; cyclic time uses Asia/Kuala_Lumpur. Context is read from events. Shared training statistics are plaintext; historical joins and public generator semantics are not asserted. |
| Sampling and optimisation | P1 §§3.4/3.9: fixed membership, a 60/40 skew, five seeds, AdamW and 30 epochs/rounds. | Final code specifies modal-department sampling and resets optimiser state each outer unit. Non-IID changes pooled occurrences too. Equal exposure is not identical optimisation. |
| SecAgg+ setup | P1 §3.8: three shares, threshold two; numerical settings to be fixed in the pilot. | Table 3.5 records final ranges and the attributed helper backport. Every accepted stage required three clients. Numerical fixtures are not a security certification. |
| Uncertainty analysis | P1 §3.11 proposes a paired hierarchical bootstrap. | Decision Closure v1.1 adopted exploratory paired seed-level Student-t intervals (df = 4). No session/client bootstrap was reported; the uncertainty target is narrower. |
| Acceptable utility and cost | P1 asks whether additional protection can avoid unacceptable loss; 0.02 AP is provisional. | No validated non-inferiority rule or operating-cost ceiling was established. Differences and costs are reported without retrospectively certifying acceptability. |
| Event localisation | P1 §3.10 proposes comparison with affected-event annotations after session scoring. | No localisation experiment was completed. Annotations support descriptive source analysis, not a localisation-performance claim. |
| System-cost outcomes | P1 lists bytes, timing, CPU, memory and inference. | Main summaries report scoped fit/evaluation time, application content and prepared-input inference. Additional process observations are retained, but no complete comparative peak-memory, full-wire-volume or isolated-cryptographic-time result is claimed. |
| Development and tests | P1 anticipates freezing before final evaluation. | Selected models/calibrations were fixed before their final scoring. Prior structural source exposure and repairs remain disclosed in C.5; the completed tests are not described as wholly untouched. |

## Search and source-coverage boundary

Original full-source verification is not repeated by this editorial revision. Existing source-level qualifications are retained. Missing full articles remain unverified. AI-assisted screening and lack of duplicated independent human screening remain disclosed in the thesis.

## Structural comparators inspected

# Primary-source structural comparison used in this revision

These are writing and organisation comparators, not additional experimental evidence for the thesis. The consulted passages were read in the original documents. No wording was copied into the manuscript. Their choices are assessed against this study's purpose rather than treated as a universal template.

| Source and inspected location | Relevant observation | Application to this manuscript |
|---|---|---|
| Universiti Malaya FCSIT postgraduate handbook 2023/24, handbook pp. 17–18 (web pages 163–164): https://ebook.um.edu.my/fsktm/pghandbook2324/files/basic-html/page163.html and https://ebook.um.edu.my/fsktm/pghandbook2324/files/basic-html/page164.html | The guide separates the research problem and aims, relevant critical literature, procedures, analysed results, interpretation and conclusions. Chapter headings should reflect their contents. | Retain the existing six-chapter structure; move realised diagnostic findings out of Methods and remove administrative review chronology from scientific discussion. This published edition is a structural comparator, not verification of current institutional requirements. |
| McMahan et al. (2017), Algorithm 1 and §3, PDF pp. 5–6: https://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf | Algorithms, client partitions, model specifications, evaluation targets and comparisons are specified near the experiments. | Keep exact model, sampling, seed and metric definitions even when lengthy; condense file-discovery and package-update narration. Retain limitations of what the realised comparison isolates. |
| Bonawitz et al. (2017), §1.2, §6.3 and §7–7.3, PDF pp. 2, 10–12: https://acmccs.github.io/papers/p1175-bonawitzA.pdf | Security assumptions and formal claims are separated from prototype timing and communication measurements; §7.3 gives the implementation setting and exclusions affecting interpretation. | Preserve the threat model, excluded security properties, measurement boundary and failed conditions. Put protocol-test dates and hashes in the evidence record. A published protocol proof does not certify this local implementation. |
| Besharati & Chan (2023), *Evaluation of Privacy-protected Federated Learning*, Ch. 3, §§4.1–4.3 and Ch. 5 (printed pp. 11–20, 23–29; PDF pp. 21–30, 33–39): https://odr.chalmers.se/bitstreams/bf4fac18-370a-4a4e-9272-21cbf20a3def/download ; institutional record https://odr.chalmers.se/items/ba6ce7bc-1b76-4533-bccd-1b326b9cdae3 | This master's thesis compares centralised and federated implementations and protected/unprotected variants. Methods contain implementation changes and parameters; evaluation links comparisons to metrics; results discuss observed trade-offs. | Keep useful implementation deviations and reproducibility settings, with findings grouped by the two research questions. Do not adopt another thesis's overbroad claims or its unfinished experiment plan as a reporting model. |

The KTH DiVA PDF initially identified as another candidate could not be fetched. It was not used as a full-text comparator. The closest EHR-FL institutional record was discoverable, but its full text was not newly obtained for this editorial comparison. Neither is represented as newly read.
