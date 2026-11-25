import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with multiple centers
        rbf_term = 0.0
        centers = np.linspace(-4, 4, min(8, self.dim))
        for i in range(self.dim):
            dist = np.sum((x - centers[i % len(centers)])**2)
            rbf_term += np.exp(-0.5 * dist) * np.sin(2.0 * x[i])
        
        # Sinusoidal oscillation component with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.7)
            sin_term += np.sin(freq * x[i]) * np.cos(0.5 * x[i])
        
        # Cross-dimensional coupling with polynomial interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i] * x[j])**2 + np.sin(x[i] + x[j])
                coupling_term += coupling * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Adaptive polynomial with chaotic modulation
        poly_term = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.3 * np.sin(5.0 * x[i])
            poly_term += mod * (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i])
        
        # Fractal-like self-similarity with recursive structure
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Noise injection with multi-scale harmonics
        noise = 0.05 * np.sum(np.sin(10.0 * x) + 0.5 * np.sin(20.0 * x))
        
        # Combine all terms with proper scaling
        return 0.8 * rbf_term + 0.6 * sin_term + 0.4 * coupling_term + 0.3 * poly_term + 0.2 * fractal_term + noise + 0.01 * np.sum(x**2)