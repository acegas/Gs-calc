#include "trianglewidget.h"
#include <QPainter>
#include <QtMath>

TriangleWidget::TriangleWidget(QWidget *parent)
    : QWidget(parent)
{
    // initialization if needed

}

void TriangleWidget::paintEvent(QPaintEvent *)
{
    QPainter p(this);
    p.setRenderHint(QPainter::Antialiasing);

    // Simple triangle drawing placeholder
    QPoint pC(40, height() - 40);          // C (right angle, bottom left)
    QPoint pB(width() - 40, height() - 40); // B (bottom right)
    QPoint pA(40, 40);                     // A (top left)

    QPolygon triangle;
    triangle << pC << pB << pA;
    p.setBrush(QColor("#d0eaff"));
    p.drawPolygon(triangle);

    // Label sides and vertices
    p.setPen(Qt::black);
    p.drawText((pC + pB) / 2 + QPoint(0, 25), "b");
    p.drawText((pA + pC) / 2 + QPoint(-20, 0), "a");
    p.drawText((pA + pB) / 2 + QPoint(-10, -10), "c");
    p.drawText(pA + QPoint(10, 30), "A");
    p.drawText(pB + QPoint(-20, -10), "B");
    p.drawText(pC + QPoint(15, -15), "C");
}

