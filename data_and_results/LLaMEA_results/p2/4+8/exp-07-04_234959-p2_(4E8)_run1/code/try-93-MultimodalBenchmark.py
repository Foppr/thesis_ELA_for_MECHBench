import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Perturbed global minimum with chaotic progression and dynamic offset
        self.global_min = np.array([(-1)**i * (2.0 + 0.5 * np.sin(i * np.pi / 3)) + 0.3 * np.sin(i * np.pi / 5) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive quadratic term with chaotic scaling and time-varying coefficients
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.2 * np.sin(2 * x + np.cos(x))))
        
        # Nested chaotic sinusoidal modulations with dynamic frequency coupling
        f2 = np.sum(np.sin(7.0 * x + np.cos(3.0 * x)) * np.cos(4.0 * x + np.sin(2.0 * x)) * np.sin(1.5 * x))
        
        # High-order polynomial with chaotic cross-terms and variable exponents
        f3 = np.sum(x**6 - 20 * x**4 + 100 * x**2 - 10 * np.sin(x))
        
        # Multi-scale exponential penalty with variable base and logarithmic correction
        f4 = np.sum(np.exp(0.5 * np.abs(x)) - 1 - 0.3 * np.log(1 + 0.5 * np.abs(x)) + 0.1 * np.sin(x))
        
        # Chaotic coupling with nested trigonometric functions and dynamic phase shifts
        f5 = np.sum(np.sin(np.cos(np.sin(x))) + np.cos(np.sin(np.cos(x))) + np.sin(0.7 * x) * np.cos(0.3 * x))
        
        # Modified interaction terms with chaotic weight variations and adaptive coupling
        f6 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.sin(0.8 * x) * np.cos(0.2 * x))
        
        # Additional chaotic term with time-varying amplitude and frequency
        f7 = np.sum(np.sin(np.pi * x * np.cos(x)) * np.cos(np.pi * x * np.sin(x)) * np.exp(-0.1 * x**2))
        
        # Combine all components with dynamically adjusted weights and chaotic scaling
        return 0.15 * f1 + 0.25 * f2 + 0.15 * f3 + 0.15 * f4 + 0.10 * f5 + 0.12 * f6 + 0.10 * f7