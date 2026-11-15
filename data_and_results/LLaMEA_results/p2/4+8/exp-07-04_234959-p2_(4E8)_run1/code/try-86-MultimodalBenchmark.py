import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize a chaotic global minimum with radial displacement
        self.global_min = np.array([2.5 * np.cos(i * np.pi / 3) + 0.5 * np.sin(i * np.pi / 5) for i in range(dim)])
    
    def f(self, x):
        # Clip input to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis component with adaptive scaling
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f1 = r * np.exp(-0.1 * r) + 0.1 * r**2
        
        # Trigonometric coupling with frequency modulation
        f2 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)))
        
        # Polynomial chaos with cross-terms
        f3 = np.sum(x**4 - 10 * x**2 + 20 * np.cos(x))
        
        # Adaptive noise component
        noise = np.random.normal(0, 0.1, self.dim)
        f4 = np.sum(np.abs(x - self.global_min) * (1 + 0.2 * np.sin(x + noise)))
        
        # Exponential barrier with sinusoidal modulation
        f5 = np.sum(np.exp(0.5 * np.abs(x)) * np.sin(x)**2)
        
        # Chaotic radial interaction term
        f6 = np.sum(np.sin(r + np.cos(x)) * np.cos(r + np.sin(x)))
        
        # Combine all terms with dynamic weights
        return 0.2 * f1 + 0.25 * f2 + 0.15 * f3 + 0.2 * f4 + 0.1 * f5 + 0.1 * f6