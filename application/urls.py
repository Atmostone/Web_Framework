from application.views import IndexView, AboutView

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
}
