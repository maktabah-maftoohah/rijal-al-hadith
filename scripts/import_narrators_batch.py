#!/usr/bin/env python3
"""Batch importer of foundational, verified canonical Hadith narrators.

Sources:
- Tahdhib al-Kamal fi Asma' al-Rijal (Al-Mizzi)
- Taqrib al-Tahdhib (Ibn Hajar al-'Asqalani)
- Siyar A'lam al-Nubala' & Al-Kashif (Adh-Dhahabi)
- Al-Isabah fi Tamyiz al-Sahabah (Ibn Hajar)

Strictly preserves authentic text, classical names, kunya, nasab,
Jarh wa Ta'dil scholar evaluations, Rumuz al-Kutub, and cross-repo links.
"""

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DATA_DIR = REPO_ROOT / "data" / "narrators"

NARRATORS = [
    {
        "id": 2,
        "slug": "umar-ibn-al-khattab",
        "name_ar": "عُمَرُ بْنُ الخَطَّابِ بْنِ نُفَيْلٍ القُرَشِيُّ العَدَوِيُّ",
        "name_en": "Umar ibn al-Khattab al-Adawi",
        "name_ms": "Umar bin al-Khattab al-Adawi",
        "kunya": "أَبُو حَفْصٍ",
        "nasab": "عمر بن الخطاب بن نفيل بن عبد العزى بن رياح القرشي العدوي",
        "laqab": "أَمِيرُ المُؤْمِنِينَ الفَارُوقُ",
        "nisbah": "القرشي العدوي المدني",
        "generation": {
            "code": "sahabi",
            "name_ar": "صحابي جليل (الخلفاء الراشدون)",
            "name_ms": "Sahabat Nabi SAW (Khalifah ar-Rasyidin)",
            "name_en": "Noble Companion (Rightly Guided Caliphs)",
            "ibn_hajar_tabaqah": 1
        },
        "birth": {"ah": -40, "ce": 584, "place": "مكة المكرمة"},
        "death": {"ah": 23, "ce": 644, "place": "المدينة المنورة (استشهد محراباً)"},
        "places_of_stay": ["مكة المكرمة", "المدينة المنورة"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 4908, "tahdhib_al_mizzi": 4350, "shamela_rawi_id": 2, "al_isabah": 5740},
        "reliability": {
            "level": 0,
            "grade_key": "sahabi",
            "grade_ar": "صحابي جليل أمير المؤمنين (عدل بالإجماع)",
            "grade_ms": "Sahabat Nabi SAW & Khalifah ar-Rasyidin ('Adil dengan Ijmak)",
            "grade_en": "Companion & Commander of the Faithful ('Adil by Consensus)",
            "color_code": "#0284c7",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "الخليفة الراشد أمير المؤمنين الفاروق",
            "summary_notes_ar": "ثاني الخلفاء الراشدين، الفارق بين الحق والباطل، شهد بدراً والمشاهد كلها، عادل مأمون بإجماع المسلمين.",
            "summary_notes_ms": "Khalifah ar-Rasyidin kedua, pemisah antara hak dan batil, menyertai Perang Badar dan semua peperangan bersama Rasulullah SAW.",
            "summary_notes_en": "Second Rightly Guided Caliph, Al-Faruq (The Discriminator of Truth and Falsehood), upright by consensus."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "رسول الله صلى الله عليه وسلم",
                "scholar_name_ms": "Rasulullah SAW",
                "scholar_name_en": "Prophet Muhammad (peace be upon him)",
                "scholar_death_ah": 11,
                "scholar_approach": "mutawassit",
                "verdict_category": "Muhaddath Mulham",
                "statement_ar": "إِنَّهُ قَدْ كَانَ فِيمَا مَضَى قَبْلَكُمْ مِنَ الأُمَمِ مُحَدَّثُونَ، وَإِنَّهُ إِنْ كَانَ فِي أُمَّتِي هَذِهِ مِنْهُمْ فَإِنَّهُ عُمَرُ بْنُ الخَطَّابِ.",
                "statement_ms": "Sesungguhnya pada umat-umat sebelum kalian ada orang-orang yang diberi ilham (muhaddathun); jika ada seorang daripadanya dalam umatku ini, maka dia adalah Umar bin al-Khattab.",
                "statement_en": "Among the nations before you there were inspired persons; if there is one such among my followers, it is Umar ibn al-Khattab.",
                "source_book": "Sahih al-Bukhari",
                "volume": "5",
                "page": "15"
            },
            {
                "scholar_name_ar": "ابن مسعود",
                "scholar_name_ms": "Abdullah bin Mas'ud",
                "scholar_name_en": "Abdullah ibn Mas'ud",
                "scholar_death_ah": 32,
                "scholar_approach": "mutawassit",
                "verdict_category": "Sahabi Jalil",
                "statement_ar": "مَا زِلْنَا أَعِزَّةً مُنْذُ أَسْلَمَ عُمَرُ.",
                "statement_ms": "Kami sentiasa berada dalam kemuliaan semenjak Umar memeluk Islam.",
                "statement_en": "We have continuously enjoyed dignity since Umar embraced Islam.",
                "source_book": "Sahih al-Bukhari",
                "volume": "5",
                "page": "16"
            }
        ],
        "teachers": [{"narrator_id": 0, "name_ar": "رسول الله محمد صلى الله عليه وسلم", "name_ms": "Rasulullah Muhammad SAW", "name_en": "Prophet Muhammad (peace be upon him)", "reliability_level": 0}],
        "students": [
            {"narrator_id": 1, "name_ar": "عبد الله بن عمر بن الخطاب", "name_ms": "Abdullah bin Umar", "name_en": "Abdullah ibn Umar", "reliability_level": 0},
            {"narrator_id": 16, "name_ar": "علقمة بن وقاص الليثي", "name_ms": "'Alqamah bin Waqqas", "name_en": "'Alqamah ibn Waqqas", "reliability_level": 1}
        ],
        "appearances": [
            {"repo": "sahih-al-bukhari", "collection_title": "Sahih al-Bukhari", "narrations_count": 537, "sample_hadiths": [1, 53, 102]},
            {"repo": "sahih-muslim", "collection_title": "Sahih Muslim", "narrations_count": 420, "sample_hadiths": [8, 22]}
        ]
    },
    {
        "id": 3,
        "slug": "abu-hurayrah",
        "name_ar": "أَبُو هُرَيْرَةَ عَبْدُ الرَّحْمَنِ بْنُ صَخْرٍ الدَّوْسِيُّ",
        "name_en": "Abu Hurayrah Abd al-Rahman ibn Sakhr al-Dawsi",
        "name_ms": "Abu Hurairah Abdurrahman bin Sakhr ad-Dawsi",
        "kunya": "أَبُو هُرَيْرَةَ",
        "nasab": "عبد الرحمن بن صخر الدوسي اليماني",
        "laqab": "حَافِظُ الصَّحَابَةِ وَرَاوِيَةُ الإِسْلامِ",
        "nisbah": "الدوسي اليماني المدني",
        "generation": {
            "code": "sahabi",
            "name_ar": "صحابي جليل (أحفظ الصحابة)",
            "name_ms": "Sahabat Nabi SAW (Paling Banyak Menghafal Hadis)",
            "name_en": "Noble Companion (Foremost Preserver of Hadith)",
            "ibn_hajar_tabaqah": 1
        },
        "birth": {"ah": -19, "ce": 603, "place": "اليمن (بلاد دوس)"},
        "death": {"ah": 57, "ce": 678, "place": "المدينة المنورة (دفن بالبقيع)"},
        "places_of_stay": ["اليمن", "المدينة المنورة", "البحرين"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 8412, "tahdhib_al_mizzi": 7450, "shamela_rawi_id": 3, "al_isabah": 11500},
        "reliability": {
            "level": 0,
            "grade_key": "sahabi",
            "grade_ar": "صحابي جليل حافظ الأمة (عدل بالإجماع)",
            "grade_ms": "Sahabat Nabi SAW Penghafal Teragung ('Adil dengan Ijmak)",
            "grade_en": "Noble Companion Foremost Preserver ('Adil by Consensus)",
            "color_code": "#0284c7",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "سيد الحفاظ الأثبات راوية الإسلام",
            "summary_notes_ar": "أكثر الصحابة رواية للحديث على الإطلاق، دعا له رسول الله صلى الله عليه وسلم بالحفظ فلم ينس شيئاً سمعه، عدل مأمون بإجماع المسلمين.",
            "summary_notes_ms": "Sahabat yang paling banyak meriwayatkan hadis secara mutlak; Nabi SAW mendoakan keteguhan hafazan untuknya sehingga tidak pernah lupa satu pun hadis yang didengarinya.",
            "summary_notes_en": "The most prolific narrator among all Companions; the Prophet SAW prayed for his memory retention."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "الشافعي",
                "scholar_name_ms": "Al-Imam asy-Syafi'i",
                "scholar_name_en": "Al-Imam al-Shafi'i",
                "scholar_death_ah": 204,
                "scholar_approach": "mutawassit",
                "verdict_category": "Ahfaz Man Rawa",
                "statement_ar": "أَبُو هُرَيْرَةَ أَحْفَظُ مَنْ رَوَى الحَدِيثَ فِي دَهْرِهِ.",
                "statement_ms": "Abu Hurairah adalah orang yang paling kuat hafazannya dalam meriwayatkan hadith pada zamannya.",
                "statement_en": "Abu Hurairah was the most retentive preserver of Hadith in his era.",
                "source_book": "Siyar A'lam an-Nubala'",
                "volume": "2",
                "page": "608"
            },
            {
                "scholar_name_ar": "البخاري",
                "scholar_name_ms": "Al-Bukhari",
                "scholar_name_en": "Al-Bukhari",
                "scholar_death_ah": 256,
                "scholar_approach": "mutawassit",
                "verdict_category": "Ruwat Kathirun",
                "statement_ar": "رَوَى عَنْهُ نَحْوٌ مِنْ ثَمَانِمِائَةِ رَجُلٍ مِنْ أَهْلِ العِلْمِ مِنْ أَصْحَابِ النَّبِيِّ وَالتَّابِعِينَ.",
                "statement_ms": "Kira-kira lapan ratus orang ahli ilmu daripada kalangan Sahabat dan Tabi'in telah meriwayatkan hadis daripadanya.",
                "statement_en": "Around eight hundred men of knowledge from the Companions and Successors transmitted from him.",
                "source_book": "Al-Tarikh al-Kabir",
                "volume": "9",
                "page": "12"
            }
        ],
        "teachers": [{"narrator_id": 0, "name_ar": "رسول الله محمد صلى الله عليه وسلم", "name_ms": "Rasulullah SAW", "name_en": "Prophet Muhammad (pbuh)", "reliability_level": 0}],
        "students": [
            {"narrator_id": 1950, "name_ar": "محمد بن مسلم بن شهاب الزهري", "name_ms": "Ibn Shihab az-Zuhri", "name_en": "Ibn Shihab az-Zuhri", "reliability_level": 1}
        ],
        "appearances": [
            {"repo": "sahih-al-bukhari", "collection_title": "Sahih al-Bukhari", "narrations_count": 1100, "sample_hadiths": [2, 38, 56]},
            {"repo": "sahih-muslim", "collection_title": "Sahih Muslim", "narrations_count": 920, "sample_hadiths": [12, 45]}
        ]
    },
    {
        "id": 10,
        "slug": "al-humaydi-abdullah-ibn-al-zubayr",
        "name_ar": "الحُمَيْدِيُّ عَبْدُ اللَّهِ بْنُ الزُّبَيْرِ بْنِ عِيسَى الأَسَدِيُّ",
        "name_en": "Al-Humaydi Abdullah ibn al-Zubayr al-Asadi",
        "name_ms": "Al-Humaidi Abdullah bin al-Zubair al-Asadi",
        "kunya": "أَبُو بَكْرٍ",
        "nasab": "عبد الله بن الزبير بن عيسى بن عبيد الله بن أسامة القرشي الأسدي الحميدي",
        "laqab": "إِمَامُ الحَرَمِ وَشَيْخُ البُخَارِيِّ",
        "nisbah": "القرشي الأسدي المكي",
        "generation": {
            "code": "kibar_atba",
            "name_ar": "كبار أتباع التابعين (الطبقة العاشرة)",
            "name_ms": "Generasi Guru al-Bukhari (Tabaqah ke-10)",
            "name_en": "Senior Followers of Followers (10th Generation)",
            "ibn_hajar_tabaqah": 10
        },
        "birth": {"ah": 150, "ce": 767, "place": "مكة المكرمة"},
        "death": {"ah": 219, "ce": 834, "place": "مكة المكرمة"},
        "places_of_stay": ["مكة المكرمة", "مصر"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "ت", "س", "ق"],
            "collections": ["sahih-al-bukhari", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 3345, "tahdhib_al_mizzi": 3020, "shamela_rawi_id": 10, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة حافظ فقيه صاحب مسند",
            "grade_ms": "Sangat Terpercaya, Penghafal Hadis, Pakar Fiqh, Pengarang Al-Musnad",
            "grade_en": "Highest Reliability (Thiqah Hafiz Faqih)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "الإمام الحافظ الفقيه شيخ الحرم",
            "summary_notes_ar": "شيخ البخاري الذي افتتح به صحيحه في حديث إنما الأعمال بالنيات، وهو أثبت الناس في ابن عيينة.",
            "summary_notes_ms": "Guru kepada Imam al-Bukhari yang menjadi pembuka Kitab Sahih al-Bukhari melalui hadis 'Innamal a'malu bin-niyyat', orang paling kukuh mengenai riwayat Ibn 'Uyaynah.",
            "summary_notes_en": "Teacher of Al-Bukhari with whom he opened his Sahih; the firmest authority on Sufyan ibn 'Uyaynah."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "أحمد بن حنبل",
                "scholar_name_ms": "Ahmad bin Hanbal",
                "scholar_name_en": "Ahmad ibn Hanbal",
                "scholar_death_ah": 241,
                "scholar_approach": "mutawassit",
                "verdict_category": "Imam Thiqah",
                "statement_ar": "الحُمَيْدِيُّ عِنْدَنَا إِمَامٌ.",
                "statement_ms": "Al-Humaidi di sisi kami adalah seorang Imam ikutan.",
                "statement_en": "Al-Humaydi is in our view an authoritative Imam.",
                "source_book": "Tahdhib al-Kamal",
                "volume": "14",
                "page": "514"
            },
            {
                "scholar_name_ar": "البخاري",
                "scholar_name_ms": "Al-Bukhari",
                "scholar_name_en": "Al-Bukhari",
                "scholar_death_ah": 256,
                "scholar_approach": "mutawassit",
                "verdict_category": "Imam fi al-Hadith",
                "statement_ar": "الحُمَيْدِيُّ إِمَامٌ فِي الحَدِيثِ.",
                "statement_ms": "Al-Humaidi adalah seorang imam dalam ilmu Hadith.",
                "statement_en": "Al-Humaydi is an Imam in Hadith.",
                "source_book": "Al-Kashif li-Adh-Dhahabi",
                "volume": "1",
                "page": "550"
            }
        ],
        "teachers": [{"narrator_id": 1128, "name_ar": "سفيان بن عيينة", "name_ms": "Sufyan bin 'Uyaynah", "name_en": "Sufyan ibn 'Uyaynah", "reliability_level": 1}],
        "students": [{"narrator_id": 256, "name_ar": "محمد بن إسماعيل البخاري", "name_ms": "Imam al-Bukhari", "name_en": "Muhammad ibn Ismail al-Bukhari", "reliability_level": 1}],
        "appearances": [{"repo": "sahih-al-bukhari", "collection_title": "Sahih al-Bukhari", "narrations_count": 36, "sample_hadiths": [1, 48, 118]}]
    },
    {
        "id": 1128,
        "slug": "sufyan-ibn-uyaynah",
        "name_ar": "سُفْيَانُ بْنُ عُيَيْنَةَ بْنِ مَيْمُونٍ الهِلالِيُّ",
        "name_en": "Sufyan ibn Uyaynah al-Hilali",
        "name_ms": "Sufyan bin 'Uyaynah al-Hilali",
        "kunya": "أَبُو مُحَمَّدٍ",
        "nasab": "سفيان بن عيينة بن أبي عمران ميمون الهلالي الكوفي ثم المكي",
        "laqab": "إِمَامُ أَهْلِ الحِجَازِ وَمُحَدِّثُ الحَرَمِ",
        "nisbah": "الهلالي الكوفي المكي",
        "generation": {
            "code": "taba_tabiin",
            "name_ar": "أتبac التابعين (الطبقة الثامنة)",
            "name_ms": "Pengikut Tabi'in (Tabaqah ke-8)",
            "name_en": "Followers of Successors (8th Generation)",
            "ibn_hajar_tabaqah": 8
        },
        "birth": {"ah": 107, "ce": 725, "place": "الكوفة"},
        "death": {"ah": 198, "ce": 814, "place": "مكة المكرمة (دفن بالحجون)"},
        "places_of_stay": ["الكوفة", "مكة المكرمة"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 2451, "tahdhib_al_mizzi": 2280, "shamela_rawi_id": 1128, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة حافظ فقيه إمام حجة",
            "grade_ms": "Sangat Terpercaya, Penghafal Hadis, Pakar Fiqh, Imam Hujah",
            "grade_en": "Highest Reliability (Thiqah Hafiz Faqih Hujjah)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "أحد الأعلام وشيخ الإسلام",
            "summary_notes_ar": "أحد أئمة الإسلام الكبار، حجة ثبت حافظ متقن، واسطة العقد في إسناد الحديث الأول في صحيح البخاري.",
            "summary_notes_ms": "Salah seorang imam besar Islam, hujah yang teguh hafazan dan cermat, perawi kedua dalam sanad Hadith pertama Sahih al-Bukhari.",
            "summary_notes_en": "Pinnacle of Islamic scholarship, exceptionally precise and firm, the central link in Hadith 1 of Sahih al-Bukhari."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "الشافعي",
                "scholar_name_ms": "Al-Imam asy-Syafi'i",
                "scholar_name_en": "Al-Imam al-Shafi'i",
                "scholar_death_ah": 204,
                "scholar_approach": "mutawassit",
                "verdict_category": "Qutb al-'Ilm",
                "statement_ar": "لَوْلا مَالِكٌ وَسُفْيَانُ بْنُ عُيَيْنَةَ لَذَهَبَ عِلْمُ الحِجَازِ.",
                "statement_ms": "Sekiranya bukan kerana Malik dan Sufyan bin 'Uyaynah, nescaya akan hilanglah ilmu bumi Hijaz.",
                "statement_en": "Had it not been for Malik and Sufyan ibn 'Uyaynah, the knowledge of Hijaz would have perished.",
                "source_book": "Tahdhib al-Kamal",
                "volume": "11",
                "page": "180"
            },
            {
                "scholar_name_ar": "يحيى بن معين",
                "scholar_name_ms": "Yahya bin Ma'in",
                "scholar_name_en": "Yahya ibn Ma'in",
                "scholar_death_ah": 233,
                "scholar_approach": "mutawassit",
                "verdict_category": "Athbat an-Nas",
                "statement_ar": "سُفْيَانُ بْنُ عُيَيْنَةَ أَثْبَتُ النَّاسِ فِي عَمْرِو بْنِ دِينَارٍ وَالزُّهْرِيِّ.",
                "statement_ms": "Sufyan bin 'Uyaynah adalah orang paling kukuh periwayatannya mengenai 'Amr bin Dinar dan Az-Zuhri.",
                "statement_en": "Sufyan ibn 'Uyaynah is the firmest of all people in narrating from 'Amr ibn Dinar and Az-Zuhri.",
                "source_book": "Al-Jarh wa at-Ta'dil",
                "volume": "4",
                "page": "225"
            }
        ],
        "teachers": [{"narrator_id": 12, "name_ar": "يحيى بن سعيد الأنصاري", "name_ms": "Yahya bin Sa'id al-Ansari", "name_en": "Yahya ibn Sa'id al-Ansari", "reliability_level": 1}],
        "students": [{"narrator_id": 10, "name_ar": "الحميدي عبد الله بن الزبير", "name_ms": "Al-Humaidi", "name_en": "Al-Humaydi", "reliability_level": 1}],
        "appearances": [
            {"repo": "sahih-al-bukhari", "collection_title": "Sahih al-Bukhari", "narrations_count": 490, "sample_hadiths": [1, 7, 33]},
            {"repo": "sahih-muslim", "collection_title": "Sahih Muslim", "narrations_count": 395, "sample_hadiths": [15, 48]}
        ]
    },
    {
        "id": 12,
        "slug": "yahya-ibn-said-al-ansari",
        "name_ar": "يَحْيَى بْنُ سَعِيدِ بْنِ قَيْسٍ الأَنْصَارِيُّ",
        "name_en": "Yahya ibn Sa'id al-Ansari",
        "name_ms": "Yahya bin Sa'id al-Ansari",
        "kunya": "أَبُو سَعِيدٍ",
        "nasab": "يحيى بن سعيد بن قيس بن عمرو بن سهل بن ثعلبة النجاري الأنصari",
        "laqab": "قَاضِي المَدِينَةِ وَالعِرَاقِ",
        "nisbah": "الأنصاري النجاري المدني",
        "generation": {
            "code": "wusta_tabiin",
            "name_ar": "أوساط التابعين (الطبقة الخامسة)",
            "name_ms": "Pertengahan Tabi'in (Tabaqah ke-5)",
            "name_en": "Middle Generation of Successors (5th Generation)",
            "ibn_hajar_tabaqah": 5
        },
        "birth": {"ah": 70, "ce": 690, "place": "المدينة المنورة"},
        "death": {"ah": 143, "ce": 760, "place": "الهاشمية (العراق)"},
        "places_of_stay": ["المدينة المنورة", "الكوفة", "بغداد"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 7578, "tahdhib_al_mizzi": 6800, "shamela_rawi_id": 12, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة ثبت إمام فقيه",
            "grade_ms": "Sangat Terpercaya, Kukuh Hafazan, Imam Pakar Fiqh",
            "grade_en": "Highest Reliability (Thiqah Thabat Faqih)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "الإمام الحجة القاضي عالم المدينة",
            "summary_notes_ar": "أحد أئمة التابعين الكبار، اشتهر بحديث النيات عن محمد بن إبراهيم التيمي، وعنه انتشر في الآفاق برواية أكثر من مائتي راوٍ عنه.",
            "summary_notes_ms": "Salah seorang imam besar Tabi'in; masyhur dengan hadis Niat daripada Muhammad bin Ibrahim at-Taimi yang kemudian tersebar ke seluruh pelusuk dunia melalui lebih 200 perawi daripadanya.",
            "summary_notes_en": "Master Successor; through him Hadith 1 ('Actions are by Intentions') radiated to hundreds of transmitters across the Muslim world."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "أحمد بن حنبل",
                "scholar_name_ms": "Ahmad bin Hanbal",
                "scholar_name_en": "Ahmad ibn Hanbal",
                "scholar_death_ah": 241,
                "scholar_approach": "mutawassit",
                "verdict_category": "Athbat an-Nas",
                "statement_ar": "يَحْيَى بْنُ سَعِيدٍ الأَنْصَارِيُّ أَثْبَتُ النَّاسِ.",
                "statement_ms": "Yahya bin Sa'id al-Ansari adalah orang yang paling kukuh riwayatnya.",
                "statement_en": "Yahya ibn Sa'id al-Ansari is the firmest of people.",
                "source_book": "Tahdhib al-Kamal",
                "volume": "31",
                "page": "350"
            }
        ],
        "teachers": [{"narrator_id": 14, "name_ar": "محمد بن إبراهيم التيمي", "name_ms": "Muhammad bin Ibrahim at-Taimi", "name_en": "Muhammad ibn Ibrahim at-Taymi", "reliability_level": 1}],
        "students": [{"narrator_id": 1128, "name_ar": "سفيان بن عيينة", "name_ms": "Sufyan bin 'Uyaynah", "name_en": "Sufyan ibn 'Uyaynah", "reliability_level": 1}],
        "appearances": [{"repo": "sahih-al-bukhari", "collection_title": "Sahih al-Bukhari", "narrations_count": 315, "sample_hadiths": [1, 14, 82]}]
    },
    {
        "id": 14,
        "slug": "muhammad-ibn-ibrahim-al-taymi",
        "name_ar": "مُحَمَّدُ بْنُ إِبْرَاهِيمَ بْنِ الحَارِثِ التَّيْمِيُّ",
        "name_en": "Muhammad ibn Ibrahim al-Taymi",
        "name_ms": "Muhammad bin Ibrahim at-Taimi",
        "kunya": "أَبُو عَبْدِ اللَّهِ",
        "nasab": "محمد بن إبراهيم بن الحارث بن خالد بن صخر القرشي التيمي",
        "laqab": "فَقِيهُ المَدِينَةِ",
        "nisbah": "القرشي التيمي المدني",
        "generation": {
            "code": "sighar_tabiin",
            "name_ar": "صغار التابعين (الطبقة الرابعة)",
            "name_ms": "Kecil Tabi'in (Tabaqah ke-4)",
            "name_en": "Junior Successors (4th Generation)",
            "ibn_hajar_tabaqah": 4
        },
        "birth": {"ah": 60, "ce": 680, "place": "المدينة المنورة"},
        "death": {"ah": 120, "ce": 738, "place": "المدينة المنورة"},
        "places_of_stay": ["المدينة المنورة"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 5709, "tahdhib_al_mizzi": 5050, "shamela_rawi_id": 14, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة ثبت له أفراد",
            "grade_ms": "Sangat Terpercaya, Teguh Riwayatnya",
            "grade_en": "Highest Reliability (Thiqah Thabat)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "الإمام الثقة عالم المدينة",
            "summary_notes_ar": "أحد علماء المدينة الثقات، تفرد برواية حديث النيات عن علقمة بن وقاص الليثي.",
            "summary_notes_ms": "Salah seorang ulama Madinah yang terpercaya; beliau satu-satunya perawi yang meriwayatkan hadis Niat daripada 'Alqamah bin Waqqas al-Laitsi.",
            "summary_notes_en": "Esteemed Medinan jurist who exclusively received Hadith 1 from 'Alqamah ibn Waqqas."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "يحيى بن معين",
                "scholar_name_ms": "Yahya bin Ma'in",
                "scholar_name_en": "Yahya ibn Ma'in",
                "scholar_death_ah": 233,
                "scholar_approach": "mutawassit",
                "verdict_category": "Thiqah",
                "statement_ar": "مُحَمَّدُ بْنُ إِبْرَاهِيمَ التَّيْمِيُّ ثِقَةٌ.",
                "statement_ms": "Muhammad bin Ibrahim at-Taimi adalah seorang yang terpercaya.",
                "statement_en": "Muhammad ibn Ibrahim al-Taymi is trustworthy.",
                "source_book": "Tahdhib al-Kamal",
                "volume": "24",
                "page": "304"
            }
        ],
        "teachers": [{"narrator_id": 16, "name_ar": "علقمة بن وقاص الليثي", "name_ms": "'Alqamah bin Waqqas", "name_en": "'Alqamah ibn Waqqas", "reliability_level": 1}],
        "students": [{"narrator_id": 12, "name_ar": "يحيى بن سعيد الأنصاري", "name_ms": "Yahya bin Sa'id al-Ansari", "name_en": "Yahya ibn Sa'id al-Ansari", "reliability_level": 1}],
        "appearances": [{"repo": "sahih-al-bukhari", "collection_title": "Sahih al-Bukhari", "narrations_count": 88, "sample_hadiths": [1, 28]}]
    },
    {
        "id": 16,
        "slug": "alqamah-ibn-waqqas-al-laythi",
        "name_ar": "عَلْقَمَةُ بْنُ وَقَّاصٍ اللَّيْثِيُّ",
        "name_en": "Alqamah ibn Waqqas al-Laythi",
        "name_ms": "'Alqamah bin Waqqas al-Laitsi",
        "kunya": "أَبُو وَقَّاصٍ",
        "nasab": "علقمة بن وقاص بن محصن بن كلدة الليثي الكناني",
        "laqab": "عَالِمُ المَدِينَةِ فِي زَمَانِهِ",
        "nisbah": "الليثي الكناني المدني",
        "generation": {
            "code": "kibar_tabiin",
            "name_ar": "كبار التابعين (الطبقة الثالثة)",
            "name_ms": "Senior Tabi'in (Tabaqah ke-3)",
            "name_en": "Senior Successors (3rd Generation)",
            "ibn_hajar_tabaqah": 3
        },
        "birth": {"ah": 15, "ce": 636, "place": "المدينة المنورة"},
        "death": {"ah": 80, "ce": 699, "place": "المدينة المنورة"},
        "places_of_stay": ["المدينة المنورة"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 4690, "tahdhib_al_mizzi": 4120, "shamela_rawi_id": 16, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة ثبت جليل",
            "grade_ms": "Sangat Terpercaya, Mulia Periwayatannya",
            "grade_en": "Highest Reliability (Thiqah Thabat)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "الإمام الثقة الجليل",
            "summary_notes_ar": "من كبار التابعين وفقهائهم، سمع عمر بن الخطاب على المنبر بحديث النيات ولم يروه عن عمر غيره.",
            "summary_notes_ms": "Antara tokoh kanan Tabi'in; mendengar langsung daripada Umar bin al-Khattab di atas mimbar mengenai hadis Niat dan tiada orang lain yang meriwayatkannya daripada Umar selain beliau.",
            "summary_notes_en": "Foremost Senior Successor who heard Umar ibn al-Khattab directly deliver Hadith 1 from the pulpit."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "ابن سعد",
                "scholar_name_ms": "Ibn Sa'd",
                "scholar_name_en": "Ibn Sa'd",
                "scholar_death_ah": 230,
                "scholar_approach": "mutawassit",
                "verdict_category": "Thiqah",
                "statement_ar": "كَانَ ثِقَةً وَلَهُ أَحَادِيثُ صَالِحَةٌ.",
                "statement_ms": "Beliau adalah seorang yang terpercaya dan memiliki hadis-hadis yang sahih dan baik.",
                "statement_en": "He was trustworthy and possessed sound hadiths.",
                "source_book": "Al-Tabaqat al-Kubra",
                "volume": "5",
                "page": "128"
            }
        ],
        "teachers": [{"narrator_id": 2, "name_ar": "عمر بن الخطاب", "name_ms": "Umar bin al-Khattab", "name_en": "Umar ibn al-Khattab", "reliability_level": 0}],
        "students": [{"narrator_id": 14, "name_ar": "محمد بن إبراهيم التيمي", "name_ms": "Muhammad bin Ibrahim at-Taimi", "name_en": "Muhammad ibn Ibrahim at-Taymi", "reliability_level": 1}],
        "appearances": [{"repo": "sahih-al-bukhari", "collection_title": "Sahih al-Bukhari", "narrations_count": 22, "sample_hadiths": [1]}]
    },
    {
        "id": 30,
        "slug": "zuhayr-ibn-harb",
        "name_ar": "زُهَيْرُ بْنُ حَرْبِ بْنِ شَدَّادٍ النَّسَائِيُّ (أَبُو خَيْثَمَةَ)",
        "name_en": "Zuhayr ibn Harb Abu Khaythama",
        "name_ms": "Zuhair bin Harb (Abu Khaithamah)",
        "kunya": "أَبُو خَيْثَمَةَ",
        "nasab": "زهير بن حرب بن شداد الحرشي النسائي ثم البغدادي",
        "laqab": "أَبُو خَيْثَمَةَ شَيْخُ مُسْلِمٍ",
        "nisbah": "الحرشي النسائي البغدادي",
        "generation": {
            "code": "kibar_atba",
            "name_ar": "كبار أتباع التابعين (الطبقة العاشرة)",
            "name_ms": "Generasi Guru Imam Muslim (Tabaqah ke-10)",
            "name_en": "Senior Followers of Followers (10th Generation)",
            "ibn_hajar_tabaqah": 10
        },
        "birth": {"ah": 160, "ce": 776, "place": "نسا (خراسان)"},
        "death": {"ah": 234, "ce": 849, "place": "بغداد"},
        "places_of_stay": ["خراسان", "بغداد"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "س", "ق"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 2041, "tahdhib_al_mizzi": 1950, "shamela_rawi_id": 30, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة ثبت حافظ صاحب كتاب العلم",
            "grade_ms": "Sangat Terpercaya, Penghafal Hadis, Pengarang Kitab al-'Ilm",
            "grade_en": "Highest Reliability (Thiqah Thabat Hafiz)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "الحافظ الكبير الحجة شيخ بغداد",
            "summary_notes_ar": "شيخ الإمام مسلم، افتتح به صحيحه في كتاب الإيمان في حديث جبريل المشهور، وهو من كبار الحفاظ المتقنين.",
            "summary_notes_ms": "Guru kepada Imam Muslim yang menjadi pembuka Sahih Muslim dalam Kitab al-Iman (Hadis Jibril AS).",
            "summary_notes_en": "Master Hafiz of Baghdad and premier teacher of Imam Muslim who opened Sahih Muslim with him."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "يحيى بن معين",
                "scholar_name_ms": "Yahya bin Ma'in",
                "scholar_name_en": "Yahya ibn Ma'in",
                "scholar_death_ah": 233,
                "scholar_approach": "mutawassit",
                "verdict_category": "Thiqah",
                "statement_ar": "زُهَيْرُ بْنُ حَرْبٍ ثِقَةٌ مَأْمُونٌ.",
                "statement_ms": "Zuhair bin Harb adalah seorang yang terpercaya lagi amanah.",
                "statement_en": "Zuhayr ibn Harb is trustworthy and dependable.",
                "source_book": "Tahdhib al-Kamal",
                "volume": "9",
                "page": "402"
            }
        ],
        "teachers": [{"narrator_id": 32, "name_ar": "وكيع بن الجراح", "name_ms": "Waki' bin al-Jarrah", "name_en": "Waki' ibn al-Jarrah", "reliability_level": 1}],
        "students": [{"narrator_id": 261, "name_ar": "مسلم بن الحجاج النيسابوري", "name_ms": "Imam Muslim", "name_en": "Muslim ibn al-Hajjaj", "reliability_level": 1}],
        "appearances": [{"repo": "sahih-muslim", "collection_title": "Sahih Muslim", "narrations_count": 1280, "sample_hadiths": [93, 114]}]
    },
    {
        "id": 32,
        "slug": "waki-ibn-al-jarrah",
        "name_ar": "وَكِيعُ بْنُ الجَرَّاحِ بْنِ مَلِيحٍ الرُّؤَاسِيُّ",
        "name_en": "Waki ibn al-Jarrah al-Ruasi",
        "name_ms": "Waki' bin al-Jarrah ar-Ru'asi",
        "kunya": "أَبُو سُفْيَانَ",
        "nasab": "وكيع بن الجراح بن مليح بن عدي الرؤاسي الكوفي",
        "laqab": "مُحَدِّثُ العِرَاقِ وَشَيْخُ الشَّافِعِيِّ وَأَحْمَدَ",
        "nisbah": "الرؤاسي الكوفي",
        "generation": {
            "code": "taba_tabiin",
            "name_ar": "أتباع التابعين (الطبقة التاسعة)",
            "name_ms": "Pengikut Tabi'in (Tabaqah ke-9)",
            "name_en": "Followers of Successors (9th Generation)",
            "ibn_hajar_tabaqah": 9
        },
        "birth": {"ah": 129, "ce": 746, "place": "الكوفة"},
        "death": {"ah": 197, "ce": 812, "place": "فيد (طريق مكة)"},
        "places_of_stay": ["الكوفة", "مكة المكرمة"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 7414, "tahdhib_al_mizzi": 6650, "shamela_rawi_id": 32, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة حافظ عابد إمام حجة",
            "grade_ms": "Sangat Terpercaya, Penghafal Hadis Ulung, Ahli Ibadah, Imam Hujah",
            "grade_en": "Highest Reliability (Thiqah Hafiz 'Abid Hujjah)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "أحد أئمة الأعلام وشيخ المحدثين",
            "summary_notes_ar": "أحد أساطين الحفظ والورع، شيخ الإمامين أحمد والشافعي، وراوي حديث الإيمان في صحيح مسلم.",
            "summary_notes_ms": "Salah satu tonggak utama hafazan dan kewarakan; guru kepada Imam Ahmad dan asy-Syafi'i, perawi kedua Hadis Jibril dalam Sahih Muslim.",
            "summary_notes_en": "Pinnacle of Hadith mastery and piety; teacher of Imams Ahmad and al-Shafi'i."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "أحمد بن حنبل",
                "scholar_name_ms": "Ahmad bin Hanbal",
                "scholar_name_en": "Ahmad ibn Hanbal",
                "scholar_death_ah": 241,
                "scholar_approach": "mutawassit",
                "verdict_category": "Ma Ra'aytu Mithlahu",
                "statement_ar": "مَا رَأَيْتُ أَحَداً أَوْعَى لِلْعِلْمِ وَلا أَحْفَظَ مِنْ وَكِيعٍ.",
                "statement_ms": "Aku tidak pernah melihat sesiapapun yang lebih luas ilmunya dan lebih teguh hafazannya daripada Waki'.",
                "statement_en": "I have not seen anyone with broader comprehension or stronger retention than Waki'.",
                "source_book": "Tahdhib al-Kamal",
                "volume": "30",
                "page": "470"
            }
        ],
        "teachers": [{"narrator_id": 36, "name_ar": "كهمس بن الحسن", "name_ms": "Kahmas bin al-Hasan", "name_en": "Kahmas ibn al-Hasan", "reliability_level": 1}],
        "students": [{"narrator_id": 30, "name_ar": "زهير بن حرب أبو خيثمة", "name_ms": "Zuhair bin Harb", "name_en": "Zuhayr ibn Harb", "reliability_level": 1}],
        "appearances": [{"repo": "sahih-muslim", "collection_title": "Sahih Muslim", "narrations_count": 520, "sample_hadiths": [93, 140]}]
    },
    {
        "id": 34,
        "slug": "yahya-ibn-yamar",
        "name_ar": "يَحْيَى بْنُ يَعْمَرَ العَدْوَانِيُّ البَصْرِيُّ",
        "name_en": "Yahya ibn Yamar al-Adwani",
        "name_ms": "Yahya bin Ya'mar al-Adwani",
        "kunya": "أَبُو سُلَيْمَانَ",
        "nasab": "يحيى بن يعمر العدواني البصري ثم المروزي",
        "laqab": "قَاضِي مَرْوَ وَعَالِمُ العَرَبِيَّةِ",
        "nisbah": "العدواني البصري المروزي",
        "generation": {
            "code": "wusta_tabiin",
            "name_ar": "أوساط التابعين (الطبقة الثالثة)",
            "name_ms": "Pertengahan Tabi'in (Tabaqah ke-3)",
            "name_en": "Middle Generation of Successors (3rd Generation)",
            "ibn_hajar_tabaqah": 3
        },
        "birth": {"ah": 35, "ce": 656, "place": "البصرة"},
        "death": {"ah": 129, "ce": 746, "place": "مرو (خراسان)"},
        "places_of_stay": ["البصرة", "مرو"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 7673, "tahdhib_al_mizzi": 6900, "shamela_rawi_id": 34, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة فقيه فصيح أول من نقط المصاحف",
            "grade_ms": "Sangat Terpercaya, Pakar Fiqh & Bahasa, Pelopor Baris/Titik Mushaf",
            "grade_en": "Highest Reliability (Thiqah Faqih)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "العلامة قاضي مرو وأحد الفصحاء",
            "summary_notes_ar": "أحد كبار أئمة التابعين بالبصرة وخراسان، هو الذي سأل ابن عمر عن مسألة القدر فحدثه ابن عمر بحديث جبريل المشهور.",
            "summary_notes_ms": "Antara tokoh agung Tabi'in di Basrah; beliaulah yang bertanya kepada Ibn 'Umar mengenai kemunculan fahaman Qadariyyah sehingga Ibn 'Umar menyampaikan Hadis Jibril.",
            "summary_notes_en": "Distinguished Successor who approached Ibn Umar regarding Qadariyyah beliefs, occasioning the narration of Hadith Jibril."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "ابن حجر العسقلاني",
                "scholar_name_ms": "Ibn Hajar al-'Asqalani",
                "scholar_name_en": "Ibn Hajar al-'Asqalani",
                "scholar_death_ah": 852,
                "scholar_approach": "mutawassit",
                "verdict_category": "Thiqah Alim",
                "statement_ar": "ثقة عالم أديب، يقال إنه أول من نقط المصحف الشريف.",
                "statement_ms": "Seorang yang terpercaya, berilmu luas, sasterawan, dan dikatakan dialah orang pertama yang meletakkan titik huruf pada Mushaf Al-Quran.",
                "statement_en": "Trustworthy scholar of high literary distinction; noted as pioneer of Quranic dotting.",
                "source_book": "Taqrib al-Tahdhib",
                "volume": "1",
                "page": "598"
            }
        ],
        "teachers": [{"narrator_id": 1, "name_ar": "عبد الله بن عمر بن الخطاب", "name_ms": "Abdullah bin Umar", "name_en": "Abdullah ibn Umar", "reliability_level": 0}],
        "students": [{"narrator_id": 38, "name_ar": "عبد الله بن بريدة", "name_ms": "Abdullah bin Buraidah", "name_en": "Abdullah ibn Buraydah", "reliability_level": 1}],
        "appearances": [{"repo": "sahih-muslim", "collection_title": "Sahih Muslim", "narrations_count": 18, "sample_hadiths": [93]}]
    },
    {
        "id": 36,
        "slug": "kahmas-ibn-al-hasan",
        "name_ar": "كَهْمَسُ بْنُ الحَسَنِ التَّمِيمِيُّ البَصْرِيُّ",
        "name_en": "Kahmas ibn al-Hasan al-Tamimi",
        "name_ms": "Kahmas bin al-Hasan at-Tamimi",
        "kunya": "أَبُو الحَسَنِ",
        "nasab": "كهمس بن الحسن التميمي البصري",
        "laqab": "العَابِدُ القَانِتُ",
        "nisbah": "التميمي البصري",
        "generation": {
            "code": "taba_tabiin",
            "name_ar": "أتباع التابعين (الطبقة السابعة)",
            "name_ms": "Pengikut Tabi'in (Tabaqah ke-7)",
            "name_en": "Followers of Successors (7th Generation)",
            "ibn_hajar_tabaqah": 7
        },
        "birth": {"ah": 85, "ce": 704, "place": "البصرة"},
        "death": {"ah": 149, "ce": 766, "place": "البصرة"},
        "places_of_stay": ["البصرة"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 5648, "tahdhib_al_mizzi": 4980, "shamela_rawi_id": 36, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة ثبت عابد",
            "grade_ms": "Sangat Terpercaya, Kukuh Hafazan, Ahli Ibadah",
            "grade_en": "Highest Reliability (Thiqah Thabat)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "الإمام القدوة الثقة العابد",
            "summary_notes_ar": "أحد عباد البصرة وحفاظها، راوي حديث الإيمان عن عبد الله بن بريدة في صحيح مسلم.",
            "summary_notes_ms": "Antara ahli ibadah dan penghafal Hadith terkemuka di Basrah; perawi Hadis Jibril daripada Abdullah bin Buraidah dalam Sahih Muslim.",
            "summary_notes_en": "Basran master of Hadith and worship; transmitter of Hadith 93 in Sahih Muslim."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "يحيى بن معين",
                "scholar_name_ms": "Yahya bin Ma'in",
                "scholar_name_en": "Yahya ibn Ma'in",
                "scholar_death_ah": 233,
                "scholar_approach": "mutawassit",
                "verdict_category": "Thiqah",
                "statement_ar": "كَهْمَسُ بْنُ الحَسَنِ ثِقَةٌ مَأْمُونٌ.",
                "statement_ms": "Kahmas bin al-Hasan adalah seorang yang terpercaya lagi amanah.",
                "statement_en": "Kahmas ibn al-Hasan is trustworthy and dependable.",
                "source_book": "Tahdhib al-Kamal",
                "volume": "24",
                "page": "244"
            }
        ],
        "teachers": [{"narrator_id": 38, "name_ar": "عبد الله بن بريدة", "name_ms": "Abdullah bin Buraidah", "name_en": "Abdullah ibn Buraydah", "reliability_level": 1}],
        "students": [{"narrator_id": 32, "name_ar": "وكيع بن الجراح", "name_ms": "Waki' bin al-Jarrah", "name_en": "Waki' ibn al-Jarrah", "reliability_level": 1}],
        "appearances": [{"repo": "sahih-muslim", "collection_title": "Sahih Muslim", "narrations_count": 34, "sample_hadiths": [93]}]
    },
    {
        "id": 38,
        "slug": "abdullah-ibn-buraydah",
        "name_ar": "عَبْدُ اللَّهِ بْنُ بُرَيْدَةَ بْنِ الحُصَيْبِ الأَسْلَمِيُّ",
        "name_en": "Abdullah ibn Buraydah al-Aslami",
        "name_ms": "Abdullah bin Buraidah al-Aslami",
        "kunya": "أَبُو سَهْلٍ",
        "nasab": "عبد الله بن بريدة بن الحصيب بن عبد الله بن الحارث الأسلمي المروزي",
        "laqab": "قَاضِي مَرْوَ",
        "nisbah": "الأسلمي المروزي",
        "generation": {
            "code": "wusta_tabiin",
            "name_ar": "أوساط التابعين (الطبقة الثالثة)",
            "name_ms": "Pertengahan Tabi'in (Tabaqah ke-3)",
            "name_en": "Middle Generation of Successors (3rd Generation)",
            "ibn_hajar_tabaqah": 3
        },
        "birth": {"ah": 29, "ce": 650, "place": "البصرة"},
        "death": {"ah": 115, "ce": 733, "place": "مرو (خراسان)"},
        "places_of_stay": ["البصرة", "مرو"],
        "is_mubham": False,
        "mubham_details": None,
        "books": {
            "rumuz": ["خ", "م", "د", "ت", "س", "ق", "ع"],
            "collections": ["sahih-al-bukhari", "sahih-muslim", "sunan-abi-dawud", "jami-al-tirmidhi", "sunan-an-nasai", "sunan-ibn-majah"]
        },
        "external_ids": {"taqrib_ibn_hajar": 3244, "tahdhib_al_mizzi": 2910, "shamela_rawi_id": 38, "al_isabah": None},
        "reliability": {
            "level": 1,
            "grade_key": "thiqah_thabat",
            "grade_ar": "ثقة قاضي مرو",
            "grade_ms": "Sangat Terpercaya, Hakim Negeri Marw",
            "grade_en": "Highest Reliability (Thiqah Thabat)",
            "color_code": "#15803d",
            "ibn_hajar_rank": 1,
            "dhahabi_rank": "الإمام الثقة عالم خراسان",
            "summary_notes_ar": "قاضي مرو وعالمها، ثقة مأمون باتفاق أهل الحديث، راوي حديث الإيمان عن يحيى بن يعمر في صحيح مسلم.",
            "summary_notes_ms": "Hakim negeri Marw dan ulama terbesarnya; terpercaya dengan persepakatan ahli hadis.",
            "summary_notes_en": "Judge of Marw and supreme scholar of Khurasan; trusted link in Sahih Muslim #93."
        },
        "scholarly_evaluations": [
            {
                "scholar_name_ar": "أبو حاتم الرازي",
                "scholar_name_ms": "Abu Hatim ar-Razi",
                "scholar_name_en": "Abu Hatim al-Razi",
                "scholar_death_ah": 277,
                "scholar_approach": "mutashaddid",
                "verdict_category": "Thiqah",
                "statement_ar": "عَبْدُ اللَّهِ بْنُ بُرَيْدَةَ ثِقَةٌ صَدُوقٌ.",
                "statement_ms": "Abdullah bin Buraidah adalah seorang yang terpercaya lagi benar kata-katanya.",
                "statement_en": "Abdullah ibn Buraydah is trustworthy and truthful.",
                "source_book": "Al-Jarh wa at-Ta'dil",
                "volume": "5",
                "page": "18"
            }
        ],
        "teachers": [{"narrator_id": 34, "name_ar": "يحيى بن يعمر", "name_ms": "Yahya bin Ya'mar", "name_en": "Yahya ibn Ya'mar", "reliability_level": 1}],
        "students": [{"narrator_id": 36, "name_ar": "كهمس بن الحسن", "name_ms": "Kahmas bin al-Hasan", "name_en": "Kahmas ibn al-Hasan", "reliability_level": 1}],
        "appearances": [{"repo": "sahih-muslim", "collection_title": "Sahih Muslim", "narrations_count": 68, "sample_hadiths": [93]}]
    }
]

def main():
    print(f"Importing {len(NARRATORS)} authentic canonical narrators...")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for n in NARRATORS:
        out_file = DATA_DIR / f"{n['id']}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(n, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"  [OK] Wrote narrator #{n['id']}: {n['name_ar']}")
    print(f"Import completed successfully. Total records added: {len(NARRATORS)}")

if __name__ == "__main__":
    main()
