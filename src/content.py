# -*- coding: utf-8 -*-
"""
Seema · سيمة — site content, English and Arabic.

Every user-facing string lives here. Each entry is a dict {"en": ..., "ar": ...}.
Arabic is written, not translated (brand book p.24). Edit copy here, then run build.py.

PLACEHOLDERS: projects in PROJECTS are clearly marked placeholders. Replace them with
real, client-approved case studies. Never publish invented clients, results or quotes.
"""

def L(en, ar):
    return {"en": en, "ar": ar}

SITE = {
    "domain": "https://seema.qa",
    "email": "hello@seema.qa",
    "web": "seema.qa",
    "city": L("Doha, Qatar", "الدوحة، قطر"),
    "registered": L("Seema for Consultations, Digital Services and Website Design",
                    "سيمة للاستشارات والخدمات الرقمية وتصميم المواقع الإلكترونية"),
    "tagline": L("The mark that makes the difference.", "العلامة التي تصنع الفرق"),
    "founded": "2026",
}

UI = {
    "skip": L("Skip to content", "انتقل إلى المحتوى"),
    "menu": L("Menu", "القائمة"),
    "close": L("Close menu", "إغلاق القائمة"),
    "start": L("Start a project", "ابدأ مشروعك"),
    "lang_other": L("عربي", "English"),
    "lang_label": L("اقرأ هذه الصفحة بالعربية", "Read this page in English"),
    "copy": L("Copy", "نسخ"),
    "copied": L("Copied", "تم النسخ"),
    "placeholder": L("Placeholder", "مثال توضيحي"),
    "read": L("Read", "اقرأ"),
    "min": L("min read", "دقائق قراءة"),
    "soon": L("In preparation", "قيد الإعداد"),
    "all": L("All", "الكل"),
    "view_case": L("View the case study", "اطّلع على دراسة الحالة"),
    "all_work": L("All work", "كل الأعمال"),
    "all_insights": L("All insights", "كل المقالات"),
    "services_link": L("Explore the service", "تعرّف على الخدمة"),
    "home_title_suffix": L("Seema · سيمة", "سيمة · Seema"),
}

NAV = [
    ("home", L("Home", "الرئيسية")),
    ("about", L("About", "من نحن")),
    ("services", L("Services", "خدماتنا")),
    ("work", L("Work", "أعمالنا")),
    ("insights", L("Insights", "رؤى")),
    ("contact", L("Contact", "تواصل معنا")),
]

FOOTER = {
    "studio": L("Studio", "الاستوديو"),
    "services": L("Services", "الخدمات"),
    "contact": L("Contact", "التواصل"),
    "rights": L("© 2026 Seema. All rights reserved.", "© ٢٠٢٦ سيمة. جميع الحقوق محفوظة."),
    "photo": L("Photography: interim images, graded to the Seema palette. To be replaced with commissioned work.",
               "الصور: صور مؤقتة معالجة بألوان سيمة، وستُستبدل بصور خاصة بنا."),
}

