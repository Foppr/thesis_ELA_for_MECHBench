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
                # Add scaled sinusoidal component with modified phase shift
                fbm_value += (1.0 / freq) * np.sin(freq * x[i] + k * 0.5) * np.exp(-0.1 * x[i]**2)
            
            # Apply amplitude and scale factor
            fbm_value *= self.fractal_amplitudes[i] * self.scale_factors[i]
            
            # Add adaptive weighting with modified exponent
            result += self.adaptive_weights[i] * np.abs(fbm_value)**1.5
            
        # Cross-dimensional coupling terms with enhanced nonlinearity
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Delayed coupling with exponential decay and additional nonlinear term
                    delay = self.coupling_delays[i][j]
                    coupled_val = x[j] - x[i]
                    coupling = self.coupling_strengths[i][j] * np.exp(-0.1 * coupled_val**2) * np.sin(self.pattern_strengths[i] * coupled_val)
                    # Add quadratic enhancement to coupling
                    coupling_term += coupling + 0.1 * coupling**2
                    
        # Add coupling component with scaling
        result += 0.7 * coupling_term**2
        
        # Fractal dimension and pattern complexity terms
        complexity_term = 0.0
        for i in range(self.dim):
            # Scale-invariant pattern with fractal dimension control and modified interaction
            pattern_val = np.sin(self.fractal_dimensions[i] * x[i]) * np.cos(self.pattern_strengths[i] * x[i])
            # Add cubic enhancement for increased nonlinearity
            complexity_term += self.fractal_amplitudes[i] * pattern_val**3
            
        result += 0.4 * complexity_term
        
        # Add noise component for robustness with modified scaling
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += self.noise_levels[i] * np.random.uniform(-1, 1) * np.exp(-0.05 * x[i]**2)
            
        result += 0.15 * noise_term
        
        # Normalize by dimension and add final scaling with modified quadratic term
        result = result / (self.dim + 1.0) + 0.7 * np.sum(x**2) / self.dim
        
        return result