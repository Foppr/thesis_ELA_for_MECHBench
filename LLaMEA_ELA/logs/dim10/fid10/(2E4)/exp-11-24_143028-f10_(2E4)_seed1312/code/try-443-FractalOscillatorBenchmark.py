import numpy as np

class FractalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters
        self.chebyshev_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        self.tent_parameters = np.random.uniform(1.5, 3.0, dim)
        # Enhanced fractal basin structures
        self.basin_centers = np.random.uniform(-4.0, 4.0, dim)
        self.basin_radii = np.random.uniform(0.5, 2.0, dim)
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-0.5, 0.5, (dim, 10))
        # Quantum interference patterns
        self.quantum_phases = np.random.uniform(0, 2*np.pi, dim)
        self.quantum_amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Adaptive noise scaling
        self.noise_levels = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic tent map component
        tent_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Apply Chebyshev polynomial approximation to tent map
            point = x[i]
            tent_val = 0.0
            for k in range(5):
                tent_val += self.chebyshev_coeffs[i, k] * np.cos(k * np.arccos(point))
            tent_values[i] = tent_val
        
        # Add polynomial chaos expansion terms
        poly_terms = np.zeros(self.dim)
        for i in range(self.dim):
            poly_val = 0.0
            for k in range(10):
                poly_val += self.poly_coeffs[i, k] * np.polynomial.hermite.hermval(x[i], [0]*k + [1])
            poly_terms[i] = poly_val
        
        # Compute quantum interference patterns
        quantum_terms = np.zeros(self.dim)
        for i in range(self.dim):
            quantum_terms[i] = self.quantum_amplitudes[i] * np.sin(self.quantum_phases[i] * x[i] + 
                                                                  np.sin(self.quantum_phases[i] * x[i]))
        
        # Enhanced basin attraction terms
        basin_terms = np.zeros(self.dim)
        for i in range(self.dim):
            # Enhanced fractal basin with Chebyshev scaling
            distance = np.abs(x[i] - self.basin_centers[i])
            basin_terms[i] = (self.basin_radii[i] / (distance + 1e-8)) * \
                            np.exp(-0.5 * (distance / self.basin_radii[i])**2) * \
                            np.cos(2 * np.pi * distance)
        
        # Combine all components
        fitness = 0.0
        for i in range(self.dim):
            # Nonlinear interaction terms with quantum coupling
            interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction += (np.sin(x[i] - x[j]) * 
                                  np.cos(self.quantum_phases[i] * x[j]) * 
                                  (1 + 0.2 * np.sin(x[i] + x[j])))
            
            # Chaotic energy term with polynomial mixing
            chaotic_energy = tent_values[i]**2 + 0.2 * tent_values[i]**3 + 0.05 * tent_values[i]**4
            
            # Polynomial chaos contribution
            poly_contribution = poly_terms[i]**2
            
            # Quantum interference component
            quantum_contribution = quantum_terms[i]**2
            
            # Basin attraction component
            basin_contribution = basin_terms[i]
            
            # Adaptive noise term
            noise_term = self.noise_levels[i] * np.random.normal(0, 1)
            
            # Combine all terms with cross-dimensional coupling
            fitness += chaotic_energy + poly_contribution + quantum_contribution + \
                      basin_contribution + interaction + noise_term
        
        # Normalize and return
        fitness = fitness / self.dim
        return fitness