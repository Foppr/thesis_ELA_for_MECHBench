import numpy as np

class LogSpiralInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Logarithmic spiral components with varying angular frequencies
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Spiral pattern with logarithmic growth
            r = np.sqrt(xi**2 + 1e-8)
            theta = np.arctan2(xi, 1.0) * (1.0 + 0.2 * np.sin(i))
            spiral = np.log(r + 1.0) * np.cos(theta)
            f2 += spiral**2
        
        # Trigonometric interference with exponentially decaying amplitudes
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # High-frequency sine wave with exponential decay
            freq = 20.0 * np.exp(-0.1 * i)
            amp = np.exp(-0.2 * np.abs(xi))
            interference = amp * np.sin(freq * xi) * np.cos(freq * xi**2)
            f3 += interference**2
        
        # Cross-dimensional coupling with recursive scaling
        f4 = 0.05 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Multi-scale harmonic modulation with phase shifts
        f5 = 0.03 * np.sum(np.sin(10.0 * x + np.pi/4) * np.cos(5.0 * x + np.pi/3) * 
                          np.sin(2.0 * x + np.pi/6))
        
        # Asymmetric penalty term for non-convexity
        f6 = 0.01 * np.sum(np.abs(x)**3.5 * np.sin(x))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6