# ---------------------------------------------------------------- services
# Names, outcome lines and scopes come from the brand book (pp.08–09).
SERVICES = [
    {
        "id": "consultations", "icon": "01_consulting", "group": "practice",
        "photo": "sv-consult", "peek": "sv-consult", "photo2": "sv-msheireb-office",
        "name": L("Consultations", "الاستشارات"),
        "outcome": L("Know what you stand for.", "اعرف ما الذي تمثّله."),
        "scope": L(["Brand strategy", "Positioning", "Naming", "Messaging", "Digital strategy"],
                   ["استراتيجية العلامة", "التموضع", "التسمية", "الرسائل", "الاستراتيجية الرقمية"]),
        "value": L("Before anything is designed, we find the point: the one idea that sets you apart and that your team can use to make decisions. We interview, research the market and test positions until the difference is clear enough to write down in a sentence.",
                   "قبل أن نصمّم أي شيء، نبحث عن النقطة: الفكرة الواحدة التي تميّزك، والتي يستطيع فريقك أن يستند إليها في قراراته. نحاور ونبحث في السوق ونختبر الخيارات، حتى يصبح الفرق واضحاً بما يكفي لنكتبه في جملة واحدة."),
        "results": L(["A positioning your leadership agrees on", "A name and messaging that work in Arabic and English", "A digital roadmap tied to business goals", "Clear rules on what to say, and what to stop saying"],
                     ["تموضع تتفق عليه القيادة", "اسم ورسائل تعمل بالعربية والإنجليزية معاً", "خارطة طريق رقمية مرتبطة بأهداف العمل", "قواعد واضحة لما تقوله، ولما تتوقف عن قوله"]),
    },
    {
        "id": "branding", "icon": "13_branding", "group": "practice",
        "photo": "sv-brand", "peek": "sv-brand", "photo2": "svc-pattern",
        "name": L("Branding", "الهوية التجارية"),
        "outcome": L("Give it a form no one can confuse.", "امنحها شكلاً لا يلتبس على أحد."),
        "scope": L(["Visual identity", "Brand guidelines", "Content design", "Social design"],
                   ["الهوية البصرية", "دليل الهوية", "تصميم المحتوى", "تصميم منصات التواصل"]),
        "value": L("We turn strategy into a complete identity system: the mark, typography in both scripts, colour, photography and the rules that keep it consistent as you grow. Arabic and Latin are designed together from the first sketch.",
                   "نحوّل الاستراتيجية إلى نظام هوية متكامل: الشعار، والخطوط بالعربية واللاتينية، والألوان، وأسلوب التصوير، والقواعد التي تحفظ اتساقها مع نموّك. نرسم الحرف العربي واللاتيني معاً منذ المسودة الأولى."),
        "results": L(["Recognition at every touchpoint", "A bilingual system your team can apply without us", "Consistency across agencies and suppliers", "A brand built to hold its value for years"],
                     ["حضور يُعرف في كل نقطة تواصل", "نظام ثنائي اللغة يطبّقه فريقك دون الحاجة إلينا", "اتساق بين كل الوكالات والموردين", "علامة مبنية لتحتفظ بقيمتها سنوات"]),
    },
    {
        "id": "websites", "icon": "04_websites", "group": "practice",
        "photo": "sv-web", "peek": "sv-web", "photo2": "sv-library",
        "name": L("Website Development", "تطوير المواقع الإلكترونية"),
        "outcome": L("Make it real where people meet you.", "اجعلها حقيقة حيث يلتقي بك الناس."),
        "scope": L(["UX and UI design", "Website development", "Landing pages", "Launch"],
                   ["تصميم تجربة المستخدم والواجهات", "تطوير المواقع", "صفحات الهبوط", "الإطلاق"]),
        "value": L("Your website is often the first proof of who you are. We design and build fast, accessible sites where Arabic is laid out right to left with its own rhythm, not mirrored from the English as an afterthought.",
                   "كثيراً ما يكون موقعك الإلكتروني أول دليل على هويتك. نصمّم ونبني مواقع سريعة وسهلة الوصول، تُكتب فيها العربية من اليمين إلى اليسار بإيقاعها الخاص، لا كنسخة معكوسة عن الإنجليزية."),
        "results": L(["A site that explains you in seconds", "More qualified enquiries", "Right-to-left Arabic with the same care as English", "A platform your team can update"],
                     ["موقع يعرّف بك في ثوانٍ", "استفسارات أكثر جدّية", "عربية من اليمين إلى اليسار بعناية الإنجليزية نفسها", "منصة يستطيع فريقك تحديثها"]),
    },
    {
        "id": "mobile", "icon": "05_mobile", "group": "service",
        "photo": "sv-mobile", "peek": "sv-mobile", "photo2": "svc-abaya-phone",
        "name": L("Mobile Applications", "تطبيقات الجوال"),
        "outcome": L("Put your service in their pocket.", "ضع خدمتك في جيوب عملائك."),
        "scope": L(["iOS apps", "Android apps", "App design", "Store launch"],
                   ["تطبيقات iOS", "تطبيقات Android", "تصميم التطبيقات", "النشر في المتاجر"]),
        "value": L("We design and build apps for iOS and Android, from the first user journey to store approval and the releases that follow. Every screen is planned in both languages from the start.",
                   "نصمّم ونطوّر تطبيقات iOS وAndroid، من أول رحلة للمستخدم حتى اعتماد المتجر والإصدارات التي تليه. نخطّط كل شاشة باللغتين منذ البداية."),
        "results": L(["Services customers can use anywhere", "Fewer calls and manual requests", "Store-ready apps in Arabic and English", "A release plan for after launch"],
                     ["خدمات يستخدمها عملاؤك أينما كانوا", "مكالمات وطلبات يدوية أقل", "تطبيقات جاهزة للمتاجر بالعربية والإنجليزية", "خطة إصدارات لما بعد الإطلاق"]),
    },
    {
        "id": "business-apps", "icon": "02_strategy", "group": "service",
        "photo": "sv-systems", "peek": "sv-systems", "photo2": "svc-msheireb",
        "name": L("Business Applications", "تطبيقات الأعمال"),
        "outcome": L("Run the business on one system.", "أدِر أعمالك من نظام واحد."),
        "scope": L(["ERP", "CRM", "Workflow automation", "Integrations"],
                   ["تخطيط موارد المؤسسة ERP", "إدارة علاقات العملاء CRM", "أتمتة سير العمل", "ربط الأنظمة"]),
        "value": L("We implement and connect the systems that run your operations, so information is entered once and flows to everyone who needs it. We start with the process, then choose and configure the technology.",
                   "ننفّذ الأنظمة التي تدير عملياتك ونربطها ببعضها، لتُدخل المعلومة مرة واحدة وتصل إلى كل من يحتاجها. نبدأ بالإجراءات، ثم نختار التقنية ونهيّئها."),
        "results": L(["One source of truth for customers, finance and operations", "Automated approvals and routine tasks", "Connected tools instead of separate spreadsheets", "Reports leadership can trust"],
                     ["مرجع واحد موثوق للعملاء والمالية والعمليات", "موافقات ومهام روتينية مؤتمتة", "أدوات مترابطة بدل جداول متفرقة", "تقارير تثق بها القيادة"]),
    },
    {
        "id": "marketing", "icon": "11_reach", "group": "service",
        "photo": "sv-marketing", "peek": "sv-marketing", "photo2": "svc-souq-stall",
        "name": L("Digital Marketing", "التسويق الرقمي"),
        "outcome": L("Reach the people who matter.", "اوصل إلى من يهمّك الوصول إليهم."),
        "scope": L(["Social media", "SEO", "Paid campaigns", "Reporting"],
                   ["منصات التواصل", "تحسين محركات البحث", "الحملات المدفوعة", "التقارير"]),
        "value": L("We plan and run campaigns that sound like your brand in both languages, and we report on what moved the business, not only on what collected likes.",
                   "نخطّط الحملات وندير تنفيذها بصوت علامتك باللغتين، ونرفع تقارير عمّا حرّك أعمالك فعلاً، لا عن الإعجابات وحدها."),
        "results": L(["Visibility with the audiences that buy", "Consistent bilingual content", "Search presence in Arabic and English", "Clear monthly reporting"],
                     ["حضور لدى الجمهور الذي يشتري", "محتوى ثنائي اللغة متّسق", "ظهور في البحث بالعربية والإنجليزية", "تقارير شهرية واضحة"]),
    },
    {
        "id": "support", "icon": "10_trust", "group": "service",
        "photo": "sv-support", "peek": "sv-support", "photo2": "svc-souq-lamps",
        "name": L("IT Help Desk & Support", "الدعم الفني"),
        "outcome": L("Keep everything running.", "حافظ على استمرارية كل شيء."),
        "scope": L(["Help desk", "Maintenance", "Monitoring", "User support"],
                   ["مكتب المساعدة", "الصيانة", "المراقبة", "دعم المستخدمين"]),
        "value": L("Once it is live, we look after it: a responsive help desk, monitoring and scheduled maintenance for the systems and sites your people rely on every day.",
                   "بعد الإطلاق نتولّى الرعاية: مكتب مساعدة سريع الاستجابة، ومراقبة وصيانة دورية للأنظمة والمواقع التي يعتمد عليها فريقك كل يوم."),
        "results": L(["Less downtime", "Faster answers for your staff", "Systems kept updated and secure", "One partner accountable from build to support"],
                     ["توقّف أقل", "إجابات أسرع لموظفيك", "أنظمة محدّثة وآمنة", "شريك واحد مسؤول من التنفيذ حتى الدعم"]),
    },
]

