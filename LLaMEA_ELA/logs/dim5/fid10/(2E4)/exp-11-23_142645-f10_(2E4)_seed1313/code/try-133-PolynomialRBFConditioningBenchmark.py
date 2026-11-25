import numpy as np

class PolynomialRBFConditioningBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with varying exponents
        poly_term = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 1.5 * np.sin(0.4 * x[i])
            poly_term += (x[i]**exp_factor) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function interactions with adaptive widths
        rbf_term = 0.0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            width = 0.5 + 0.3 * np.cos(0.3 * x[i])
            rbf_term += np.exp(-0.5 * ((x[i] - centers[i % len(centers)]) / width)**2)
        
        # Gradient-based conditioning with position-dependent scaling
        grad_condition = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.8 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
            grad_condition += scale * x[i]**3 * np.exp(-0.2 * np.abs(x[i]))
        
        # Multi-scale harmonic interference with dynamic phase coupling
        harmonic = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(1.2 * x[i]) + 0.3 * np.cos(0.8 * x[i])
            freq = 1.0 + 0.6 * np.sin(0.7 * x[i])
            harmonic += freq * np.sin(freq * x[i] + phase) * np.exp(-0.25 * x[i]**2)
        
        # Cross-dimension coupling with non-linear correlation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_factor = 0.5 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
                cross_coupling += corr_factor * np.exp(-0.1 * ((x[i] - x[j])**2 + 0.01))
        
        # Asymmetric basin with piecewise smooth transitions
        basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                basin += 0.6 * np.sin(1.4 * x[i]) * np.exp(-0.15 * x[i]**2) + 0.4 * x[i]**3
            else:
                basin += 0.5 * np.cos(1.3 * x[i]) * np.exp(-0.1 * x[i]**2) + 0.3 * x[i]**4
        
        # Combined fitness with weighted components
        total = 0.2 * poly_term + 0.25 * rbf_term + 0.2 * grad_condition + 0.15 * harmonic + 0.15 * cross_coupling + 0.05 * basin
        
        return total