# start .login
if ( -e /etc/csh.modules ) then
	source /etc/csh.modules
# put any common module loads here or in system csh.login
#	module add null
endif

# user module loads
if ( -f $HOME/.modules ) then 
	source $HOME/.modules
endif

# Shell variables and settings

# umask 027

# set path=($path ~/bin)
# setenv MANPATH $MANPATH":"$HOME/man

# user environment
if ( -f $HOME/.login.ext ) then 
	source $HOME/.login.ext
endif

if (! $?prompt) exit			#exit if not interactive

# end .login
