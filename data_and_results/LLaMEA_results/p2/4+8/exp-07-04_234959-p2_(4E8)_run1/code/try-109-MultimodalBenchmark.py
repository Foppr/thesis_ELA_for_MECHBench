import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamically shifted global minimum with chaotic progression
        self.global_min = np.array([(-1)**i * 2.0 + 0.3 * np.sin(i * np.pi / 3 + np.sqrt(i + 1)) for i in range(dim)])
        # Adaptive noise parameters
        self.noise_scale = 0.5 + 0.2 * np.sin(dim * np.pi / 4)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic scaling and chaotic modulation
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.2 * np.sin(x * np.cos(x))))
        
        # Enhanced sinusoidal modulations with chaotic frequency progression and cross-dimensional coupling
        f2 = np.sum(np.sin(7.0 * x + np.cos(x)) * np.cos(4.0 * x + np.sin(x)) * np.sin(0.5 * np.sum(x**2)))
        
        # Higher-order polynomial interactions with cross-terms and chaotic coupling
        f3 = np.sum(x**6 - 20 * x**4 + 100 * x**2 + 10 * np.sin(x) * np.cos(x))
        
        # Exponential penalty with logarithmic scaling and adaptive weight
        f4 = np.sum(np.exp(0.4 * np.abs(x)) - 1 - 0.3 * np.log(1 + np.abs(x)) + 0.1 * np.sin(x))
        
        # Chaotic component using nested sine and cosine with dynamic phase
        f5 = np.sum(np.sin(np.cos(x + np.sin(x))) + np.cos(np.sin(x + np.cos(x))))
        
        # Additional chaotic coupling term with modified interaction and noise injection
        noise = self.noise_scale * np.random.normal(0, 1, self.dim)
        f6 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.sin(0.7 * x + noise))
        
        # Combine all components with varying weights and chaotic scaling
        return 0.15 * f1 + 0.25 * f2 + 0.20 * f3 + 0.15 * f4 + 0.10 * f5 + 0.15 * f6