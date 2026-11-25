import numpy as np

class ChaoticSineRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters with logistic map modulation
        self.chaotic_params = np.random.uniform(0.1, 2.0, dim)
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-1.5, 1.5, (dim, 6))
        # Dynamic ridge parameters with chaotic positioning
        self.ridge_centers = np.random.uniform(-4.5, 4.5, (dim, 4))
        self.ridge_widths = np.random.uniform(0.3, 3.0, (dim, 4))
        self.ridge_heights = np.random.uniform(0.5, 6.0, (dim, 4))
        # Adaptive conditioning with chaotic modulation
        self.conditioning_factors = np.random.uniform(0.05, 2.5, dim)
        # Phase coupling terms between dimensions
        self.phase_couplings = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Weighted combination coefficients
        self.weights = np.random.uniform(0.1, 1.0, 5)
        self.weights /= np.sum(self.weights)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sine wave with logistic modulation
        chaotic_energy = 0.0
        for i in range(self.dim):
            # Logistic map for dynamic parameter modulation
            r = self.logistic_r[i]
            param_mod = 1.0 + 0.5 * np.sin(r * (1 - x[i] ** 2) * np.pi / 2)
            chaotic_freq = self.chaotic_params[i] * param_mod
            chaotic_energy += np.sin(chaotic_freq * x[i]) ** 2
            
        # Polynomial chaos expansion with higher order terms
        poly_energy = 0.0
        for i in range(self.dim):
            poly_val = 0.0
            for j in range(6):
                poly_val += self.poly_coeffs[i, j] * (x[i] ** j)
            poly_energy += poly_val ** 2
            
        # Dynamic ridge structure with chaotic positioning
        ridge_energy = 0.0
        for i in range(self.dim):
            ridge_val = 0.0
            for j in range(4):
                center = self.ridge_centers[i, j]
                width = self.ridge_widths[i, j]
                height = self.ridge_heights[i, j]
                ridge_val += height * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
            ridge_energy += ridge_val
            
        # Adaptive conditioning with chaotic modulation
        cond_energy = 0.0
        for i in range(self.dim):
            # Chaotic modulation of conditioning factor
            chaos_mod = 1.0 + 0.3 * np.sin(self.logistic_r[i] * x[i])
            cond_factor = self.conditioning_factors[i] * chaos_mod
            cond_energy += cond_factor * x[i] ** 4
            
        # Phase coupling between dimensions
        phase_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    phase_energy += self.phase_couplings[i, j] * np.sin(x[i] + x[j])
                    
        # Combine all components with weighted sum
        total = (self.weights[0] * chaotic_energy + 
                self.weights[1] * poly_energy + 
                self.weights[2] * ridge_energy + 
                self.weights[3] * cond_energy + 
                self.weights[4] * phase_energy)
                
        return total