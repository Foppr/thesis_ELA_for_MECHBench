import numpy as np

class FractalRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like term with power-law scaling and chaotic modulation
        fractal_term = 0.0
        for i in range(self.dim):
            base = np.abs(x[i])
            fractal_term += (base**1.8 + 0.4 * base**3.2) * \
                           np.sin(2.0 * np.pi * x[i] / (1.0 + 0.15 * base)) * \
                           np.exp(-0.05 * base)
        
        # Enhanced nested sinusoidal modulations with dynamic frequencies
        nested_mod = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.4 * x[i])
            nested_mod += np.sin(freq * x[i]**2) * np.cos(freq * x[i]) * \
                         np.exp(-0.15 * x[i]**2) * \
                         (1.0 + 0.2 * np.sin(3.0 * x[i]))
        
        # Stronger asymmetric dimensional coupling with exponential weights
        asym_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.25 * (x[i]**2 + x[j]**2))
                asym_coupling += weight * (np.sin(x[i]) * np.cos(x[j])**2 + 
                                         0.8 * np.cos(x[i]) * np.sin(x[j])**2) * \
                                (1.0 + 0.3 * np.sin(2.0 * x[i] * x[j]))
        
        # Enhanced ridge structure with chaotic perturbations
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += (x[i]**2 + 0.25 * x[i]**4) * \
                         np.exp(-0.6 * np.abs(x[i])) * \
                         (1.0 + 0.4 * np.sin(5.0 * x[i]) + 0.1 * np.cos(10.0 * x[i]))
        
        # Enhanced cross-dimensional exponential interference
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.exp(-0.15 * (x[i]**2 + x[j]**2)) * \
                            np.sin(x[i] * x[j]) * \
                            np.cos(0.6 * (x[i] + x[j])) * \
                            (1.0 + 0.2 * np.sin(4.0 * x[i]))
        
        # Enhanced chaotic harmonic modulation with dynamic scaling
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(x[i]) * np.cos(3.0 * x[i]) * \
                          np.exp(-0.35 * x[i]**2) * \
                          (1.0 + 0.3 * np.sin(7.0 * x[i]) + 0.1 * np.cos(14.0 * x[i]))
        
        # Combine all terms with optimized weighting
        result = 0.6 * fractal_term + 0.7 * nested_mod + 0.5 * asym_coupling + \
                 0.8 * ridge_term + 0.4 * cross_exp + 0.9 * chaotic_mod
        
        return result