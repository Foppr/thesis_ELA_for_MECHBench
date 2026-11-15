import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Global minimum perturbed by a chaotic logistic map
        self.global_min = np.array([0.5 * (1 + np.tanh(i * 0.3)) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like component with self-similar structure
        f1 = np.sum(np.sin(2 ** np.floor(np.log2(np.abs(x) + 1e-8))) * np.cos(2 ** np.ceil(np.log2(np.abs(x) + 1e-8))))
        
        # Adaptive polynomial coupling with chaotic scaling
        f2 = np.sum((x**3 - 3 * x) * np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Multi-scale sinusoidal interference
        f3 = np.sum(np.sin(10 * x) + np.cos(7 * x) + np.sin(4 * x) + np.cos(2 * x))
        
        # Exponential barrier with logarithmic perturbation
        f4 = np.sum(np.exp(0.2 * np.abs(x)) * np.log(1 + np.abs(x)))
        
        # Chaotic logistic map component for global minimum perturbation
        logistic_map = np.array([0.5 * (1 + np.tanh(i * 0.3)) for i in range(self.dim)])
        f5 = np.sum((x - logistic_map)**2 * (1 + 0.05 * np.sin(x)))
        
        # Fractional Brownian motion-like fractal noise
        f6 = np.sum(np.sin(x * np.pi) * np.cos(x * np.pi / 2) * np.sin(x * np.pi / 3))
        
        # Combine all components with varying weights
        return 0.2 * f1 + 0.2 * f2 + 0.15 * f3 + 0.2 * f4 + 0.15 * f5 + 0.1 * f6