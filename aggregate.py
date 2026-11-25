import pandas as pd, re, numpy as np, sys
d = pd.read_pickle('/home/claude/data/out/raw.pkl')
d['qi'] = d['取引時期'].map(lambda s: (lambda m: int(m[1])*4+int(m[2])-1)(re.match(r'(\d+)年第(\d)四半期', s)))
d['a'] = pd.to_numeric(d['面積（㎡）'], errors='coerce')
d['p'] = d['取引価格（総額）'].astype(float)
d['by'] = pd.to_numeric(d['建築年'].str.extract(r'(\d{4})')[0], errors='coerce')
old = pd.read_csv('/home/claude/plugin_zip/skills/oneroom-simulator/references/oneroom-torihiki-kakaku-2026.csv')

def muni(area, ku):
    return ku if area == '東京都' else area + ku

def dedup(df):
    """成約価格情報のうち、不動産取引価格情報と同じ取引とみられる行を1対1で除く。
    鍵：市区町村コード・地区名・面積・建築年・価格。
    1回目：取引時期が同じもの同士、2回目：残りで取引価格側が1四半期後のもの。
    同じ鍵の行が複数あるときは、少ない方の件数までしか除かない（同じ区分内の行は消さない）。"""
    key = ['市区町村コード', '地区名', '面積（㎡）', '建築年', 'p']
    T = df[df['価格情報区分'] == '不動産取引価格情報'][key + ['qi']].copy()
    S = df[df['価格情報区分'] == '成約価格情報'][key + ['qi']].copy()
    T['tq'] = T['qi']; S['tq'] = S['qi']
    drop = []
    for shift in (0, 1):
        S2 = S.copy(); S2['tq'] = S2['qi'] + shift
        k = key + ['tq']
        S2['_n'] = S2.groupby(k).cumcount(); T2 = T.copy(); T2['_n'] = T2.groupby(k).cumcount()
        m = S2.reset_index().merge(T2.reset_index()[k + ['_n', 'index']].rename(columns={'index': 'tidx'}), on=k + ['_n'])
        drop += m['index'].tolist()
        S = S.drop(index=m['index']); T = T.drop(index=m['tidx'])
    return df.drop(index=drop), len(drop)

def stats(s):
    s = s / 10000
    if len(s) == 0:
        return 0, None, None, None
    r10 = lambda v: int(np.floor(v / 10 + 0.5) * 10)
    return len(s), r10(np.median(s)), r10(np.percentile(s, 25)), r10(np.percentile(s, 75))

def build(df, q0=2025*4+2, q1=2026*4+1):
    x = df[(df.qi >= q0) & (df.qi <= q1) & (df.a >= 15) & (df.a <= 30)]
    rows = []
    for _, r in old.iterrows():
        y = x[x['市区町村名'] == muni(r['エリア'], r['区'])]
        n, med, _, _ = stats(y.p)
        n1, m1, a1, b1 = stats(y[y.by >= 2010].p)
        n2, m2, a2, b2 = stats(y[y.by <= 2009].p)
        rows.append([r['エリア'], r['区'], n, med, n1, m1, a1, b1, n2, m2, a2, b2])
    return pd.DataFrame(rows, columns=old.columns)
