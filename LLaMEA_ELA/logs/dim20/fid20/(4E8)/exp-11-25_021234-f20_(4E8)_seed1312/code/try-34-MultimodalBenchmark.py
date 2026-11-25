import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = 0.1 * np.sum(x**2)
        
        # Multi-scale fractal-like oscillations with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(1, 6):
            freq = 2 ** i
            amp = 1.0 / (i * 2.0)
            f2 += amp * np.sum(np.sin(freq * x) * np.cos(freq * x**2))
        
        # Adaptive noise component that changes based on x magnitude
        noise_amp = 0.05 * (1 + np.mean(np.abs(x)) / 5.0)
        f3 = noise_amp * np.sum(np.random.uniform(-1, 1, self.dim) * np.sin(3.0 * x))
        
        # Central attracting basin with exponential decay
        center_dist = np.sqrt(np.sum((x - np.zeros_like(x))**2))
        f4 = 0.5 * np.exp(-0.1 * center_dist**2)
        
        # Additional high-frequency perturbation to increase complexity
        f5 = 0.02 * np.sum(np.sin(20.0 * x) * np.exp(-0.5 * x**2))
        
        return f1 + f2 + f3 + f4 + f5