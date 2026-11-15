import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Perturbed global minimum position with chaotic offset
        self.global_min = np.array([(-1)**i * 2.5 + 0.5 * np.sin(i * np.pi / 4) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling and fractional noise
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.1 * np.sin(x) + 0.05 * np.random.randn()))
        
        # Enhanced sinusoidal modulations with chaotic frequency progression and fractal noise
        f2 = np.sum(np.sin(5.0 * x + np.cos(x)) * np.cos(3.0 * x + np.sin(x)) * (1 + 0.1 * np.random.randn()))
        
        # Higher-order polynomial interactions with cross-terms and chaotic coupling
        f3 = np.sum(x**5 - 15 * x**3 + 50 * x + 0.01 * np.sum(x**6 * np.sin(x)))
        
        # Exponential penalty with logarithmic scaling and chaotic perturbation
        f4 = np.sum(np.exp(0.3 * np.abs(x)) - 1 - 0.2 * np.log(1 + np.abs(x)) + 0.05 * np.sin(x**2))
        
        # Chaotic component using nested sine and cosine with fractal modulation
        f5 = np.sum(np.sin(np.cos(x)) + np.cos(np.sin(x)) + 0.03 * np.random.randn() * np.sin(x))
        
        # Additional chaotic coupling term with modified interaction and fractional scaling
        f6 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.sin(0.5 * x) * (1 + 0.05 * np.random.randn()))
        
        # Cross-dimensional coupling with chaotic phase shifts and fractal noise
        f7 = np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) * np.exp(-0.1 * np.abs(x[:-1] - x[1:])) * (1 + 0.02 * np.random.randn()))
        
        # Add a fractional Brownian motion-like fractal component for increased complexity
        fractal = np.sum(np.sin(2**np.arange(1, self.dim+1) * x) * (1 / (2**np.arange(1, self.dim+1))))
        
        # Nested chaotic coupling with adaptive modulation and enhanced fractal structure
        nested_coupling = np.sum(np.sin(np.sin(x) * np.cos(x)) * np.cos(np.cos(x) * np.sin(x)) * (1 + 0.03 * np.random.randn()) * np.sin(0.3 * x))
        
        # Adaptive fractal modulation with dynamic scaling factors
        adaptive_fractal = np.sum(np.sin(np.power(2, np.arange(1, self.dim+1)) * x) * (1 / np.power(2, np.arange(1, self.dim+1) * (1 + 0.1 * np.sin(x)))))
        
        # Enhanced chaotic interference with dynamic coupling and modified weights
        chaotic_interference = np.sum(np.sin(x * np.sin(x)) * np.cos(x * np.cos(x)) * (1 + 0.08 * np.random.randn()) * np.cos(0.4 * x**2))
        
        # Multi-scale fractal modulation with varying frequency components
        multi_scale_fractal = np.sum(np.sin(np.arange(1, self.dim+1) * x * np.sin(x)) * (1 / np.arange(1, self.dim+1)**1.5))
        
        # Enhanced cross-dimensional coupling with dynamic phase shifts
        enhanced_coupling = np.sum(np.sin(x[:-1] * x[1:] + np.cos(x[:-1] + x[1:])) * np.cos(x[:-1] * x[1:] - np.sin(x[:-1] - x[1:])) * (1 + 0.04 * np.random.randn()))
        
        # Combined chaotic and fractal components with varying weights
        return 0.12 * f1 + 0.18 * f2 + 0.12 * f3 + 0.12 * f4 + 0.08 * f5 + 0.06 * f6 + 0.10 * f7 + 0.06 * fractal + 0.04 * nested_coupling + 0.04 * adaptive_fractal + 0.05 * chaotic_interference + 0.03 * multi_scale_fractal + 0.03 * enhanced_coupling