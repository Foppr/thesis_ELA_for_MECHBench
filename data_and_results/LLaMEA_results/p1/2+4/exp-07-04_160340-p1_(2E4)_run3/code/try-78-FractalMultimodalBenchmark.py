import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Generate fractal-like structure using iterative complex polynomial mapping
        # z_{n+1} = z_n^2 + c, where c is a complex constant based on input
        result = 0.0
        for i in range(self.dim):
            # Create complex variable from real input
            z = complex(x[i], 0.0)
            c = complex(np.sin(x[i]), np.cos(x[i]))
            
            # Iterate complex polynomial map
            for _ in range(5):  # 5 iterations for fractal complexity
                z = z * z + c
            
            # Use real part of result for fitness
            result += abs(z.real) ** 2
        
        # Add multiple global minima at different locations
        minima_positions = [
            np.array([0.0] * self.dim),
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with varying weights
        penalty = 0.0
        weights = [0.8, 0.6, 0.7, 0.5, 0.4, 0.9, 0.3]
        for i, (pos, weight) in enumerate(zip(minima_positions, weights)):
            distance = np.sum((x - pos)**2)
            penalty += weight * np.exp(-distance / (2.0 * (i + 1)**2))
        
        # Add non-smooth discontinuous regions
        discontinuity = 0.0
        for i in range(self.dim):
            discontinuity += np.abs(np.sin(np.pi * x[i])) * np.abs(np.cos(np.pi * x[i]))
        
        # Combine all terms
        result = result + penalty + 0.1 * discontinuity
        
        # Add nested structure with varying scales
        nested = 0.0
        for i in range(self.dim):
            nested += np.sin(10 * x[i]) * np.cos(5 * x[i])
        
        result += 0.05 * nested
        
        return result