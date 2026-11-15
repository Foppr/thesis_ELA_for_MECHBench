import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamically shift global minimum with chaotic perturbation using logistic map
        self.global_min = np.array([5.0 * np.sin(i * 0.7) * np.cos(i * 0.3) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis component with chaotic scaling and sinusoidal modulation
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f1 = r * (1.0 + 0.3 * np.sin(3.0 * r) * np.cos(2.0 * r))
        
        # Trigonometric modulations with dynamic frequencies and phase shifts
        f2 = np.sum(np.sin(3.0 * x + np.cos(2.0 * x)) * np.cos(2.5 * x + np.sin(1.5 * x)) * np.exp(-0.1 * np.abs(x)))
        
        # Logarithmic penalty with variable base and chaotic modulation
        f3 = np.sum(np.log(1.0 + 0.7 * np.abs(x)) * (1.0 + 0.2 * np.sin(4.0 * x) * np.cos(3.0 * x)))
        
        # Hyperbolic and exponential component with adaptive scaling
        f4 = np.sum(np.tanh(x) * np.exp(-0.3 * x**2) * np.sin(2.0 * x))
        
        # Chaotic sine composition with multiple phase modulations and step-like transitions
        f5 = np.sum(np.sin(np.pi * np.sin(np.cos(x))) * np.cos(np.pi * np.cos(np.sin(x))) * np.log(1.0 + np.abs(x)))
        
        # Additional cubic polynomial coupling terms for increased complexity
        f6 = np.sum((x**3) * np.sin(x) * np.cos(0.5 * x))
        
        # Combine all components with optimized weights and chaotic scaling factors
        return 0.15 * f1 + 0.2 * f2 + 0.15 * f3 + 0.15 * f4 + 0.15 * f5 + 0.2 * f6