import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic logistic map parameters with temporal modulation
        self.r_params = np.random.uniform(3.8, 4.0, dim)
        # Adaptive basin scaling factors with fractal-like distribution
        self.basin_scaling = np.random.uniform(0.3, 2.5, dim)
        # Phase transition points with dynamic positioning and temporal variation
        self.phase_transitions = np.random.uniform(-5.0, 5.0, dim)
        # Hybrid interaction coefficients combining polynomial and sinusoidal terms
        self.poly_coeffs = np.random.uniform(-1.5, 1.5, (dim, dim))
        self.sin_coeffs = np.random.uniform(-3.0, 3.0, (dim, dim))
        # Dynamic penalty landscapes with time-varying thresholds and exponents
        self.penalty_thresholds = np.random.uniform(0.5, 5.0, dim)
        self.penalty_exponents = np.random.uniform(1.5, 7.0, dim)
        # Multi-scale chaotic attractor positions with fractal-like distribution
        self.attractor_positions = np.random.uniform(-5.0, 5.0, (dim, 15))
        # Adaptive coupling strengths between dimensions with directional bias
        self.coupling_strengths = np.random.uniform(0.05, 1.5, (dim, dim))
        # Additional sinusoidal chaotic modulation components
        self.sin_modulation = np.random.uniform(-0.5, 0.5, dim)
        # Higher-order polynomial terms for increased complexity
        self.high_order_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced chaotic logistic map component with temporal modulation
        for i in range(self.dim):
            logistic_term = self.r_params[i] * x[i] * (1.0 - x[i])
            # Add sinusoidal modulation to the chaotic dynamics
            modulation = np.sin(self.sin_modulation[i] * x[i])
            result += (logistic_term + modulation) ** 2
            
        # Basin attraction energy with adaptive scaling and phase transitions
        basin_energy = 0.0
        for i in range(self.dim):
            dist_to_transition = np.abs(x[i] - self.phase_transitions[i])
            basin_energy += self.basin_scaling[i] * np.exp(-dist_to_transition / 1.5)
            
        # Hybrid polynomial-sinusoidal interactions
        hybrid_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_interaction = self.poly_coeffs[i, j] * x[i] ** 2 * x[j]
                    sin_interaction = self.sin_coeffs[i, j] * np.sin(x[i]) * np.sin(x[j])
                    hybrid_energy += poly_interaction + sin_interaction
                    
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
                    
        # Higher-order polynomial interactions
        higher_order_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        higher_order_energy += self.high_order_coeffs[i, j, k] * x[i] ** 2 * x[j] * x[k]
                        
        # Combine all components with weighted contributions
        total = 0.25 * result + 0.2 * basin_energy + 0.15 * hybrid_energy + 0.15 * penalty_energy + 0.1 * attractor_energy + 0.1 * coupling_energy + 0.05 * higher_order_energy
        
        return total