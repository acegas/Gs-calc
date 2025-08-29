#pragma once
#include <QString>
#include <optional>

struct TriangleResult {
    double a = 0, b = 0, c = 0, A = 0, B = 0;
    bool valid = false;
    QString error; // empty if no error
};

// Use std::optional<double> to indicate if a field was provided
TriangleResult solveTriangle(
    std::optional<double> a,
    std::optional<double> b,
    std::optional<double> c,
    std::optional<double> A,
    std::optional<double> B
    );
