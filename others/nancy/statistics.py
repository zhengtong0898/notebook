from collections import Counter
from typing import List, Tuple
from pypinyin import lazy_pinyin


def count_single_word(filename="lvyexianzong.txt"):
    """
    统计哪个字出现的频率最高, 列出top50.
    """
    with open(filename, "r") as f:
        content = f.read()
        counter = Counter(content)
        ordered_items: List[Tuple[str, int]] = counter.most_common()
        for k, v in ordered_items:
            k_pinyin = ' '.join(lazy_pinyin(k))
            if "ang" in k_pinyin:
                print(f"词频: {v:>4}; 拼音: {k_pinyin:>18}; 词组: {k};")


def count_group_words(filename="lvyexianzong.txt"):
    """
    先分词然后统计哪一组词出现的频率最高, 列出top20

    词频:   14; 拼音:          xuan feng; 词组: 旋风;
    词频:   13; 拼音:            tuo tuo; 词组: 托托;
    词频:    7; 拼音:            shu shu; 词组: 叔叔;
    词频:    6; 拼音:            heng li; 词组: 亨利;
    词频:    6; 拼音:          shen shen; 词组: 婶婶;
    词频:    6; 拼音:              wu zi; 词组: 屋子;
    词频:    6; 拼音:                 ：“; 词组: ：“;
    词频:    5; 拼音:             qi lai; 词组: 起来;
    词频:    5; 拼音:                 ！”; 词组: ！”;
    词频:    4; 拼音:           yi chang; 词组: 一场;
    词频:    4; 拼音:            mei you; 词组: 没有;
    词频:    3; 拼音:           cao yuan; 词组: 草原;
    词频:    3; 拼音:          tian kong; 词组: 天空;
    词频:    3; 拼音:           geng jia; 词组: 更加;
    词频:    3; 拼音:             yi xia; 词组: 一下;
    词频:    3; 拼音:           shuo dao; 词组: 说道;
    词频:    3; 拼音:         jiao sheng; 词组: 叫声;
    词频:    3; 拼音:             xia qu; 词组: 下去;
    词频:    3; 拼音:          wang wang; 词组: 汪汪;
    词频:    2; 拼音:              qi yi; 词组: 奇异;
    """
    import jieba

    count = 0
    with open(filename, "r") as f:
        content = f.read()
        seg_list = jieba.cut(content, cut_all=True)
        counter = Counter(seg_list)
        ordered_items: List[Tuple[str, int]] = counter.most_common()
        for k, v in ordered_items:
            # if count >= 20:
            #     break

            if "ang" not in ' '.join(lazy_pinyin(k)):
                continue

            if len(k) > 1:
                print(f"词频: {v:>4}; 拼音: {' '.join(lazy_pinyin(k)):>18}; 词组: {k};")
                count += 1


if __name__ == '__main__':
    count_single_word()
    count_group_words()
