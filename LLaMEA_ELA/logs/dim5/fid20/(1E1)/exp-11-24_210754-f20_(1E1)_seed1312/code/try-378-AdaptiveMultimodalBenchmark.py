import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with adaptive exponents
        f1 = np.sum((x**3.5 + 0.7 * x**2.3 + 0.3 * x**1.8) / self.dim)
        
        # Trigonometric modulation with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 20.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.4))
            f2 += np.sin(freq * xi) * np.cos(freq * xi**1.5) * np.exp(-0.1 * xi**2)
        
        # Exponential decay with sinusoidal perturbations
        f3 = 0.1 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Cross-dimensional interaction terms with asymmetric coupling
        f4 = 0.05 * np.sum((x[:-1]**2.1 + 0.8 * x[1:]**1.9) * np.sin(x[:-1] * x[1:]))
        
        # Fractal-like scaling with recursive structure
        f5 = 0.15 * np.sum(np.sin(30.0 * np.sin(5.0 * x)) * np.cos(25.0 * np.cos(3.0 * x)))
        
        # Asymmetric saddle points with variable curvature
        f6 = 0.12 * np.sum((x**4.2 + 0.5 * x**3.1 - 0.7 * x**2.5) * np.exp(-0.2 * np.abs(x)))
        
        # Adaptive noise component with dimension-dependent intensity
        noise_intensity = 0.03 * (1.0 + 0.2 * np.sin(self.dim * 0.5))
        f7 = noise_intensity * np.sum(np.random.rand(self.dim) * x**2)
        
        # Combined fitness value
        return f1 + f2 + f3 + f4 + f5 + f6 + f7