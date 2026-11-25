import numpy as np

class PolynomialChaosRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and widths for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with adaptive weights
        f1 = 0.3 * np.sum(x**4) / self.dim
        
        # Radial basis function component with dynamic centers
        rbf_sum = 0.0
        for i in range(10):
            dist = np.sum((x - self.centers[i])**2)
            rbf_sum += np.exp(-self.widths[i] * dist)
        f2 = 0.4 * rbf_sum / 10.0
        
        # Adaptive symmetry breaking with harmonic modulation
        sym_break = 0.0
        for i in range(self.dim):
            sym_break += np.sin(2.0 * x[i]) * np.cos(3.0 * x[(i+1) % self.dim])
        f3 = 0.25 * sym_break / self.dim
        
        # Multi-scale harmonic coupling with varying amplitudes
        coupling = 0.0
        for i in range(self.dim):
            coupling += np.sin(5.0 * x[i]) * np.cos(7.0 * x[(i+2) % self.dim]) * \
                       np.sin(3.0 * x[(i+1) % self.dim])
        f4 = 0.2 * coupling / self.dim
        
        # Dynamic conditioning with exponential scaling
        cond_factor = 1.0 + 0.5 * np.sin(0.5 * np.sum(x**2))
        f5 = 0.18 * np.sum(cond_factor * x**3) / self.dim
        
        # Fractional polynomial with variable exponents
        exponents = 2.0 + 0.3 * np.sin(x)
        f6 = 0.15 * np.sum(x**exponents) / self.dim
        
        # Cross-dimensional coupling with adaptive weights
        weights = 1.0 + 0.2 * np.cos(0.4 * x[:-1] + 0.3 * x[1:])
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += weights[i] * x[i] * x[i+1]
        f7 = 0.12 * cross_coupling / self.dim
        
        # Chaotic modulation with logistic map dynamics
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(10.0 * x[i] + np.sin(5.0 * x[(i+3) % self.dim]))
        f8 = 0.1 * chaotic_mod / self.dim
        
        # Asymmetric polynomial with mixed powers
        asym_poly = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asym_poly += x[i]**2.5
            else:
                asym_poly += x[i]**3.5
        f9 = 0.14 * asym_poly / self.dim
        
        # Multi-scale interaction with varying coupling strengths
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += np.sin(8.0 * x[i]) * np.cos(6.0 * x[(i+1) % self.dim]) * \
                          np.sin(4.0 * x[(i+2) % self.dim])
        f10 = 0.09 * multi_scale / self.dim
        
        # Enhanced non-separability with permutation-invariant terms
        perm_term = np.sum(x)**2 + np.sum(x**2)**2
        f11 = 0.08 * perm_term / self.dim
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11