import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute a more complex rotation matrix with orthogonalization
        self.rotation = np.random.rand(dim, dim)
        self.rotation = np.linalg.qr(self.rotation)[0]
        # Add a non-uniform shift to increase asymmetry
        self.shift = np.random.uniform(-1.0, 1.0, dim)
        # Add a random scaling factor for each dimension
        self.scales = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation, shift, and scaling
        x_scaled = self.scales * (np.dot(self.rotation, x) + self.shift)
        
        # Compute the multimodal function with enhanced chaotic and barrier components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with exponential scaling
            result += (x_scaled[i] ** 2) * np.exp(0.1 * i)
            # Composite sinusoidal components with chaotic modulation
            freq1 = (i + 1) * np.pi / 2
            freq2 = (i + 1) * np.pi / 4
            sin1 = np.sin(freq1 * x_scaled[i])
            sin2 = np.sin(freq2 * x_scaled[i])
            result += 5 * sin1 * sin2
            # Logarithmic barrier with exponential decay
            log_term = np.log(1 + np.abs(x_scaled[i]) ** 3)
            result += log_term * np.exp(-0.05 * i)
            # Exponential decay term with chaotic modulation
            exp_decay = np.exp(-0.1 * np.abs(x_scaled[i])) * np.sin(np.pi * x_scaled[i])
            result += exp_decay * (i + 1) * 0.2
            # Additional chaotic component using a tent map-like term
            tent_map = 1 - 2 * np.abs(x_scaled[i] - np.floor(x_scaled[i] + 0.5))
            result += tent_map * np.cos(x_scaled[i] * np.pi * (i + 1)) * 0.1
        
        # Add a penalty term for large values with a non-linear scaling
        result += 0.01 * np.sum(np.abs(x_scaled) ** 4)
        
        return result