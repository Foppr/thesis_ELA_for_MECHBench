import numpy as np

class SineWaveChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_waves = 12
        self.polynomial_order = 4
        self.attraction_strength = 1.5
        self.noise_level = 0.03
        self.conditioning_factor = 1.2
        
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
        
        # Enhanced polynomial chaos expansion with chaotic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic polynomial coefficients using multiple sine/cosine combinations
            coeff = 1.0 + 0.7 * np.sin(i * 2.1) + 0.5 * np.cos(i * 1.7) + 0.3 * np.sin(i * 0.9) + 0.2 * np.cos(i * 2.3)
            poly_term += coeff * (xi ** self.polynomial_order)
        
        # Enhanced sine-wave modulation with dynamic frequencies and phases
        sine_term = 0.0
        for i in range(self.num_waves):
            # Dynamic frequency, phase, and amplitude based on wave index
            freq = 1.5 + 0.8 * np.sin(i * 1.3) + 0.4 * np.cos(i * 0.7)
            phase = 0.3 * np.sin(i * 2.7) + 0.2 * np.cos(i * 1.9)
            amp = 1.2 + 0.5 * np.sin(i * 1.1) + 0.3 * np.cos(i * 0.8)
            
            # Combine all dimensions with sine-wave modulation
            wave_sum = 0.0
            for j in range(self.dim):
                wave_sum += amp * np.sin(freq * x[j] + phase) * (1.0 + 0.1 * np.sin(j * 0.5))
            sine_term += wave_sum ** 2
        
        # Enhanced gradient-based attraction fields with dynamic centers
        attraction_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Dynamic attraction centers with chaotic positioning
            center = 2.5 * np.sin(i * 1.5) + 1.5 * np.cos(i * 0.9) + 0.8 * np.sin(i * 3.1)
            dist = (xi - center) ** 2
            # Add conditioning factor to improve landscape difficulty
            attraction_term += self.attraction_strength * np.exp(-dist / (2.0 * self.conditioning_factor))
        
        # Add noise for dynamic behavior
        noise = self.noise_level * np.random.randn()
        
        # Combine all components with optimized weights
        return 0.35 * poly_term + 0.4 * sine_term + 0.2 * attraction_term + 0.05 * noise