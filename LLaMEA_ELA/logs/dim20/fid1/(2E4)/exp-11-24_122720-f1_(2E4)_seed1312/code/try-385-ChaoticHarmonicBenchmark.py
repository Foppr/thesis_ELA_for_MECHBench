import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic map parameters
        self.chebyshev_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        # Spherical harmonics coefficients
        self.sph_harm_amplitudes = np.random.uniform(0.5, 2.0, (dim, 3))
        self.sph_harm_orders = np.random.randint(1, 4, dim)
        # Asymmetric polynomial coupling terms
        self.poly_coupling = np.random.uniform(-0.5, 0.5, (dim, 3))
        # Chaotic tent map parameters
        self.tent_map_params = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component
        tent_sum = 0
        for i in range(self.dim):
            # Apply tent map iteration
            xi = x[i]
            for _ in range(5):  # Multiple iterations for chaos
                if xi < self.tent_map_params[i]:
                    xi = self.tent_map_params[i] * xi
                else:
                    xi = (1 - self.tent_map_params[i]) * (1 - xi)
            tent_sum += xi**2
        
        # Chebyshev polynomial component
        cheby_sum = 0
        for i in range(self.dim):
            # Evaluate Chebyshev polynomial of degree 3
            t_x = np.clip(x[i] / 5.0, -1.0, 1.0)  # Normalize to [-1,1]
            T0 = 1
            T1 = t_x
            T2 = 2 * t_x**2 - 1
            T3 = 4 * t_x**3 - 3 * t_x
            cheby_term = (self.chebyshev_coeffs[i, 0] * T0 + 
                         self.chebyshev_coeffs[i, 1] * T1 + 
                         self.chebyshev_coeffs[i, 2] * T2 + 
                         self.chebyshev_coeffs[i, 3] * T3)
            cheby_sum += cheby_term
        
        # Spherical harmonics component
        sph_sum = 0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2)) / 5.0
            theta = np.arctan2(x[i], x[(i+1)%self.dim]) if self.dim > 1 else 0
            phi = np.arccos(x[i] / (r * 5.0 + 1e-8))
            
            # Simple harmonic terms
            sph_term = (self.sph_harm_amplitudes[i, 0] * np.sin(self.sph_harm_orders[i] * theta) +
                       self.sph_harm_amplitudes[i, 1] * np.cos(self.sph_harm_orders[i] * phi) +
                       self.sph_harm_amplitudes[i, 2] * np.sin(self.sph_harm_orders[i] * phi))
            sph_sum += sph_term
        
        # Asymmetric polynomial coupling
        poly_coupling_sum = 0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.poly_coupling[i, 0] + 
                        self.poly_coupling[i, 1] * x_i**2 + 
                        self.poly_coupling[i, 2] * x_i**3)
            poly_coupling_sum += np.abs(poly_term) * np.sign(x_i)
        
        # Combine all components
        result = (0.8 * tent_sum + 
                 1.2 * cheby_sum + 
                 0.6 * sph_sum + 
                 1.0 * poly_coupling_sum)
        
        return result