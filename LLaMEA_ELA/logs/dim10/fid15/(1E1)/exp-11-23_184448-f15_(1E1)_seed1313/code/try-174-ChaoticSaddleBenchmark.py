import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial term with adaptive scaling
        r_squared = np.sum(x**2)
        radial_term = np.exp(-0.1 * r_squared) * (r_squared + 1e-8)
        
        # Dynamic phase-shifted sinusoidal components with time-delayed feedback
        saddle_term = 0.0
        for i in range(self.dim):
            delay_idx = (i + self.dim//4) % self.dim
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            phase = 0.5 * np.cos(i * np.pi / (self.dim + 2))
            saddle_term += np.sin(x[i] * freq + phase) * np.cos(x[delay_idx] * 0.3) * np.exp(-0.2 * (x[i] - x[delay_idx])**2)
        
        # Fractional Brownian motion inspired coupling with dynamic exponents
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                # Dynamic scaling factor based on dimensionality
                scale_factor = 0.3 + 0.7 * np.sin(np.log(dist + 1) * (self.dim + 1) / 10.0)
                coupling_term += (x[i]**4 + x[j]**4) * np.exp(-0.5 * dist) * scale_factor
        
        # Adaptive ridge structures with chaotic local minima
        local_minima = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 6))
            depth = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 3))
            weight = np.exp(-0.2 * (x[i] - center)**2)
            local_minima += weight * depth * (x[i]**8 - 4*x[i]**6 + 6*x[i]**4 - 4*x[i]**2 + 1)
        
        # Multi-scale chaotic symmetry with recurrent delayed feedback
        symmetry_term = 0.0
        scales = [0.1, 0.3, 0.7, 1.2, 2.0]
        for scale in scales:
            delayed_r = np.sum(np.roll(x, self.dim//5)**2)
            symmetry_term += np.sin(r_squared / scale) * np.cos(delayed_r / (scale + 1)) * np.exp(-0.1 * np.abs(scale - 1.0))
        
        # Chaotic noise with dynamic amplitude modulation
        noise = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            noise += amp_mod * np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 3)) * np.tan(x[i] / (i + 4))
        
        # Dimensionality-dependent chaotic scaling with exponential growth
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 5)
        
        return dim_factor * (0.2 * radial_term + 0.3 * saddle_term + 
                            0.25 * coupling_term + 0.15 * local_minima + 
                            0.08 * symmetry_term + 0.07 * noise)