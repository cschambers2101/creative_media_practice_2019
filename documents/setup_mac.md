# Setup Your Mac for Development

## Introduction
These instructions should be followed to set up your Mac for command line development using open source software.

## Homebrew Package Manager
As we will be using Linux packages for development and MacOS doesn't include a full linux toolset, we need to install a package manager to assist with this. The default standard is Homebrew, the missing package manager.

### Install Homebrew
To install Homebrew run this command in the terminal (all on one line):

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Further details on Homebrew can be found on their [webpage](https://brew.sh).

## Install Vim
Vim is the text editor we will use and is installed on the majority of Unix systems available today (if it's not Vi will be).

We should just update ours by installing using Homebrew.

```
Brew install vim
```

## Terminal Setup
You can use the built in terminal for development, but many developers will use iTerm on a Mac as it others more features.

MacOS uses the Zsh shell for its commands, where most Linux distributions currently use Bash. You can install Zsh onto any Linux distribution (beyond the scope of this document).

Zsh uses a config file hidden in your home directory:

```
~/.zshrc
```

This is the file you will add configuration settings into later.

### Install iTerm
We will install iTerm using Homebrew:

```
brew cask install iterm2
```

You can set a hotkey up in System Preferences to show iTerm

*Preferences > Keys > Hotkey > ☑️ Show/hide all windows with a system-wide hotkey*

We can mimic some unix functionality on the Mac by setting these preferences:

*Preferences > General > Selection > ☑️ Copy to pasteboard on selection
Preferences > Pointer > General > ☑️ Three-finger tap emulates middle click
Preferences > General > Pointer > ☑️ Focus follows mouse*

### iTerm Disable native full screen
By disabling native full screen, you can quickly make iTerm2 take the whole screen without the usual full-screen animation.

*Preferences > General > Window > ☐ Native full screen windows*

Shortcut for full screen: ⌥ Return

### Split panes
You can divide up your tabs into multiple panes with separate sessions and quickly switch between them. This works very nicely with focus-follow mouse.

*Right Click > Split Pane Vertically 
Right Click > Split Pane Horizontally*

I recommend creating new key bindings for those actions:

*Preferences > Keys > Key Binding > +*

I use ⌥ v and ⌥ h.

You should also enable shell integration:

```
iTerm2 > Install Shell Integration
```

Then, add the following to your ~/.zshrc using vim:

```
source ~/.iterm2_shell_integration.zsh.
```

### Profiles
There are many settings for the profiles in iTerm and these are personal preference, choose what you like!

## Install git
Next we need to install Git using Homebrew:

```
Brew install git
```

## Zsh
As macOS’s default shell since Catalina, Zsh is built on top of Bash and provides a lot of cool features.

Oh My Zsh is a community-driven framework for managing your Zsh configuration. It provides hundreds of plugins and themes and makes configuring Zsh a breeze.

To install Oh My Zsh, run:

```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

We can configure Zsh by running:

```
vim ~/.zshrc
```

You’ll see a lot of configurations added by Oh My Zsh that you can play with. If you ever need to reset your .zshrc, you can find the template [here](https://github.com/ohmyzsh/ohmyzsh/blob/master/templates/zshrc.zsh-template).

There are many [plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins) available.

### PowerLevel10k Theme
We will install the PowerLevel10k Theme using Homebrew:

```
brew install romkatv/powerlevel10k/powerlevel10k
```

And add the following line to your ~/.zshrc:

```
source ~/.oh-my-zsh/custom/themes/powerlevel10k/powerlevel10k.zsh-theme
```

It’ll override any value you have set $ZSH_THEME to.

Restart iTerm2, and you should see the configuration wizard. In the future, you can run it again with p10k configure.

### Install Plug-ins
#### zsh-syntax-highlighting
This plugin enables highlighting of commands while they’re typed. This helps in reviewing commands before running them, particularly in catching syntax errors.

To install it, type: 

```
brew install zsh-syntax-highlighting
```


And add the following line to your ~/.zshrc:

```
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

#### zsh-autosuggestions
This plugin suggests commands as you type based on your history and completion.

To install it, run:

```
brew install zsh-autosuggestions
```

And add the following line to your ~/.zshrc:

```
source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh
```

#### zsh-history-substring-search
This plugin allows you to type in any part of any command from your history, and then press chosen keys, such as the UP and DOWN arrows, to cycle through matches.

To install it, run:

```
brew install zsh-history-substring-search
```

And add the following line to your ~/.zshrc:

```
source /usr/local/share/zsh-history-substring-search/zsh-history-substring-search.zsh
```

If you want to use zsh-syntax-highlighting along with this script, then make sure you load it before you load this script.

Also, you need to map your arrow keys. Add the following after the source command.

```
bindkey '^[OA' history-substring-search-up
bindkey '^[OB' history-substring-search-down
```

#### Oh My Zsh plugins

Oh My Zsh has many plugins available. To install them, just add the plugins name to the *plugins* array in your ~/.zshrc file.

For example to add some recommended plugins change your plugins=() line to read:

```
plugins=(alias-finder brew common-aliases copydir copyfile docker docker-compose dotenv encode64 extract git jira jsontools node npm npx osx urltools vi-mode vscode web-search z)
```

- **alias-finder**: This plugin searches the defined aliases and outputs any that match the command inputted. This makes learning new aliases easier.
- **brew**: The plugin adds several aliases for common brew commands
- **common-aliases**: This plugin creates helpful shortcut aliases for many commonly used commands
- **copydir**: Copies the path of your current folder to the system clipboard
- **copyfile**: Puts the contents of a file in your system clipboard so you can paste it anywhere
- **docker**: This plugin adds auto-completion for Docker.
- **docker-compose**: This plugin provides completion for Docker Compose — as well as some aliases for frequent Docker Compose commands
- **dotenv**: Automatically load your project ENV variables from a .env file when you cd into the project root directory
- **encode64**: Alias plugin for encoding or decoding using the base64 command
- **extract:** This plugin defines a function called extract that extracts the archive file you pass it, and it supports a wide variety of archive file types
- **git:** Provides many aliases and a few useful functions
- **jira:** CLI support for Jira interaction
- **jsontools:** Handy command-line tools for dealing with JSON data
- **node:** This plugin adds the node-docs function, which opens the specific section in the Node.js documentation
- **npm:** The npm plugin provides completion as well as adding many useful aliases.
- **npx:** This plugin automatically registers the npx command-not-found handler if npx exists in your $PATH
- **osx:** This plugin provides a few utilities to make it more enjoyable on macOS
- **urltools:** This plugin provides two aliases to URL encode and URL decode strings
- **vi-mode:** This plugin increase Vi-like Zsh functionality
- **vscode:** This plugin makes interaction between the command line and the VS Code editor easier
- **web-search:** This plugin adds aliases for searching with Google, Wikipedia, Bing, YouTube, and other popular services
- **z:** This plugin defines the z command that tracks your most visited directories and allows you to access them with very few keystrokes

#### Aliases

You can add aliases to your ~/.zshrc file for to create shortcuts for any command you like.
	
For example: You often type the command *cd ..* to go up a directory. It is very easy to miss the space in this command and accidentally type *cc..* instead. We can add an alias to this	mistake so when it happens it types the correct command instead.

In your ~/.zshrc type:

```
alias cd..=‘cd ..’
```

You can use this formula for any command you’d like to shorten. E.g.

```
alias tnew=‘tmux new -s ‘
alias attach=‘tmux attach-session -t ‘
```

If you set this line in your ~/.zshrc file, it will search all aliases as you type commands:

```
ZSH_ALIAS_FINDER_AUTOMATIC=”true”
```

## Node.us
Node is the most popular framework for running and building web applications.

To install it, run:

```
brew install node
```

## Docker
Docker allows you to develop and deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files.

To install it, run:

```
brew cask install docker
```

You should also check out lazydocker, a great CLI tool for docker and docker-compose.

## Htop

Htop allows you to see all processes running on your computer from the terminal.

To install it, run:

```
brew install hoop
```

## Visual Studio Code
An IDE/editor for web development at the moment. It’s fast with tons of extensions, and it’s open source.

To install it, run:

```
brew cask install visual-studio-code
```

## Rectangle
Rectangle allows you to move and resize windows in macOS using keyboard shortcuts or snap areas.

The main shortcuts are:

Left half: ⌥⌘ Arrow-Left
Right half: ⌥⌘ Arrow-Right
Top half: ⌥⌘ Arrow-Up
Bottom half: ⌥⌘ Arrow-Down
Center window: ⌥⌘ C
Maximize window: ⌥⌘ F

To install it, run:

```
brew cask install rectangle
```

## Vim Configuration
Vim is a highly configurable text editor with many different options and should be configured to your personal taste.

NEVER copy someone else's ~/.vimrc file unless you know what you are doing.

I recommend some things to install. First should be a plugin manager and the one I recommend is [Vim-Plug](https://github.com/junegunn/vim-plug).

Install Vim-Plug:

```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

You then need to add this to the top of your ~/.vimrc file:

```
" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

" Make sure you use single quotes
" Add your plugins here



" Initialize plugin system
call plug#end()
```

You then need to add your plugins:

I recommend:

### coc.nvim
[coc.nvim](https://github.com/neoclide/coc.nvim) - gives you autocomplete like vscode

To install, add this under the "add plugins here section:

```
Plug 'neoclide/coc.nvim', {'branch': 'release'}
```

You will then need to restart vim to install the base plugin. 

There is some configuration for coc.nvim to go into your ~/.vimrc file. Copy this directly after the section for vim-plug.

```
" TextEdit might fail if hidden is not set.
set hidden

" Some servers have issues with backup files, see #649.
set nobackup
set nowritebackup

" Give more space for displaying messages.
set cmdheight=2

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" Don't pass messages to |ins-completion-menu|.
set shortmess+=c

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved.
if has("patch-8.1.1564")
  " Recently vim can merge signcolumn and number column into one
  set signcolumn=number
else
  set signcolumn=yes
endif

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
if has('nvim')
  inoremap <silent><expr> <c-space> coc#refresh()
else
  inoremap <silent><expr> <c-@> coc#refresh()
endif

" Make <CR> auto-select the first completion item and notify coc.nvim to
" format on enter, <cr> could be remapped by other vim plugin
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

" Use `[g` and `]g` to navigate diagnostics
" Use `:CocDiagnostics` to get all diagnostics of current buffer in location list.
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  elseif (coc#rpc#ready())
    call CocActionAsync('doHover')
  else
    execute '!' . &keywordprg . " " . expand('<cword>')
  endif
endfunction

" Highlight the symbol and its references when holding the cursor.
autocmd CursorHold * silent call CocActionAsync('highlight')

" Symbol renaming.
nmap <leader>rn <Plug>(coc-rename)

" Formatting selected code.
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder.
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Applying codeAction to the selected region.
" Example: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap keys for applying codeAction to the current buffer.
nmap <leader>ac  <Plug>(coc-codeaction)
" Apply AutoFix to problem on the current line.
nmap <leader>qf  <Plug>(coc-fix-current)

" Map function and class text objects
" NOTE: Requires 'textDocument.documentSymbol' support from the language server.
xmap if <Plug>(coc-funcobj-i)
omap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap af <Plug>(coc-funcobj-a)
xmap ic <Plug>(coc-classobj-i)
omap ic <Plug>(coc-classobj-i)
xmap ac <Plug>(coc-classobj-a)
omap ac <Plug>(coc-classobj-a)

" Remap <C-f> and <C-b> for scroll float windows/popups.
" Note coc#float#scroll works on neovim >= 0.4.0 or vim >= 8.2.0750
nnoremap <nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
nnoremap <nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
inoremap <nowait><expr> <C-f> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(1)\<cr>" : "\<Right>"
inoremap <nowait><expr> <C-b> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(0)\<cr>" : "\<Left>"

" NeoVim-only mapping for visual mode scroll
" Useful on signatureHelp after jump placeholder of snippet expansion
if has('nvim')
  vnoremap <nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#nvim_scroll(1, 1) : "\<C-f>"
  vnoremap <nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#nvim_scroll(0, 1) : "\<C-b>"
endif

" Use CTRL-S for selections ranges.
" Requires 'textDocument/selectionRange' support of language server.
nmap <silent> <C-s> <Plug>(coc-range-select)
xmap <silent> <C-s> <Plug>(coc-range-select)

" Add `:Format` command to format current buffer.
command! -nargs=0 Format :call CocAction('format')

" Add `:Fold` command to fold current buffer.
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" Add `:OR` command for organize imports of the current buffer.
command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

" Add (Neo)Vim's native statusline support.
" NOTE: Please see `:h coc-status` for integrations with external plugins that
" provide custom statusline: lightline.vim, vim-airline.
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

" Mappings for CoCList
" Show all diagnostics.
nnoremap <silent><nowait> <space>a  :<C-u>CocList diagnostics<cr>
" Manage extensions.
nnoremap <silent><nowait> <space>e  :<C-u>CocList extensions<cr>
" Show commands.
nnoremap <silent><nowait> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document.
nnoremap <silent><nowait> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols.
nnoremap <silent><nowait> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent><nowait> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent><nowait> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list.
nnoremap <silent><nowait> <space>p  :<C-u>CocListResume<CR>
```

There are then further extensions required depending on the programming language that you want autocomplete for.

You do this from inside Vim by running this command:

```
:CocInstall <plugin name>
```

Further information [here](https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions).

You can put multiple plugins on one command. For web development run this:

```
:CocInstall cic-css coc-emmet coc-eslint coc-git coc-gist coc-html coc-json coc-markdownlint coc-python coc-sh coc-spell-checker coc-sql coc-tsserver coc-xml
```

### Bracey
[Bracey](https://github.com/turbio/bracey.vim) is a live server for Vim. It requires node to work, so make sure you have that installed from the earlier instruction.

Add this to your vim-plug section of the ~/.zshrc file:

```
Plug 'turbio/bracey.vim', {'do': 'npm install --prefix server'}
```

### SASS
[SASS](https://sass-lang.com) can be installed with Homebrew. The macOS command line tools must be installed first:

```
xcode-select --install
```

Then install the GCC compiler:

```
Brew install gcc
```

Then you can run:

```
brew install sass/sass/sass
```

### Live Server
We now need to setup live server to run. First install it with Node rpm:

```
npm install -g live-server
```

You can now start a live server from any directory containing your index.html file.

Change into the directory you wish to start the server:

```
Cd <directory>
```

Then start the server

```
live-server
```

This should open a webpage showing your development site.







