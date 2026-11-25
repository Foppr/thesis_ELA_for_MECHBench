import numpy as np

class FractalGradientAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension with fractal and gradient properties
        self.fractal_dimensions = np.random.uniform(1.1, 2.9, dim)
        self.gradient_magnitudes = np.random.uniform(0.5, 3.0, dim)
        self.attractor_positions = np.random.uniform(-4.0, 4.0, dim)
        self.attractor_strengths = np.random.uniform(1.0, 4.0, dim)
        self.resonance_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 2.5, dim)
        self.hill_climbing_rates = np.random.uniform(0.1, 0.9, dim)
        self.stochastic_noise_levels = np.random.uniform(0.01, 0.3, dim)
        self.basin_widths = np.random.uniform(0.5, 2.0, dim)
        self.coupling_strengths = np.random.uniform(0.2, 1.0, (dim, dim))
        self.multiscale_factors = np.random.uniform(0.1, 1.5, dim)
        self.spectral_peaks = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Fractal gradient components with self-similar structure
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dimensions[i]
            grad_mag = self.gradient_magnitudes[i]
            
            # Multi-scale fractal gradient with power-law scaling
            fractal_gradient = grad_mag * np.sin(xi) * np.cos(xi)
            fractal_gradient += 0.5 * np.sin(2 * xi) * np.cos(2 * xi)
            fractal_gradient += 0.3 * np.sin(4 * xi) * np.cos(4 * xi)
            
            # Power-law scaling with fractal dimension
            result += fractal_gradient * (np.abs(xi)**fractal_dim)
            
        # Hybrid attractor landscape with resonance phenomena
        for i in range(self.dim):
            xi = x[i]
            pos = self.attractor_positions[i]
            strength = self.attractor_strengths[i]
            freq = self.resonance_frequencies[i]
            
            # Stochastic resonance-like attraction with fractal basin
            distance = np.abs(xi - pos)
            basin_width = self.basin_widths[i] * (1.0 + 0.2 * np.sin(0.5 * xi))
            
            # Multi-scale basin attraction with power-law decay
            attractor_term = strength * np.exp(-distance**2 / (2 * basin_width**2))
            result += attractor_term
            
        # Multiscale fractal components with hybrid harmonic structure
        for i in range(self.dim):
            xi = x[i]
            amp = self.fractal_amplitudes[i]
            scale_factor = self.multiscale_factors[i]
            
            # Multi-scale fractal harmonic with spectral peaks
            fractal_component = amp * np.sin(scale_factor * xi) * np.cos(scale_factor * xi)
            fractal_component += 0.5 * np.sin(2 * scale_factor * xi) * np.cos(2 * scale_factor * xi)
            fractal_component += 0.3 * np.sin(3 * scale_factor * xi) * np.cos(3 * scale_factor * xi)
            
            # Spectral peak modulation
            spectral_mod = self.spectral_peaks[i] * np.sin(xi)
            result += fractal_component * (1.0 + 0.2 * spectral_mod)
            
        # Cross-dimensional coupling with hybrid fractal interaction
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling_strength = self.coupling_strengths[i][j]
                
                # Fractal-like cross-dimension coupling with power-law interaction
                coupling_term = coupling_strength * np.sin(xi + xj) * np.cos(xi - xj)
                coupling_term += 0.4 * np.sin(2 * (xi + xj)) * np.cos(2 * (xi - xj))
                result += coupling_term
                
        # Stochastic noise with fractal characteristics
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.stochastic_noise_levels[i]
            
            # Fractal noise component with multi-scale influence
            noise_component = noise_level * np.sin(10.0 * xi) * np.cos(5.0 * xi)
            noise_component += 0.3 * np.sin(20.0 * xi) * np.cos(10.0 * xi)
            result += noise_component
            
        # Hill-climbing gradient with self-similar scaling
        for i in range(self.dim):
            xi = x[i]
            rate = self.hill_climbing_rates[i]
            
            # Self-similar hill-climbing component
            hill_term = rate * np.exp(-xi**2 / 2) * (1.0 + 0.3 * np.sin(3 * xi))
            result += hill_term
            
        # Global scaling with fractal modulation
        global_factor = 1.0 + 0.5 * np.sin(np.sum(x) / self.dim)
        global_factor *= (1.0 + 0.2 * np.cos(2.0 * np.sum(x)))
        result *= global_factor
        
        return result