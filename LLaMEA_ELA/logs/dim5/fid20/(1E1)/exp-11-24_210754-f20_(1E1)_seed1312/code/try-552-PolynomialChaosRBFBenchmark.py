import numpy as np

class PolynomialChaosRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with Hermite polynomials
        f1 = 0.25 * np.sum(x**4 - 6*x**2 + 3) / self.dim
        
        # Radial basis function component with adaptive widths
        rbf_sum = 0.0
        for i in range(10):
            dist = np.sum((x - self.centers[i])**2)
            rbf_sum += np.exp(-self.widths[i] * dist)
        f2 = 0.3 * rbf_sum / 10.0
        
        # Adaptive gradient modulation with variable scaling
        grad_mod = 1.0 + 0.5 * np.sin(0.3 * np.sum(x**2))
        f3 = 0.2 * np.sum(grad_mod * x**3) / self.dim
        
        # Multi-scale harmonic interference with frequency modulation
        freqs = 1.0 + 0.4 * np.cos(0.2 * x)
        f4 = 0.25 * np.sum(np.sin(freqs * x) * np.cos(1.5 * x)) / self.dim
        
        # Cross-dimensional coupling with polynomial interaction
        coupling = 0.0
        for i in range(self.dim-1):
            coupling += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        f5 = 0.15 * coupling / self.dim
        
        # Chaotic modulation with logistic map dynamics
        chaotic = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]
            else:
                x_prev = x[i-1]
            chaotic += np.sin(r * x_prev * (1 - x_prev)) * x[i]**2
        f6 = 0.18 * chaotic / self.dim
        
        # Fractional polynomial with variable exponents
        exponents = 2.0 + 0.3 * np.sin(0.5 * x)
        f7 = 0.12 * np.sum(x**exponents) / self.dim
        
        # Adaptive conditioning with dynamic scaling factors
        scales = 1.0 + 0.6 * np.cos(0.4 * x)
        f8 = 0.1 * np.sum(scales * x**2) / self.dim
        
        # Multi-modal sine-cosine coupling with phase shifts
        phase_shifts = np.linspace(0, np.pi, self.dim)
        modal_coupling = 0.0
        for i in range(self.dim):
            modal_coupling += np.sin(x[i] + phase_shifts[i]) * np.cos(x[i] - phase_shifts[i])
        f9 = 0.14 * modal_coupling / self.dim
        
        # Combined non-separable structure with variable coupling strength
        coupling_strength = 0.5 + 0.3 * np.sin(0.2 * np.sum(x))
        f10 = 0.08 * coupling_strength * np.sum(x[:-1]**2 * x[1:]**2) / self.dim
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10