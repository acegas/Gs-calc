#pragma once

#include <QMainWindow>
#include <QTabWidget>
#include <QWidget>
#include <QLineEdit>
#include <QPushButton>
#include <QLabel>
#include "trianglewidget.h"

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);

private:
    QTabWidget *tabWidget;

    // Calculator Tab
    QWidget *calcTab;
    QLineEdit *calcDisplay;
    // Add buttons as needed...

    // Percent Finder Tab
    QWidget *percentTab;
    QLineEdit *percentOriginal;
    QLineEdit *percentNew;
    QLabel *percentResult;

    // Triangle Solver Tab
    QWidget *triangleTab;
    TriangleWidget *triangleWidget;
    QLineEdit *sideA;
    QLineEdit *sideB;
    QLineEdit *sideC;
    QLineEdit *angleA;
    QLineEdit *angleB;
    QLabel   *triResult;
    QPushButton *solveButton;

    void setupCalculatorTab();
    void setupPercentTab();
    void setupTriangleTab();

private slots:
    void solveTriangle();
    void calcPercent();
};
