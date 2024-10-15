# Herd

[Documentation](https://herd.laravel.com/docs/1/getting-started/sites?ref=herd)

Laravel and PHP development environment that includes everything needed to get started with Laravel ([and other](https://herd.laravel.com/docs/1/extending-herd/supported-frameworks)) framework development

Hosts projects at `~/Herd/my-project` and can access the site by going to its `.test` domain as so `my-project.test`

## Features

- **CLI tools** php, composer, laravel, expose, node, npm, and nvm
- **Fast and Lightweight**: Herd is designed to be fast and efficient, making it ideal for local Laravel development.
- **Easy to Use**: With a simple setup process, you can get started with Herd quickly.
- **Cross-Platform**: Herd works seamlessly on macOS, Windows, and Linux.
- **Integrated with Laravel**: Specifically built to work with Laravel, providing a smooth development experience.
- **Manage multiple version of PHP** and switch in seconds. You can even pin sites to specific PHP versions.
- **Frontend tooling** included with nvm
- **Deploy to servers** from local sites with Laravel Forge integration
For more details, visit the [official Herd website](https://herd.laravel.com).
- **Search local log files** with Log Viewer with access to jumping straight into an IDE from a log entry. Also instant refresh on new entry.

### Pro Features

- Organized and stylized debugging GUI
- Seamlessly run and manage services
- Debug application mails with local email service


## Link an Existing Site

```bash
cd ~/Sites/your-project
herd link
herd link custom-domain
```