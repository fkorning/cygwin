# start .cshrc
if ($?tcsh) then
        set modules_shell="tcsh"
else
        set modules_shell="csh"
endif
alias module 'eval `/usr/local/Modules/$MODULE_VERSION/bin/modulecmd '$modules_shell '\!*`'

if ( -f $HOME/.cshrc.ext ) then 
	source $HOME/.cshrc.ext
endif

if (! $?prompt) exit			#exit if not interactive

# alias rm 'rm -i'
alias sh bash

# end .cshrc
