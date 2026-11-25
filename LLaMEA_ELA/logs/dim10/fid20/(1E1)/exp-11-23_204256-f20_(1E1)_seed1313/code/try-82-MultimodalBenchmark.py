import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic sine-wave perturbations with non-uniform frequencies and amplitudes
        f2 = 0.7 * np.sum(np.sin(15 * np.pi * x_normalized + np.sin(7 * np.pi * x_normalized)) ** 2)
        f3 = 0.4 * np.sum(np.sin(25 * np.pi * x_normalized + np.sin(11 * np.pi * x_normalized)) ** 2)
        
        # Nested higher-order polynomial terms with exponential scaling
        f4 = 0.15 * np.sum(x_normalized**4)
        f5 = 0.08 * np.sum(x_normalized**6)
        
        # Exponentially modulated cosine terms for increased complexity
        f6 = 0.25 * np.sum(np.cos(10 * np.pi * x_normalized * np.exp(-0.1 * np.abs(x_normalized))) ** 2)
        
        # Complex cross-dimensional couplings with chaotic interactions
        f7 = 0.2 * np.sum(x_normalized[:-1] ** 4 * x_normalized[1:] * np.sin(5 * np.pi * x_normalized[:-1]))
        f8 = 0.18 * np.sum(x_normalized[:-2] ** 2 * x_normalized[1:-1] ** 3 * x_normalized[2:] ** 2 * np.cos(3 * np.pi * x_normalized[1:-1]))
        
        # Highly adaptive exponential conditioning factor
        adaptive_scale = 1.0 + 0.5 * np.exp(0.1 * self.dim) + 0.2 * np.sin(0.05 * self.dim)
        
        # Add chaotic noise term to increase non-smoothness
        noise = 0.05 * np.sum(np.random.rand(self.dim) * (1 + np.abs(x_normalized)))
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8) + noise