import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with conditioning
        f1 = np.sum(x**4) / self.dim
        
        # Trigonometric components with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 20.0 * (1.0 + 0.5 * np.sin(i * 0.7))
            f2 += np.sin(freq * xi) * np.cos(freq * xi**1.5) * np.exp(-0.1 * xi**2)
        
        # Radial basis function components with clustered centers
        f3 = 0.0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                f3 += np.exp(-0.5 * (x[i] - center)**2) * np.sin(10.0 * (x[i] - center))
        
        # Cross-term interaction with asymmetric coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += (x[i]**2 + x[i+1]**2) * np.sin(5.0 * (x[i] - x[i+1]))
        
        # Saddle point structure with exponential decay
        f5 = 0.3 * np.sum(np.exp(-0.5 * np.abs(x)) * np.cos(15.0 * x))
        
        # Fractional power terms for increased nonlinearity
        f6 = 0.2 * np.sum(np.abs(x)**1.7 * np.sin(25.0 * x))
        
        # Asymmetric multimodal component with multiple local minima
        f7 = 0.15 * np.sum((x**3.5 + 0.5 * x**2.3 - 0.3 * x) * np.exp(-0.2 * np.abs(x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7