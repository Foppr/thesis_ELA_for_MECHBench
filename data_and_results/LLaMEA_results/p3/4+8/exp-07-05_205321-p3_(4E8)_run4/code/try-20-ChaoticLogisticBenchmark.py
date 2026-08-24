import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension does not match function dimension")
        
        # Clamp input to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize chaotic system with logistic maps
        chaos_value = 0.0
        r = 3.99  # Chaotic parameter
        
        # Use each dimension as initial condition for logistic map
        for i in range(self.dim):
            # Apply logistic map iterations
            xi = x[i]
            for _ in range(100):  # Burn-in iterations
                xi = r * xi * (1 - xi)
            
            # Accumulate chaotic contribution
            chaos_value += xi * np.sin(xi * np.pi)
        
        # Add quadratic basin term to encourage convergence
        basin = 0.1 * np.sum(x**2)
        
        # Add periodic interference terms for multimodality
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(2 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
            
        # Add interaction terms between dimensions
        interaction = 0
        for i in range(self.dim-1):
            interaction += np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
            
        # Add noise for increased complexity
        noise = 0.01 * np.sum(np.random.rand(self.dim) * x)
        
        return basin + 0.5 * chaos_value + 0.3 * periodic + 0.2 * interaction + noise