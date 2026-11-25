import numpy as np

class FractalBrownianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters
        self.hurst_exponents = np.random.uniform(0.1, 0.9, dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.scale_factors = np.random.uniform(0.5, 3.0, dim)
        # Cross-dimensional coupling parameters
        self.coupling_strengths = np.random.uniform(0.1, 1.5, (dim, dim))
        self.coupling_delays = np.random.randint(1, 6, (dim, dim))
        # Adaptive scaling parameters
        self.adaptive_weights = np.random.uniform(0.5, 2.0, dim)
        self.noise_levels = np.random.uniform(0.01, 0.3, dim)
        # Fractal dimension and complexity control
        self.fractal_dimensions = np.random.uniform(1.0, 3.0, dim)
        self.pattern_strengths = np.random.uniform(0.5, 2.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal Brownian motion component for each dimension
        for i in range(self.dim):
            # Generate fractal Brownian motion value
            fbm_value = 0.0
            n_terms = int(10 * (self.hurst_exponents[i] + 0.5))
            
            for k in range(1, n_terms + 1):
                # Scale the frequency based on Hurst exponent
                freq = k ** (2.0 * self.hurst_exponents[i] - 1.0)
                # Add scaled sinusoidal component
                fbm_value += (1.0 / freq) * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
            # Apply amplitude and scale factor
            fbm_value *= self.fractal_amplitudes[i] * self.scale_factors[i]
            
            # Add adaptive weighting
            result += self.adaptive_weights[i] * fbm_value**2
            
        # Cross-dimensional coupling terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Delayed coupling with exponential decay
                    delay = self.coupling_delays[i][j]
                    coupled_val = x[j] - x[i]
                    coupling = self.coupling_strengths[i][j] * np.exp(-0.1 * coupled_val**2) * np.sin(self.pattern_strengths[i] * coupled_val)
                    coupling_term += coupling
                    
        # Add coupling component with scaling
        result += 0.5 * coupling_term**2
        
        # Fractal dimension and pattern complexity terms
        complexity_term = 0.0
        for i in range(self.dim):
            # Scale-invariant pattern with fractal dimension control
            pattern_val = np.sin(self.fractal_dimensions[i] * x[i]) * np.cos(self.pattern_strengths[i] * x[i])
            complexity_term += self.fractal_amplitudes[i] * pattern_val**2
            
        result += 0.3 * complexity_term
        
        # Add noise component for robustness
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += self.noise_levels[i] * np.random.uniform(-1, 1) * np.exp(-0.05 * x[i]**2)
            
        result += 0.1 * noise_term
        
        # Normalize by dimension and add final scaling
        result = result / (self.dim + 1.0) + 0.5 * np.sum(x**2) / self.dim
        
        return result