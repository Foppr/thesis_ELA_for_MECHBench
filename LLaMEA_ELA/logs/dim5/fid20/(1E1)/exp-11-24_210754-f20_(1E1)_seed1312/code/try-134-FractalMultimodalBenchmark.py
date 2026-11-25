import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Highly oscillatory fractal structure with chaotic Gaussian modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic frequency modulation with Gaussian perturbations
            freq = 50.0 * (1.0 + 0.7 * np.sin(i * 0.9)) * np.exp(-0.1 * i)
            # Superimposed chaotic Gaussian field
            gaussian_mod = np.exp(-0.5 * (xi - np.sin(i * 0.3))**2 / (0.5 + 0.2 * np.cos(i * 0.4)))
            mod = np.sin(freq * xi) * gaussian_mod * np.cos(freq * xi**1.8)
            f2 += mod**2
        
        # Enhanced polynomial corruption with fractional powers and dynamic coefficients
        f3 = 0.05 * np.sum((x**6.2 + 0.9 * x**5.7 + 0.7 * x**3.4 + 0.4 * x**2.8 + 0.1 * x**1.9) / self.dim)
        
        # Saddle point structure with multi-scale interference and exponential decay
        f4 = 0.3 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(15.0 * x) * np.cos(10.0 * x) * np.tanh(2.0 * x))
        
        # Fractal self-similarity with recursive scaling and high-frequency components
        f5 = 0.3 * np.sum(np.sin(60.0 * np.sin(15.0 * x)) * np.cos(50.0 * np.cos(12.0 * x)) * np.exp(-0.1 * np.abs(x)))
        
        # Cross-term interactions with asymmetric coupling and dynamic weights
        f6 = 0.08 * np.sum(np.sin(0.8 * x[:-1] + 1.2 * x[1:]) * np.cos(1.5 * x[:-1] - 0.7 * x[1:]) * (1.0 + 0.3 * np.sin(i * 0.6)))
        
        # Fractional Brownian motion-like roughness with increased variance and multi-scale features
        f7 = 0.15 * np.sum(np.abs(x)**1.8 * np.sin(25.0 * x) * np.cos(15.0 * x))
        
        # Asymmetric saddle points with varying curvature, enhanced nonlinearity, and stochastic perturbations
        f8 = 0.2 * np.sum((x**4.1 + 0.7 * x**3.5 - 0.5 * x**2.2 + 0.2 * x) * np.exp(-0.15 * np.abs(x)) * (1.0 + 0.2 * np.sin(x)))
        
        # Additional chaotic coupling terms with dynamic scaling and phase shifts
        f9 = 0.1 * np.sum(np.sin(20.0 * x + 0.5 * np.sin(30.0 * x)) * np.cos(15.0 * x + 0.3 * np.cos(25.0 * x)))
        
        # Combine all components with adjusted weights for improved fitness and complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9