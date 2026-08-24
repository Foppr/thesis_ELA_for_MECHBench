import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize time-varying global minimum with chaotic dynamics
        self.t = 0.0
        self.global_min = np.array([2.0 * np.sin(i * 0.3 + self.t) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial coupling with varying exponents
        f1 = np.sum((x - self.global_min)**3 + 0.5 * (x - self.global_min)**2)
        
        # Exponential barrier terms with dynamic scaling
        f2 = np.sum(np.exp(-0.5 * (x - self.global_min)**2) * np.cos(2.0 * x))
        
        # Trigonometric modulation with adaptive frequency
        f3 = np.sum(np.sin(3.0 * x + np.cos(x)) * np.exp(-0.1 * np.abs(x)))
        
        # Time-varying component for global minimum
        self.t += 0.01
        self.global_min = np.array([2.0 * np.sin(i * 0.3 + self.t) for i in range(self.dim)])
        
        # Add adaptive noise to increase robustness
        noise = np.random.normal(0, 0.01, self.dim)
        f4 = np.sum((x - self.global_min + noise)**2 * np.sin(x))
        
        # Hyperbolic tangent and logarithmic interaction
        f5 = np.sum(np.tanh(x) * np.log(1.0 + np.abs(x)))
        
        # Combine all components with optimized weights
        return 0.3 * f1 + 0.25 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5