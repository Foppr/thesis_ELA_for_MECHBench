import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Chaotic component using logistic map-like dynamics
        chaotic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x_scaled[i]
            else:
                x_prev = x_scaled[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev)) * np.cos(x_scaled[i])
        
        # Multi-modal polynomial with dynamic exponents
        modal_term = 0.0
        for i in range(self.dim):
            exponent = 2 + 2 * np.sin(i) + 0.5 * np.cos(i * 2)
            modal_term += (x_scaled[i]**exponent - 3 * x_scaled[i]**2 + 2 * x_scaled[i])**2
        
        # Saddle point structure with varying curvature
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x_scaled[i]**4 - 6 * x_scaled[i]**2 + 8) * np.sin(x_scaled[i])
        
        # Non-separable interaction terms with dynamic weights
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (i + j) / (self.dim * (self.dim - 1) / 2)
                interaction_term += weight * np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
        
        # Dynamic curvature based on position
        curvature_term = 0.0
        for i in range(self.dim):
            dynamic_curvature = 1 + 0.5 * np.sin(x_scaled[i] * 3)
            curvature_term += dynamic_curvature * x_scaled[i]**2
        
        # Boundary avoidance with variable penalty exponents
        boundary_term = 0.0
        for i in range(self.dim):
            penalty_exp = 2.5 + 0.8 * np.sin(i)
            boundary_term += np.abs(x_scaled[i])**penalty_exp
        
        return chaotic_term + modal_term + saddle_term + interaction_term + curvature_term + boundary_term