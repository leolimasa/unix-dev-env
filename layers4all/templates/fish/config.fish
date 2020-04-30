
set -x PATH ~/Projects/Sandbox/unix-dev-env/bin/ $PATH
{% for i in injections.fish %}{{ i }}
{% endfor %}
source ~/.config/fish/local_config.fish
