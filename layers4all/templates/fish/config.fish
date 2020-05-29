
set -x PATH ~/Projects/Sandbox/unix-dev-env/bin/ $PATH
set -x PATH ~/.npm/bin/ $PATH
if test (uname) = "Darwin"
  set -x PATH ~/Projects/Sandbox/unix-dev-env/bin/mac $PATH
end
function fish_right_prompt
  #intentionally left blank
end

function hsearch
  set cmdtorun (history | fzf)
  eval $cmdtorun
end

{% for i in injections.fish %}{{ i }}
{% endfor %}
source ~/.config/fish/local_config.fish

