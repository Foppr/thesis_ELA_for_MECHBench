import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial term with varying degrees and adaptive scaling
        poly_term = np.sum((x**3 + 0.5 * x**2.7 + 0.3 * x**1.8 + 0.1 * x**1.2) * (1.0 + 0.2 * np.sin(x)))
        
        # Trigonometric component with multiple frequencies and phase shifts
        trig_term = np.sum(np.cos(2.0 * x) + 0.7 * np.cos(5.0 * x + 0.5) + 0.3 * np.cos(9.0 * x - 1.2))
        
        # Radial basis function with dynamic centers and varying widths
        rbf_term = 0.0
        centers = np.linspace(-4.5, 4.5, int(np.sqrt(self.dim)) + 1)
        for i in range(len(centers)):
            if i < self.dim:
                width = 0.8 + 0.4 * np.sin(i * 0.7)
                rbf_term += np.exp(-0.5 * (x[i] - centers[i%len(centers)])**2 / width**2)
        
        # Coupled oscillatory terms to create interference patterns
        osc_term = np.sum(np.sin(x) * np.cos(1.5 * x) * np.exp(-0.1 * x**2))
        
        # Adaptive nonlinearity with exponential modulation
        nonlinear_term = np.sum(np.exp(0.5 * np.abs(x)) * np.sin(3.0 * x))
        
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
            
        # Global scaling and offset to ensure fitness values are well-distributed
        return 0.25 * poly_term + 0.20 * trig_term + 0.18 * rbf_term + 0.15 * osc_term + 0.12 * nonlinear_term + 0.08 * cross_term + 1.5