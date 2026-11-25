import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with stochastic coefficients
        chaos_component = 0
        for i in range(self.dim):
            # Stochastic polynomial coefficients
            coeff = np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            poly_term = coeff * x[i]**(i + 1)
            chaos_component += poly_term
            
        # Logarithmic barrier function component with dynamic thresholds
        barrier_component = 0
        for i in range(self.dim):
            # Dynamic threshold based on dimension
            threshold = 2.0 + 0.5 * np.sin(i * np.pi / self.dim)
            # Log barrier with soft constraint
            if abs(x[i]) < threshold:
                barrier_component += -np.log(threshold - abs(x[i])) * (1.0 + 0.1 * np.sin(i * np.pi / (self.dim + 3)))
            else:
                barrier_component += (x[i]**2) * (1.0 + 0.05 * np.cos(i * np.pi / (self.dim + 4)))
        
        # Saddle-point interaction terms with varying coupling strengths
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.3 * np.sin((i + j) * np.pi / (self.dim + 1))
                # Saddle-point interaction: x_i^2 - x_j^2
                saddle_term += coupling * (x[i]**2 - x[j]**2)
        
        # Exponentially varying curvature component
        exp_curvature = 0
        for i in range(self.dim):
            # Exponential scaling with dimension-dependent base
            base = 1.5 + 0.2 * np.cos(i * np.pi / (self.dim + 2))
            exp_curvature += (base**(abs(x[i]) + 1)) * np.sin(i * np.pi / self.dim)
        
        # Global normalization and scaling
        norm_factor = 1.0 + 0.3 * np.sin(self.dim * np.pi / 8)
        
        # Combine all components with dynamic weights
        weight1 = 0.4 + 0.1 * np.cos(self.dim * np.pi / 5)
        weight2 = 0.3 + 0.15 * np.sin(self.dim * np.pi / 6)
        weight3 = 0.2 + 0.1 * np.cos(self.dim * np.pi / 7)
        weight4 = 0.1 + 0.05 * np.sin(self.dim * np.pi / 9)
        
        return weight1 * chaos_component + weight2 * barrier_component + weight3 * saddle_term + weight4 * exp_curvature * norm_factor