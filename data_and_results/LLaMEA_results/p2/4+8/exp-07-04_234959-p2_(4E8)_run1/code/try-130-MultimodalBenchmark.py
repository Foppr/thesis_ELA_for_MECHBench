import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Perturbed global minimum with chaotic offset and fractal noise
        self.global_min = np.array([(-1)**i * 2.5 + 0.5 * np.sin(i * np.pi / 4) + 0.1 * np.random.randn() for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling and fractal modulation
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.1 * np.sin(x) + 0.05 * np.cos(x**2)))
        
        # Enhanced sinusoidal modulations with chaotic frequency progression and fractal coupling
        f2 = np.sum(np.sin(5.0 * x + np.cos(x)) * np.cos(3.0 * x + np.sin(x)) * (1 + 0.1 * np.sin(np.sum(x))))
        
        # Higher-order polynomial interactions with cross-terms and dynamic coupling
        f3 = np.sum(x**5 - 15 * x**3 + 50 * x + 0.5 * x**4 * np.sin(x))
        
        # Exponential penalty with logarithmic scaling and chaotic perturbation
        f4 = np.sum(np.exp(0.3 * np.abs(x)) - 1 - 0.2 * np.log(1 + np.abs(x)) + 0.05 * np.sin(x**3))
        
        # Chaotic component using nested sine and cosine with fractal scaling
        f5 = np.sum(np.sin(np.cos(x)) + np.cos(np.sin(x)) + 0.1 * np.sin(np.cos(x**2)))
        
        # Additional chaotic coupling term with modified interaction and fractal noise
        f6 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.sin(0.5 * x) * (1 + 0.05 * np.cos(x)))
        
        # Introduce a new chaotic interaction term with dynamic coupling and fractional Brownian motion
        f7 = np.sum(np.sin(x * np.sin(x)) * np.cos(x * np.cos(x)) * np.exp(-0.1 * x**2) * (1 + 0.1 * np.sin(np.sum(x))))
        
        # Add a new fractal noise component with chaotic scaling
        f8 = np.sum(0.1 * np.sin(x * np.pi * np.exp(x)) * np.cos(x * np.pi * np.log(1 + np.abs(x))))
        
        # Combine all components with varying weights and chaotic scaling
        return 0.10 * f1 + 0.25 * f2 + 0.20 * f3 + 0.15 * f4 + 0.10 * f5 + 0.12 * f6 + 0.08 * f7 + 0.05 * f8