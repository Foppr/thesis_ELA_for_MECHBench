import numpy as np

class SineWaveChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_waves = 8
        self.polynomial_order = 3
        self.attraction_strength = 2.0
        self.noise_level = 0.05
        
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
            # Chaotic polynomial coefficients using sine waves
            coeff = 1.2 + 0.8 * np.sin(i * 2.1) + 0.5 * np.cos(i * 1.7) + 0.3 * np.sin(i * 0.9)
            poly_term += coeff * (xi ** self.polynomial_order)
        
        # Sine-wave modulation component with varying frequencies and phases
        sine_term = 0.0
        for i in range(self.num_waves):
            freq = 1.0 + 0.5 * np.sin(i * 1.3) + 0.3 * np.cos(i * 0.7)
            phase = 0.5 * np.sin(i * 2.7) + 0.4 * np.cos(i * 1.9)
            amp = 1.0 + 0.6 * np.sin(i * 1.1) + 0.3 * np.cos(i * 0.8)
            
            # Combine all dimensions with sine-wave modulation
            wave_sum = 0.0
            for j in range(self.dim):
                wave_sum += amp * np.sin(freq * x[j] + phase)
            sine_term += wave_sum ** 2
        
        # Gradient-based attraction fields to create local minima
        attraction_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Attraction centers with chaotic positioning
            center = 3.0 * np.sin(i * 1.5) + 2.0 * np.cos(i * 0.9)
            dist = (xi - center) ** 2
            attraction_term += self.attraction_strength * np.exp(-dist / 2.0)
        
        # Add noise to create dynamic behavior
        noise = self.noise_level * np.random.randn()
        
        # Combine all components with different weights
        return 0.4 * poly_term + 0.3 * sine_term + 0.2 * attraction_term + 0.1 * noise