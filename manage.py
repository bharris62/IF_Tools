import click
from flask import current_app

from insulinfirst import create_app
from insulinfirst.extensions import db

HERE = ''

app = create_app()


@app.cli.command()
def list_routes():
    """ List available routes in the application."""
    output = []
    for rule in current_app.url_map.iter_rules():

        methods = ','.join(rule.methods)
        url = str(rule)
        if '_debug_toolbar' in url:
            continue
        line = "{:50s} {:30s} {}".format(rule.endpoint, methods, url)
        output.append(line)

    click.echo('\n'.join(sorted(output)))

    return


@app.cli.command()
def create_db():
    db.create_all()
    db.session.commit()
    click.echo('Database has been created')

    return


@app.cli.command()
def run_scrapers():
    from insulinfirst.tasks.amazon.amazon_strips import amazon_strips

    click.echo('Running Scrapers!')
    amazon_strips()

    click.echo('Scrapers Finished!')

    return


if __name__ == '__main__':
    app.cli()

