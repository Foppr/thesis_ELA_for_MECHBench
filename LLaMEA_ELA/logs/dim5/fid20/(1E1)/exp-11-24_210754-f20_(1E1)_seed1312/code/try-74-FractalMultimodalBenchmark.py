import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic sine-wave modulations with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Frequency modulation based on dimension index
            freq = 30.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.4))
            # Amplitude scaling with exponential decay
            amp = 1.0 / (1.0 + 0.1 * np.abs(xi))
            mod = amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
            f2 += mod**2
        
        # Polynomial corruption with fractional powers and varying coefficients
        f3 = 0.04 * np.sum((x**4.8 + 0.7 * x**3.9 + 0.6 * x**2.7 + 0.3 * x**1.8) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(9.0 * x))
        
        # Fractal-like self-similarity through nested trigonometric functions with recursive scaling
        f5 = 0.2 * np.sum(np.sin(50.0 * np.sin(12.0 * x)) * np.cos(40.0 * np.cos(10.0 * x)))
        
        # Cross-term interactions with asymmetric coupling and higher-order interference
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.8 * x[1:]) * np.cos(1.2 * x[:-1] - x[1:]))
        
        # Fractional Brownian motion-like roughness with increased nonlinearity and variance
        f7 = 0.12 * np.sum(np.abs(x)**1.7 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with variable curvature and enhanced nonlinear behavior
        f8 = 0.18 * np.sum((x**4.1 + 0.5 * x**3.2 - 0.3 * x**1.9) * np.exp(-0.15 * np.abs(x)))
        
        # Add a global scaling factor to balance the contributions of all terms
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8