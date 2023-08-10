# -*- coding: utf-8 -*-

from learn_redshift import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_redshift.tests import run_cov_test

    run_cov_test(__file__, "learn_redshift.api", preview=False)
