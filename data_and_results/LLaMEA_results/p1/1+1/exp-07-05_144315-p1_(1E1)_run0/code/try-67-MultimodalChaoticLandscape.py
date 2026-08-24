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
        
        # Modified multimodal component with shifted Gaussian peaks
        multimodal = 0.0
        for i in range(1, 7):
            center = np.full(self.dim, i * 0.4)
            multimodal += np.exp(-0.3 * np.sum((x - center)**2)) * np.sin(3 * np.pi * np.sum(x - center))
        
        # Add higher-order polynomial terms for increased nonlinearity
        cubic = 0.03 * np.sum(x**3)
        quartic = 0.008 * np.sum(x**4)
        
        # Modified global scaling with distance from origin
        distance = np.sqrt(np.sum(x**2))
        scaling = 1.0 + 0.15 * distance + 0.02 * distance**2
        
        # Add chaotic modulation term
        chaotic = 0.1 * np.sum(np.sin(10 * x) * np.cos(5 * x))
        
        # Introduce additional chaotic modulation with different frequency
        chaotic2 = 0.05 * np.sum(np.sin(15 * x) * np.cos(3 * x) * np.exp(-0.02 * x**2))
        
        # Add a new component with exponential decay and sinusoidal modulation
        exp_sin = 0.2 * np.sum(np.exp(-0.22 * x**2) * np.sin(5 * x))
        
        # Combine all components with adjusted weights
        return radial + 0.8 * sin_osc + 0.45 * cross_term + 0.6 * multimodal + cubic + quartic + scaling + chaotic + chaotic2 + exp_sin