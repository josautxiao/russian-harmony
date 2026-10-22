# 参与改进 · Contributing · Участие в проекте

## 中文

欢迎纠错、补充教材、改善翻译或提出教学指导。不会使用Git也可以提交Issue：说明要解决的问题、所在文件和最小例子即可。请勿上传整本受版权保护的教材、全文OCR或私人资料。

### 教材内容

1. 给出作者、书名、版本、年份、主题和印刷页。PDF页仅作补充，说明所用扫描件。
2. 对照[来源索引](references/source-map.md)，保留A的绪论与41主题顺序；不适合现有主题的内容放补充部分。
3. 共同规则合并，独有内容另标，真实冲突分别保留来源。不要把宽松例外改成全局许可。
4. 用自己的解释、简短必要引用和原创例子，不搬运长篇原文或整组教材谱例。记谱与OCR争议必须核对原页。
5. 同步更新`references/source-index.json`、来源表、差异表以及相关主题入口。

### 教师经验与审美指导

请分别提供：指导观点、提出者/来源、适用阶段与风格、技术判断方法、优先级、例外，以及两个可比较的原创版本。清楚标注“强制条件”“条件性建议”“个人偏好”或“尚待验证”。

建议形成独立参考文件并从技能入口链接，而不是直接改写教材共识。判断次序通常是任务的明确约束、当前教材或教师口径，再在合法选择中比较音乐效果；如果这些要求冲突，说明冲突，不静默覆盖。

### 提交前

运行 `python3 scripts/validate_repository.py`；涉及音乐规则变化时，再用实际短例检查前后连接、倾向音及原有用法。纯README翻译不需要重新OCR整本书。提交说明包括变化、出处和验证方法。新版本更新[CHANGELOG](CHANGELOG.md)。检查通过不代表已经验证全部音乐内容。

## English

Corrections, additional sources, translations and pedagogical guidance are welcome. If you do not use Git, open an Issue describing the problem, file and minimal example. Do not upload copyrighted books, full OCR transcripts or private data.

For textbook additions, provide author, title, edition, year, topic and printed pages, with scan-specific PDF positions as a supplement. Keep A's introduction and 41-topic sequence. Merge shared material, label additions and retain source-specific disagreements. Use original explanations and examples, rather than long copied passages or collections of textbook scores. Verify notation against the original page. Update the source index, crosswalk, differences and relevant entry points together.

For teacher experience or aesthetic guidance, identify whose view it is, applicable stage and style, operational criteria, priority, exceptions and contrasting original examples. Label mandatory conditions, conditional advice, personal preference and unverified proposals separately. Add a linked reference layer rather than silently replacing textbook consensus. Respect explicit exercise constraints and the requested textbook/teacher framework before comparing musical effects within acceptable choices. Explain conflicts.

Before submitting, run `python3 scripts/validate_repository.py`. Changes to musical rules also need a concrete short example and checks of neighboring connections, tendency tones and existing behavior. README translations do not require OCR of the books. Describe the change, sources and validation; update the [changelog](CHANGELOG.md) for a release. Structural checks are not comprehensive musical validation.

## Русский

Приветствуются исправления, новые источники, переводы и педагогические рекомендации. Если вы не пользуетесь Git, создайте Issue с описанием проблемы, указанием файла и минимальным примером. Не загружайте учебники, защищённые авторским правом, полные тексты OCR и личные данные.

При добавлении учебника укажите автора, название, издание, год, тему и печатные страницы; страницы конкретного PDF служат дополнением. Сохраняйте введение и 41 тему A как основную последовательность. Объединяйте общее, обозначайте дополнения и сохраняйте различия с указанием источников. Используйте собственные пояснения и примеры, а не большие фрагменты текста или подборки нотных примеров из книг. Проверяйте нотацию по оригиналу. Вместе обновляйте индекс источников, соответствие тем, различия и ссылки.

Для педагогического опыта и эстетических рекомендаций укажите автора позиции, этап обучения, стиль, критерии выбора, приоритет, исключения и сравнимые собственные примеры. Разделяйте обязательные условия, условные советы, личные предпочтения и непроверенные предложения. Добавляйте отдельный связанный справочный слой, не подменяя молча общие положения учебников. Сначала учитывайте явные ограничения задачи и выбранную систему учебника/педагога, затем сравнивайте музыкальный результат допустимых вариантов. Описывайте конфликты требований.

Перед отправкой выполните `python3 scripts/validate_repository.py`. Изменение музыкальных правил также проверяется на конкретном коротком примере: соседние соединения, разрешения и прежние способы применения. Перевод README не требует повторного OCR книг. Опишите изменение, источники и проверку; перед выпуском обновите [CHANGELOG](CHANGELOG.md). Проверка структуры не заменяет музыкальной проверки.

## 贡献许可 / Contribution license / Лицензия вклада

提交原创贡献表示你有权提供这些内容，并同意按本项目CC BY-NC 4.0非商业许可共享该贡献。不得提交未经授权的教材全文、盗版链接或私人数据。

Submit only contributions you have the right to provide and agree to share under this project's CC BY-NC 4.0 non-commercial license. Do not submit unauthorized book texts, piracy links or private data.

Предоставляйте только материалы, на которые у вас есть соответствующие права, и соглашайтесь распространять свой вклад по некоммерческой лицензии проекта CC BY-NC 4.0. Не добавляйте неразрешённые тексты книг, пиратские ссылки или личные данные.
