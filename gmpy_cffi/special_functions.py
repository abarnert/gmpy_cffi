from gmpy_cffi.interface import gmp, ffi
from gmpy_cffi.mpfr import mpfr, _new_mpfr
from gmpy_cffi.convert import _pyint_to_mpfr

def _init_check_mpfr(x):
    """
    Returns a new mpfr and a pointer to a c mpfr storing the value of x
    """
    if isinstance(x, mpfr):
        res = _new_mpfr(gmp.mpfr_get_prec(x._mpfr))
        mpfr_x = x._mpfr
    elif isinstance(x, float):
        res = _new_mpfr()
        gmp.mpfr_set_d(res, x, gmp.MPFR_RNDN)
        mpfr_x = res        # avoid initialising another c mpfr
    elif isinstance(x, (int, long)):
        res = _new_mpfr()
        _pyint_to_mpfr(x, res)
        mpfr_x = res        # avoid initialising another c mpfr
    else:
        raise TypeError
    return res, mpfr_x


def log(x):
    """
    log(x) -> number

    Return the natural logarithm of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_log(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def log2(x):
    """
    log2(x) -> number

    Return the base-2 logarithm of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_log2(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def log10(x):
    """
    log10(x) -> number

    Return the base-10 logarithm of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_log10(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def exp(x):
    """
    exp(x) -> number

    Return the exponential of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_exp(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def exp2(x):
    """
    exp2(x) -> number

    Return 2**x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_exp2(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def exp10(x):
    """
    exp10(x) -> number

    Return 10**x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_exp10(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def cos(x):
    """
    cos(x) -> number

    Return the cosine of x; x in radians.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_cos(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def sin(x):
    """
    sin(x) -> number

    Return the sine of x; x in radians.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_sin(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def tan(x):
    """
    tan(x) -> number

    Return the tangent of x; x in radians.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_tan(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def sin_cos(x):
    """
    sin_cos(x) -> (number, number)

    Return a tuple containing the sine and cosine of x; x in radians.
    """
    if isinstance(x, mpfr):
        res1 = _new_mpfr(gmp.mpfr_get_prec(x._mpfr))
        res2 = _new_mpfr(gmp.mpfr_get_prec(x._mpfr))
        mpfr_x = x._mpfr
    elif isinstance(x, float):
        res1 = _new_mpfr()
        res2 = _new_mpfr()
        mpfr_x = res1
    elif isinstance(x, (int, long)):
        res1 = _new_mpfr()
        res2 = _new_mpfr()
        mpfr_x = res1
        _pyint_to_mpfr(x, mpfr_x)
    else:
        raise TypeError
    gmp.mpfr_sin_cos(res1, res2, mpfr_x, gmp.MPFR_RNDN)
    return (mpfr._from_c_mpfr(res1), mpfr._from_c_mpfr(res2))


def sec(x):
    """
    sec(x) -> number

    Return the secant of x; x in radians.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_sec(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def csc(x):
    """
    csc(x) -> number

    Return the cosecant of x; x in radians.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_csc(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def cot(x):
    """
    cot(x) -> number

    Return the cotangent of x; x in radians.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_cot(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def acos(x):
    """
    acos(x) -> number

    Return the arc-cosine of x; x in radians.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_acos(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def asin(x):
    """
    asin(x) -> number

    Return the arc-sine of x; x in radians.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_asin(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def atan(x):
    """
    atan(x) -> number

    Return the arc-tangent of x; x in radians.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_atan(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def atan2(y, x):
    """
    atan2(y, x) -> number

    Return the arc-tangent of (y/x).
    """
    # X
    if isinstance(x, mpfr):
        mpfr_x = x._mpfr
    elif isinstance(x, float):
        mpfr_x = _new_mpfr()
        gmp.mpfr_set_d(mpfr_x, x, gmp.MPFR_RNDN)
    elif isinstance(x, (int, long)):
        mpfr_x = _new_mpfr()
        _pyint_to_mpfr(x, mpfr_x)
    else:
        raise TypeError

    # Y
    if isinstance(y, mpfr):
        mpfr_y = y._mpfr
    elif isinstance(y, float):
        mpfr_y = _new_mpfr()
        gmp.mpfr_set_d(mpfr_y, y, gmp.MPFR_RNDN)
    elif isinstance(y, (int, long)):
        mpfr_y = _new_mpfr()
        _pyint_to_mpfr(y, mpfr_y)
    else:
        raise TypeError

    res = _new_mpfr(min(gmp.mpfr_get_prec(mpfr_x), gmp.mpfr_get_prec(mpfr_x)))
    gmp.mpfr_atan2(res, mpfr_y, mpfr_x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def cosh(x):
    """
    cosh(x) -> number

    Return the hyperbolic cosine of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_cosh(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def sinh(x):
    """
    sinh(x) -> number

    Return the hyperbolic sine of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_sinh(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def tanh(x):
    """
    tanh(x) -> number

    Return the hyperbolic tangent of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_tanh(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def sinh_cosh(x):
    """
    sinh_cosh(x) -> (number, number)

    Return a tuple containing the hyperbolic sine and cosine of x.
    """
    if isinstance(x, mpfr):
        res1 = _new_mpfr(gmp.mpfr_get_prec(x._mpfr))
        res2 = _new_mpfr(gmp.mpfr_get_prec(x._mpfr))
        mpfr_x = x._mpfr
    elif isinstance(x, float):
        res1 = _new_mpfr()
        res2 = _new_mpfr()
        mpfr_x = res1
        gmp.mpfr_set_d(mpfr_x, x, gmp.MPFR_RNDN)
    elif isinstance(x, (int, long)):
        res1 = _new_mpfr()
        res2 = _new_mpfr()
        mpfr_x = res1
        _pyint_to_mpfr(x, mpfr_x)
    else:
        raise TypeError
    gmp.mpfr_sinh_cosh(res1, res2, mpfr_x, gmp.MPFR_RNDN)
    return (mpfr._from_c_mpfr(res1), mpfr._from_c_mpfr(res2))


def sech(x):
    """
    sech(x) -> number

    Return the hyperbolic secant of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_sech(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def csch(x):
    """
    csch(x) -> number

    Return the hyperbolic cosecant of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_csch(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def coth(x):
    """
    coth(x) -> number

    Return the hyperbolic cotangent of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_coth(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def acosh(x):
    """
    acosh(x) -> number

    Return the inverse hyperbolic cosine of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_acosh(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def asinh(x):
    """
    asinh(x) -> number

    Return the inverse hyperbolic sine of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_asinh(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)


def atanh(x):
    """
    atanh(x) -> number

    Return the inverse hyperbolic tangent of x.
    """
    res, x = _init_check_mpfr(x)
    gmp.mpfr_atanh(res, x, gmp.MPFR_RNDN)
    return mpfr._from_c_mpfr(res)