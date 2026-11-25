import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with varying degrees for conditioning
        f1 = np.sum((x**3 + 0.5 * x**2 + 0.1 * x) / self.dim)
        
        # Trigonometric components with multiple frequencies and phases
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq1 = 20.0 + 5.0 * np.sin(i * 0.7)
            freq2 = 15.0 + 3.0 * np.cos(i * 0.9)
            f2 += np.sin(freq1 * xi) * np.cos(freq2 * xi) * np.exp(-0.1 * xi**2)
        
        # Radial basis function components with varying centers and widths
        f3 = 0.0
        centers = np.linspace(-4, 4, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i]
            width = 1.5 + 0.5 * np.sin(i * 0.5)
            f3 += np.exp(-0.5 * ((x - center) / width)**2)
        
        # Cross-term interactions with asymmetric coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += (x[i]**2 + x[i+1]**2) * np.sin(5.0 * x[i] * x[i+1])
        
        # Saddle point structure with exponential decay
        f5 = 0.3 * np.sum(np.exp(-0.2 * np.abs(x)) * np.cos(8.0 * x))
        
        # Fractional power components for added nonlinearity
        f6 = 0.1 * np.sum(np.abs(x)**1.7 * np.sin(10.0 * x))
        
        # Asymmetric multimodal components with varying amplitudes
        f7 = 0.2 * np.sum((x**4 - 2 * x**2 + 1) * np.exp(-0.5 * x**2))
        
        # Combined fitness with weighted contributions
        return f1 + f2 + f3 + f4 + f5 + f6 + f7