# ---------------------------------------------------------------- process
PROCESS = [
    (L("Listen", "نصغي"), L("Interviews with leadership, customers and staff. We learn the business before we form a view.",
                            "مقابلات مع القيادة والعملاء والفريق. نفهم العمل قبل أن نكوّن رأياً.")),
    (L("Find the point", "نجد النقطة"), L("We name the one difference worth owning and agree it with you in writing.",
                                          "نحدّد الفرق الوحيد الذي يستحق أن تمتلكه، ونتفق عليه معك كتابةً.")),
    (L("Give it form", "نمنحها شكلاً"), L("Identity, website, app or system: we design the expression and test it with real users.",
                                          "هوية أو موقع أو تطبيق أو نظام: نصمّم التعبير عنها ونختبره مع مستخدمين حقيقيين.")),
    (L("Launch and look after it", "نطلق ونرعى"), L("We launch, measure and support, so the mark keeps its meaning after we hand over.",
                                                   "نطلق ونقيس وندعم، لتبقى العلامة محتفظة بمعناها بعد التسليم.")),
]

# ---------------------------------------------------------------- about
PRINCIPLES = [
    (L("Senior attention", "خبرة حاضرة"), L("The people who win your trust are the people who do the work. No hand-offs to a junior team after the pitch.",
                                            "من يكسب ثقتك هو من ينجز العمل. لا نسلّم مشروعك لفريق مبتدئ بعد الاجتماع الأول.")),
    (L("Arabic and English, as equals", "العربية والإنجليزية بالقدر نفسه"), L("Every word, layout and interface is written and designed in both languages from the first draft.",
                                            "كل كلمة وكل تصميم وكل واجهة نكتبها ونصمّمها باللغتين منذ المسودة الأولى.")),
    (L("One accountable partner", "شريك واحد مسؤول"), L("Strategy, identity, technology and support under one roof, so nothing is lost between suppliers.",
                                            "الاستراتيجية والهوية والتقنية والدعم تحت سقف واحد، فلا يضيع شيء بين الموردين.")),
    (L("Built to last", "صُنع ليبقى"), L("We design for the long term: systems your team can run, brands that hold their value for years.",
                                            "نصمّم للمدى الطويل: أنظمة يديرها فريقك، وعلامات تحتفظ بقيمتها سنوات.")),
]

AUDIENCE = [
    (L("Founders", "المؤسسون"), L("Building a company that should look established from its first day.", "يبنون شركة يجب أن تبدو راسخة منذ يومها الأول.")),
    (L("Family businesses", "الشركات العائلية"), L("Preparing a respected name for its next generation.", "يهيّئون اسماً محترماً لجيله القادم.")),
    (L("Established companies", "الشركات القائمة"), L("Repositioning, modernising or bringing scattered systems together.", "تعيد تموضعها، أو تحدّث أدواتها، أو تجمع أنظمتها المتفرقة.")),
    (L("Public sector", "القطاع العام"), L("Communicating clearly with citizens, residents and partners in both languages.", "تتواصل بوضوح مع المواطنين والمقيمين والشركاء باللغتين.")),
]

