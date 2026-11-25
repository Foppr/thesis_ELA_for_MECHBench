import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Enhanced fractal sinusoidal modulations with higher frequency chaos and perturbed scaling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Increased chaotic modulation with fractional frequency and phase shifts
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 1.1)) * (1.0 + 0.5 * np.cos(i * 0.9))
            mod = np.sin(freq * xi) * np.cos(freq * xi**2.3) * np.exp(-0.3 * np.abs(xi))
            f2 += mod**2
        
        # Stronger polynomial corruption with irregular fractional powers and asymmetric coefficients
        f3 = 0.05 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.6 * x**3.8 + 0.3 * x**2.5) / self.dim)
        
        # Multi-scale saddle point structure with complex exponential and trigonometric interference
        f4 = 0.3 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Recursive fractal self-similarity with higher frequency nested components and non-uniform scaling
        f5 = 0.3 * np.sum(np.sin(55.0 * np.sin(15.0 * x)) * np.cos(45.0 * np.cos(12.0 * x)))
        
        # Stronger cross-term interactions with asymmetric coupling and non-linear phase modulation
        f6 = 0.08 * np.sum(np.sin(x[:-1] + 0.7 * x[1:]) * np.cos(1.2 * x[:-1] - 0.8 * x[1:]))
        
        # Fractional Brownian motion-like roughness with enhanced variance and irregular exponents
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x))
        
        # Asymmetric saddle points with variable curvature, higher-order polynomial terms, and exponential decay
        f8 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.1 - 0.5 * x**2.3) * np.exp(-0.15 * np.abs(x)))
        
        # Introduce novel chaotic coupling terms with modified interaction strengths and higher-order nonlinearities
        f9 = 0.1 * np.sum(np.sin(20.0 * x + 0.5 * np.sin(5.0 * x)) * np.cos(10.0 * x**1.5))
        
        # Combine all components with adjusted weights for improved fitness and discrimination
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9