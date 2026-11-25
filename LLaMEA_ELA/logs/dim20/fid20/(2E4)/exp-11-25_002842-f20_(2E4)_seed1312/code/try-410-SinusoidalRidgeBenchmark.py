import numpy as np

class SinusoidalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic phase modulation parameters
        self.phase_mod = np.random.uniform(0.1, 2.0, dim)
        self.phase_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Polynomial modulation coefficients
        self.poly_mod = np.random.uniform(-1.0, 1.0, (dim, 4))
        # Multi-scale ridge parameters
        self.ridge_centers = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.ridge_widths = np.random.uniform(0.3, 3.0, (dim, 5))
        self.ridge_heights = np.random.uniform(0.5, 4.0, (dim, 5))
        # Adaptive conditioning with chaotic modulation
        self.conditioning_factors = np.random.uniform(0.05, 2.5, dim)
        self.conditioning_mod = np.random.uniform(0.1, 1.5, dim)
        # Weighted combination coefficients
        self.weights = np.random.uniform(0.1, 1.0, 5)
        self.weights /= np.sum(self.weights)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sinusoidal oscillation with phase coupling
        phase_energy = 0.0
        for i in range(self.dim):
            phase = self.phase_mod[i] * (1 + 0.2 * np.sin(x[i]))
            coupled_phase = 0.0
            for j in range(self.dim):
                if i != j:
                    coupled_phase += self.phase_coupling[i, j] * np.sin(x[j])
            phase_energy += np.sin(phase * x[i] + coupled_phase) ** 2
            
        # Polynomial modulation with adaptive coefficients
        poly_energy = 0.0
        for i in range(self.dim):
            poly_val = 0.0
            for j in range(4):
                poly_val += self.poly_mod[i, j] * (x[i] ** (j + 1))
            poly_energy += poly_val ** 2
            
        # Multi-scale ridge structure
        ridge_energy = 0.0
        for i in range(self.dim):
            ridge_val = 0.0
            for j in range(5):
                center = self.ridge_centers[i, j]
                width = self.ridge_widths[i, j]
                height = self.ridge_heights[i, j]
                ridge_val += height * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
            ridge_energy += ridge_val
            
        # Adaptive conditioning with chaotic modulation
        cond_energy = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i] * (1 + self.conditioning_mod[i] * np.sin(x[i]))
            cond_energy += cond_factor * x[i] ** 3
            
        # Cross-dimensional interaction term
        cross_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_energy += np.sin(x[i] * x[j]) ** 2
                
        # Combine all components with weighted sum
        total = (self.weights[0] * phase_energy + 
                self.weights[1] * poly_energy + 
                self.weights[2] * ridge_energy + 
                self.weights[3] * cond_energy + 
                self.weights[4] * cross_energy)
                
        return total