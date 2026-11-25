import numpy as np

class FractalBrownianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal parameters
        self.hurst_exponents = np.random.uniform(0.1, 0.9, dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.frequency_scales = np.random.uniform(0.5, 3.0, dim)
        # Cross-dimensional coupling - increased strength
        self.coupling_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.coupling_matrix[i, j] = np.random.uniform(-1.0, 1.0) * np.exp(-abs(i-j)/max(1, dim/4))
        # Adaptive roughness parameters
        self.roughness_adaptation = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for fractal computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute fractal Brownian motion with adaptive roughness
        fbm_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Generate fractal component with Hurst exponent
            hurst = self.hurst_exponents[i]
            amplitude = self.fractal_amplitudes[i]
            
            # Compute fractal contribution from multiple scales
            fractal_sum = 0.0
            num_scales = min(8, max(3, int(self.frequency_scales[i])))
            for scale in range(1, num_scales + 1):
                freq = 2 ** scale
                # Sample at different frequencies
                sample_point = normalized_x[i] * freq
                # Use sine wave with varying amplitude and frequency
                fractal_sum += amplitude * (1.0 / freq) ** (2.0 * hurst) * np.sin(freq * sample_point)
            
            # Add adaptive roughness term
            roughness_factor = 1.0 + self.roughness_adaptation[i] * np.sin(normalized_x[i] * 10.0)
            fbm_values[i] = fractal_sum * roughness_factor
            
        # Add cross-dimensional coupling effects
        coupled_values = np.zeros(self.dim)
        for i in range(self.dim):
            coupling_effect = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_effect += self.coupling_matrix[i, j] * fbm_values[j]
            coupled_values[i] = fbm_values[i] + coupling_effect
        
        # Compute fitness with polynomial and exponential terms plus trigonometric interactions
        fitness = 0.0
        for i in range(self.dim):
            # Polynomial energy terms
            term1 = coupled_values[i]**2
            term2 = 0.3 * coupled_values[i]**4
            term3 = 0.1 * np.exp(-coupled_values[i]**2)
            
            # Add basin interaction terms (self-similarity) with trigonometric enhancement
            basin_term = 0.0
            for j in range(self.dim):
                if i != j:
                    basin_term += 0.5 * np.exp(-((coupled_values[i] - coupled_values[j])**2) / 0.3) * np.sin(coupled_values[i] * coupled_values[j])
            
            fitness += term1 + term2 + term3 + basin_term
        
        # Add global scaling
        fitness = fitness / self.dim
        # Add small noise for robustness
        noise = np.random.uniform(-0.005, 0.005)
        return fitness + noise