# ---------------------------------------------------------------- work (PLACEHOLDERS)
# Each entry renders a listing on work.html and its own page from the case-study template.
PROJECTS = [
    {
        "slug": "hospitality-group", "tags": ["branding", "web"],
        "cover": "cs-majlis-coffee", "gallery": ["cs-dallah-set", "cs-qahwa", "cs-courtyard"],
        "title": L("A hospitality group, built around the ritual of welcome", "مجموعة ضيافة تُبنى حول طقس الترحيب"),
        "client": L("Hospitality group (placeholder)", "مجموعة ضيافة (مثال)"),
        "sector": L("Hospitality", "الضيافة"),
        "services": L("Brand strategy, identity, website", "الاستراتيجية، الهوية، الموقع"),
        "year": L("To be confirmed", "يُحدَّد لاحقاً"),
        "place": L("Doha, Qatar", "الدوحة، قطر"),
        "challenge": L("A growing group of cafés and venues had expanded faster than its brand. Each venue looked different, and guests could not tell they belonged to one family.",
                       "مجموعة مقاهٍ ومواقع ضيافة نمت أسرع من علامتها. بدا كل موقع مختلفاً عن الآخر، ولم يدرك الضيوف أنها تنتمي إلى عائلة واحدة."),
        "point": L("Hospitality is a ritual, not a menu.", "الضيافة طقس، لا قائمة طعام."),
        "approach": L(["Guest and staff interviews across venues", "A single brand idea built on the ritual of welcome", "An identity system flexible enough for every venue"],
                      ["مقابلات مع الضيوف والفريق في كل المواقع", "فكرة واحدة للعلامة تقوم على طقس الترحيب", "نظام هوية مرن يتّسع لكل المواقع"]),
        "solution": L("A master brand with a shared signature, a bilingual type system and a website that presents every venue under one roof.",
                      "علامة رئيسية بتوقيع مشترك، ونظام خطوط ثنائي اللغة، وموقع إلكتروني يجمع كل المواقع تحت سقف واحد."),
        "measures": L(["Guest recognition across venues", "Direct bookings through the website", "Time to open a new venue on brand"],
                      ["تعرّف الضيوف على العلامة في كل المواقع", "الحجوزات المباشرة عبر الموقع", "الوقت اللازم لافتتاح موقع جديد وفق الهوية"]),
    },
    {
        "slug": "clinic-network", "tags": ["strategy", "web", "apps"],
        "cover": "cs-courtyard-water", "gallery": ["svc-abaya-phone", "cs-courtyard", "qa-mia-arches"],
        "title": L("A clinic network that patients can reach in two taps", "شبكة عيادات يصل إليها المريض بلمستين"),
        "client": L("Healthcare provider (placeholder)", "مقدّم رعاية صحية (مثال)"),
        "sector": L("Healthcare", "الرعاية الصحية"),
        "services": L("Digital strategy, website, mobile app", "الاستراتيجية الرقمية، الموقع، تطبيق الجوال"),
        "year": L("To be confirmed", "يُحدَّد لاحقاً"),
        "place": L("Qatar", "قطر"),
        "challenge": L("Booking an appointment meant a phone call during working hours. Patients waited on hold, and front-desk teams spent their day answering the same questions.",
                       "كان حجز الموعد يعني اتصالاً هاتفياً في أوقات الدوام. ينتظر المرضى على الخط، ويقضي فريق الاستقبال يومه في الإجابة عن الأسئلة نفسها."),
        "point": L("Care begins before the visit.", "الرعاية تبدأ قبل الزيارة."),
        "approach": L(["Mapping every patient question to a digital answer", "Designing booking, reminders and results in both languages", "Connecting the app to the clinic’s existing systems"],
                      ["ربط كل سؤال للمريض بإجابة رقمية", "تصميم الحجز والتذكير والنتائج باللغتين", "ربط التطبيق بأنظمة العيادة القائمة"]),
        "solution": L("A bilingual website and a mobile app for booking, reminders and follow-up, designed around the questions patients actually ask.",
                      "موقع إلكتروني وتطبيق جوال ثنائيا اللغة للحجز والتذكير والمتابعة، صُمّما حول الأسئلة التي يطرحها المرضى فعلاً."),
        "measures": L(["Share of bookings made online", "Calls to the front desk", "Missed appointments"],
                      ["نسبة الحجوزات الإلكترونية", "عدد المكالمات إلى الاستقبال", "المواعيد الفائتة"]),
    },
    {
        "slug": "trading-house", "tags": ["systems", "support"],
        "cover": "cs-dhows-fanar", "gallery": ["cs-spreadsheet", "cs-dhows-line", "svc-msheireb"],
        "title": L("A family trading house, moved from spreadsheets to one system", "بيت تجاري عائلي ينتقل من الجداول إلى نظام واحد"),
        "client": L("Trading company (placeholder)", "شركة تجارية (مثال)"),
        "sector": L("Trade and distribution", "التجارة والتوزيع"),
        "services": L("ERP, CRM, integrations, IT support", "ERP، CRM، ربط الأنظمة، الدعم الفني"),
        "year": L("To be confirmed", "يُحدَّد لاحقاً"),
        "place": L("Doha, Qatar", "الدوحة، قطر"),
        "challenge": L("Stock, orders and invoices lived in separate spreadsheets kept by different people. Month-end took weeks, and no one trusted a single number.",
                       "كانت المخزونات والطلبات والفواتير موزّعة على جداول منفصلة يديرها أشخاص مختلفون. استغرق إقفال الشهر أسابيع، ولم يثق أحد برقم واحد."),
        "point": L("One number everyone believes.", "رقم واحد يصدّقه الجميع."),
        "approach": L(["Documenting how work really flows today", "Choosing and configuring ERP and CRM around that flow", "Training, migration and ongoing support"],
                      ["توثيق كيف يسير العمل فعلاً اليوم", "اختيار نظامي ERP وCRM وتهيئتهما وفق هذا المسار", "التدريب ونقل البيانات والدعم المستمر"]),
        "solution": L("A connected ERP and CRM with automated approvals, one dashboard for leadership and a help desk for the team.",
                      "نظاما ERP وCRM مترابطان مع موافقات مؤتمتة، ولوحة متابعة واحدة للقيادة، ومكتب مساعدة للفريق."),
        "measures": L(["Days to close the month", "Manual data entry", "Support response time"],
                      ["أيام إقفال الشهر", "حجم الإدخال اليدوي للبيانات", "زمن الاستجابة للدعم"]),
    },
    {
        "slug": "cultural-initiative", "tags": ["branding", "marketing"],
        "cover": "cs-calligraphy", "gallery": ["qa-katara-towers", "cs-mia-night", "svc-pattern"],
        "title": L("A cultural initiative that speaks to a new generation", "مبادرة ثقافية تخاطب جيلاً جديداً"),
        "client": L("Cultural programme (placeholder)", "برنامج ثقافي (مثال)"),
        "sector": L("Culture and heritage", "الثقافة والتراث"),
        "services": L("Identity, content, social campaigns", "الهوية، المحتوى، حملات التواصل"),
        "year": L("To be confirmed", "يُحدَّد لاحقاً"),
        "place": L("GCC", "الخليج"),
        "challenge": L("A programme celebrating Arabic script had strong content but reached mostly the audience it already had.",
                       "برنامج يحتفي بالخط العربي يملك محتوى قوياً، لكنه لم يصل إلا إلى جمهوره المعتاد."),
        "point": L("Heritage, handled as something alive.", "تراث نتعامل معه ككائن حي."),
        "approach": L(["Research with younger audiences in Arabic and English", "An identity that lets the script lead", "A content calendar built for social platforms"],
                      ["بحث مع جمهور أصغر سناً بالعربية والإنجليزية", "هوية تترك للخط أن يقود", "خطة محتوى مصممة لمنصات التواصل"]),
        "solution": L("A new identity, a set of social templates and a campaign that invites people to write, not only to watch.",
                      "هوية جديدة، ومجموعة قوالب لمنصات التواصل، وحملة تدعو الناس إلى الكتابة لا إلى المشاهدة فقط."),
        "measures": L(["Reach among new audiences", "Participation in the campaign", "Growth in programme sign-ups"],
                      ["الوصول إلى جمهور جديد", "المشاركة في الحملة", "نمو التسجيل في البرنامج"]),
    },
]

