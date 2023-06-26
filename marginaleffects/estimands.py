import numpy as np
import polars as pl

estimands = {
    "difference": lambda hi, lo, eps, x, y: hi - lo,
    "differenceavg": lambda hi, lo, eps, x, y: (hi.mean() - lo.mean()),
    # "differenceavgwts": lambda hi, lo, w: (hi * w).sum() / w.sum() - (lo * w).sum() / w.sum(),

    "dydx": lambda hi, lo, eps, x, y: (hi - lo) / eps,
    "eyex": lambda hi, lo, eps, x, y: (hi - lo) / eps * (x / y),
    "eydx": lambda hi, lo, eps, x, y: ((hi - lo) / eps) / y,
    "dyex": lambda hi, lo, eps, x, y: ((hi - lo) / eps) * x,

    "dydxavg": lambda hi, lo, eps, x, y: np.array([np.mean((hi - lo) / eps)]),
    "eyexavg": lambda hi, lo, eps, x, y: np.array([np.mean((hi - lo) / eps * (x / y))]),
    "eydxavg": lambda hi, lo, eps, x, y: np.array([np.mean((hi - lo) / eps) / y]),
    "dyexavg": lambda hi, lo, eps, x, y: np.array([np.mean(((hi - lo) / eps) * x)]),
    # "dydxavgwts": lambda hi, lo, eps, w: (((hi - lo) / eps) * w).sum() / w.sum(),
    # "eyexavgwts": lambda hi, lo, eps, y, x, w: (((hi - lo) / eps) * (x / y) * w).sum() / w.sum(),
    # "eydxavgwts": lambda hi, lo, eps, y, x, w: ((((hi - lo) / eps) / y) * w).sum() / w.sum(),
    # "dyexavgwts": lambda hi, lo, eps, x, w: (((hi - lo) / eps) * x * w).sum() / w.sum(),

    "ratio": lambda hi, lo, eps, x, y: hi / lo,
    "ratioavg": lambda hi, lo, eps, x, y: np.array([np.mean(hi) / np.mean(lo)]),
    # "ratioavgwts": lambda hi, lo, w: (hi * w).sum() / w.sum() / (lo * w).sum() / w.sum(),

    "lnratio": lambda hi, lo, eps, x, y: np.log(hi / lo),
    "lnratioavg": lambda hi, lo, eps, x, y: np.array([np.log(np.mean(hi) / np.mean(lo))]),
    # "lnratioavgwts": lambda hi, lo, w: np.log((hi * w).sum() / w.sum() / (lo * w).sum() / w.sum()),

    "lnor": lambda hi, lo, eps, x, y: np.log((hi / (1 - hi)) / (lo / (1 - lo))),
    "lnoravg": lambda hi, lo, eps, x, y: np.array(np.log((np.mean(hi) / (1 - np.mean(hi))) / (np.mean(lo) / (1 - np.mean(lo))))),
    # "lnoravgwts": lambda hi, lo, w: np.log(((hi * w).sum() / w.sum() / (1 - (hi * w).sum() / w.sum())) / ((lo * w).sum() / w.sum() / (1 - (lo * w).sum() / w.sum()))),

    "lift": lambda hi, lo, eps, x, y: (hi - lo) / lo,
    "liftavg": lambda hi, lo, eps, x, y: np.array([(np.mean(hi) - np.mean(lo)) / np.mean(lo)]),

    "expdydx": lambda hi, lo, eps, x, y: ((np.exp(hi) - np.exp(lo)) / np.exp(eps)) / eps,
    "expdydxavg": lambda hi, lo, eps, x, y: np.array(np.mean(((np.exp(hi) - np.exp(lo)) / np.exp(eps)) / eps)),
    # "expdydxavgwts": lambda hi, lo, eps, w: ((((np.exp(hi) - np.exp(lo)) / np.exp(eps)) / eps) * w).sum() / w.sum(),
}
