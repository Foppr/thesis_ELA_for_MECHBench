import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add fractal-like hierarchical structure with nested minima
        fractal_sum = 0
        for i in range(12):
            # Create nested minima at different scales with enhanced complexity
            scale = 0.6**(i+1)
            center = np.array([np.sin(i * 0.4) * 3.5 * scale, np.cos(i * 0.4) * 3.5 * scale])
            if self.dim >= 2:
                diff = x[:2] - center
                # Enhanced varying amplitudes and frequencies for fractal structure
                amplitude = 2.5 * (1.0 + 0.6 * np.sin(i * 0.8))
                frequency = 1.2 + 0.4 * np.cos(i * 0.6)
                fractal_sum += amplitude * np.exp(-0.5 * np.sum(diff**2) / (0.15 * frequency))
        
        f += 2.0 * fractal_sum
        
        # Add dynamic amplitude modulation based on input values with chaotic pattern
        amp_mod = 0
        for i in range(self.dim):
            # Use more complex chaotic modulation with recursive pattern
            amp = 1.2 + 0.6 * np.sin(x[i] * 2.5 + np.sin(x[i] * 4.0) + np.cos(x[i] * 1.5))
            amp_mod += amp * np.cos(x[i] * 1.8 + np.cos(x[i] * 0.9) + np.sin(x[i] * 2.2))
        f += 1.0 * amp_mod
        
        # Add hierarchical coupling with multiple levels and enhanced complexity
        coupling_sum = 0
        for level in range(4):
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    # Level-dependent coupling strength with enhanced variation
                    strength = 0.6 * (level + 1)
                    # Dynamic coupling with more complex fractal-like pattern
                    coupling = strength * np.sin(x[i] * x[j] * 0.6 + 
                                                np.sin(x[i] + x[j]) * 0.4 * (level + 1) +
                                                np.cos(x[i] * x[j] * 0.3))
                    coupling_sum += coupling
        f += 1.5 * coupling_sum
        
        # Add self-similar sinusoidal interactions with enhanced complexity
        self_similar_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create more complex self-similar pattern with varying frequencies
                freq1 = 1.2 + 0.3 * np.sin(x[i] * 0.6)
                freq2 = 1.2 + 0.3 * np.cos(x[j] * 0.6)
                self_similar_sum += np.sin(x[i] * freq1) * np.cos(x[j] * freq2) + \
                                   0.5 * np.sin(x[i] * freq2) * np.cos(x[j] * freq1)
        f += 0.8 * self_similar_sum
        
        # Add multi-scale chaotic interactions with enhanced complexity
        chaotic_sum = 0
        for i in range(self.dim):
            # Use more complex chaotic map for dynamic interaction
            chaotic_val = np.sin(x[i] * 3.5 + np.sin(x[i] * 8.0) + np.cos(x[i] * 2.0))
            chaotic_sum += chaotic_val * np.cos(x[i] * 2.5 + np.cos(x[i] * 6.0) + np.sin(x[i] * 3.0))
        f += 0.5 * chaotic_sum
        
        # Add polynomial chaos with hierarchical structure and enhanced complexity
        poly_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced hierarchical polynomial terms
                poly_sum += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j] * 0.4) + \
                           0.3 * x[i] * x[j] * np.cos(x[i] + x[j])
        f += 0.9 * poly_sum
        
        # Add multiple global minima with enhanced fractal distribution
        minima_positions = []
        for i in range(25):
            # Enhanced fractal-like distribution of minima
            angle = i * 0.25 * np.pi
            radius = 2.8 * (0.6**(i % 6))
            minima_positions.append([radius * np.cos(angle), radius * np.sin(angle)])
            
        minima_sum = 0
        for i, pos in enumerate(minima_positions):
            if self.dim >= len(pos):
                diff = x[:len(pos)] - np.array(pos)
                # Enhanced varying amplitudes for minima
                amplitude = 1.2 + 0.4 * np.sin(i * 0.5)
                minima_sum += amplitude * np.exp(-0.25 * np.sum(diff**2))
        f += 2.2 * minima_sum
        
        # Add enhanced noise with fractal pattern
        noise = 0
        for i in range(self.dim):
            # Enhanced fractal noise pattern
            noise += np.sin(x[i] * 9.0 + np.sin(x[i] * 13.0) + np.sin(x[i] * 5.0) + np.cos(x[i] * 2.0))
        f += 0.3 * noise
        
        # Add cross-dimensional interaction terms for increased non-separability
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_sum += np.sin(x[i] * x[j] * 0.5) * np.cos(x[i] + x[j]) * 0.2
        f += 0.6 * cross_sum
        
        return f