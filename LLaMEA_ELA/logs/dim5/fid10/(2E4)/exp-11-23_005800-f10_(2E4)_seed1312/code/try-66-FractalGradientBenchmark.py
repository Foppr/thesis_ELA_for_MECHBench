import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal parameters
        self.hurst = 0.3
        self.fractal_dim = 1.5
        self.base_freq = 2.0
        self.gradient_strength = 0.8
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal component using fractional Brownian motion-like approach
        fractal = 0.0
        for i in range(self.dim):
            # Scale x to [0, 1] for fractal generation
            scaled_x = (x[i] + 5.0) / 10.0
            
            # Multi-fractal scaling with different frequencies
            freqs = [self.base_freq * (2 ** k) for k in range(5)]
            weights = [1.0 / (2 ** k) for k in range(5)]
            
            fractal_component = 0.0
            for freq, weight in zip(freqs, weights):
                # Using sine waves with varying frequencies and amplitudes
                fractal_component += weight * np.sin(freq * scaled_x * np.pi)
            
            fractal += fractal_component
            
        # Adaptive gradient field component
        gradient = 0.0
        for i in range(self.dim):
            # Directional bias based on dimension index
            direction = np.sin(i * np.pi / self.dim) if i % 2 == 0 else np.cos(i * np.pi / self.dim)
            
            # Gradient strength modulated by solution proximity to center
            proximity_factor = 1.0 / (1.0 + np.exp(-self.gradient_strength * abs(x[i])))
            
            # Combined gradient effect
            gradient += direction * x[i] * proximity_factor
            
        # Multi-scale harmonic interference with varying amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0]
            phases = [0.0, np.pi/6, np.pi/3, np.pi/2, 2*np.pi/3]
            amplitudes = [1.0, 0.8, 0.6, 0.4, 0.2]
            
            for f, p, a in zip(freqs, phases, amplitudes):
                harmonic += a * np.sin(f * x[i] + p) * np.cos(f * x[i] / 3.0 + p/3.0)
                
        # Cross-dimensional coupling with fractal-like interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                # Fractal-like weight based on dimension indices
                weight = (1.0 + np.sin((i + j) * np.pi / self.dim)) * np.exp(-0.1 * abs(diff))
                cross += weight * np.exp(-0.5 * (diff**2)) * np.sin(3.0 * diff)
                
        # Polynomial and exponential combination for non-linearity
        poly_exp = 0.0
        for i in range(self.dim):
            # Higher-order polynomial with exponential decay
            poly_exp += (x[i]**4 + x[i]**3 + x[i]**2) * np.exp(-0.1 * abs(x[i]))
            
        # Global scaling and offset to ensure proper fitness values
        result = 0.5 * fractal + 0.8 * gradient + 0.6 * harmonic + 0.4 * cross + 0.3 * poly_exp
        
        # Add fractal dimension scaling factor
        result *= (1.0 + self.fractal_dim * np.sum(np.abs(x)) / self.dim)
        
        return result + 5.0 * self.dim  # Offset to ensure positive fitness values