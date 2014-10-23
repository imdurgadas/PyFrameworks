from oslo.config import cfg


token_group = cfg.OptGroup(name='token', title='A oslo config example')

token_opts = [
    cfg.StrOpt('admin_token', default=None, help='super admin token')
]

opt_durgadas_group = cfg.OptGroup(name='durgadas', title='complex try')

durgadas_opts = [
    cfg.StrOpt('name', default=None, help='name'),
    cfg.ListOpt('passion', default=None, help='passion list'),
    cfg.BoolOpt('enable', default=False, help='flag for test')
]

CONF = cfg.CONF
CONF.register_group(token_group)
CONF.register_opts(token_opts, token_group)

CONF.register_group(opt_durgadas_group)
CONF.register_opts(durgadas_opts, opt_durgadas_group)

