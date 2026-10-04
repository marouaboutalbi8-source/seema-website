# -*- coding: utf-8 -*-
"""v6 copy for the Editions-style service chapters and the Approach scene."""
from content import L

# head: the chapter headline (large first letter); desc: one line per scope item, same order as SERVICES[...]["scope"];
# feat: two featured cards (scope index, photo, prompt shown over the photo)
SVC_V6 = {
    "consultations": {
        "head": L("Clarity, before anything is designed", "الوضوح، قبل أي تصميم"),
        "desc": [
            L("Where you play, who you serve and why you win, written as a plan your leadership can act on.", "أين تنافس، ومن تخدم، ولماذا تتفوّق، مكتوبة كخطة تستطيع القيادة العمل بها."),
            L("The one difference worth owning, tested against competitors and agreed in a single sentence.", "الفرق الوحيد الذي يستحق أن تمتلكه، مُختبَراً أمام المنافسين ومُتّفقاً عليه في جملة واحدة."),
            L("Names for companies, products and services that work in Arabic and English, checked for meaning and availability.", "أسماء للشركات والمنتجات والخدمات تعمل بالعربية والإنجليزية، مع التحقق من المعنى والتوفّر."),
            L("What you say, in what order, to each audience, with the words to use and the words to drop.", "ماذا تقول، وبأي ترتيب، ولكل جمهور، مع الكلمات التي تُستخدم والكلمات التي تُترك."),
            L("A roadmap for your website, apps and systems, prioritised by what moves the business.", "خارطة طريق لموقعك وتطبيقاتك وأنظمتك، مرتّبة حسب ما يحرّك العمل."),
        ],
        "feat": [(1, "sv-msheireb-office", L("What makes us different?", "ما الذي يميّزنا؟")),
                 (2, "ink-pen-minimal", L("A name that works in both scripts", "اسم يعمل باللغتين"))],
    },
    "branding": {
        "head": L("A form no one can confuse", "شكل لا يلتبس على أحد"),
        "desc": [
            L("The mark, colour, type in both scripts and photography, designed as one system.", "الشعار والألوان والخطوط بلغتين وأسلوب التصوير، مصمّمة كنظام واحد."),
            L("Clear rules and ready-made templates, so your team and suppliers apply the brand the same way.", "قواعد واضحة وقوالب جاهزة، ليطبّق فريقك ومورّدوك الهوية بالطريقة نفسها."),
            L("Presentations, reports and documents that carry the brand as well as the logo does.", "عروض وتقارير ومستندات تحمل الهوية كما يحملها الشعار."),
            L("Templates and art direction for every platform, in Arabic and English.", "قوالب وتوجيه فني لكل منصة، بالعربية والإنجليزية."),
        ],
        "feat": [(0, "cs-calligraphy", L("Arabic and Latin, drawn together", "العربية واللاتينية، تُرسمان معاً")),
                 (1, "svc-pattern", L("One system, every touchpoint", "نظام واحد، في كل نقطة تواصل"))],
    },
    "websites": {
        "head": L("Real where people meet you", "حقيقة حيث يلتقي بك الناس"),
        "desc": [
            L("Journeys and screens designed around what visitors came to do, tested before they are built.", "رحلات وشاشات مصمّمة حول ما جاء الزائر لفعله، ومختبرة قبل بنائها."),
            L("Fast, accessible sites on a platform your team can update without a developer.", "مواقع سريعة وسهلة الوصول على منصة يحدّثها فريقك دون مطوّر."),
            L("Focused pages for campaigns and launches, built to turn visits into enquiries.", "صفحات مركّزة للحملات والإطلاقات، مبنية لتحويل الزيارات إلى استفسارات."),
            L("Hosting, analytics, search set-up and training, so the site works from the first day.", "الاستضافة والتحليلات وإعداد محركات البحث والتدريب، ليعمل الموقع من اليوم الأول."),
        ],
        "feat": [(0, "sv-library", L("Arabic first, not mirrored", "العربية أولاً، لا معكوسة")),
                 (1, "svc-facade", L("Fast on every phone", "سريع على كل هاتف"))],
    },
    "mobile": {
        "head": L("Your service, in their pocket", "خدمتك في جيوبهم"),
        "desc": [
            L("Native apps for iPhone and iPad, built to Apple’s standards and to your brand’s.", "تطبيقات أصلية لآيفون وآيباد، مبنية وفق معايير Apple ومعايير علامتك."),
            L("The same quality on Android, so every customer gets the same experience.", "الجودة نفسها على أندرويد، ليحصل كل عميل على التجربة ذاتها."),
            L("Flows that take seconds, with Arabic and English designed screen by screen.", "مسارات تستغرق ثوانٍ، بالعربية والإنجليزية مصمّمة شاشةً بشاشة."),
            L("Store listings, review and release, then a plan for the updates that follow.", "صفحات المتجر والمراجعة والإصدار، ثم خطة للتحديثات التالية."),
        ],
        "feat": [(2, "svc-abaya-phone", L("Book in two taps", "احجز بلمستين")),
                 (3, "cs-qahwa", L("Live on the App Store and Google Play", "متاح على App Store وGoogle Play"))],
    },
    "business-apps": {
        "head": L("One system, not twelve spreadsheets", "نظام واحد، لا اثنا عشر جدولاً"),
        "desc": [
            L("Finance, inventory, purchasing and HR in one place, set up the way your business works.", "المالية والمخزون والمشتريات والموارد البشرية في مكان واحد، مُعدّة بالطريقة التي يعمل بها عملك."),
            L("Every customer, enquiry and deal in one view, shared by sales and service.", "كل عميل واستفسار وصفقة في عرض واحد، يتشاركه فريقا المبيعات والخدمة."),
            L("Approvals, requests and notifications that move on their own.", "موافقات وطلبات وإشعارات تسير من تلقاء نفسها."),
            L("Your systems connected, so data is entered once and trusted everywhere.", "أنظمتك متصلة، فتُدخل البيانات مرة واحدة ويُعتمد عليها في كل مكان."),
        ],
        "feat": [(0, "svc-msheireb", L("Stock, orders and invoices in one view", "المخزون والطلبات والفواتير في عرض واحد")),
                 (2, "cs-spreadsheet", L("Approve it from your phone", "وافق عليه من هاتفك"))],
    },
    "marketing": {
        "head": L("Reach the people who matter", "اصل إلى من يهمّك"),
        "desc": [
            L("Content calendars, production and community management in Arabic and English.", "تقويم المحتوى وإنتاجه وإدارة المجتمع بالعربية والإنجليزية."),
            L("Search visibility in both languages, built on content people are looking for.", "ظهور في نتائج البحث باللغتين، مبني على محتوى يبحث عنه الناس."),
            L("Targeted campaigns on search and social, with budgets tied to results.", "حملات موجّهة على محركات البحث ومنصات التواصل، بميزانيات مرتبطة بالنتائج."),
            L("Monthly reports in plain language: what worked, what didn’t and what we’ll change.", "تقارير شهرية بلغة واضحة: ما الذي نجح، وما الذي لم ينجح، وما الذي سنغيّره."),
        ],
        "feat": [(0, "svc-souq-stall", L("Ramadan campaign, scheduled", "حملة رمضان، مُجدولة")),
                 (2, "qa-katara-towers", L("Spend where it converts", "أنفق حيث تتحقق النتائج"))],
    },
    "support": {
        "head": L("Everything, kept running", "كل شيء يعمل باستمرار"),
        "desc": [
            L("One number and one inbox for every IT question, answered by people who know your set-up.", "رقم واحد وصندوق بريد واحد لكل سؤال تقني، يجيب عنه من يعرف أنظمتك."),
            L("Updates, backups and security patches handled on a schedule, not in a crisis.", "التحديثات والنسخ الاحتياطي وتصحيحات الأمان وفق جدول، لا في أوقات الأزمات."),
            L("Your systems watched around the clock, so problems are found before your staff find them.", "أنظمتك مراقبة على مدار الساعة، لتُكتشف المشكلات قبل أن يكتشفها فريقك."),
            L("Onboarding, training and day-to-day help for your team, in Arabic and English.", "التهيئة والتدريب والمساعدة اليومية لفريقك، بالعربية والإنجليزية."),
        ],
        "feat": [(0, "svc-souq-lamps", L("Fixed before you notice", "يُحل قبل أن تلاحظ")),
                 (2, "palm-shutter", L("All systems normal", "كل الأنظمة تعمل"))],
    },
}

# one photograph per Approach step
PROC_PHOTOS = ["svc-majlis", "cs-calligraphy", "svc-pattern", "cs-dhows-fanar"]
# the giant word shown for each Approach step
PROC_WORDS = [L("Listen", "نصغي"), L("Find", "نجد"), L("Form", "نشكّل"), L("Launch", "نطلق")]
