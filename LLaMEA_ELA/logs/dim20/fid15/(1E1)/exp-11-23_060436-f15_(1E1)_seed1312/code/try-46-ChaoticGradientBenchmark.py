import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2) * 0.1
        
        # Chaotic gradient component with periodic attractors
        chaotic = 0
        for i in range(self.dim):
            # Multi-attractor periodic function with exponential decay
            attractor1 = np.sin(3.0 * x[i]) * np.exp(-0.5 * (x[i] - 1.0)**2)
            attractor2 = np.cos(2.5 * x[i]) * np.exp(-0.3 * (x[i] + 2.0)**2)
            attractor3 = np.sin(1.8 * x[i]) * np.exp(-0.7 * (x[i] - 3.0)**2)
            chaotic += attractor1 + attractor2 + attractor3
            
        # Saddle-point enhancing component with cross-dimension interactions
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                # Create saddle-like structure using product of sinusoids
                saddle += np.sin(2.0 * x[i]) * np.cos(1.5 * x[j]) * \
                         np.exp(-0.1 * (x[i]**2 + x[j]**2)) * \
                         np.sin(0.5 * (x[i] - x[j])**2)
        
        # High-frequency oscillation component to increase condition number
        oscillation = 0
        for i in range(self.dim):
            # Add rapidly varying terms that create many local optima
            oscillation += (np.sin(10.0 * x[i]) + np.cos(15.0 * x[i])) * \
                          np.exp(-0.05 * x[i]**2) * \
                          (1.0 + 0.1 * np.sin(5.0 * x[i]))
        
        # Combine all components with carefully chosen weights
        return quadratic + chaotic * 0.4 + saddle * 0.3 + oscillation * 0.3