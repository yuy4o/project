# encoding=utf-8
import jieba.analyse
text = "一、为促进电力用户公平负担，合理配置电力资源，将我省大工业用电、一般工商业及其它用电归并为工商业用电。归并后,我省电力用户\
用电价格分为居民生活用电、农业生产用电 和工商业用电三类。居民生活用电和农业生产用电继续执行现 行目录销售电价政策。工商业用电各电压等\
级输配电价具体标 准见附件1。"

# 分词
seg_list = jieba.cut(text)  # 默认是精确模式
print("/ ".join(seg_list))

import jieba
jieba.load_userdict("userdict.txt")
from TextRank import textRank

# TextRank1
T = textRank.TextRank(text,pr_config={'alpha': 0.85, 'max_iter': 100})
print(T.get_n_keywords(20)) # T.get_n_sentences(10)

# TextRank2
res = jieba.analyse.textrank(text, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
print(res)

#  TF-IDF
res2 = jieba.analyse.extract_tags(text, topK=20, withWeight=False, allowPOS=())
print(res2)