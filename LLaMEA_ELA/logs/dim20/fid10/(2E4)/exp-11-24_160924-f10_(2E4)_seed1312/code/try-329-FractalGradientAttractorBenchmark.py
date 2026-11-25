import numpy as np

class FractalGradientAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension with fractal and gradient properties
        self.fractal_dimensions = np.random.uniform(1.2, 2.8, dim)
        self.gradient_magnitudes = np.random.uniform(0.3, 3.5, dim)
        self.attractor_positions = np.random.uniform(-4.5, 4.5, dim)
        self.attractor_strengths = np.random.uniform(0.8, 4.5, dim)
        self.resonance_frequencies = np.random.uniform(0.3, 3.5, dim)
        self.fractal_amplitudes = np.random.uniform(0.3, 3.0, dim)
        self.hill_climbing_rates = np.random.uniform(0.05, 0.95, dim)
        self.stochastic_noise_levels = np.random.uniform(0.02, 0.4, dim)
        self.basin_widths = np.random.uniform(0.3, 2.5, dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.2, (dim, dim))
        self.multiscale_factors = np.random.uniform(0.05, 2.0, dim)
        self.spectral_peaks = np.random.uniform(0.8, 6.0, dim)
        self.chaos_parameters = np.random.uniform(0.1, 1.0, dim)
        self.filter_bandwidths = np.random.uniform(0.5, 3.0, dim)
        self.adaptive_scaling_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Fractal gradient components with self-similar structure
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dimensions[i]
            grad_mag = self.gradient_magnitudes[i]
            
            # Multi-scale fractal gradient with power-law scaling and chaotic modulation
            fractal_gradient = grad_mag * np.sin(xi) * np.cos(xi)
            fractal_gradient += 0.5 * np.sin(2 * xi) * np.cos(2 * xi)
            fractal_gradient += 0.3 * np.sin(4 * xi) * np.cos(4 * xi)
            fractal_gradient *= (1.0 + 0.2 * np.sin(self.chaos_parameters[i] * xi))
            
            # Power-law scaling with fractal dimension
            result += fractal_gradient * (np.abs(xi)**fractal_dim)
            
        # Hybrid attractor landscape with resonance phenomena and adaptive filtering
        for i in range(self.dim):
            xi = x[i]
            pos = self.attractor_positions[i]
            strength = self.attractor_strengths[i]
            freq = self.resonance_frequencies[i]
            
            # Stochastic resonance-like attraction with fractal basin and spectral filtering
            distance = np.abs(xi - pos)
            basin_width = self.basin_widths[i] * (1.0 + 0.3 * np.sin(0.4 * xi))
            
            # Multi-scale basin attraction with power-law decay and adaptive scaling
            attractor_term = strength * np.exp(-distance**2 / (2 * basin_width**2))
            attractor_term *= (1.0 + 0.1 * np.sin(self.adaptive_scaling_factors[i] * xi))
            result += attractor_term
            
        # Multiscale fractal components with hybrid harmonic structure and spectral filtering
        for i in range(self.dim):
            xi = x[i]
            amp = self.fractal_amplitudes[i]
            scale_factor = self.multiscale_factors[i]
            
            # Multi-scale fractal harmonic with spectral peaks and chaotic modulation
            fractal_component = amp * np.sin(scale_factor * xi) * np.cos(scale_factor * xi)
            fractal_component += 0.5 * np.sin(2 * scale_factor * xi) * np.cos(2 * scale_factor * xi)
            fractal_component += 0.3 * np.sin(3 * scale_factor * xi) * np.cos(3 * scale_factor * xi)
            
            # Spectral peak modulation with adaptive filtering
            spectral_mod = self.spectral_peaks[i] * np.sin(xi)
            fractal_component *= (1.0 + 0.2 * spectral_mod)
            fractal_component *= (1.0 + 0.15 * np.cos(self.filter_bandwidths[i] * xi))
            result += fractal_component
            
        # Cross-dimensional coupling with hybrid fractal interaction and chaotic resonance
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling_strength = self.coupling_strengths[i][j]
                
                # Fractal-like cross-dimension coupling with power-law interaction and chaotic modulation
                coupling_term = coupling_strength * np.sin(xi + xj) * np.cos(xi - xj)
                coupling_term += 0.4 * np.sin(2 * (xi + xj)) * np.cos(2 * (xi - xj))
                coupling_term *= (1.0 + 0.1 * np.sin(self.chaos_parameters[i] * xi) * np.cos(self.chaos_parameters[j] * xj))
                result += coupling_term
                
        # Stochastic noise with fractal characteristics and adaptive filtering
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.stochastic_noise_levels[i]
            
            # Fractal noise component with multi-scale influence and spectral modulation
            noise_component = noise_level * np.sin(10.0 * xi) * np.cos(5.0 * xi)
            noise_component += 0.3 * np.sin(20.0 * xi) * np.cos(10.0 * xi)
            noise_component *= (1.0 + 0.1 * np.sin(self.filter_bandwidths[i] * xi))
            result += noise_component
            
        # Hill-climbing gradient with self-similar scaling and chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            rate = self.hill_climbing_rates[i]
            
            # Self-similar hill-climbing component with adaptive scaling
            hill_term = rate * np.exp(-xi**2 / 2) * (1.0 + 0.3 * np.sin(3 * xi))
            hill_term *= (1.0 + 0.1 * np.cos(self.chaos_parameters[i] * xi))
            result += hill_term
            
        # Global scaling with fractal modulation and spectral filtering
        global_factor = 1.0 + 0.5 * np.sin(np.sum(x) / self.dim)
        global_factor *= (1.0 + 0.2 * np.cos(2.0 * np.sum(x)))
        global_factor *= (1.0 + 0.1 * np.sin(self.filter_bandwidths[0] * np.sum(x)))
        result *= global_factor
        
        return result