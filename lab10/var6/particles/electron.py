q = 1.60217663e-19
m = 9.1093837e-31
h = 6.62607015e-27
c = 299792458


def calc_specific_charge():
    return q / m


def calc_compton_wavelength():
    return h / (m / c)
