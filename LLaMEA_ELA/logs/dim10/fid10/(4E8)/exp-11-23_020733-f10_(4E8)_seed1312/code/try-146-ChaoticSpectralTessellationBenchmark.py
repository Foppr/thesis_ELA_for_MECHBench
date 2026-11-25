import numpy as np

class ChaoticSpectralTessellationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.chebyshev_coeffs = np.random.uniform(-0.5, 0.5, (dim, 5))
        self.tessellation_levels = np.random.randint(2, 6, dim)
        self.spectral_filters = np.random.uniform(0.1, 2.0, dim)
        self.dynamical_couplings = np.random.uniform(-0.3, 0.3, (dim, dim))
        self.transition_points = np.random.uniform(-5.0, 5.0, (dim, 3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base chaotic quadratic term
        base_term = np.sum(x**2) * (1.0 + 0.2 * np.sin(np.sum(x**3)))
        result += 0.1 * base_term
        
        # Chaotic Chebyshev polynomial components
        for i in range(self.dim):
            cheb_poly = np.polynomial.chebyshev.chebval(x[i], self.chebyshev_coeffs[i])
            result += 0.5 * cheb_poly
            
        # Hierarchical tessellation with adaptive scaling
        for i in range(self.dim):
            level_sum = 0.0
            for level in range(1, self.tessellation_levels[i] + 1):
                scale = 2.0 ** (-level)
                # Tessellated pattern with multiple frequencies
                tesselation = np.sin(scale * x[i]) + 0.5 * np.cos(2 * scale * x[i])
                level_sum += scale * tesselation
                
            result += 0.3 * level_sum
            
        # Spectral filtering with dynamic weights
        for i in range(self.dim):
            filtered_x = x[i] * self.spectral_filters[i]
            spectral_component = np.sin(filtered_x) + 0.3 * np.cos(3 * filtered_x)
            result += 0.2 * spectral_component
            
        # Cross-dimensional chaotic coupling
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.dynamical_couplings[i, j]
                    coupling_term = coupling_strength * np.sin(x[i] + x[j])
                    coupling_sum += coupling_term
                    
            result += 0.1 * coupling_sum
            
        # Sharp transition regions with adaptive thresholds
        for i in range(self.dim):
            transitions = 0.0
            for point in self.transition_points[i]:
                # Hyperbolic tangent based transition function
                trans_func = np.tanh(10 * (x[i] - point))
                transitions += 2.0 * (1.0 + trans_func) * np.exp(-0.5 * (x[i] - point)**2)
                
            result += 0.4 * transitions
            
        # Non-smooth high-frequency oscillations
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(x[i])
            high_freq_term = np.sin(freq * x[i]) * np.cos(freq * x[i])
            result += 0.25 * high_freq_term
            
        # Adaptive conditioning based on neighborhood
        neighborhood_sum = 0.0
        for i in range(self.dim):
            neighbor_sum = 0.0
            for j in range(max(0, i-1), min(self.dim, i+2)):
                if i != j:
                    neighbor_sum += np.abs(x[i] - x[j])
            neighborhood_sum += neighbor_sum
            
        condition_factor = 1.0 + 0.3 * np.tanh(neighborhood_sum)
        result *= condition_factor
        
        # Add noise with chaotic amplitude modulation
        noise_amplitude = 0.1 * (1.0 + 0.2 * np.sin(np.sum(x**4)))
        noise = noise_amplitude * np.random.uniform(-1, 1)
        result += noise
        
        return result