import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with slight bias
        f = 0.5 * np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Add periodic sinusoidal interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.3 * np.sin(2 * x[i]) * np.cos(3 * x[(i + 1) % self.dim]) * np.sin(5 * x[(i + 2) % self.dim])
            
        # Asymmetric saddle point contributions
        for i in range(self.dim):
            f += 0.2 * (x[i]**2 - x[(i + 1) % self.dim]**2)**2
            
        # Gradient-dependent conditioning: modify based on local gradient magnitude
        grad_magnitude = np.sqrt(np.sum(2 * x**2))  # Simplified gradient norm
        f += 0.05 * grad_magnitude * np.sum(np.abs(x))
        
        # Add chaotic cross-dimensional coupling with varying phase shifts
        for i in range(self.dim):
            f += 0.15 * np.sin(7 * x[i] + 0.5) * np.cos(4 * x[(i + 3) % self.dim] - 1.2)
            
        # Non-uniform penalty terms with exponential scaling
        f += 0.2 * np.sum(np.exp(0.2 * np.abs(x)) - 1)
        
        # Multi-modal interaction terms with varying intensities
        for i in range(self.dim):
            f += 0.25 * np.sin(6 * x[i]) * np.cos(9 * x[(i + 2) % self.dim]) * np.sin(3 * x[(i + 4) % self.dim])
            
        # Add a global saddle structure
        f += 0.1 * (np.sum(x**2) - self.dim)**2
        
        return f