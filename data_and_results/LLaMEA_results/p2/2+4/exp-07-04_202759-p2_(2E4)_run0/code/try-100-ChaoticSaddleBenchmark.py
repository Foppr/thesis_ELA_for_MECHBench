import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic forcing coefficients
        self.forcing_coeffs = np.sin(np.arange(dim) * np.pi / dim) * 0.5 + 0.5
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Saddle-point component with varying curvature
        saddle = np.sum(x**2 * np.cos(x)) + 0.5 * np.sum(x**4 * np.sin(x))
        
        # Multi-scale harmonic interactions
        harmonic = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                harmonic += np.sin(dist * (i + j + 1)) * np.cos(dist * (i - j + 1)) * np.exp(-0.1 * dist**2)
        
        # Periodic forcing with dimension-dependent amplitude
        periodic = 0
        for i in range(self.dim):
            periodic += self.forcing_coeffs[i] * np.sin(x[i] * (1 + 0.1 * np.sin(i))) * np.cos(x[i] * (1 + 0.1 * np.cos(i)))
        
        # Gradient-dependent damping term
        damping = 0
        for i in range(self.dim):
            grad_term = np.abs(np.cos(x[i])) * np.exp(-0.5 * x[i]**2)
            damping += grad_term * (x[i]**3 + 0.5 * x[i]**2)
        
        # Multi-scale fractal-like structure
        fractal = 0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(3 * x[i])
            fractal += scale * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Cross-dimensional coupling with chaotic modulation
        cross_coupling = 0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling = 2.0 + np.sin(x[i] * x[j] * 0.5)
            cross_coupling += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Combine all components with dynamic weights
        return 0.25 * saddle + 0.2 * harmonic + 0.15 * periodic + 0.1 * damping + 0.15 * fractal + 0.1 * cross_coupling