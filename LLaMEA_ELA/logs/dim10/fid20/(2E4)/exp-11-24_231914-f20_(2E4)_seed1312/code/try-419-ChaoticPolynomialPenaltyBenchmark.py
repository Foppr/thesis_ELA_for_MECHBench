import numpy as np

class ChaoticPolynomialPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Chaotic tent map parameters for enhanced sensitivity
        self.tent_maps = np.random.uniform(1.1, 1.9, size=dim)
        self.tent_offsets = np.random.uniform(-0.5, 0.5, size=dim)
        
        # Polynomial chaos expansion coefficients with higher order terms
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, size=(dim, 5))
        
        # Dynamic penalty function parameters with time-varying components
        self.penalty_weights = np.random.uniform(0.5, 3.0, size=dim)
        self.penalty_exponents = np.random.uniform(1.5, 4.0, size=dim)
        
        # Enhanced harmonic components with variable frequencies and amplitudes
        self.harmonic_freqs = np.random.uniform(2.0, 8.0, size=dim)
        self.harmonic_amps = np.random.uniform(1.0, 3.5, size=dim)
        
        # Fractal-like basin interactions with recursive scaling
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=dim)
        self.basin_strengths = np.random.uniform(1.0, 6.0, size=dim)
        self.basin_radii = np.random.uniform(0.2, 3.0, size=dim)
        self.fractal_dims = np.random.uniform(1.1, 2.5, size=dim)
        
        # Quantum-inspired interference terms with phase modulation
        self.quantum_phases = np.random.uniform(0, 6*np.pi, size=dim)
        self.quantum_amplitudes = np.random.uniform(0.5, 3.0, size=dim)
        
        # Adaptive memory-based penalty parameters
        self.memory_weights = np.random.uniform(0.1, 1.5, size=dim)
        self.memory_decay = np.random.uniform(0.8, 0.99, size=dim)
        
        # Hyper-chaotic coupling matrix with non-linear feedback
        self.hyper_coupling = np.random.uniform(-2.0, 2.0, size=(dim, dim))
        np.fill_diagonal(self.hyper_coupling, 0.0)
        
        # Additional noise parameters for increased robustness testing
        self.noise_level = np.random.uniform(0.01, 0.2, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with enhanced nonlinearity
        chaotic_component = 0.0
        for i in range(self.dim):
            tent_val = self.tent_maps[i] * np.abs(x[i] - self.tent_offsets[i])
            chaotic_component += tent_val
            
        # Polynomial chaos expansion component with higher order terms
        poly_component = 0.0
        for i in range(self.dim):
            poly_val = 0.0
            for j in range(5):
                poly_val += self.poly_coeffs[i, j] * (x[i]**j)
            poly_component += poly_val
            
        # Dynamic penalty function with time-varying components
        penalty_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i])
            penalty_val = self.penalty_weights[i] * (dist**self.penalty_exponents[i]) * np.exp(-dist/5.0)
            penalty_component += penalty_val
            
        # Enhanced harmonic component with multiple frequencies
        harmonic_component = 0.0
        for i in range(self.dim):
            harm_val = self.harmonic_amps[i] * (np.sin(self.harmonic_freqs[i] * x[i]) + 
                                               0.3 * np.sin(3 * self.harmonic_freqs[i] * x[i]) +
                                               0.1 * np.sin(5 * self.harmonic_freqs[i] * x[i]))
            harmonic_component += harm_val
            
        # Fractal-like basin interaction with recursive scaling
        basin_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            basin_val = self.basin_strengths[i] * np.exp(-dist**self.fractal_dims[i] / (self.basin_radii[i]**2))
            basin_component += basin_val
            
        # Quantum-inspired interference term
        quantum_component = 0.0
        for i in range(self.dim):
            quantum_val = self.quantum_amplitudes[i] * np.sin(self.quantum_phases[i] + x[i]**1.5)
            quantum_component += quantum_val
            
        # Adaptive memory-based penalty with exponential decay
        memory_component = 0.0
        for i in range(self.dim):
            memory_val = self.memory_weights[i] * (x[i]**2) * np.exp(-self.memory_decay[i] * np.abs(x[i]))
            memory_component += memory_val
            
        # Hyper-chaotic coupling with non-linear feedback
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_val = self.hyper_coupling[i, j] * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                    coupling_component += coupling_val
                    
        # Add noise to increase robustness
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_level[i] * np.random.uniform(-1, 1)
            noise_component += noise_val
            
        # Combine all components with modified weights
        return (2.0 * chaotic_component + 
                1.5 * poly_component + 
                2.5 * penalty_component + 
                1.8 * harmonic_component + 
                2.2 * basin_component + 
                1.3 * quantum_component + 
                1.7 * memory_component + 
                1.4 * coupling_component + 
                0.8 * noise_component)