import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced nested sinusoidal modulations with chaotic frequency scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic frequency modulation using multiple sine/cosine interactions
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * (1.0 + 0.5 * np.cos(i * 0.6)) * (1.0 + 0.3 * np.tan(i * 0.4))
            # Fractal-like interaction using nested trigonometric functions
            mod = np.sin(freq * xi) * np.cos(freq * xi**2) * np.exp(-0.3 * np.abs(xi)) * np.sin(2.0 * xi)
            f2 += mod**2
        
        # Polynomial corruption with non-uniform fractional powers and variable coefficients
        f3 = 0.04 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**3.8 + 0.4 * x**2.5 + 0.15 * x**1.9) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x) * np.tan(0.5 * x))
        
        # Fractal self-similarity through recursive scaling with higher-order harmonics
        f5 = 0.3 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)) * np.exp(-0.1 * x**2))
        
        # Cross-term interactions with asymmetric coupling and dynamic phase shifts
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:] + 0.3 * np.sin(i * 0.7)) * np.cos(1.2 * x[:-1] - x[1:] + 0.4 * np.cos(i * 0.5)))
        
        # Fractional Brownian motion-like roughness with variable Hurst exponent effects
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(3.0 * x))
        
        # Asymmetric saddle points with varying curvature and non-uniform nonlinearities
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 - 0.5 * x**2.3) * np.exp(-0.15 * np.abs(x)) * np.sin(2.0 * x))
        
        # Add a novel chaotic perturbation term with recursive scaling
        f9 = 0.1 * np.sum(np.sin(100.0 * np.sin(20.0 * x)) * np.cos(80.0 * np.cos(15.0 * x)) * (1.0 + 0.2 * np.sin(x)))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9