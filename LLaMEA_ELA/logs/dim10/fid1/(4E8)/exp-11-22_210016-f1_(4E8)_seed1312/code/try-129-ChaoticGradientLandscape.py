import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic harmonic component with nested frequencies
        chaotic_harmonic = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * x[i]) + 0.2 * np.cos(0.7 * x[i])
            chaotic_harmonic += (np.sin(freq * x[i]) + 
                               0.3 * np.cos(freq * x[i]**2) + 
                               0.1 * np.sin(2.0 * freq * x[i])) * \
                              np.exp(-0.1 * x[i]**2)
        
        # Adaptive exponential damping with chaotic modulation
        exp_damping = 0.0
        for i in range(self.dim):
            damping_factor = 1.0 + 0.4 * np.sin(0.5 * x[i] + 1.0) * np.cos(0.3 * x[i])
            exp_damping += damping_factor * np.exp(-0.2 * x[i]**2) * (x[i]**4 + 0.5 * x[i]**6)
        
        # Cross-dimensional interference with chaotic coupling
        cross_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_freq = 1.0 + 0.3 * np.sin(0.4 * x[i] + 0.2 * x[j])
                cross_interference += (np.sin(coupling_freq * x[i] * x[j]) * 
                                    np.cos(coupling_freq * (x[i]**2 + x[j]**2)) * 
                                    np.exp(-0.1 * (x[i]**2 + x[j]**2)))
        
        # Nested polynomial with chaotic coefficients
        nested_poly = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.3 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
            nested_poly += coeff * (x[i]**3 + 0.2 * x[i]**5 + 0.05 * x[i]**7)
        
        # Saddle point modifier with chaotic perturbation
        saddle_modifier = 0.0
        for i in range(self.dim):
            perturb = 0.2 * np.sin(1.5 * x[i] + 0.8 * np.cos(x[i]))
            saddle_modifier += (x[i]**2 + perturb) * np.exp(-0.3 * x[i]**2)
        
        # Combine all terms with dynamic weights
        result = 0.7 * chaotic_harmonic + 0.5 * exp_damping + 0.6 * cross_interference + \
                 0.4 * nested_poly + 0.3 * saddle_modifier
        
        return result