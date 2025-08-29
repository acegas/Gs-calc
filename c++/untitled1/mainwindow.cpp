#include "mainwindow.h"
#include "trianglemath.h"
#include <QTabWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QGridLayout>
#include <QLabel>
#include <QPushButton>
#include <cmath>
#include <optional>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    tabWidget = new QTabWidget(this);
    setCentralWidget(tabWidget);

    setupCalculatorTab();
    setupPercentTab();
    setupTriangleTab();
}

//
// ---- TAB 1: Calculator (minimal placeholder, button logic not implemented here) ----
//
void MainWindow::setupCalculatorTab()
{
    calcTab = new QWidget;
    QVBoxLayout *layout = new QVBoxLayout(calcTab);
    calcDisplay = new QLineEdit;
    calcDisplay->setReadOnly(true);
    layout->addWidget(calcDisplay);

    // You can add button grid/layout here!
    // Example: row of just dummy buttons for illustration
    // QGridLayout *grid = new QGridLayout;
    // layout->addLayout(grid);

    tabWidget->addTab(calcTab, "Calculator");
}

//
// ---- TAB 2: Percent Finder ----
//
void MainWindow::setupPercentTab()
{
    percentTab = new QWidget;
    QGridLayout *layout = new QGridLayout(percentTab);

    layout->addWidget(new QLabel("Original:"), 0, 0);
    percentOriginal = new QLineEdit;
    layout->addWidget(percentOriginal, 0, 1);

    layout->addWidget(new QLabel("New Value:"), 1, 0);
    percentNew = new QLineEdit;
    layout->addWidget(percentNew, 1, 1);

    QPushButton *calcBtn = new QPushButton("Calculate % Changed");
    percentResult = new QLabel("");
    layout->addWidget(calcBtn, 2, 0, 1, 2);
    layout->addWidget(percentResult, 3, 0, 1, 2);

    connect(calcBtn, &QPushButton::clicked, this, &MainWindow::calcPercent);

    tabWidget->addTab(percentTab, "Percent Finder");
}

void MainWindow::calcPercent()
{
    bool ok1, ok2;
    double orig = percentOriginal->text().toDouble(&ok1);
    double newval = percentNew->text().toDouble(&ok2);
    if(ok1 && ok2 && orig != 0) {
        double percent = ((newval - orig) / orig) * 100.0;
        percentResult->setText(QString("Change: %1%").arg(percent, 0, 'f', 2));
    } else {
        percentResult->setText("Error");
    }
}

//
// ---- TAB 3: Right Triangle Solver ----
//
void MainWindow::setupTriangleTab()
{
    triangleTab = new QWidget;
    QHBoxLayout *mainLayout = new QHBoxLayout(triangleTab);

    // Left input panel
    QWidget *inputWidget = new QWidget;
    QGridLayout *inputLayout = new QGridLayout(inputWidget);
    inputLayout->addWidget(new QLabel("Side a:"), 0, 0);
    sideA = new QLineEdit;
    inputLayout->addWidget(sideA, 0, 1);

    inputLayout->addWidget(new QLabel("Side b:"), 1, 0);
    sideB = new QLineEdit;
    inputLayout->addWidget(sideB, 1, 1);

    inputLayout->addWidget(new QLabel("Side c:"), 2, 0);
    sideC = new QLineEdit;
    inputLayout->addWidget(sideC, 2, 1);

    inputLayout->addWidget(new QLabel("Angle A:"), 3, 0);
    angleA = new QLineEdit;
    inputLayout->addWidget(angleA, 3, 1);

    inputLayout->addWidget(new QLabel("Angle B:"), 4, 0);
    angleB = new QLineEdit;
    inputLayout->addWidget(angleB, 4, 1);

    solveButton = new QPushButton("Calculate");
    triResult = new QLabel("");
    inputLayout->addWidget(solveButton, 5, 0, 1, 2);
    inputLayout->addWidget(triResult, 6, 0, 1, 2);

    connect(solveButton, &QPushButton::clicked, this, &MainWindow::solveTriangle);

    // Triangle drawing panel
    triangleWidget = new TriangleWidget;
    triangleWidget->setMinimumSize(280, 220);

    mainLayout->addWidget(inputWidget);
    mainLayout->addWidget(triangleWidget);

    tabWidget->addTab(triangleTab, "Right Triangle Solver");
}

// Slot for triangle calculation
void MainWindow::solveTriangle()
{
    auto get = [](QLineEdit *e) -> std::optional<double> {
        bool ok = false;
        double val = e->text().toDouble(&ok);
        return ok ? std::make_optional(val) : std::nullopt;
    };
    auto res = solveTriangle(
        get(sideA), get(sideB), get(sideC), get(angleA), get(angleB)
        );
    if(!res.valid) {
        triResult->setText(res.error);
        return;
    }

    sideA->setText(QString::number(res.a, 'f', 4));
    sideB->setText(QString::number(res.b, 'f', 4));
    sideC->setText(QString::number(res.c, 'f', 4));
    angleA->setText(QString::number(res.A, 'f', 2));
    angleB->setText(QString::number(res.B, 'f', 2));

    triResult->setText("Solved!");
    triangleWidget->setTriangle(res.a, res.b, res.c, res.A, res.B);
}
