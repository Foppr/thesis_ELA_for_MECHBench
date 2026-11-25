import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Periodic Gaussian components with varying widths and centers
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Adaptive width and center based on dimension index
            width = 1.0 + 0.5 * np.sin(i * 0.7)
            center = 2.0 * np.cos(i * 0.9)
            f2 += np.exp(-0.5 * ((xi - center) / width)**2) * np.sin(5.0 * xi)
        
        # Saddle-point structure with asymmetric curvature
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            f3 += (xi**4 - 2.0 * xi**2) * np.cos(0.5 * xi)
        
        # Multi-scale interference terms with varying frequencies
        f4 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freqs = [3.0, 7.0, 11.0]
            for freq in freqs:
                f4 += np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Adaptive noise component with dimension-dependent strength
        noise_strength = 0.2 + 0.1 * np.sin(self.dim * 0.3)
        f5 = noise_strength * np.sum(np.random.normal(0, 1, self.dim) * x**2)
        
        # Cross-term interaction with exponential decay
        f6 = 0.0
        for i in range(self.dim - 1):
            f6 += np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * np.sin(3.0 * (x[i] + x[i+1]))
        
        # Asymmetric polynomial corruption with varying exponents
        f7 = 0.0
        for i in range(self.dim):
            xi = x[i]
            exps = [2.5, 3.7, 4.1]
            for exp in exps:
                f7 += (xi**exp) * np.cos(0.8 * xi)
        
        # Combined fitness with adjusted weights
        return f1 + 0.5 * f2 + 0.3 * f3 + 0.4 * f4 + 0.2 * f5 + 0.6 * f6 + 0.3 * f7