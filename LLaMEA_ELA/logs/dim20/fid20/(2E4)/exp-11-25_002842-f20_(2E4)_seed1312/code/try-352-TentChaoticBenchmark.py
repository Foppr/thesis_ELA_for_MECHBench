import numpy as np

class TentChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperchaotic logistic map parameters with memory effects
        self.r_params = np.random.uniform(3.57, 4.0, dim)
        # Memory-dependent phase transition points with temporal bias
        self.phase_transitions = np.random.uniform(-5.0, 5.0, dim)
        # Multi-scale fractal potential coefficients with recursive scaling
        self.fractal_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim, 5))
        # Non-linear coupling strengths with directional memory
        self.coupling_strengths = np.random.uniform(0.1, 1.2, (dim, dim))
        # Adaptive basin structures with time-varying scaling factors
        self.basin_scaling = np.random.uniform(0.5, 2.5, dim)
        # Hybrid polynomial-trigonometric interactions with dynamic exponents
        self.poly_coeffs = np.random.uniform(-1.8, 1.8, (dim, dim))
        self.trig_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Multi-modal penalty landscapes with memory-dependent thresholds
        self.penalty_thresholds = np.random.uniform(1.0, 4.0, dim)
        self.penalty_exponents = np.random.uniform(2.0, 6.0, dim)
        # Memory-based chaotic attractor positions with recursive fractal distribution
        self.attractor_positions = np.random.uniform(-5.0, 5.0, (dim, 15))
        # Temporal memory coefficients for adaptive fitness scoring
        self.memory_coeff = np.random.uniform(0.3, 0.9, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Hyperchaotic logistic map component with memory effects
        for i in range(self.dim):
            logistic_term = self.r_params[i] * x[i] * (1.0 - x[i])
            result += logistic_term ** 2
            
        # Memory-dependent basin attraction energy
        basin_energy = 0.0
        for i in range(self.dim):
            dist_to_transition = np.abs(x[i] - self.phase_transitions[i])
            basin_energy += self.basin_scaling[i] * np.exp(-dist_to_transition / 2.0) * self.memory_coeff[i]
            
        # Multi-scale fractal potential interactions
        fractal_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    scale_factor = 1.0 + np.sum(self.fractal_coeffs[i, j, :] * np.sin(x[i] * x[j]))
                    fractal_energy += scale_factor * x[i] ** 3 * x[j]
                    
        # Hybrid polynomial-trigonometric interactions with dynamic exponents
        hybrid_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_interaction = self.poly_coeffs[i, j] * x[i] ** 2 * x[j]
                    trig_interaction = self.trig_coeffs[i, j] * np.sin(x[i]) * np.cos(x[j])
                    hybrid_energy += poly_interaction + trig_interaction
                    
        # Non-linear coupling with memory-dependent strengths
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_energy += self.coupling_strengths[i, j] * np.sin(x[i]) * x[j]
                    
        # Dynamic penalty landscape with memory-dependent thresholds and exponents
        penalty_energy = 0.0
        for i in range(self.dim):
            distance_from_origin = np.abs(x[i])
            if distance_from_origin > self.penalty_thresholds[i]:
                penalty_energy += (distance_from_origin - self.penalty_thresholds[i]) ** self.penalty_exponents[i]
                
        # Multi-modal attractor energy with fractal-like positioning and recursive scaling
        attractor_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.attractor_positions[i, :]))
            attractor_energy += min_dist ** 2
            
        # Combine all components with weighted contributions
        total = 0.25 * result + 0.15 * basin_energy + 0.20 * fractal_energy + 0.15 * hybrid_energy + 0.10 * coupling_energy + 0.10 * penalty_energy + 0.05 * attractor_energy
        
        return total