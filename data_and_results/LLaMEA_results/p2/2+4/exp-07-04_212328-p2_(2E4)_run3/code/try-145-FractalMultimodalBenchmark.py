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
        for i in range(15):
            # Create nested minima at different scales
            scale = 0.5**(i+1)
            center = np.array([np.sin(i * 0.3) * 4.0 * scale, np.cos(i * 0.3) * 4.0 * scale])
            if self.dim >= 2:
                diff = x[:2] - center
                # Use varying amplitudes and frequencies for fractal structure
                amplitude = 1.8 * (1.0 + 0.5 * np.sin(i * 0.7))
                frequency = 1.3 + 0.3 * np.cos(i * 0.5)
                fractal_sum += amplitude * np.exp(-0.5 * np.sum(diff**2) / (0.12 * frequency))
        
        f += 2.2 * fractal_sum
        
        # Add dynamic amplitude modulation based on input values
        amp_mod = 0
        for i in range(self.dim):
            # Use chaotic modulation with recursive pattern
            amp = 1.5 + 0.4 * np.sin(x[i] * 3.0 + np.sin(x[i] * 5.0))
            amp_mod += amp * np.cos(x[i] * 2.0 + np.cos(x[i] * 1.0))
        f += 1.5 * amp_mod
        
        # Add hierarchical coupling with multiple levels
        coupling_sum = 0
        for level in range(5):
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    # Level-dependent coupling strength
                    strength = 0.8 * (level + 1)
                    # Dynamic coupling with fractal-like pattern
                    coupling = strength * np.sin(x[i] * x[j] * 0.7 + 
                                                np.sin(x[i] + x[j]) * 0.5 * (level + 1))
                    coupling_sum += coupling
        f += 2.0 * coupling_sum
        
        # Add self-similar sinusoidal interactions
        self_similar_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create self-similar pattern with varying frequencies
                freq1 = 1.2 + 0.2 * np.sin(x[i] * 0.7)
                freq2 = 1.2 + 0.2 * np.cos(x[j] * 0.7)
                self_similar_sum += np.sin(x[i] * freq1) * np.cos(x[j] * freq2)
        f += 1.0 * self_similar_sum
        
        # Add multi-scale chaotic interactions
        chaotic_sum = 0
        for i in range(self.dim):
            # Use chaotic map for dynamic interaction
            chaotic_val = np.sin(x[i] * 4.0 + np.sin(x[i] * 9.0))
            chaotic_sum += chaotic_val * np.cos(x[i] * 3.0 + np.cos(x[i] * 7.0))
        f += 0.8 * chaotic_sum
        
        # Add polynomial chaos with hierarchical structure
        poly_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hierarchical polynomial terms
                poly_sum += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j] * 0.5)
        f += 1.2 * poly_sum
        
        # Add multiple global minima with fractal distribution
        minima_positions = []
        for i in range(30):
            # Fractal-like distribution of minima
            angle = i * 0.25 * np.pi
            radius = 3.8 * (0.5**(i % 7))
            minima_positions.append([radius * np.cos(angle), radius * np.sin(angle)])
            
        minima_sum = 0
        for i, pos in enumerate(minima_positions):
            if self.dim >= len(pos):
                diff = x[:len(pos)] - np.array(pos)
                # Varying amplitudes for minima
                amplitude = 1.5 + 0.3 * np.sin(i * 0.4)
                minima_sum += amplitude * np.exp(-0.12 * np.sum(diff**2))
        f += 2.5 * minima_sum
        
        # Add noise with fractal pattern
        noise = 0
        for i in range(self.dim):
            # Fractal noise pattern
            noise += np.sin(x[i] * 10.0 + np.sin(x[i] * 15.0) + np.sin(x[i] * 6.0))
        f += 0.3 * noise
        
        # Add additional complexity with cross-dimensional interactions
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                cross_sum += np.sin(x[i] * x[j] * 0.9) * np.cos(x[i] + x[j])
        f += 0.8 * cross_sum
        
        # Add new chaotic interaction term
        chaotic_term = 0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * 2.5 + np.sin(x[i] * 6.0) + np.sin(x[i] * 3.0))
        f += 0.6 * chaotic_term
        
        # Add higher-order polynomial interactions
        poly_high = 0
        for i in range(self.dim):
            poly_high += x[i]**4 + x[i]**3 + x[i]**2
        f += 0.4 * poly_high
        
        return f