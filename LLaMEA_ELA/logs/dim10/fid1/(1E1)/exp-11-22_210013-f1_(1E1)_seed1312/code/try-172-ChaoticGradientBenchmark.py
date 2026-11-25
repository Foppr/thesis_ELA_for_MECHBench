import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.1
        self.c = 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize chaotic sequence
        chaotic_seq = np.zeros(self.dim)
        for i in range(self.dim):
            if i == 0:
                chaotic_seq[i] = 0.5
            else:
                chaotic_seq[i] = self.a * chaotic_seq[i-1] * (1 - chaotic_seq[i-1])
        
        # Chaotic gradient component with exponential decay
        grad_chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic sequence to modulate gradient direction
            modulation = np.sin(chaotic_seq[i] * np.pi * 2) + 1.0
            grad_chaotic += modulation * np.exp(-self.b * (xi - 1)**2) * (xi - 1)**3
        
        # Saddle point structure with multiple interacting peaks
        saddle = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create saddle points at various locations
            saddle += (xi**2 - 4)**2 + (xi - 2)**4
            
        # Non-convex interaction terms with varying weights
        interaction = 0.0
        for i in range(self.dim):
            xi = x[i]
            x_next = x[(i + 1) % self.dim]
            interaction += 0.3 * np.sin(5 * xi) * np.cos(3 * x_next)
            interaction += 0.2 * xi**4 * np.sin(2 * x_next)
            
        # Add global structure with periodicity and noise
        global_struct = 0.0
        for i in range(self.dim):
            xi = x[i]
            global_struct += 0.5 * np.cos(4 * xi) + 0.1 * np.sin(20 * xi)
            
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            xi = x[i]
            noise += 0.1 * np.sin(30 * xi) * np.cos(25 * xi)
            
        # Combine all components with different scaling factors
        return 1.2 * grad_chaotic + 0.8 * saddle + 1.5 * interaction + 0.6 * global_struct + 0.4 * noise