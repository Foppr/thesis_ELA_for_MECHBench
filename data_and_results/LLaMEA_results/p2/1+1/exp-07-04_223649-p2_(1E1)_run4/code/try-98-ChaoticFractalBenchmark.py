import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants for dynamic modulation
        self.chaos_factor = 0.5 + np.random.rand() * 0.5
        self.fractal_dim = 1.5 + np.random.rand() * 0.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic particle interaction terms with dynamic coupling
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling based on chaotic map
                coupling_strength = self.chaos_factor * np.sin(x[i] * x[j] * (i + j + 1)) * np.cos(x[i] + x[j])
                chaotic_interaction += coupling_strength / (1.0 + np.abs(x[i] - x[j]))
        
        # Fractal-like self-similar structure using sine-cosine combinations
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal component
            scale = 1.0 + np.sin(i * 0.5) * 0.5
            fractal_term += np.sin(x[i] * scale) * np.cos(x[i] * scale**2) * np.sin(x[i] * scale**3)
        
        # Dynamic gradient modulation with time-varying parameters
        gradient_mod = 0.0
        for i in range(self.dim):
            # Modulate gradient based on neighbor interactions
            neighbor_sum = 0.0
            if i > 0:
                neighbor_sum += np.abs(x[i] - x[i-1])
            if i < self.dim - 1:
                neighbor_sum += np.abs(x[i] - x[i+1])
            
            # Dynamic modulation factor
            mod_factor = 1.0 + 0.5 * np.sin(neighbor_sum * 2.0)
            gradient_mod += mod_factor * x[i]**3
        
        # High-frequency oscillatory landscape with amplitude modulation
        high_freq = 0.0
        for i in range(self.dim):
            # Amplitude varies with position
            amp = 1.0 + 0.5 * np.sin(x[i] * 0.3)
            high_freq += amp * np.sin(x[i] * 10.0) * np.cos(x[i] * 8.0)
        
        # Add all components to the result
        result = result + chaotic_interaction + fractal_term + gradient_mod + high_freq
        
        # Add a global multimodal component with multiple peaks
        global_peaks = 0.0
        for i in range(self.dim):
            # Multiple peaks with varying heights and positions
            peak_positions = [1.0, -1.0, 2.0, -2.0, 3.0, -3.0]
            for pos in peak_positions:
                global_peaks += np.exp(-0.5 * ((x[i] - pos) / 0.5)**2) * np.cos(2.0 * np.pi * (x[i] - pos))
        
        result = result + global_peaks
        
        return result