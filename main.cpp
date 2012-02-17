#include <QtGui/QApplication>
#include <QDeclarativeView>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QDeclarativeView view;


    //view.setSource(QUrl("qrc:/qml/qmlcalendar/main.qml"));
    //view.show();

    //QObject::connect(view.engine(), SIGNAL(quit()), &a, SLOT(quit()));
        view.setSource(QUrl("qrc:/qml/qmlcalendar/main.qml"));
        view.setResizeMode(QDeclarativeView::SizeRootObjectToView);
        view.showFullScreen();
        view.setAttribute(Qt::WA_OpaquePaintEvent);
        view.setAttribute(Qt::WA_NoSystemBackground);
        view.viewport()->setAttribute(Qt::WA_OpaquePaintEvent);
        view.viewport()->setAttribute(Qt::WA_NoSystemBackground);

    return app.exec();
}