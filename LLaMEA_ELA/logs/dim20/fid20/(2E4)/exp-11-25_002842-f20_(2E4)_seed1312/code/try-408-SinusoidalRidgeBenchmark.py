import numpy as np

class SinusoidalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Adaptive frequency modulation parameters
        self.freq_mod = np.random.uniform(0.5, 3.0, dim)
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 5))
        # Dynamic ridge parameters
        self.ridge_centers = np.random.uniform(-4.0, 4.0, (dim, 3))
        self.ridge_widths = np.random.uniform(0.5, 2.5, (dim, 3))
        self.ridge_heights = np.random.uniform(1.0, 5.0, (dim, 3))
        # Adaptive conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 3.0, dim)
        # Phase shift parameters for each dimension
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Weighted combination coefficients
        self.weights = np.random.uniform(0.1, 1.0, 4)
        self.weights /= np.sum(self.weights)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Sinusoidal oscillation with adaptive frequency
        freq_energy = 0.0
        for i in range(self.dim):
            freq = self.freq_mod[i] * (1 + 0.3 * np.sin(x[i]))
            freq_energy += np.sin(freq * x[i] + self.phase_shifts[i]) ** 2
            
        # Polynomial chaos expansion
        poly_energy = 0.0
        for i in range(self.dim):
            poly_val = 0.0
            for j in range(5):
                poly_val += self.poly_coeffs[i, j] * (x[i] ** j)
            poly_energy += poly_val ** 2
            
        # Dynamic ridge structure
        ridge_energy = 0.0
        for i in range(self.dim):
            ridge_val = 0.0
            for j in range(3):
                center = self.ridge_centers[i, j]
                width = self.ridge_widths[i, j]
                height = self.ridge_heights[i, j]
                ridge_val += height * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
            ridge_energy += ridge_val
            
        # Adaptive conditioning
        cond_energy = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i] * (1 + 0.2 * np.cos(x[i]))
            cond_energy += cond_factor * x[i] ** 4
            
        # Combine all components with weighted sum
        total = (self.weights[0] * freq_energy + 
                self.weights[1] * poly_energy + 
                self.weights[2] * ridge_energy + 
                self.weights[3] * cond_energy)
                
        return total