from oslo.config import cfg


opt_test_group = cfg.OptGroup(name='test', title='A oslo config example')

test_opts = [
    cfg.BoolOpt('enable', default=False, help='flag for test')
]

opt_durgadas_group = cfg.OptGroup(name='durgadas', title='complex try')

durgadas_opts = [
    cfg.StrOpt('name', default=None, help='name'),
    cfg.ListOpt('passion', default=None, help='passion list')
]

CONF = cfg.CONF
CONF.register_group(opt_test_group)
CONF.register_opts(test_opts, opt_test_group)
CONF.register_group(opt_durgadas_group)
CONF.register_opts(durgadas_opts, opt_durgadas_group)