WORK_FILTERS = [
    ("all", UI["all"]),
    ("strategy", L("Strategy", "الاستراتيجية")),
    ("branding", L("Branding", "الهوية")),
    ("web", L("Web", "المواقع")),
    ("apps", L("Apps", "التطبيقات")),
    ("systems", L("Business systems", "أنظمة الأعمال")),
    ("marketing", L("Marketing", "التسويق")),
    ("support", L("Support", "الدعم")),
]

# ---------------------------------------------------------------- insights
TOPICS = [
    ("all", UI["all"]),
    ("brand", L("Brand strategy", "استراتيجية العلامة")),
    ("transformation", L("Digital transformation", "التحوّل الرقمي")),
    ("web", L("Website design", "تصميم المواقع")),
    ("tech", L("Business technology", "تقنية الأعمال")),
    ("advice", L("Practical advice", "نصائح عملية")),
]

ARTICLES = [
    {
        "slug": "three-questions-before-your-website", "topic": "advice", "photo": "ink-pen-minimal", "minutes": 6,
        "date": L("September 2026", "سبتمبر ٢٠٢٦"),
        "title": L("Three questions to answer before you design your website", "ثلاثة أسئلة أجب عنها قبل أن تصمّم موقعك"),
        "dek": L("Most website projects go wrong before the first screen is drawn. These three questions prevent it.",
                 "معظم مشاريع المواقع تتعثّر قبل رسم الشاشة الأولى. هذه الأسئلة الثلاثة تحول دون ذلك."),
        "body": {
            "en": """
<p>A new website is one of the most visible things a business does, and one of the easiest to get wrong. The problems rarely start with design or code. They start earlier, when a team begins choosing colours and templates before it has agreed what the site is for.</p>
<p>Before we draw a single screen, we ask every client the same three questions. They take an afternoon to answer. They save months.</p>
<h2><span class="n">01</span>Who is the one visitor that matters most?</h2>
<p>Every website has many audiences: customers, partners, job seekers, investors, government. Trying to serve them all equally produces a homepage that serves none of them. Choose the visitor whose decision matters most to the business this year, and design the first screen for them.</p>
<p>That choice does not exclude everyone else. It gives the page an order. The others still find what they need, one level down.</p>
<blockquote>A homepage that speaks to everyone is heard by no one.</blockquote>
<h2><span class="n">02</span>What should they do next?</h2>
<p>Write down the single action you want that visitor to take: book a call, request a quote, download the app, apply. If you cannot name it, the site will not know what to ask for, and visitors will leave without doing anything.</p>
<p>Once the action is clear, every page can lead towards it. Content that does not help the visitor reach that step is a candidate for removal.</p>
<h2><span class="n">03</span>What is the one thing they should remember?</h2>
<p>This is the point: the difference that makes you, you. It should fit in one sentence, and a visitor should be able to repeat it after thirty seconds on the site. If your leadership team gives five different answers, the website will say all five, and visitors will remember none.</p>
<div class="callout"><strong>In both languages</strong>For businesses in Qatar and the Gulf, answer each question in Arabic and in English. If the answer sounds natural in only one language, it is not finished yet.</div>
<h2><span class="n">After</span>Then design</h2>
<p>With these three answers written down, design decisions become easier and faster. The team is no longer debating taste. It is asking whether a page helps the right visitor take the right step and remember the right thing.</p>
<p>That is what we mean by define, don’t decorate.</p>
""",
            "ar": """
<p>الموقع الإلكتروني الجديد من أكثر ما تقوم به الشركة ظهوراً، ومن أسهل ما يمكن أن يخطئ فيه فريق العمل. ونادراً ما تبدأ المشكلات من التصميم أو البرمجة، بل قبل ذلك بكثير، حين يبدأ الفريق باختيار الألوان والقوالب قبل أن يتفق على الغاية من الموقع.</p>
<p>قبل أن نرسم أي شاشة، نطرح على كل عميل الأسئلة الثلاثة نفسها. تستغرق الإجابة عنها بعد ظهر واحد، وتوفّر شهوراً من العمل.</p>
<h2><span class="n">٠١</span>من الزائر الأهم؟</h2>
<p>لكل موقع جماهير متعددة: عملاء وشركاء وباحثون عن عمل ومستثمرون وجهات حكومية. ومحاولة خدمتهم جميعاً بالقدر نفسه تنتج صفحة رئيسية لا تخدم أحداً. اختر الزائر الذي يهمّ قراره أعمالك أكثر من غيره هذا العام، وصمّم الشاشة الأولى له.</p>
<p>هذا الاختيار لا يُقصي الآخرين، بل يمنح الصفحة ترتيباً. سيجد الآخرون ما يحتاجونه في المستوى التالي.</p>
<blockquote>الصفحة التي تخاطب الجميع لا يسمعها أحد.</blockquote>
<h2><span class="n">٠٢</span>ما الخطوة التالية التي تريدها منه؟</h2>
<p>اكتب الإجراء الوحيد الذي تريد من هذا الزائر أن يتخذه: أن يحجز مكالمة، أو يطلب عرض سعر، أو ينزّل التطبيق، أو يقدّم طلباً. إن لم تستطع تسميته، فلن يعرف الموقع ما يطلبه، وسيغادر الزوار دون أن يفعلوا شيئاً.</p>
<p>حين يتضح الإجراء، تستطيع كل صفحة أن تقود إليه. وأي محتوى لا يساعد الزائر على بلوغ تلك الخطوة مرشّح للحذف.</p>
<h2><span class="n">٠٣</span>ما الشيء الوحيد الذي يجب أن يتذكّره؟</h2>
<p>هذه هي النقطة: الفرق الذي يجعلك أنت. يجب أن تتسع لها جملة واحدة، وأن يستطيع الزائر أن يكرّرها بعد ثلاثين ثانية على الموقع. فإذا قدّم فريق القيادة خمس إجابات مختلفة، سيقول الموقع الخمس كلها، ولن يتذكّر الزوار أياً منها.</p>
<div class="callout"><strong>باللغتين</strong>للشركات في قطر والخليج: أجب عن كل سؤال بالعربية وبالإنجليزية. إن بدت الإجابة طبيعية في لغة واحدة فقط، فهي لم تكتمل بعد.</div>
<h2><span class="n">بعد ذلك</span>ابدأ التصميم</h2>
<p>حين تُكتب هذه الإجابات الثلاث، تصبح قرارات التصميم أسهل وأسرع. لا يعود الفريق يتجادل حول الذوق، بل يسأل: هل تساعد هذه الصفحة الزائر المناسب على اتخاذ الخطوة المناسبة وتذكّر الشيء المناسب؟</p>
<p>هذا ما نعنيه حين نقول: نُعرِّف، لا نُزخرِف.</p>
""",
        },
    },
    {
        "slug": "bilingual-is-not-translated", "topic": "brand", "photo": "cs-calligraphy", "minutes": 5,
        "date": L("September 2026", "سبتمبر ٢٠٢٦"),
        "title": L("Bilingual is not translated: designing Arabic and English as equals", "ثنائية اللغة ليست ترجمة: العربية والإنجليزية على قدم المساواة"),
        "dek": L("Why the Arabic version of a brand should never be the last step, and what changes when it comes first.",
                 "لماذا لا ينبغي أن تكون النسخة العربية آخر خطوة في بناء العلامة، وما الذي يتغيّر حين تأتي أولاً."),
        "body": {
            "en": """
<p>In many Gulf projects, the Arabic version arrives late. The English copy is approved, the layout is signed off, and then someone is asked to “add the Arabic”. The result is familiar: a mirrored page, a font chosen because it was available, and sentences that read as translations because they are.</p>
<p>Audiences notice. Arabic readers can tell within a line whether a brand was written for them or converted for them.</p>
<h2><span class="n">01</span>Write, don’t translate</h2>
<p>A tagline that works in English often has no natural Arabic equivalent, and the reverse is true. Treat each language as its own draft, written to the same brief. Agree the idea first, then let each language find its own words for it.</p>
<blockquote>We write in Arabic; we don’t translate into it.</blockquote>
<h2><span class="n">02</span>Choose type as a pair</h2>
<p>Arabic and Latin typefaces should be chosen together, so that weight, rhythm and personality match. Arabic usually needs to be set slightly larger, around ten percent, and with more generous line spacing, so that both scripts feel equal on the page.</p>
<h2><span class="n">03</span>Lay out right to left, properly</h2>
<p>Right-to-left is more than flipping a layout. Reading order, navigation, icons that imply direction, number formats and the placement of images all need decisions. Some elements mirror; others, such as logos and media controls, should not.</p>
<div class="callout"><strong>A simple test</strong>Show the Arabic version to a native reader without the English beside it. If they can tell which language came first, there is more work to do.</div>
<h2><span class="n">After</span>Equal weight</h2>
<p>When both languages are designed from the first sketch, neither feels like an afterthought. The brand becomes one identity with two voices, and that is what audiences in the region expect.</p>
""",
            "ar": """
<p>في كثير من المشاريع الخليجية، تصل النسخة العربية متأخرة. يُعتمد النص الإنجليزي، ويُعتمد التصميم، ثم يُطلب من أحدهم أن «يضيف العربي». والنتيجة مألوفة: صفحة معكوسة، وخط اختير لأنه متوفر، وجمل تُقرأ كترجمة لأنها ترجمة فعلاً.</p>
<p>والجمهور يلاحظ. يدرك القارئ العربي من السطر الأول إن كانت العلامة كُتبت له أم حُوّلت إليه.</p>
<h2><span class="n">٠١</span>اكتب، لا تترجم</h2>
<p>الشعار اللفظي الناجح بالإنجليزية كثيراً ما لا يجد مقابلاً عربياً طبيعياً، والعكس صحيح. تعامل مع كل لغة كمسودة مستقلة تُكتب وفق الموجّهات نفسها. اتفق على الفكرة أولاً، ثم دع كل لغة تجد كلماتها.</p>
<blockquote>نكتب بالعربية، ولا نترجم إليها.</blockquote>
<h2><span class="n">٠٢</span>اختر الخطوط كزوج</h2>
<p>ينبغي أن يُختار الخط العربي والخط اللاتيني معاً، ليتناسب الوزن والإيقاع والشخصية. وغالباً ما تحتاج العربية إلى حجم أكبر قليلاً، بنحو عشرة في المئة، وإلى تباعد أوسع بين الأسطر، ليبدو الخطان متكافئين على الصفحة.</p>
<h2><span class="n">٠٣</span>صمّم من اليمين إلى اليسار كما ينبغي</h2>
<p>الاتجاه من اليمين إلى اليسار أكثر من قلب التصميم. ترتيب القراءة، والتنقّل، والأيقونات التي تدل على اتجاه، وصيغ الأرقام، ومواضع الصور، كلها تحتاج إلى قرارات. بعض العناصر يُعكس، وبعضها، كالشعارات وأزرار تشغيل الوسائط، لا يُعكس.</p>
<div class="callout"><strong>اختبار بسيط</strong>اعرض النسخة العربية على قارئ عربي دون أن تضع الإنجليزية بجانبها. إن استطاع أن يعرف أي اللغتين جاءت أولاً، فما زال أمامك عمل.</div>
<h2><span class="n">بعد ذلك</span>وزن متساوٍ</h2>
<p>حين تُصمَّم اللغتان منذ المسودة الأولى، لا تبدو أي منهما إضافة لاحقة. تصبح العلامة هوية واحدة بصوتين، وهذا ما ينتظره الجمهور في المنطقة.</p>
""",
        },
    },
    {
        "slug": "when-to-replace-spreadsheets", "topic": "tech", "photo": "cs-spreadsheet", "minutes": 5,
        "date": L("September 2026", "سبتمبر ٢٠٢٦"),
        "title": L("When is it time to replace spreadsheets with a business system?", "متى يحين وقت استبدال الجداول بنظام أعمال؟"),
        "dek": L("Five signs that your spreadsheets have stopped saving time and started costing it.",
                 "خمس علامات على أن جداول البيانات توقّفت عن توفير الوقت وبدأت تستهلكه."),
        "body": {
            "en": """
<p>Spreadsheets are where most businesses start, and for good reason. They are flexible, familiar and free. But there is a point where the flexibility becomes the problem, and the business starts working for its spreadsheets instead of the other way round.</p>
<h2><span class="n">01</span>The same data is typed more than once</h2>
<p>If an order is entered by sales, retyped by operations and entered again by finance, you are paying three times for one piece of information, with three chances for error.</p>
<h2><span class="n">02</span>Month-end takes weeks</h2>
<p>When closing the month means collecting files from several people and reconciling them by hand, leadership is always looking at last month’s picture, too late to act on it.</p>
<h2><span class="n">03</span>Only one person understands the file</h2>
<p>If a critical workbook depends on the one colleague who built it, the business carries a risk every time that person is away.</p>
<blockquote>The question is not whether to use a system. It is which process to fix first.</blockquote>
<h2><span class="n">04</span>Approvals happen by email and memory</h2>
<p>Purchase requests, leave, discounts: when approvals live in inboxes, nobody can see what is waiting, and nothing can be audited.</p>
<h2><span class="n">05</span>No one trusts a single number</h2>
<p>When two reports give two different figures for the same thing, meetings are spent arguing about data instead of deciding what to do.</p>
<div class="callout"><strong>Where to start</strong>Pick the one process that causes the most pain, map how it really works today, and fix that first. A good ERP or CRM project grows from one working process, not from a list of every feature on the market.</div>
""",
            "ar": """
<p>تبدأ معظم الشركات بجداول البيانات، ولسبب وجيه: فهي مرنة ومألوفة ومجانية. لكن تأتي لحظة تتحوّل فيها المرونة إلى مشكلة، فتصبح الشركة تعمل من أجل جداولها بدلاً من أن تعمل الجداول من أجلها.</p>
<h2><span class="n">٠١</span>البيانات نفسها تُدخل أكثر من مرة</h2>
<p>إذا أدخل فريق المبيعات الطلب، ثم أعاد فريق العمليات كتابته، ثم أدخلته المالية مرة ثالثة، فأنت تدفع ثلاث مرات مقابل معلومة واحدة، مع ثلاث فرص للخطأ.</p>
<h2><span class="n">٠٢</span>إقفال الشهر يستغرق أسابيع</h2>
<p>حين يعني إقفال الشهر جمع الملفات من عدة أشخاص ومطابقتها يدوياً، تبقى القيادة تنظر إلى صورة الشهر الماضي، بعد فوات وقت التصرّف.</p>
<h2><span class="n">٠٣</span>شخص واحد فقط يفهم الملف</h2>
<p>إذا كان ملف أساسي يعتمد على الزميل الوحيد الذي أنشأه، فالشركة تتحمّل خطراً في كل مرة يغيب فيها.</p>
<blockquote>السؤال ليس هل نستخدم نظاماً، بل أي إجراء نصلحه أولاً.</blockquote>
<h2><span class="n">٠٤</span>الموافقات تمرّ عبر البريد والذاكرة</h2>
<p>طلبات الشراء والإجازات والخصومات: حين تبقى الموافقات في صناديق البريد، لا يرى أحد ما ينتظر، ولا يمكن تدقيق أي شيء.</p>
<h2><span class="n">٠٥</span>لا أحد يثق برقم واحد</h2>
<p>حين يعطي تقريران رقمين مختلفين للشيء نفسه، تُصرف الاجتماعات في الجدال حول البيانات بدلاً من اتخاذ القرار.</p>
<div class="callout"><strong>من أين تبدأ</strong>اختر الإجراء الذي يسبّب أكبر قدر من المعاناة، ووثّق كيف يسير فعلاً اليوم، وابدأ بإصلاحه. مشروع ERP أو CRM الناجح ينمو من إجراء واحد يعمل جيداً، لا من قائمة بكل الميزات المتوفرة في السوق.</div>
""",
        },
    },
    # In preparation: listed, not linked, until written.
    {"slug": None, "topic": "brand",
     "title": L("Positioning before pixels", "التموضع قبل التصميم"),
     "dek": L("Why the strongest identities start with a sentence, not a sketch.", "لماذا تبدأ أقوى الهويات بجملة، لا برسمة.")},
    {"slug": None, "topic": "transformation",
     "title": L("Digital transformation starts with one process", "التحوّل الرقمي يبدأ بإجراء واحد"),
     "dek": L("A practical way to begin without a three-year programme.", "طريقة عملية للبدء دون برنامج يمتد ثلاث سنوات.")},
    {"slug": None, "topic": "web",
     "title": L("Right to left is a design decision, not a setting", "الاتجاه من اليمين إلى اليسار قرار تصميمي، لا إعداد تقني"),
     "dek": L("What mirrors, what doesn’t, and why it matters to Arabic readers.", "ما الذي يُعكس وما لا يُعكس، ولماذا يهمّ ذلك القارئ العربي.")},
    {"slug": None, "topic": "brand",
     "title": L("What a brand guideline should actually contain", "ما الذي يجب أن يتضمّنه دليل الهوية فعلاً"),
     "dek": L("Fewer rules, better rules: a guide your team will open.", "قواعد أقل وأوضح: دليل سيفتحه فريقك فعلاً.")},
    {"slug": None, "topic": "tech",
     "title": L("Keeping a small IT estate secure without a big team", "حماية البنية التقنية الصغيرة دون فريق كبير"),
     "dek": L("The routines that prevent most problems before they start.", "الممارسات الدورية التي تمنع معظم المشكلات قبل وقوعها.")},
]
