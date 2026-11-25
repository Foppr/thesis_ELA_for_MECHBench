import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.tent_map = np.array([0.5] * dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Chaotic tent map component with dynamic parameter
        chaotic_term = 0.0
        for i in range(self.dim):
            # Tent map: f(x) = mu * x if x < 0.5 else mu * (1 - x)
            mu = 3.9 + 0.1 * np.sin(0.1 * i)
            self.tent_map[i] = mu * self.tent_map[i] if self.tent_map[i] < 0.5 else mu * (1 - self.tent_map[i])
            chaotic_term += self.tent_map[i] * np.sin(x_scaled[i] * 3) * np.cos(x_scaled[i] * 2)
            
        # Polynomial interaction terms with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x_scaled[i]**3 + x_scaled[j]**2) * np.sin(x_scaled[i] * x_scaled[j] * 0.5)
                
        # Spectral frequency modulation with multiple harmonics
        spec_term = 0.0
        for i in range(self.dim):
            spec_term += (np.sin(10 * x_scaled[i]) + 
                         0.5 * np.cos(15 * x_scaled[i]) + 
                         0.3 * np.sin(25 * x_scaled[i]) +
                         0.1 * np.cos(35 * x_scaled[i]))
            
        # Fractal-like self-similarity component
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(x_scaled[i] * 2**i) * np.cos(x_scaled[i] * 3**i)
            
        # Cross-dimensional coupling with exponential weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i + j))
                cross_term += weight * np.sin(x_scaled[i] * x_scaled[j]) * np.cos(x_scaled[i] + x_scaled[j])
                
        # Add a global periodic modulation
        global_mod = 1.0 + 0.2 * np.sin(np.sum(x_scaled) * 7)
        
        # Combine all terms
        return chaotic_term + poly_term + spec_term + fractal_term + cross_term + global_mod + 3.0