import numpy as np

class SineWaveChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_waves = 8
        self.polynomial_order = 3
        self.attraction_strength = 2.5
        self.noise_level = 0.07
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        result = 0.0
        
        # Polynomial chaos expansion component with sine-wave modulation
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic polynomial coefficients using sine waves with modified frequencies
            coeff = 1.5 + 0.7 * np.sin(i * 2.3) + 0.6 * np.cos(i * 1.9) + 0.4 * np.sin(i * 1.1)
            poly_term += coeff * (xi ** self.polynomial_order)
        
        # Sine-wave modulation component with varying frequencies and phases
        sine_term = 0.0
        for i in range(self.num_waves):
            freq = 1.2 + 0.4 * np.sin(i * 1.5) + 0.3 * np.cos(i * 0.9)
            phase = 0.6 * np.sin(i * 2.9) + 0.5 * np.cos(i * 2.1)
            amp = 1.2 + 0.5 * np.sin(i * 1.3) + 0.4 * np.cos(i * 0.9)
            
            # Combine all dimensions with sine-wave modulation and cross-dimensional interactions
            wave_sum = 0.0
            for j in range(self.dim):
                wave_sum += amp * np.sin(freq * x[j] + phase) * (1.0 + 0.1 * np.sin(i + j))
            sine_term += wave_sum ** 2
        
        # Gradient-based attraction fields to create local minima
        attraction_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Attraction centers with modified chaotic positioning
            center = 2.5 * np.sin(i * 1.7) + 1.8 * np.cos(i * 1.1)
            dist = (xi - center) ** 2
            attraction_term += self.attraction_strength * np.exp(-dist / 1.5)
        
        # Add noise to create dynamic behavior
        noise = self.noise_level * np.random.randn()
        
        # Combine all components with different weights
        return 0.35 * poly_term + 0.35 * sine_term + 0.25 * attraction_term + 0.05 * noise