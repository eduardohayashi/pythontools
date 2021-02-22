## DESCRIPTION
__description = '''Software description. Will appear in --help CLI option '''

## CONFIGS
db_host = '127.0.0.1'
db_user = 'root'
db_pass = '!@#$%'
db_port = '5432'

# Use _help_{config} to set config help description (will appear in --help option)
# Use _single_{config} to set a single char argument
_help_my_config1 = "config1 help text"
_single_my_config1 = 'c'
my_config1 = 123

_help_my_config2 = "config2 help text"
_single_my_config2 = 2
my_config2 = 'abc'

_help_my_config3 = "config3 help text"
_single_my_config3 = 'm3'
my_config3 = True
