import numpy as np

class SineChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine map parameters with dynamic variation
        self.sine_params = np.random.uniform(0.5, 2.0, dim)
        # Phase transition points with chaotic modulation
        self.phase_transitions = np.random.uniform(-5.0, 5.0, dim)
        # Hybrid polynomial-trigonometric interaction coefficients
        self.poly_trig_coeffs = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Adaptive basin scaling with dynamic feedback
        self.basin_scaling = np.random.uniform(0.5, 3.0, dim)
        # Multi-scale chaotic frequencies for complex dynamics
        self.freqs = np.random.uniform(0.2, 8.0, dim)
        # Sparse coupling matrix with directional bias
        self.coupling_matrix = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Nonlinear transformation parameters
        self.nonlinear_params = np.random.uniform(0.1, 2.5, dim)
        # Multi-modal attractor positions with clustering
        self.attractor_positions = np.random.uniform(-5.0, 5.0, (dim, 8))
        # Dynamic conditioning factors with time-varying weights
        self.conditioning_factors = np.random.uniform(0.7, 1.8, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Sine map chaotic component with phase transitions
        for i in range(self.dim):
            sine_val = np.sin(self.sine_params[i] * (x[i] - self.phase_transitions[i]))
            result += sine_val ** 2
            
        # Hybrid polynomial-trigonometric interactions
        poly_trig_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_trig_energy += self.poly_trig_coeffs[i, j] * x[i] * np.cos(x[j])
                    
        # Adaptive basin mechanism with chaotic modulation
        basin_energy = 0.0
        for i in range(self.dim):
            basin_energy += self.basin_scaling[i] * (np.abs(x[i]) - 2.0) ** 3
            
        # Multi-scale frequency component with dynamic scaling
        freq_energy = 0.0
        for i in range(self.dim):
            freq_term = np.cos(self.freqs[i] * x[i])
            freq_term += 0.6 * np.cos(2 * self.freqs[i] * x[i])
            freq_term += 0.3 * np.cos(3 * self.freqs[i] * x[i])
            freq_energy += freq_term ** 2
            
        # Sparse cross-dimensional coupling with directional bias
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j and np.random.rand() > 0.65:
                    coupling_energy += self.coupling_matrix[i, j] * x[i] * x[j]
                    
        # Nonlinear transformation component with modified exponents
        nonlinear_energy = 0.0
        for i in range(self.dim):
            nonlinear_energy += self.nonlinear_params[i] * (x[i] ** 4 + 0.3 * x[i] ** 5 + 0.05 * x[i] ** 6)
            
        # Multi-modal attractor energy with clustering
        attractor_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.attractor_positions[i, :]))
            attractor_energy += min_dist ** 2
            
        # Combine all components with dynamic weights
        total = 0.35 * result + 0.20 * poly_trig_energy + 0.15 * basin_energy + 0.12 * freq_energy + 0.08 * coupling_energy + 0.06 * nonlinear_energy + 0.04 * attractor_energy
        
        # Apply dynamic conditioning with chaotic feedback
        for i in range(self.dim):
            total += self.conditioning_factors[i] * np.sin(x[i]) * np.cos(0.3 * x[i])
            
        return total