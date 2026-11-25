import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with cross-dimensional coupling
        chaos_component = 0
        for i in range(self.dim):
            coeff = np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            poly_term = coeff * x[i]**(i + 1)
            # Add cross-dimensional interaction term
            for j in range(i+1, self.dim):
                cross_interaction = 0.1 * np.sin((i+j) * np.pi / (self.dim + 3)) * x[i] * x[j]
                poly_term += cross_interaction
            chaos_component += poly_term
            
        # Enhanced logarithmic barrier function with multi-scale thresholds
        barrier_component = 0
        for i in range(self.dim):
            # Multi-scale threshold based on dimension and position
            threshold = 2.5 + 0.8 * np.sin(i * np.pi / self.dim) + 0.3 * np.cos(i * np.pi / (self.dim + 1))
            if abs(x[i]) < threshold:
                barrier_component += -np.log(threshold - abs(x[i])) * (1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 3)))
            else:
                # Penalty term with varying exponent
                penalty_exp = 1.5 + 0.5 * np.cos(i * np.pi / (self.dim + 2))
                barrier_component += (abs(x[i])**penalty_exp) * (1.0 + 0.1 * np.sin(i * np.pi / (self.dim + 4)))
        
        # Enhanced saddle-point interaction with non-linear coupling
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-linear coupling strength
                coupling = 0.7 + 0.3 * np.sin((i + j) * np.pi / (self.dim + 1)) * np.cos((i - j) * np.pi / (self.dim + 2))
                # Non-linear saddle interaction: x_i^3 - x_j^3
                saddle_term += coupling * (x[i]**3 - x[j]**3)
        
        # Exponentially varying curvature with enhanced dimensionality scaling
        exp_curvature = 0
        for i in range(self.dim):
            # Enhanced exponential base and scaling factor
            base = 1.8 + 0.4 * np.cos(i * np.pi / (self.dim + 2)) + 0.1 * np.sin(i * np.pi / (self.dim + 3))
            scale_factor = 1.0 + 0.2 * np.sin(i * np.pi / self.dim) + 0.1 * np.cos(i * np.pi / (self.dim + 1))
            exp_curvature += (base**(abs(x[i]) + 1)) * scale_factor * np.sin(i * np.pi / self.dim)
        
        # Global normalization and scaling with enhanced dimensionality effect
        norm_factor = 1.0 + 0.5 * np.sin(self.dim * np.pi / 8) + 0.2 * np.cos(self.dim * np.pi / 9)
        
        # Dynamic weights with enhanced trigonometric modulation
        weight1 = 0.3 + 0.2 * np.cos(self.dim * np.pi / 5) + 0.1 * np.sin(self.dim * np.pi / 6)
        weight2 = 0.4 + 0.15 * np.sin(self.dim * np.pi / 6) + 0.1 * np.cos(self.dim * np.pi / 7)
        weight3 = 0.2 + 0.1 * np.cos(self.dim * np.pi / 7) + 0.05 * np.sin(self.dim * np.pi / 8)
        weight4 = 0.1 + 0.05 * np.sin(self.dim * np.pi / 9) + 0.02 * np.cos(self.dim * np.pi / 10)
        
        return weight1 * chaos_component + weight2 * barrier_component + weight3 * saddle_term + weight4 * exp_curvature * norm_factor