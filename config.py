import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY is not set in the environment.")

DOMAINS = [
    "reuters.com", "apnews.com", "bloomberg.com", "bbc.com", "cnn.com", "nytimes.com", 
    "washingtonpost.com", "wsj.com", "aljazeera.com", "aljazeera.net", "alarabiya.net", 
    "skynewsarabia.com", "aawsat.com", "alquds.co.uk", "ahram.org.eg", "almasryalyoum.com", 
    "okaz.com.sa", "alriyadh.com", "albayan.ae", "theguardian.com", "ft.com", "economist.com", 
    "foreignpolicy.com", "foreignaffairs.com", "politico.com", "axios.com", "time.com", 
    "newsweek.com", "theatlantic.com", "haaretz.com", "timesofisrael.com", "jpost.com", 
    "middleeasteye.net", "al-monitor.com", "asharq.com", "almayadeen.net", "arabic.rt.com", 
    "alhurra.com", "france24.com", "dw.com", "lemonde.fr", "elpais.com", "english.news.cn", 
    "tass.com", "euronews.com", "trtworld.com", "scmp.com", "independent.co.uk", "spiegel.de", 
    "annahar.com", "alraimedia.com", "alseyassah.com", "alkhaleej.ae", "addustour.com", 
    "aletihad.ae", "omandaily.om", "alayam.com", "alghad.com", "stratfor.com", "brookings.edu", 
    "chathamhouse.org", "rand.org", "cfr.org", "mei.edu", "atlanticcouncil.org", "iiss.org", 
    "csis.org", "carnegieendowment.org", "vox.com", "vice.com", "businessinsider.com", 
    "forbes.com", "marketwatch.com", "ibtimes.com", "csmonitor.com", 
    "arabnews.com", "thenationalnews.com"
]

MAX_ARTICLES_PER_DOMAIN = 3
SEARCH_QUERY = "Iran OR إيران OR US-Iran OR US-Iran OR ايران OR US-Iran"
WHEN_PARAM = "1d"
