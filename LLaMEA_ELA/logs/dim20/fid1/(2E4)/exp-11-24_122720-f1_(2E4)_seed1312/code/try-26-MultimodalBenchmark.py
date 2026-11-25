import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillation component with exponential modulation
        chaotic_osc = 0
        for i in range(self.dim):
            chaotic_osc += (np.sin(x[i]) * np.cos(x[i] * np.pi / (i + 1)) * 
                           np.exp(-0.1 * x[i]**2) * np.sin(3 * x[i] * np.pi / (i + 1)))
        
        # Multi-modal radial basis function with dynamic centers
        rbf = 0
        for i in range(self.dim):
            center = 2 * np.sin(i * np.pi / 4) + 0.5 * np.cos(i * np.pi / 2)
            rbf += np.exp(-0.5 * (x[i] - center)**2 / (0.5 + i * 0.05)) * (1 + 0.1 * np.sin(i))
        
        # Hybrid penalty term with both quartic and exponential components
        hybrid_penalty = 0
        for i in range(self.dim):
            term1 = x[i]**4 - 6 * x[i]**3 + 11 * x[i]**2 - 6 * x[i]
            term2 = np.exp(-0.5 * x[i]**2) * np.sin(2 * x[i])
            hybrid_penalty += (term1**2 + 0.5 * term2**2)
        
        # Adaptive scaling factors based on dimensionality
        scale1 = 0.3 + 0.1 * np.sin(self.dim * np.pi / 8)
        scale2 = 0.4 + 0.2 * np.cos(self.dim * np.pi / 6)
        scale3 = 0.01 + 0.005 * np.sin(self.dim * np.pi / 4)
        
        # Combine all components with dynamic weighting
        return scale1 * chaotic_osc + scale2 * rbf + scale3 * hybrid_penalty + 3 * self.dim