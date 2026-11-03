# Next 23 — Sparse Cognitive Learning Research

> **Status:** Specification baseline **v0.1.1 FROZEN** (design/documentary freeze only). **T3-A NOT RUN**. No algorithmic, biological, or compositional-generalization performance claim has been experimentally verified.

مشروع بحثي لتصميم شبكة إدراكية متناثرة تتعلم محليًا دون خوارزمية الانتشار العكسي (Backpropagation)، وتعالج التنبؤ والدليل والذاكرة السياقية والربط الديناميكي. الهدف البحثي البعيد هو إعادة تركيب العلاقات والمعرفة على مدخلات لم تُشاهد حرفيًا أثناء التدريب. **الهدف فرضية قابلة للتفنيد، وليس قدرة متحققة حاليًا.**

## ترتيب المرجعيات (Normative precedence)

1. [LLA-001 — Learning Algorithm](docs/learning/LLA-001-v0.1.1-FROZEN.md): قوانين التعلم المحلي ودورة A → F.
2. [CORE-001 — Architecture](docs/core/CORE-001-v0.1.1-FROZEN.md): مكونات وآليات تنفيذ النواة، بشرط توافقها مع LLA.
3. [T3A-001 — Experimental Contract](docs/experiments/T3A-001-v0.1.1-FROZEN.md): شروط الاختبار المعزول لسلامة الربط.
4. [Final Review](reports/reviews/NEXT23-FCR-001-FINAL-REVIEW-AND-FREEZE.md) و[Freeze Manifest](docs/governance/NEXT23-FREEZE-MANIFEST.json): حالة المرجع وبصمات النسخ.

إذا وُجد تعارض حقيقي بين الوثائق، **توقف التنفيذ وأصدر تقرير تعارض**؛ لا تختَر تفسيرًا من تلقاء نفسك. لا تتغير النسخ المجمدة إلا بمراجعة مستقلة وإصدار جديد.

## دورة التعلم الأساسية

`Prediction → Observation → Error & Contrast → Evidence & Learning Opportunity → Local Learning → Contextual Authority → Prediction`

- الدليل الرصدي `E+`/`E-` منفصل عن المنفعة `V` والتعديل `q`.
- النجاح التنبؤي اللاحق لخلية خفية لا يصبح تلقائيًا حقيقة رصدية.
- درجات الفروع ليست احتمالات معايرة تلقائيًا.
- استنتاجات `Inferred` لا تُرقّى إلى `Observed` بمجرد إنتاجها داخليًا.
- الروابط المؤقتة تحافظ على **هوية الكيان** منفصلة عن **سماته**.

## حدود T3-A

T3-A يختبر **Binding Integrity**: فتحات الأدوار الخاصة بمثيل العلاقة، رموز الكيانات المؤقتة، قنوات الربط المنضبطة، `Probe/Echo`، `Query-Scoped Competition`، تحرير الموارد، ومنع التسرب. الأدوار والكيانات والعلاقات التجريبية معطاة في تجهيز الاختبار. **لا يثبت T3-A تعلم القواعد أو القدرة على التعميم التركيبي أو نجاح الخوارزمية كاملة.**

المخرجات الأساسية قبل أي ادعاء قبول: نتائج `T3A-01..T3A-10`، اختبارات كسر عدائية، أثر انتقال إشارات حقيقي، تقرير بوابات قبول، وتنفيذ قابل لإعادة التشغيل. `T3-B` مرحلة منفصلة لاكتشاف القواعد محليًا.

## هيكل المستودع

```text
docs/
  learning/       LLA-001 frozen specification
  core/           CORE-001 frozen specification
  experiments/    T3A-001 frozen experiment contract
  governance/     freeze manifest
  history/        original v0.1.0 drafts (archival)
contracts/        agent delegation contracts
reports/reviews/  final consolidated review
scripts/          specification integrity verification
.github/workflows/ frozen specification integrity checks
AGENTS.md         constraints for coding agents
```

## سياسة العمل

- `main`: مرجع مستقر للمواصفات المجمدة والتنفيذ المقبول فقط؛ لا دمج مباشر لتجارب غير مُراجعة.
- `experiment/t3a-01-binding-integrity`: فرع T3-A المعزول (تبدأ فيه التجربة فقط بعد التفويض).
- يجب أن يكون كل تغيير في القانون أو المواصفة عبر طلب مراجعة ونسخة جديدة؛ أبقِ الملفات المجمدة الأصلية سليمة.
- لا يملك وكيل البرمجة صلاحية إعلان `PASS` دون أدلة، أو تعديل المصدر المرجعي لتبرير الكود.
- راجع [AGENTS.md](AGENTS.md) و[عقد التفويض لـT3-A](contracts/T3A-AGENT-DELEGATION-001.md) قبل البدء.

## التحقق من سلامة المرجع

```bash
python scripts/verify_freeze.py
```

هذا فحص بصمات وثائقية فقط؛ **ليس اختبارًا لخوارزمية التعلم**.

## الترخيص والمساهمات

لم يُعتمد ترخيص مفتوح المصدر بعد. ظهور المستودع عامًا لا يمنح تلقائيًا ترخيصًا لإعادة توزيع محتوياته. أي سياسة ترخيص أو تعاون تُقرر لاحقًا.
