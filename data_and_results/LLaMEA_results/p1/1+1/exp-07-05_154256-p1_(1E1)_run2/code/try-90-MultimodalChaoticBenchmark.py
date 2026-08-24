import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.sigma = 0.1
        self.alpha = 2.0
        self.beta = 3.0
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**4 + 0.3 * r**3 + 0.1 * r**2
        
        # Sinusoidal waves with varying frequencies and amplitudes
        wave_term = 0
        for i in range(self.dim):
            wave_term += np.sin(self.alpha * x[i]) * np.cos(self.beta * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional interaction terms
        interaction_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += (x[i] * x[j]) * np.sin(0.5 * (x[i] + x[j]))
                
        # Chaotic modulation based on radial distance
        chaotic_mod = 1.0 + 0.3 * np.sin(10 * r) * np.cos(5 * r)
        
        # Add noise-like perturbations
        noise = np.sum(np.sin(20 * x) * np.cos(15 * x))
        
        # Combine all terms
        result = (radial_term + 
                  2.0 * wave_term + 
                  0.5 * interaction_term + 
                  0.2 * noise) * chaotic_mod
        
        return result