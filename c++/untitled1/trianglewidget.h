#pragma once
#include <QWidget>

class TriangleWidget : public QWidget
{
    Q_OBJECT
public:
    explicit TriangleWidget(QWidget *parent = nullptr);
public slots:
    void setTriangle(double a, double b, double c, double A, double B);

protected:
    void paintEvent(QPaintEvent *event) override;
    // Add methods to set triangle values if needed
private:
    double m_a = 0, m_b = 0, m_c = 0, m_A = 0, m_B = 0;

};
