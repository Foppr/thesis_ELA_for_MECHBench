import numpy as np

class ChaoticPolynomialPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Chaotic tent map parameters for dimension coupling
        self.chebyshev_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, 4))
        self.tent_maps = np.random.uniform(0.5, 1.5, size=dim)
        
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, size=(dim, 6))
        
        # Dynamic penalty function parameters
        self.penalty_weights = np.random.uniform(0.5, 3.0, size=dim)
        self.penalty_exponents = np.random.uniform(1.5, 4.0, size=dim)
        
        # Enhanced harmonic components with fractal-like irregularities
        self.harmonic_amplitudes = np.random.uniform(0.5, 2.5, size=dim)
        self.harmonic_frequencies = np.random.uniform(1.0, 5.0, size=dim)
        self.fractal_dims = np.random.uniform(1.1, 2.9, size=dim)
        
        # Novel basin interactions with fractal irregularities
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=dim)
        self.basin_strengths = np.random.uniform(1.0, 5.0, size=dim)
        self.basin_radii = np.random.uniform(0.3, 2.5, size=dim)
        
        # Hyper-chaotic cross-dimensional coupling
        self.hyper_coupling_matrix = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        np.fill_diagonal(self.hyper_coupling_matrix, 0.0)
        
        # Adaptive memory-based penalty parameters
        self.memory_weights = np.random.uniform(0.1, 1.5, size=dim)
        self.memory_decay_rates = np.random.uniform(0.01, 0.5, size=dim)
        
        # Quantum-inspired interference terms
        self.quantum_phases = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_amplitudes = np.random.uniform(0.3, 1.8, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component
        tent_component = 0.0
        for i in range(self.dim):
            tent_val = self.tent_maps[i] * np.abs(x[i] - 2.5) if x[i] < 2.5 else (1 - self.tent_maps[i]) * np.abs(x[i] - 2.5)
            tent_component += tent_val
            
        # Polynomial chaos expansion component
        poly_component = 0.0
        for i in range(self.dim):
            poly_val = 0.0
            for j in range(6):
                poly_val += self.poly_coeffs[i, j] * np.power(x[i], j)
            poly_component += poly_val
            
        # Dynamic penalty component
        penalty_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i])
            penalty_val = self.penalty_weights[i] * np.power(dist, self.penalty_exponents[i])
            penalty_component += penalty_val
            
        # Enhanced harmonic component with fractal irregularities
        harmonic_component = 0.0
        for i in range(self.dim):
            freq = self.harmonic_frequencies[i]
            fractal_factor = np.sin(np.log(1 + x[i]**2)) * (1 + 0.1 * np.sin(self.fractal_dims[i] * x[i]))
            harmonic_val = self.harmonic_amplitudes[i] * np.sin(freq * x[i]) * fractal_factor
            harmonic_component += harmonic_val
            
        # Basin interaction with fractal irregularities
        basin_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            fractal_irr = 1 + 0.2 * np.sin(self.fractal_dims[i] * x[i])
            basin_val = self.basin_strengths[i] * np.exp(-dist / self.basin_radii[i]) * fractal_irr
            basin_component += basin_val
            
        # Hyper-chaotic cross-dimensional coupling
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.hyper_coupling_matrix[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Adaptive memory-based penalty component
        memory_component = 0.0
        for i in range(self.dim):
            memory_val = self.memory_weights[i] * np.exp(-self.memory_decay_rates[i] * np.abs(x[i]))
            memory_component += memory_val
            
        # Quantum-inspired interference component
        quantum_component = 0.0
        for i in range(self.dim):
            quantum_val = self.quantum_amplitudes[i] * np.sin(self.quantum_phases[i] + x[i])
            quantum_component += quantum_val
            
        # Combine all components with different weights
        return (1.5 * tent_component + 
                1.2 * poly_component + 
                1.8 * penalty_component + 
                2.0 * harmonic_component + 
                1.6 * basin_component + 
                1.3 * coupling_component + 
                1.4 * memory_component + 
                1.7 * quantum_component)