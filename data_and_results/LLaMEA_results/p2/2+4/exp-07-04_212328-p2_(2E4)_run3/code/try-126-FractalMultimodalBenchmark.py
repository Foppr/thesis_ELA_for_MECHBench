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
                amplitude = 2.5 * (1.0 + 0.5 * np.sin(i * 0.7))  # Increased base amplitude
                frequency = 1.2 + 0.3 * np.cos(i * 0.5)  # Slightly increased frequency
                fractal_sum += amplitude * np.exp(-0.5 * np.sum(diff**2) / (0.15 * frequency))  # Reduced variance
        
        f += 1.8 * fractal_sum  # Increased weight
        
        # Add dynamic amplitude modulation based on input values
        amp_mod = 0
        for i in range(self.dim):
            # Use chaotic modulation with recursive pattern
            amp = 1.2 + 0.6 * np.sin(x[i] * 2.0 + np.sin(x[i] * 3.0))  # Increased modulation
            amp_mod += amp * np.cos(x[i] * 1.8 + np.cos(x[i] * 0.8))  # Increased frequency
        f += 1.0 * amp_mod  # Increased weight
        
        # Add hierarchical coupling with multiple levels
        coupling_sum = 0
        for level in range(3):
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    # Level-dependent coupling strength
                    strength = 0.7 * (level + 1)  # Increased coupling strength
                    # Dynamic coupling with fractal-like pattern
                    coupling = strength * np.sin(x[i] * x[j] * 0.6 +  # Increased frequency
                                                np.sin(x[i] + x[j]) * 0.4 * (level + 1))  # Increased modulation
                    coupling_sum += coupling
        f += 1.5 * coupling_sum  # Increased weight
        
        # Add self-similar sinusoidal interactions
        self_similar_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create self-similar pattern with varying frequencies
                freq1 = 1.2 + 0.2 * np.sin(x[i] * 0.5)  # Increased base frequency
                freq2 = 1.2 + 0.2 * np.cos(x[j] * 0.5)  # Increased base frequency
                self_similar_sum += np.sin(x[i] * freq1) * np.cos(x[j] * freq2)
        f += 0.8 * self_similar_sum  # Increased weight
        
        # Add multi-scale chaotic interactions
        chaotic_sum = 0
        for i in range(self.dim):
            # Use chaotic map for dynamic interaction
            chaotic_val = np.sin(x[i] * 3.5 + np.sin(x[i] * 7.0))  # Increased frequency
            chaotic_sum += chaotic_val * np.cos(x[i] * 2.5 + np.cos(x[i] * 5.0))  # Increased frequency
        f += 0.5 * chaotic_sum  # Increased weight
        
        # Add polynomial chaos with hierarchical structure
        poly_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hierarchical polynomial terms
                poly_sum += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j] * 0.4)  # Increased frequency
        f += 0.9 * poly_sum  # Increased weight
        
        # Add multiple global minima with fractal distribution
        minima_positions = []
        for i in range(20):
            # Fractal-like distribution of minima
            angle = i * 0.3 * np.pi
            radius = 3.5 * (0.5**(i % 5))  # Increased radius
            minima_positions.append([radius * np.cos(angle), radius * np.sin(angle)])
            
        minima_sum = 0
        for pos in minima_positions:
            if self.dim >= len(pos):
                diff = x[:len(pos)] - np.array(pos)
                # Varying amplitudes for minima
                amplitude = 1.2 + 0.3 * np.sin(i * 0.4)  # Increased base amplitude
                minima_sum += amplitude * np.exp(-0.15 * np.sum(diff**2))  # Reduced variance
        f += 2.0 * minima_sum  # Increased weight
        
        # Add noise with fractal pattern
        noise = 0
        for i in range(self.dim):
            # Fractal noise pattern
            noise += np.sin(x[i] * 9.0 + np.sin(x[i] * 12.0) + np.sin(x[i] * 4.0))  # Increased frequency
        f += 0.3 * noise  # Increased weight
        
        return f