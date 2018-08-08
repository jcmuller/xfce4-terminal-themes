# xfce4-terminal-themes

Switch xfce4-terminal themes with ease!

## Installation
```bash
$ pip install xfce4_terminal_themes
```

## Usage

You need to create a `$XDG_HOME/xfce4/terminal/themes` file.

It's anatomy is:

```ini
[Theme Name]
AnyPropertyThat = xfce4 terminal understands

[Theme Name 2]
FontName = Terminus 11

[Theme Name 3]
ColorForeground = #123456
```

Then, you can list themes, see the current theme, and set themes.

### List themes:
```sh
$ ./xfce4-terminal-themes -l
Theme Name 1
Theme Name 2
Theme Name 3
```

### Current theme:
```sh
$ ./xfce4-terminal-themes -c
Theme name: Theme Name 2
Font name: Terminus
Font size: 11
```

### Set theme:
```sh
$ ./xfce4-terminal-themes "Theme Name 3"
```

## Contributing

1. Fork it ( https://github.com/[my-github-username]/pianobar_notify/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
