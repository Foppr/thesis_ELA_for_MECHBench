import numpy as np

class FractalRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal-like term with power-law scaling and exponential modulation
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += (np.abs(x[i])**1.9 + 0.4 * np.abs(x[i])**3.5) * \
                           np.sin(2.0 * np.pi * x[i] / (1.0 + 0.15 * np.abs(x[i]))) * \
                           np.exp(-0.05 * x[i]**2)
        
        # Nested sinusoidal modulations with dynamic frequency and amplitude
        nested_mod = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.5 * x[i])
            amp = 1.0 + 0.3 * np.cos(0.7 * x[i])
            nested_mod += amp * np.sin(freq * x[i]**2) * np.cos(freq * x[i]) * \
                         np.exp(-0.15 * x[i]**2)
        
        # Asymmetric dimensional coupling with multi-scale exponential weights
        asym_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight1 = np.exp(-0.3 * (x[i]**2 + x[j]**2))
                weight2 = np.exp(-0.1 * (x[i]**4 + x[j]**4))
                asym_coupling += (weight1 * weight2) * (np.sin(x[i]) * np.cos(x[j])**2 + 
                                                       0.8 * np.cos(x[i]) * np.sin(x[j])**2)
        
        # Power-law based ridge structure with chaotic perturbations and multi-scale harmonics
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += (x[i]**2 + 0.3 * x[i]**4 + 0.1 * x[i]**6) * \
                         np.exp(-0.6 * np.abs(x[i])) * \
                         (1.0 + 0.4 * np.sin(5.0 * x[i]) + 0.2 * np.cos(3.0 * x[i]))
        
        # Cross-dimensional exponential interference with dynamic phase shifts
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = 0.5 * np.sin(0.3 * (x[i] + x[j]))
                cross_exp += np.exp(-0.2 * (x[i]**2 + x[j]**2)) * \
                            np.sin(x[i] * x[j] + phase_shift) * \
                            np.cos(0.5 * (x[i] + x[j]) + phase_shift)
        
        # Chaotic harmonic modulation with dynamic scaling and multi-frequency components
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += (np.sin(x[i]) * np.cos(3.0 * x[i]) * \
                           np.exp(-0.35 * x[i]**2) * \
                           (1.0 + 0.3 * np.sin(7.0 * x[i]) + 0.1 * np.cos(11.0 * x[i]))) * \
                          (1.0 + 0.2 * np.sin(2.0 * x[i]))
        
        # Multi-scale fractal interference with varying dimensional coupling
        multi_fractal = 0.0
        for i in range(self.dim):
            multi_fractal += (np.abs(x[i])**2.1 + 0.25 * np.abs(x[i])**4.3) * \
                            np.sin(3.0 * np.pi * x[i] / (1.0 + 0.2 * np.abs(x[i]))) * \
                            np.cos(0.5 * x[i]) * \
                            np.exp(-0.1 * x[i]**2)
        
        # Combine all terms with dynamic weighting and normalization
        result = 0.6 * fractal_term + 0.7 * nested_mod + 0.5 * asym_coupling + \
                 0.8 * ridge_term + 0.4 * cross_exp + 0.9 * chaotic_mod + \
                 0.3 * multi_fractal
        
        return result