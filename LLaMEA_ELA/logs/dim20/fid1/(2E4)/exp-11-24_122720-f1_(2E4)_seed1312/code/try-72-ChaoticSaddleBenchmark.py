import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with modified stochastic coefficients
        chaos_component = 0
        for i in range(self.dim):
            # Modified chaotic coefficients
            coeff = np.sin(i * np.pi / (self.dim + 3)) * np.cos(i * np.pi / (self.dim + 4))
            poly_term = coeff * x[i]**(i + 2)
            chaos_component += poly_term
            
        # Logarithmic barrier function component with dynamic thresholds
        barrier_component = 0
        for i in range(self.dim):
            # Modified threshold
            threshold = 1.5 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
            # Log barrier with soft constraint
            if abs(x[i]) < threshold:
                barrier_component += -np.log(threshold - abs(x[i])) * (1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 5)))
            else:
                barrier_component += (x[i]**2) * (1.0 + 0.1 * np.cos(i * np.pi / (self.dim + 6)))
        
        # Saddle-point interaction terms with modified coupling strengths
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified coupling strength
                coupling = 0.7 + 0.2 * np.sin((i + j) * np.pi / (self.dim + 3))
                # Saddle-point interaction: x_i^2 - x_j^2
                saddle_term += coupling * (x[i]**2 - x[j]**2)
        
        # Exponentially varying curvature component
        exp_curvature = 0
        for i in range(self.dim):
            # Modified exponential base
            base = 1.3 + 0.4 * np.cos(i * np.pi / (self.dim + 3))
            exp_curvature += (base**(abs(x[i]) + 1)) * np.sin(i * np.pi / self.dim)
        
        # Global normalization and scaling
        norm_factor = 1.0 + 0.2 * np.sin(self.dim * np.pi / 9)
        
        # Combine all components with modified weights
        weight1 = 0.35 + 0.1 * np.cos(self.dim * np.pi / 6)
        weight2 = 0.35 + 0.15 * np.sin(self.dim * np.pi / 7)
        weight3 = 0.25 + 0.1 * np.cos(self.dim * np.pi / 8)
        weight4 = 0.05 + 0.05 * np.sin(self.dim * np.pi / 10)
        
        return weight1 * chaos_component + weight2 * barrier_component + weight3 * saddle_term + weight4 * exp_curvature * norm_factor