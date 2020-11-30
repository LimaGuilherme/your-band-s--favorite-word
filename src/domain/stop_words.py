STOP_WORDS = {
    "0o", '0s', "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac",
    "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected",
    "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all",
    "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst",
    "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything",
    "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate",
    "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking",
    "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3",
    "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand",
    "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best",
    "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief",
    "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant",
    "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj",
    "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider",
    "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't",
    "course",
    "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc",
    "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't",
    "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards",
    "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee",
    "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty",
    "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc",
    "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example",
    "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire",
    "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly",
    "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy",
    "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes",
    "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens",
    "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll",
    "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers",
    "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how",
    "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8",
    "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm",
    "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate",
    "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward",
    "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've",
    "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km",
    "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb",
    "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little",
    "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made",
    "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg",
    "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most",
    "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2",
    "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn",
    "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn",
    "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel",
    "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off",
    "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only",
    "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours",
    "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page",
    "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps",
    "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly",
    "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably",
    "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r",
    "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs",
    "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively",
    "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt",
    "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec",
    "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves",
    "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed",
    "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns",
    "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty",
    "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something",
    "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify",
    "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such",
    "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking",
    "tb",
    "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats",
    "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter",
    "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto",
    "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv",
    "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three",
    "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together",
    "too",
    "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt",
    "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under",
    "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use",
    "used",
    "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve",
    "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants",
    "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were",
    "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence",
    "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon",
    "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom",
    "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within",
    "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www",
    "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj",
    "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr",
    "ys", "yt", "z", "zero", "zi", "zz", "ov", "thy", 'ye', 'thee', 'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um',
    'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao',
    'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também',
    'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem',
    'nas', 'me', 'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha',
    'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 'essas', 'esses',
    'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas',
    'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles',
    'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram',
    'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse',
    'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve',
    'houvemos',
    'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver',
    'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam',
    'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos',
    'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria',
    'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos',
    'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver',
    'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam', "acerca", "agora",
    "algmas", "alguns", "ali", "ambos", "antes", "apontar", "aquela", "aquelas", "aquele", "aqueles", "aqui", "atrás",
    "bem", "bom", "cada", "caminho", "cima", "com", "como", "comprido", "conhecido", "corrente", "das", "debaixo",
    "dentro", "desde", "desligado", "deve", "devem", "deverá", "direita", "diz", "dizer", "dois", "dos", "e", "é", "ela",
    "ele", "eles", "em", "enquanto", "então", "está", "estado", "estão", "estar", "estará", "este", "estes", "esteve",
    "estive", "estivemos", "estiveram", "eu", "fará", "faz", "fazer", "fazia", "fez", "fim", "foi", "fora", "horas",
    "iniciar", "inicio", "ir", "irá", "ista", "iste", "isto", "ligado", "maioria", "maiorias", "mais", "mas", "mesmo",
    "meu", "muito", "muitos", "não", "nome", "nós", "nosso", "novo", "o", "onde", "os", "ou", "outro", "para", "parte",
    "pegar", "pelo", "pessoas", "pode", "poderá", "podia", "por", "porque", "povo", "promeiro", "qual", "qualquer",
    "quando", "quê", "quem", "quieto", "saber", "são", "sem", "ser", "seu", "somente", "tal", "também", "tem", "têm",
    "tempo", "tenho", "tentar", "tentaram", "tente", "tentei", "teu", "teve", "tipo", "tive", "todos", "trabalhar",
    "trabalho", "tu", "último", "um", "uma", "umas", "uns", "usa", "usar", "valor", "veja", "ver", "verdade",
    "verdadeiro", "você", "a", "à", "adeus", "aí", "ainda", "além", "algo", "algumas", "ano", "anos", "ao", "aos",
    "apenas", "apoio", "após", "aquilo", "área", "as", "às", "assim", "até", "através", "baixo", "bastante", "boa",
    "boas", "bons", "breve", "cá", "catorze", "cedo", "cento", "certamente", "certeza", "cinco", "coisa", "conselho",
    "contra", "custa", "da", "dá", "dão", "daquela", "daquelas", "daquele", "daqueles", "dar", "de", "demais", "depois",
    "dessa", "dessas", "desse", "desses", "desta", "destas", "deste", "destes", "dez", "dezanove", "dezasseis",
    "dezassete", "dezoito", "dia", "diante", "dizem", "do", "doze", "duas", "dúvida", "elas", "embora", "entre", "era",
    "és", "essa", "essas", "esse", "esses", "esta", "estas", "estás", "estava", "estiveste", "estivestes", "estou",
    "exemplo", "faço", "falta", "favor", "fazeis", "fazem", "fazemos", "fazes", "final", "fomos", "for", "foram", "forma",
    "foste", "fostes", "fui", "geral", "grande", "grandes", "grupo", "há", "hoje", "hora", "isso", "já", "lá", "lado",
    "local", "logo", "longe", "lugar", "maior", "mal", "máximo", "me", "meio", "menor", "menos", "mês", "meses", "meus",
    "mil", "minha", "minhas", "momento", "na", "nada", "naquela", "naquelas", "naquele", "naqueles", "nas", "nem",
    "nenhuma", "nessa", "nessas", "nesse", "nesses", "nesta", "nestas", "neste", "nestes", "nível", "no", "noite", "nos",
    "nossa", "nossas", "nossos", "nova", "novas", "nove", "novos", "num", "numa", "número", "nunca", "obra", "obrigada",
    "obrigado", "oitava", "oitavo", "oito", "ontem", "onze", "outra", "outras", "outros", "parece", "partir", "paucas",
    "pela", "pelas", "pelos", "perto", "pôde", "podem", "poder", "põe", "põem", "ponto", "pontos", "porquê", "posição",
    "possível", "possivelmente", "posso", "pouca", "pouco", "poucos", "primeira", "primeiras", "primeiro", "primeiros",
    "própria", "próprias", "próprio", "próprios", "próxima", "próximas", "próximo", "próximos", "puderam", "quáis",
    "quanto", "quarta", "quarto", "quatro", "que", "quer", "quereis", "querem", "queremas", "queres", "quero", "questão",
    "quinta", "quinto", "quinze", "relação", "sabe", "sabem", "se", "segunda", "segundo", "sei", "seis", "sempre",
    "seria", "sete", "sétima", "sétimo", "seus", "sexta", "sexto", "sim", "sistema", "sob", "sobre", "sois", "somos",
    "sou", "sua", "suas", "talvez", "tanta", "tantas", "tanto", "tão", "tarde", "te", "temos", "tendes", "tens", "ter",
    "terceira", "terceiro", "teus", "tivemos", "tiveram", "tiveste", "tivestes", "toda", "todas", "todo", "três", "treze",
    "tua", "tuas", "tudo", "vai", "vais", "vão", "vários", "vem", "vêm", "vens", "vez", "vezes", "viagem", "vindo",
    "vinte", "vocês", "vos", "vós", "vossa", "vossas", "vosso", "vossos", "zero", "[chorus]", "[verse]", "[verse", "-", "[chorus",
    "1]", "[pre-chorus]", "3]", "oh,", "pra", "tá", "vou", "fiz", "chorus", "hey", "2", "1", "", "1", "2",
    "3", "4", "5", "6", "7", "8", "9", "10", "11", "instrumental", "ive"
}
