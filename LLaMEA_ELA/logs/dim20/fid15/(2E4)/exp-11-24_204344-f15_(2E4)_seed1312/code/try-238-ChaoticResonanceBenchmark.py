import numpy as np

class ChaoticResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Hyperbolic tangent gradient component with dynamic scaling
        tanh_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.7)
            tanh_term += scale * np.tanh(x[i] * (1.0 + 0.2 * np.cos(i * 0.4))) ** 3
        
        # Polynomial chaos component with random coefficients
        poly_term = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.5 * np.sin(i * 0.6 + self.dim)
            power = 2 + int(3 * np.cos(i * 0.5))
            poly_term += coeff * x[i] ** power
        
        # Dynamic resonance field with time-varying frequencies
        res_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * 0.3 + self.dim * 0.1)
            amp = 0.5 + 0.5 * np.cos(i * 0.4 + self.dim * 0.2)
            res_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Cross-dimensional coupling with chaotic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.tanh(x[i] * x[j]) * np.sin(3.0 * (x[i]**2 + x[j]**2))
                cross_term += coupling
        
        # Multi-modal chaotic wells with varying positions and shapes
        well_term = 0.0
        for i in range(self.dim):
            pos1 = 2.0 + 1.5 * np.sin(i * 0.5)
            pos2 = -1.5 + 2.0 * np.cos(i * 0.3)
            well1 = (x[i] - pos1)**2 * np.exp(-0.5 * (x[i] - pos1)**2)
            well2 = (x[i] - pos2)**4 * np.exp(-0.3 * (x[i] - pos2)**2)
            well_term += 0.6 * well1 + 0.4 * well2
        
        # Chaotic perturbation with adaptive noise
        noise_term = 0.0
        for i in range(self.dim):
            noise = np.sin(i * 0.2 + self.dim * 0.3) * np.cos(x[i] * 0.5)
            noise_term += noise
        
        # Final combination with chaotic weights
        total = 0.25 * tanh_term + 0.2 * poly_term + 0.15 * res_term + 0.2 * cross_term + 0.15 * well_term + 0.05 * noise_term
        
        # Global chaotic scaling factor
        chaos_factor = 1.0 + 0.2 * np.sin(self.dim * 0.4) * np.cos(self.dim * 0.3)
        
        return total * chaos_factor