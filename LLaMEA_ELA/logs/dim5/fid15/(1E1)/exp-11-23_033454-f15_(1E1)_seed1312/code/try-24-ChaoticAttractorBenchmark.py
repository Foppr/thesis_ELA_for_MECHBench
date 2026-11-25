import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for different dimensions
        self.chaos_params = []
        for i in range(dim):
            self.chaos_params.append({
                'a': 3.9 + 0.1 * np.sin(i),
                'b': 0.5 + 0.3 * np.cos(i),
                'c': 0.1 + 0.2 * np.sin(i/2)
            })
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic attractor component with fractional dimensionality
        for i in range(self.dim):
            param = self.chaos_params[i]
            
            # Create chaotic map with varying parameters
            x_i = x[i]
            if i > 0:
                x_prev = x[i-1]
            else:
                x_prev = x[-1]  # Wrap around
            
            # Fractional chaotic dynamics
            chaotic_term = param['a'] * x_i * (1 - x_i) + param['b'] * x_prev * (1 - x_prev)
            
            # Add fractional exponentiation for varying conditioning
            fractional_exp = 1.0 + 0.5 * np.sin(i / self.dim * np.pi)
            chaotic_term = np.power(np.abs(chaotic_term), fractional_exp)
            
            # Add to result with dimension-specific weights
            weight = 0.5 + 0.5 * np.cos(i / self.dim * np.pi)
            result += weight * chaotic_term
        
        # Add periodic oscillatory component for additional complexity
        period_term = 0.0
        for i in range(self.dim):
            period_term += np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 1) * 0.5)
        
        # Add quadratic basin term to create a central attraction
        basin_term = 0.1 * np.sum(x**2)
        
        # Combine all terms with different scaling factors
        result = 0.3 * result + 0.4 * period_term - basin_term
        
        # Add noise for robustness testing
        noise = 0.01 * np.random.randn()
        
        return result + noise