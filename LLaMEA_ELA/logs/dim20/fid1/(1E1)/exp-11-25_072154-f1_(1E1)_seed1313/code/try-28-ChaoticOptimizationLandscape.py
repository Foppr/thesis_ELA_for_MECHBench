import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with multiple exponential terms
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-r) * (1 + 0.3 * np.sin(3 * r) + 0.2 * np.cos(7 * r))
        
        # Modified trigonometric oscillations with varying frequencies
        trig = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Enhanced exponential interaction terms with cross-dimensional coupling
        exp_interaction = 0.0
        for i in range(self.dim - 1):
            exp_interaction += np.exp(-0.3 * (x_scaled[i] - x_scaled[i+1])**2) * (1 + 0.1 * np.sin(5 * (x_scaled[i] + x_scaled[i+1])))
        
        # Chaotic component with higher frequency oscillations
        chaotic = np.sum(np.sin(15 * r**2) * np.cos(12 * r**2) * np.exp(-0.5 * r))
        
        # Additional harmonic component for increased complexity
        harmonic = np.sum(np.sin(4 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled))
        
        # Combine all components with optimized weights
        return 0.35 * radial + 0.25 * trig + 0.2 * exp_interaction + 0.15 * chaotic + 0.05 * harmonic