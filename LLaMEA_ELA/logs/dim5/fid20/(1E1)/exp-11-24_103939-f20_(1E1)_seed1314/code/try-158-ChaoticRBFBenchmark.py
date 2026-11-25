import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dimensionality
        self.chaotic_seq = np.array([np.sin(2**i * np.pi * 0.12345) for i in range(dim)])
        
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Chaotic component using logistic map-inspired terms
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += self.chaotic_seq[i] * np.sin(10 * x_scaled[i]) * np.cos(8 * x_scaled[i])
        
        # Radial basis functions with dynamic centers and varying widths
        rbf_sum = 0.0
        num_centers = min(7, self.dim)
        for i in range(num_centers):
            center = np.sin(i * 0.5) * 0.8
            width = 0.1 + 0.3 * np.sin(i * 0.3)
            rbf_sum += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Coupling terms with varying strength based on dimension index
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = (i + j) / (self.dim * (self.dim - 1) / 2)
                coupling_term += coupling_strength * np.sin(x_scaled[i]) * np.cos(x_scaled[j])
        
        # Polynomial with mixed exponents and variable coefficients
        poly_term = 0.0
        for i in range(self.dim):
            coeff = 0.5 + 0.3 * np.sin(i * 0.7)
            poly_term += coeff * (x_scaled[i]**5 + 0.7 * x_scaled[i]**4 - 0.3 * x_scaled[i]**3)
        
        # Sine-cosine interaction with frequency modulation
        freq_mod = np.array([2 + 3 * np.sin(i * 0.4) for i in range(self.dim)])
        trig_term = np.sum(np.sin(freq_mod * x_scaled) * np.cos(freq_mod * x_scaled))
        
        # Boundary avoidance with exponential penalty
        boundary_penalty = np.sum(np.exp(2 * np.abs(x_scaled)) - 1)
        
        return chaotic_term + rbf_sum + coupling_term + poly_term + trig_term + boundary_penalty