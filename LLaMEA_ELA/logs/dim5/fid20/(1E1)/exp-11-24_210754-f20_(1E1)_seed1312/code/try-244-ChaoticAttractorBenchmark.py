import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic conditioning term
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic attractor components with periodic modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Periodic forcing with chaotic scaling
            freq = 20.0 * (1.0 + 0.5 * np.sin(i * 0.7))
            # Attractor-like behavior with exponential decay and sinusoidal modulation
            mod = np.exp(-0.1 * xi**2) * np.sin(freq * xi) * np.cos(freq * xi**1.5)
            f2 += mod**2
        
        # Multi-scale interference with asymmetric coupling
        f3 = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Asymmetric interaction between adjacent variables
                inter = np.sin(x[i] + 0.7 * x[i+1]) * np.cos(0.9 * x[i] - x[i+1])
                f3 += inter**2
        
        # Fractional power and exponential mixing for nonlinearity
        f4 = 0.3 * np.sum((np.abs(x)**1.8 + 0.5 * np.exp(-0.5 * np.abs(x))) * np.sin(15.0 * x))
        
        # Saddle point with varying curvature and multi-modal structure
        f5 = 0.2 * np.sum(x**4.0 * np.cos(5.0 * x) + 0.3 * x**2.5 * np.sin(8.0 * x))
        
        # Gradient complexity through nested trigonometric terms
        f6 = 0.15 * np.sum(np.sin(25.0 * np.sin(10.0 * x)) + np.cos(15.0 * np.cos(7.0 * x)))
        
        # Cross-term interaction with varying coupling strength and phase shift
        f7 = 0.1 * np.sum(np.sin(x[:-1] * x[1:] + 0.3) * np.cos(1.2 * x[:-1] - 0.8 * x[1:]))
        
        # Combining all components with adaptive weights
        return f1 + f2 + f3 + f4 + f5 + f6 + f7