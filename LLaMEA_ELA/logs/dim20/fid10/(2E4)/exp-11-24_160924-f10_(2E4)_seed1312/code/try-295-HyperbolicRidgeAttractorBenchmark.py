import numpy as np

class HyperbolicRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.ridge_centers = np.random.uniform(-3.0, 3.0, dim)
        self.ridge_heights = np.random.uniform(1.0, 4.0, dim)
        self.ridge_widths = np.random.uniform(0.5, 2.0, dim)
        self.polynomial_degrees = np.random.randint(3, 7, dim)
        self.tanh_amplitudes = np.random.uniform(0.5, 2.5, dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.5, dim)
        self.adaptation_factors = np.random.uniform(0.3, 1.2, dim)
        # Additional dynamic parameters
        self.dynamic_exponents = np.random.uniform(1.0, 3.0, dim)
        self.modulation_frequencies = np.random.uniform(2.0, 6.0, dim)
        self.basin_depths = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add hyperbolic ridge contributions
        for i in range(self.dim):
            xi = x[i]
            center = self.ridge_centers[i]
            height = self.ridge_heights[i]
            width = self.ridge_widths[i]
            degree = self.polynomial_degrees[i]
            
            # Hyperbolic tangent ridge with polynomial modulation
            ridge_term = height * np.tanh((xi - center) / width) * (xi**degree)
            result += ridge_term
            
        # Add polynomial gradient components with hyperbolic modulation
        for i in range(self.dim):
            xi = x[i]
            degree = self.polynomial_degrees[i]
            tanh_amp = self.tanh_amplitudes[i]
            
            # Polynomial with hyperbolic tangent gradient modulation
            poly_term = (xi**degree) * np.tanh(tanh_amp * xi)
            result += 0.5 * poly_term
            
        # Add dynamic coupling between dimensions
        for i in range(self.dim):
            xi = x[i]
            coupling_strength = self.coupling_strengths[i]
            adaptation_factor = self.adaptation_factors[i]
            
            # Dynamic coupling that adapts based on position
            coupling_mod = 1.0 + adaptation_factor * np.tanh(xi)
            result += coupling_strength * coupling_mod * np.sum(x**2) / self.dim
            
        # Add adaptive dimension interaction with hyperbolic scaling
        for i in range(self.dim):
            xi = x[i]
            exponent = self.dynamic_exponents[i]
            freq = self.modulation_frequencies[i]
            
            # Adaptive modulation based on position and frequency
            adaptive_term = np.sin(freq * xi) * np.tanh(xi) * (1.0 + 0.2 * np.sin(xi**2))
            result += 0.3 * adaptive_term
            
        # Add basin depth modulation with polynomial scaling
        for i in range(self.dim):
            xi = x[i]
            basin_depth = self.basin_depths[i]
            
            # Basin structure with polynomial depth and hyperbolic scaling
            basin_term = basin_depth * (xi**4) * np.tanh(xi)
            result += 0.2 * basin_term
            
        # Add cross-dimensional interaction with dynamic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi, xj = x[i], x[j]
                coupling_strength = self.coupling_strengths[i] * self.coupling_strengths[j]
                
                # Dynamic cross-coupling with hyperbolic tangent interaction
                cross_term = coupling_strength * np.tanh(xi + xj) * (xi**2 + xj**2)
                result += 0.15 * cross_term
                
        # Add polynomial ridge structure with varying depths and widths
        for i in range(self.dim):
            xi = x[i]
            degree = self.polynomial_degrees[i]
            width = self.ridge_widths[i]
            
            # Multi-scale polynomial ridge with hyperbolic scaling
            poly_ridge = (xi**degree) * np.tanh(xi / width)
            result += 0.25 * poly_ridge
            
        # Add frequency-modulated component with dynamic scaling
        freq_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = self.modulation_frequencies[i]
            
            # Frequency modulation with hyperbolic tangent
            freq_component += np.sin(freq * xi) * np.tanh(xi)
        result += 0.3 * freq_component**2
        
        # Add global scaling based on input magnitude
        input_magnitude = np.sum(x**2)**0.5
        global_scale = 1.0 + 0.3 * np.tanh(input_magnitude / self.dim)
        result *= global_scale
        
        # Add final hyperbolic modulation with adaptive parameters
        final_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            amp = self.tanh_amplitudes[i]
            
            # Final hyperbolic component with dynamic amplitude
            final_term += np.tanh(amp * xi) * (xi**3)
        result += 0.15 * final_term
        
        return result