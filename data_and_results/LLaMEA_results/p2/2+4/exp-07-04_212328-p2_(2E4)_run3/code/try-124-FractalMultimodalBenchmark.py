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
        for i in range(10):
            # Create nested minima at different scales
            scale = 0.5**(i+1)
            center = np.array([np.sin(i * 0.3) * 4.0 * scale, np.cos(i * 0.3) * 4.0 * scale])
            if self.dim >= 2:
                diff = x[:2] - center
                # Use varying amplitudes and frequencies for fractal structure
                amplitude = 2.0 * (1.0 + 0.5 * np.sin(i * 0.7))
                frequency = 1.0 + 0.3 * np.cos(i * 0.5)
                fractal_sum += amplitude * np.exp(-0.5 * np.sum(diff**2) / (0.2 * frequency))
        
        f += 1.5 * fractal_sum
        
        # Add dynamic amplitude modulation based on input values
        amp_mod = 0
        for i in range(self.dim):
            # Use chaotic modulation with recursive pattern
            amp = 1.0 + 0.5 * np.sin(x[i] * 2.0 + np.sin(x[i] * 3.0))
            amp_mod += amp * np.cos(x[i] * 1.5 + np.cos(x[i] * 0.8))
        f += 0.8 * amp_mod
        
        # Add hierarchical coupling with multiple levels
        coupling_sum = 0
        for level in range(3):
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    # Level-dependent coupling strength
                    strength = 0.5 * (level + 1)
                    # Dynamic coupling with fractal-like pattern
                    coupling = strength * np.sin(x[i] * x[j] * 0.5 + 
                                                np.sin(x[i] + x[j]) * 0.3 * (level + 1))
                    coupling_sum += coupling
        f += 1.2 * coupling_sum
        
        # Add self-similar sinusoidal interactions
        self_similar_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create self-similar pattern with varying frequencies
                freq1 = 1.0 + 0.2 * np.sin(x[i] * 0.5)
                freq2 = 1.0 + 0.2 * np.cos(x[j] * 0.5)
                self_similar_sum += np.sin(x[i] * freq1) * np.cos(x[j] * freq2)
        f += 0.6 * self_similar_sum
        
        # Add multi-scale chaotic interactions
        chaotic_sum = 0
        for i in range(self.dim):
            # Use chaotic map for dynamic interaction
            chaotic_val = np.sin(x[i] * 3.0 + np.sin(x[i] * 7.0))
            chaotic_sum += chaotic_val * np.cos(x[i] * 2.0 + np.cos(x[i] * 5.0))
        f += 0.4 * chaotic_sum
        
        # Add polynomial chaos with hierarchical structure
        poly_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hierarchical polynomial terms
                poly_sum += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j] * 0.3)
        f += 0.7 * poly_sum
        
        # Add multiple global minima with fractal distribution
        minima_positions = []
        for i in range(20):
            # Fractal-like distribution of minima
            angle = i * 0.3 * np.pi
            radius = 3.0 * (0.5**(i % 5))
            minima_positions.append([radius * np.cos(angle), radius * np.sin(angle)])
            
        minima_sum = 0
        for pos in minima_positions:
            if self.dim >= len(pos):
                diff = x[:len(pos)] - np.array(pos)
                # Varying amplitudes for minima
                amplitude = 1.0 + 0.3 * np.sin(i * 0.4)
                minima_sum += amplitude * np.exp(-0.2 * np.sum(diff**2))
        f += 1.8 * minima_sum
        
        # Add noise with fractal pattern
        noise = 0
        for i in range(self.dim):
            # Fractal noise pattern
            noise += np.sin(x[i] * 8.0 + np.sin(x[i] * 12.0) + np.sin(x[i] * 4.0))
        f += 0.2 * noise
        
        # Add improved complexity with enhanced non-separability
        # Introduce more complex interaction terms to increase difficulty
        complex_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    # Triple interaction terms for increased complexity
                    complex_interaction += np.sin(x[i] * x[j] * x[k] * 0.1) * (1.0 + 0.1 * np.sin(x[i] + x[j] + x[k]))
        f += 0.5 * complex_interaction
        
        # Add enhanced chaotic behavior with higher frequency components
        enhanced_chaos = 0
        for i in range(self.dim):
            enhanced_chaos += np.sin(x[i] * 10.0 + np.sin(x[i] * 20.0) + np.sin(x[i] * 5.0))
        f += 0.3 * enhanced_chaos
        
        # Add improved hierarchical structure with more levels
        hierarchical_sum = 0
        for level in range(4):
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    # More complex hierarchical coupling
                    strength = 0.3 * (level + 1) * np.sin(level * 0.2)
                    hierarchical_sum += strength * np.cos(x[i] * x[j] * 0.2 + np.sin(x[i] + x[j]) * 0.1 * (level + 1))
        f += 1.0 * hierarchical_sum
        
        return f