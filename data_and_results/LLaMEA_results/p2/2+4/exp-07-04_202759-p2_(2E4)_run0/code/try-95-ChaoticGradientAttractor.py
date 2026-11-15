import numpy as np

class ChaoticGradientAttractor:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic coefficients for dynamic modulation
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component with adaptive conditioning
        quadratic = np.sum(self.coeffs * x**2)
        
        # Chaotic gradient modulation with periodic attractors
        chaotic_grad = 0
        for i in range(self.dim):
            # Periodic attractor function with varying frequency
            freq = 2 * np.pi * (1 + 0.5 * np.sin(0.3 * x[i]))
            chaotic_grad += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Saddle-point corridor with multi-scale interactions
        corridor = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for multi-scale
                dist = np.abs(x[i] - x[j])
                corridor += np.sin(10 * dist) * np.exp(-0.5 * dist**2) * (1 + 0.2 * np.sin(3 * x[i]))
        
        # Adaptive conditioning based on position
        adaptive = 0
        for i in range(self.dim):
            adaptive += (1 + 0.3 * np.sin(2 * x[i])) * np.exp(-0.2 * x[i]**2) * x[i]**3
        
        # Multi-modal component with dynamic peaks
        multimodal = 0
        for i in range(self.dim):
            # Dynamic peak positions based on x values
            peak_pos = 2 * np.sin(0.5 * x[i]) + 0.5 * np.cos(0.7 * x[i])
            multimodal += np.exp(-0.5 * (x[i] - peak_pos)**2) * np.sin(5 * x[i])
        
        # Combine all components with dynamic weights
        return 0.3 * quadratic + 0.25 * chaotic_grad + 0.2 * corridor + 0.15 * adaptive + 0.1 * multimodal