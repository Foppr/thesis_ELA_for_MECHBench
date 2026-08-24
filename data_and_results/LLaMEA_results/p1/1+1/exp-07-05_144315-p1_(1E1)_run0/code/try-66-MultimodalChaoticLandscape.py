import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple peaks
        radial = np.sum((x**2) * np.exp(-0.1 * x**2))
        
        # Sinusoidal oscillations with varying frequencies
        sin_osc = np.sum(np.sin(3 * x) * np.cos(7 * x) * np.exp(-0.05 * x**2))
        
        # Enhanced cross-term interactions creating complex landscape
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.exp(-0.12 * (x[i]**2 + x[j]**2)) * np.cos(0.5 * x[i] * x[j])
        
        # Increased multimodal component with more and stronger Gaussian peaks
        multimodal = 0.0
        for i in range(1, 11):  # Increased from 6 to 10 peaks
            center = np.full(self.dim, i * 0.35)  # Reduced spacing
            multimodal += 1.5 * np.exp(-0.25 * np.sum((x - center)**2)) * np.sin(4 * np.pi * np.sum(x - center))
        
        # Add higher-order polynomial terms for increased nonlinearity
        cubic = 0.04 * np.sum(x**3)
        quartic = 0.01 * np.sum(x**4)
        
        # Modified global scaling with distance from origin
        distance = np.sqrt(np.sum(x**2))
        scaling = 1.0 + 0.2 * distance + 0.025 * distance**2
        
        # Stronger chaotic modulation term
        chaotic = 0.15 * np.sum(np.sin(12 * x) * np.cos(6 * x))
        
        # Additional chaotic modulation with different frequency
        chaotic2 = 0.08 * np.sum(np.sin(18 * x) * np.cos(4 * x) * np.exp(-0.03 * x**2))
        
        # Add a new component with exponential decay and sinusoidal modulation
        exp_sin = 0.25 * np.sum(np.exp(-0.25 * x**2) * np.sin(6 * x))
        
        # Combine all components with adjusted weights
        return radial + 0.85 * sin_osc + 0.5 * cross_term + 0.7 * multimodal + cubic + quartic + scaling + chaotic + chaotic2 + exp_sin