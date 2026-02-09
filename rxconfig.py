import reflex as rx

config = rx.Config(
    app_name="Housing_Dashboard_Reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)