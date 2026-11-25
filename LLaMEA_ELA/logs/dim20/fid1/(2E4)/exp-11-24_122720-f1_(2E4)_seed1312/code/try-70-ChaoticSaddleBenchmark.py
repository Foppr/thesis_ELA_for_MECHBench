import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with trigonometric coupling
        chaos_component = 0
        for i in range(self.dim):
            coeff = np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            poly_term = coeff * x[i]**(i + 1)
            chaos_component += poly_term
            
        # Adaptive logarithmic barrier with dynamic thresholds and coupling
        barrier_component = 0
        for i in range(self.dim):
            threshold = 2.5 + 0.3 * np.sin(i * np.pi / self.dim) + 0.2 * np.cos(i * np.pi / (self.dim + 1))
            if abs(x[i]) < threshold:
                barrier_component += -np.log(threshold - abs(x[i])) * (1.0 + 0.15 * np.sin(i * np.pi / (self.dim + 3)))
            else:
                barrier_component += (x[i]**2) * (1.0 + 0.1 * np.cos(i * np.pi / (self.dim + 4)))
        
        # Saddle-point interaction with adaptive coupling strengths and cross-terms
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.6 + 0.2 * np.sin((i + j) * np.pi / (self.dim + 1)) * np.cos((i - j) * np.pi / (self.dim + 2))
                saddle_term += coupling * (x[i]**2 - x[j]**2) * np.sin((i + j) * np.pi / self.dim)
        
        # Multi-scale exponentially varying curvature with directional dependence
        exp_curvature = 0
        for i in range(self.dim):
            base = 1.4 + 0.3 * np.cos(i * np.pi / (self.dim + 2)) + 0.1 * np.sin(i * np.pi / self.dim)
            exp_curvature += (base**(abs(x[i]) + 1)) * np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 3))
        
        # Global normalization and scaling with dimension-dependent adjustments
        norm_factor = 1.0 + 0.25 * np.sin(self.dim * np.pi / 8) + 0.1 * np.cos(self.dim * np.pi / 12)
        
        # Dynamic weights with enhanced variation
        weight1 = 0.35 + 0.1 * np.cos(self.dim * np.pi / 5) + 0.05 * np.sin(self.dim * np.pi / 10)
        weight2 = 0.35 + 0.15 * np.sin(self.dim * np.pi / 6) + 0.05 * np.cos(self.dim * np.pi / 11)
        weight3 = 0.2 + 0.1 * np.cos(self.dim * np.pi / 7) + 0.05 * np.sin(self.dim * np.pi / 12)
        weight4 = 0.1 + 0.05 * np.sin(self.dim * np.pi / 9) + 0.02 * np.cos(self.dim * np.pi / 13)
        
        return weight1 * chaos_component + weight2 * barrier_component + weight3 * saddle_term + weight4 * exp_curvature * norm_factor