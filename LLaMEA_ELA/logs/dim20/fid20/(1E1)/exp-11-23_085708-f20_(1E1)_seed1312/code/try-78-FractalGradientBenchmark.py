import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Base polynomial landscape with fractal recursion
        result = 0.0
        for i in range(self.dim):
            # Recursive polynomial terms with varying degrees
            term = x_scaled[i]**2 + 0.5 * x_scaled[i]**4 + 0.1 * x_scaled[i]**6
            # Add interaction between dimensions using fractal-like pattern
            for j in range(i+1, self.dim):
                interaction = np.sin(x_scaled[i] * x_scaled[j] * 2) * np.cos(x_scaled[i] - x_scaled[j])
                term += interaction * (i + j + 1) * 0.05
                
            result += term
            
        # Add directional gradient fields with varying orientations
        grad_field = 0.0
        for i in range(self.dim):
            # Create directional bias using sine and cosine combinations
            direction = np.sin(x_scaled[i] * 3) * np.cos(x_scaled[i] * 2)
            grad_field += direction * (i + 1) * 0.3
            
        # Fractal component with self-similar structure at multiple scales
        fractal_term = 0.0
        for scale in [1, 2, 3]:
            for i in range(self.dim):
                fractal_term += np.sin(x_scaled[i] * scale * 5) * np.cos(x_scaled[i] * scale * 3) * (0.5 ** scale)
                
        # Add a global harmonic modulation based on the number of dimensions
        dim_mod = np.sin(np.sum(x_scaled) * 0.5) * np.cos(np.sum(x_scaled) * 0.3)
        
        # Combine all components with appropriate weights
        total = result + grad_field + fractal_term + dim_mod * 2.0
        
        # Ensure the global minimum is at the origin (scaled to match domain)
        return total + 5.0