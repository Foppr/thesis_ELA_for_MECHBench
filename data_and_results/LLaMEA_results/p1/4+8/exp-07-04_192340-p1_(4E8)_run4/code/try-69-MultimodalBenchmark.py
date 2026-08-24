import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coefficients and dynamic parameters
        self.coeffs = np.random.rand(dim) * 3 + 1
        self.saddle_points = np.random.rand(dim) * 10 - 5
        self.phase_shifts = np.random.rand(dim) * np.pi
        self.frac_orders = np.random.rand(dim) * 0.5 + 0.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic exponential terms with dynamic saddle points
        result = 0.0
        for i in range(self.dim):
            # Exponential decay with chaotic coefficients and phase shifts
            result += self.coeffs[i] * np.exp(-0.5 * (x[i] - self.saddle_points[i])**2)
            # Saddle point contribution with varying curvature and fractional gradients
            result += 0.5 * (x[i] - self.saddle_points[i])**2 * np.sin(x[i] + self.phase_shifts[i])
            # Fractional-order gradient component for ultra-complex curvature
            result += 0.1 * np.sin(self.coeffs[i] * x[i]**self.frac_orders[i]) * np.cos(x[i])
            # Quaternion-inspired coupling terms for increased multimodality
            if i > 0:
                result += 0.2 * np.sin(x[i-1] * x[i]) * np.cos(0.5 * (x[i-1] + x[i]))
                
        # Add high-order coupling terms for ultra-complex landscape
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for efficiency
                result += 0.03 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * (i + j)
                
        # Add global minimum with ultra-complex penalty
        result += 0.0001 * np.sum(np.abs(x)**7)
        
        # Add chaotic noise component
        noise = np.sum(np.sin(10 * x) * np.cos(5 * x))
        result += 0.01 * noise
        
        return result