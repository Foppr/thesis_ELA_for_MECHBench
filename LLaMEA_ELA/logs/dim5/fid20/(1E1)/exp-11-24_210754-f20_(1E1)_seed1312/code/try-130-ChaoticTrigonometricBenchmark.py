import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic trigonometric components with dynamic phase shifts
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Dynamic phase shift based on dimension index
            phase = np.sin(i * 0.7) * np.cos(i * 0.3) * 2.0
            # Nested trigonometric polynomial with varying frequencies
            term = np.sin(15.0 * xi + phase) + 0.5 * np.cos(25.0 * xi + phase) + 0.3 * np.sin(40.0 * xi + phase)
            f2 += term**2
        
        # Asymmetric valley structure with exponential modulation
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric exponential decay with sinusoidal modulation
            val = np.exp(-0.5 * xi**2) * np.sin(10.0 * xi)
            # Introduce asymmetry through polynomial transformation
            f3 += val * (1.0 + 0.4 * xi**3)
        
        # Multi-scale interference pattern with frequency modulation
        f4 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Frequency modulation based on dimension index
            freq_mod = 1.0 + 0.3 * np.sin(i * 0.5)
            # Interference pattern with multiple sine waves
            interference = np.sin(freq_mod * 8.0 * xi) * np.cos(freq_mod * 12.0 * xi)
            f4 += interference**2
        
        # Saddle point structure with asymmetric curvature
        f5 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric cubic term with exponential decay
            cubic_term = xi**3 * np.exp(-0.1 * np.abs(xi))
            # Add sinusoidal modulation to create saddle points
            mod = np.sin(5.0 * xi) * np.cos(3.0 * xi)
            f5 += cubic_term * mod
        
        # Combine all components with dynamic weights
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4 + 0.5 * f5