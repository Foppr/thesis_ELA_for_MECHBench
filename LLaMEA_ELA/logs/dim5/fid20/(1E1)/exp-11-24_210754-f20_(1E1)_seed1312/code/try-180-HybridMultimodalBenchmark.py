import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with varying degrees for conditioning
        f1 = np.sum((x**3.7 + 0.7 * x**2.9 + 0.3 * x**1.8) / self.dim)
        
        # Trigonometric components with multiple frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 20.0 + 15.0 * np.sin(i * 0.7)
            amp = 1.0 + 0.5 * np.cos(i * 0.9)
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Radial basis function components with random centers and varying widths
        f3 = 0.0
        centers = np.random.uniform(-5, 5, (self.dim, self.dim))
        widths = np.random.uniform(0.5, 2.5, self.dim)
        for i in range(self.dim):
            diff = x - centers[i]
            f3 += np.exp(-np.sum((diff**2) / (2 * widths[i]**2)))
        
        # Cross-term interactions with asymmetric coupling
        f4 = 0.0
        for i in range(self.dim-1):
            f4 += np.sin(x[i] + 0.8 * x[i+1]) * np.cos(1.2 * x[i] - x[i+1])
        
        # Saddle point structure with hyperbolic tangent components
        f5 = 0.3 * np.sum(np.tanh(x)**2 + 0.5 * np.tanh(x**3))
        
        # Fractional power interactions to increase nonlinearity
        f6 = 0.15 * np.sum(np.abs(x)**1.3 * np.sin(25.0 * x))
        
        # Combined fitness with weighted components
        return f1 + f2 + f3 + f4 + f5 + f6