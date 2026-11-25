import numpy as np

class TentChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters with dynamic variation
        self.r_params = np.random.uniform(1.5, 2.0, dim)
        # Adaptive basin scaling factors with chaotic modulation
        self.basin_scaling = np.random.uniform(0.3, 1.5, dim)
        # Phase transition points with dynamic positioning and temporal variation
        self.phase_transitions = np.random.uniform(-5.0, 5.0, dim)
        # Hybrid interaction coefficients combining polynomial and trigonometric terms
        self.poly_coeffs = np.random.uniform(-1.5, 1.5, (dim, dim))
        self.trig_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Dynamic penalty landscapes with time-varying thresholds and exponents
        self.penalty_thresholds = np.random.uniform(0.5, 3.0, dim)
        self.penalty_exponents = np.random.uniform(1.5, 5.0, dim)
        # Multi-scale chaotic attractor positions with fractal-like distribution
        self.attractor_positions = np.random.uniform(-5.0, 5.0, (dim, 8))
        # Adaptive coupling strengths between dimensions with directional bias
        self.coupling_strengths = np.random.uniform(0.05, 0.8, (dim, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic tent map component with dynamic r-values
        for i in range(self.dim):
            if x[i] < 0.5:
                tent_term = self.r_params[i] * x[i]
            else:
                tent_term = self.r_params[i] * (1.0 - x[i])
            result += tent_term ** 2
            
        # Basin attraction energy with adaptive scaling and phase transitions
        basin_energy = 0.0
        for i in range(self.dim):
            dist_to_transition = np.abs(x[i] - self.phase_transitions[i])
            basin_energy += self.basin_scaling[i] * np.exp(-dist_to_transition / 1.5)
            
        # Hybrid polynomial-trigonometric interactions
        hybrid_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_interaction = self.poly_coeffs[i, j] * x[i] ** 3 * x[j]
                    trig_interaction = self.trig_coeffs[i, j] * np.sin(x[i]) * np.cos(x[j])
                    hybrid_energy += poly_interaction + trig_interaction
                    
        # Dynamic penalty landscape with varying thresholds and exponents
        penalty_energy = 0.0
        for i in range(self.dim):
            distance_from_origin = np.abs(x[i])
            if distance_from_origin > self.penalty_thresholds[i]:
                penalty_energy += (distance_from_origin - self.penalty_thresholds[i]) ** self.penalty_exponents[i]
                
        # Multi-scale attractor energy with fractal-like positioning
        attractor_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.attractor_positions[i, :]))
            attractor_energy += min_dist ** 2
            
        # Cross-dimensional coupling with adaptive strengths
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_energy += self.coupling_strengths[i, j] * x[i] * x[j]
                    
        # Combine all components with weighted contributions
        total = 0.35 * result + 0.2 * basin_energy + 0.25 * hybrid_energy + 0.15 * penalty_energy + 0.05 * attractor_energy + 0.05 * coupling_energy
        
        return total