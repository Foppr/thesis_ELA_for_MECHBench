import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute delay indices for time-delayed feedback
        self.delay_indices = [max(0, i - 1) for i in range(dim)]
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Fractional Brownian motion-like correlation term
        fbm_term = 0.0
        for i in range(self.dim):
            corr_sum = 0.0
            for j in range(max(0, i-3), i):
                if i != j:
                    distance = abs(x_normalized[i] - x_normalized[j])
                    corr_sum += np.exp(-distance * (1 + 0.1 * j)) / (1 + distance)
            fbm_term += corr_sum * (1.0 + 0.2 * np.sin(i * 0.5))
        
        # Time-delayed feedback with chaotic coupling
        delay_term = 0.0
        for i in range(self.dim):
            if i > 0:
                delay_idx = self.delay_indices[i]
                coupling_strength = 0.5 + 0.3 * np.sin(i * 0.7)
                delay_term += coupling_strength * np.sin(x_normalized[i] - 0.5 * x_normalized[delay_idx])
        
        # Multi-modal polynomial with chaotic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            # Chaotic coefficient using sine modulation
            coeff = 1.0 + 0.3 * np.sin(i * 2.1 + np.sin(i * 0.9))
            # Varying degree with chaotic pattern
            degree = 2 + int(3 * np.sin(i * 0.8)) % 3
            poly_term += coeff * (x_normalized[i] ** degree)
        
        # Trigonometric component with phase modulation and non-linear coupling
        trig_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(i * 0.6 + np.cos(i * 0.3))
            amp_mod = 1.0 + 0.2 * np.cos(i * 0.4 + np.sin(i * 0.7))
            trig_term += amp_mod * np.sin(freq_mod * x_normalized[i]) * np.cos(freq_mod * x_normalized[i] * 0.8)
        
        # Cross-dimensional interaction with memory effect
        memory_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Memory-weighted coupling with chaotic weight modulation
                memory_weight = 0.5 + 0.3 * np.sin(i * 0.4 + j * 0.6)
                interaction = (x_normalized[i] - x_normalized[j]) ** 2
                memory_interaction += memory_weight * interaction
        
        # Non-linear transformation with chaotic scaling
        nonlinear_term = 0.0
        for i in range(self.dim):
            # Apply chaotic scaling factor
            scale_factor = 1.0 + 0.4 * np.sin(i * 1.3 + np.cos(i * 0.8))
            nonlinear_term += scale_factor * np.tanh(x_normalized[i] ** 3)
        
        # Combine all terms with dynamic weights
        total = (0.25 * poly_term + 
                 0.2 * trig_term + 
                 0.15 * fbm_term + 
                 0.15 * delay_term + 
                 0.1 * memory_interaction + 
                 0.15 * nonlinear_term)
        
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            freq_mod = 2.0 + np.sin(i * 0.9) + 0.3 * np.cos(i * 0.5)
            noise += np.sin(freq_mod * x_normalized[i]) * np.cos(freq_mod * x_normalized[i] * 0.6)
        
        return total + 0.05 * noise