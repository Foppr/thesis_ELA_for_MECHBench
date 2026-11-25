import numpy as np

class TentChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters with dynamic variation
        self.tent_params = np.random.uniform(1.5, 3.0, dim)
        # Phase transition points with chaotic modulation
        self.phase_transitions = np.random.uniform(-5.0, 5.0, dim)
        # Hybrid polynomial-trigonometric interaction coefficients
        self.poly_trig_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Adaptive penalty scaling with dynamic feedback
        self.penalty_scaling = np.random.uniform(0.5, 2.5, dim)
        # Multi-scale chaotic frequencies for complex dynamics
        self.freqs = np.random.uniform(0.5, 10.0, dim)
        # Sparse coupling matrix with directional bias (modified structure)
        self.coupling_matrix = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Nonlinear transformation parameters (modified)
        self.nonlinear_params = np.random.uniform(0.1, 3.0, dim)
        # Multi-modal attractor positions with clustering
        self.attractor_positions = np.random.uniform(-5.0, 5.0, (dim, 10))
        # Dynamic conditioning factors with time-varying weights
        self.conditioning_factors = np.random.uniform(0.8, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Tent map chaotic component with phase transitions
        for i in range(self.dim):
            tent_val = self.tent_params[i] * np.abs(x[i] - self.phase_transitions[i])
            tent_val = np.minimum(tent_val, 1.0 - tent_val)
            result += tent_val ** 2
            
        # Hybrid polynomial-trigonometric interactions
        poly_trig_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_trig_energy += self.poly_trig_coeffs[i, j] * x[i] * np.sin(x[j])
                    
        # Adaptive penalty mechanism with chaotic modulation
        penalty_energy = 0.0
        for i in range(self.dim):
            penalty_energy += self.penalty_scaling[i] * (np.abs(x[i]) - 2.5) ** 4
            
        # Multi-scale frequency component with dynamic scaling
        freq_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.freqs[i] * x[i])
            freq_term += 0.7 * np.sin(2 * self.freqs[i] * x[i])
            freq_term += 0.4 * np.sin(3 * self.freqs[i] * x[i])
            freq_energy += freq_term ** 2
            
        # Sparse cross-dimensional coupling with directional bias (modified coupling)
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j and np.random.rand() > 0.7:
                    coupling_energy += self.coupling_matrix[i, j] * x[i] * x[j]
                    
        # Nonlinear transformation component (modified to cubic + quintic)
        nonlinear_energy = 0.0
        for i in range(self.dim):
            nonlinear_energy += self.nonlinear_params[i] * (x[i] ** 3 + 0.3 * x[i] ** 5)
            
        # Multi-modal attractor energy with clustering
        attractor_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.attractor_positions[i, :]))
            attractor_energy += min_dist ** 2
            
        # Combine all components with dynamic weights (slightly modified)
        total = 0.3 * result + 0.25 * poly_trig_energy + 0.15 * penalty_energy + 0.12 * freq_energy + 0.08 * coupling_energy + 0.06 * nonlinear_energy + 0.04 * attractor_energy
        
        # Apply dynamic conditioning with chaotic feedback (modified)
        for i in range(self.dim):
            total += self.conditioning_factors[i] * np.cos(x[i]) * np.sin(0.5 * x[i])
            
        return total