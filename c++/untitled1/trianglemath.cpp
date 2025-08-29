#include "trianglemath.h"
#include <cmath>
#include <algorithm>  // for std::max
#include <QString>
#include <optional>

static constexpr double deg2rad(double d) { return d * M_PI / 180.0; }
static constexpr double rad2deg(double r) { return r * 180.0 / M_PI; }

TriangleResult solveTriangle(
    std::optional<double> a,
    std::optional<double> b,
    std::optional<double> c,
    std::optional<double> A,
    std::optional<double> B
    ) {
    TriangleResult res;
    try {
        if (a.has_value() && b.has_value()) {
            res.a = a.value();
            res.b = b.value();
            res.c = std::hypot(res.a, res.b);
            res.A = rad2deg(std::atan2(res.a, res.b));
            res.B = 90.0 - res.A;
        } else if (a.has_value() && c.has_value()) {
            res.a = a.value();
            res.c = c.value();
            res.b = std::sqrt(std::max(0.0, res.c * res.c - res.a * res.a));
            res.A = rad2deg(std::asin(res.a / res.c));
            res.B = 90.0 - res.A;
        } else if (b.has_value() && c.has_value()) {
            res.b = b.value();
            res.c = c.value();
            res.a = std::sqrt(std::max(0.0, res.c * res.c - res.b * res.b));
            res.B = rad2deg(std::asin(res.b / res.c));
            res.A = 90.0 - res.B;
        } else if (a.has_value() && A.has_value()) {
            res.a = a.value();
            res.A = A.value();
            double A_rad = deg2rad(res.A);
            res.c = res.a / std::sin(A_rad);
            res.b = std::sqrt(std::max(0.0, res.c * res.c - res.a * res.a));
            res.B = 90.0 - res.A;
        } else if (b.has_value() && B.has_value()) {
            res.b = b.value();
            res.B = B.value();
            double B_rad = deg2rad(res.B);
            res.c = res.b / std::sin(B_rad);
            res.a = std::sqrt(std::max(0.0, res.c * res.c - res.b * res.b));
            res.A = 90.0 - res.B;
        } else if (c.has_value() && A.has_value()) {
            res.c = c.value();
            res.A = A.value();
            double A_rad = deg2rad(res.A);
            res.a = res.c * std::sin(A_rad);
            res.b = std::sqrt(std::max(0.0, res.c * res.c - res.a * res.a));
            res.B = 90.0 - res.A;
        } else if (c.has_value() && B.has_value()) {
            res.c = c.value();
            res.B = B.value();
            double B_rad = deg2rad(res.B);
            res.b = res.c * std::sin(B_rad);
            res.a = std::sqrt(std::max(0.0, res.c * res.c - res.b * res.b));
            res.A = 90.0 - res.B;
        } else {
            res.valid = false;
            res.error = "Enter at least two values, including one side.";
            return res;
        }
        res.valid = true;
        return res;
    } catch (...) {
        res.valid = false;
        res.error = "Error: Check your inputs.";
        return res;
    }
}
