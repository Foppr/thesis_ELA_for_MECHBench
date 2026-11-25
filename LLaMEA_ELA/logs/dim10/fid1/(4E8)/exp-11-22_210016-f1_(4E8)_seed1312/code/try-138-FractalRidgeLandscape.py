import numpy as np

class FractalRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal-like term with power-law scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += (np.abs(x[i])**1.7 + 0.3 * np.abs(x[i])**3.1) * \
                           np.sin(2.0 * np.pi * x[i] / (1.0 + 0.1 * np.abs(x[i])))
        
        # Nested sinusoidal modulations with varying frequencies
        nested_mod = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * x[i])
            nested_mod += np.sin(freq * x[i]**2) * np.cos(freq * x[i]) * \
                         np.exp(-0.1 * x[i]**2)
        
        # Asymmetric dimensional coupling with exponential weights
        asym_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.2 * (x[i]**2 + x[j]**2))
                asym_coupling += weight * (np.sin(x[i]) * np.cos(x[j])**2 + 
                                         0.7 * np.cos(x[i]) * np.sin(x[j])**2)
        
        # Power-law based ridge structure with chaotic perturbations
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += (x[i]**2 + 0.2 * x[i]**4) * \
                         np.exp(-0.5 * np.abs(x[i])) * \
                         (1.0 + 0.3 * np.sin(5.0 * x[i]))
        
        # Cross-dimensional exponential interference
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.exp(-0.1 * (x[i]**2 + x[j]**2)) * \
                            np.sin(x[i] * x[j]) * \
                            np.cos(0.5 * (x[i] + x[j]))
        
        # Chaotic harmonic modulation with dynamic scaling
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(x[i]) * np.cos(3.0 * x[i]) * \
                          np.exp(-0.3 * x[i]**2) * \
                          (1.0 + 0.2 * np.sin(7.0 * x[i]))
        
        # Combine all terms with dynamic weighting
        result = 0.5 * fractal_term + 0.6 * nested_mod + 0.4 * asym_coupling + \
                 0.7 * ridge_term + 0.3 * cross_exp + 0.8 * chaotic_mod
        
        return result