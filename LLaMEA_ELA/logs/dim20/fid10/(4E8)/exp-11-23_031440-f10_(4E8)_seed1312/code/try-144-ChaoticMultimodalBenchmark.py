import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential component with varying bases and scaling
        exp_term = 0.0
        for i in range(self.dim):
            base = 1.5 + 0.5 * np.sin(i * np.pi / self.dim)
            scale = 1.0 + 0.2 * np.cos(i * np.pi / self.dim)
            exp_term += scale * (np.exp(base * x_norm[i]) - 1.0)
        
        # Logarithmic component with adaptive offsets and multipliers
        log_term = 0.0
        for i in range(self.dim):
            offset = 0.1 + 0.2 * np.sin(i * np.pi / self.dim)
            multiplier = 1.0 + 0.3 * np.cos(i * np.pi / self.dim)
            log_term += multiplier * np.log(np.abs(x_norm[i]) + offset)
        
        # Elliptic component with varying eccentricities and orientations
        ellip_term = 0.0
        for i in range(self.dim):
            eccentricity = 0.5 + 0.3 * np.sin(i * np.pi / self.dim)
            angle = np.pi * i / self.dim
            x1 = x_norm[i] * np.cos(angle) - x_norm[(i+1) % self.dim] * np.sin(angle)
            x2 = x_norm[i] * np.sin(angle) + x_norm[(i+1) % self.dim] * np.cos(angle)
            ellip_term += (x1**2 + eccentricity * x2**2) / (1.0 + eccentricity)
        
        # Multi-scale interference with chaotic sinusoidal patterns
        interfere_term = 0.0
        scales = [1, 2, 3, 4]
        for i in range(self.dim):
            for scale in scales:
                freq = scale * (i + 1)
                phase = np.pi * np.sin(i * np.pi / self.dim)
                interfere_term += np.sin(freq * x_norm[i] + phase) * \
                                np.cos(freq * x_norm[i] + phase) * \
                                np.exp(-0.5 * (x_norm[i] ** 2))
        
        # Dynamic conditioning based on chaotic logistic map
        condition_factor = 1.0
        r = 3.8  # Chaos parameter
        x_prev = 0.5
        for i in range(self.dim):
            x_next = r * x_prev * (1 - x_prev)
            condition_factor *= (1.0 + 0.5 * np.sin(x_next * np.pi))
            x_prev = x_next
        
        # Multi-dimensional coupling with dynamic strength
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.abs(x_norm[i] - x_norm[j])
                strength = 0.3 + 0.2 * np.sin((i + j) * np.pi / self.dim)
                coupling_term += strength * np.exp(-dist**2) * np.sin(5 * dist)
        
        # Combine all terms with adaptive weights
        total = (0.3 * exp_term + 0.25 * log_term + 0.2 * ellip_term + 
                0.15 * interfere_term + 0.1 * coupling_term) * condition_factor
        
        return total